@echo off
REM Activate virtual environment and run Streamlit app

echo Starting AI Nexus Platform...
call venv\Scripts\activate
streamlit run app\app.py
pause
