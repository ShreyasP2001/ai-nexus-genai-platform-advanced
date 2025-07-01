import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

def forecast_interface():
    st.header("📈 Business Forecasting")
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("Data Preview", df.head())

        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        if len(numeric_cols) < 2:
            st.error("CSV must contain at least two numeric columns for forecasting.")
            return

        x_col = st.selectbox("Select X-axis (e.g., time)", numeric_cols)
        y_col = st.selectbox("Select Y-axis (value to forecast)", numeric_cols)

        if x_col and y_col:
            X = df[[x_col]].values.reshape(-1, 1)
            y = df[y_col].values

            model = LinearRegression()
            model.fit(X, y)

            future_x = np.arange(X.max() + 1, X.max() + 11).reshape(-1, 1)
            future_y = model.predict(future_x)

            fig, ax = plt.subplots()
            ax.plot(X, y, label="Historical", marker='o')
            ax.plot(future_x, future_y, label="Forecast", linestyle='--', marker='x')
            ax.set_xlabel(x_col)
            ax.set_ylabel(y_col)
            ax.set_title("Forecasting")
            ax.legend()
            st.pyplot(fig)

            forecast_df = pd.DataFrame({x_col: future_x.flatten(), y_col: future_y})
            st.write("Forecasted Data", forecast_df)
