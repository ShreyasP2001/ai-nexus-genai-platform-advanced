import streamlit as st
import whisper
import tempfile
import os

def transcribe_audio():
    st.header("🎙️ Voice Transcription with Whisper")

    audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

    if audio_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
            tmp_file.write(audio_file.read())
            tmp_path = tmp_file.name

        st.info("Transcribing audio...")

        try:
            model = whisper.load_model("base")
            result = model.transcribe(tmp_path)
            st.success("Transcription Complete")
            st.text_area("Transcribed Text", result["text"], height=200)
        except Exception as e:
            st.error(f"Error during transcription: {str(e)}")
        finally:
            os.remove(tmp_path)
