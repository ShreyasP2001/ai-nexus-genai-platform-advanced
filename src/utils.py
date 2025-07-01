import os
from dotenv import load_dotenv

def load_environment():
    """Load API keys and environment variables."""
    env_path = ".env"
    if os.path.exists(env_path):
        load_dotenv(dotenv_path=env_path)
    else:
        print("⚠️ .env file not found. Using system environment variables.")
