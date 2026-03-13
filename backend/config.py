import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Settings:
    """
    Central configuration class for the application.
    All environment variables should be accessed from here.
    """

    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")

    if not GEMINI_API_KEY:
        raise ValueError(
            "GEMINI_API_KEY is missing. Please set it in your .env file."
        )


# Create a global settings instance
settings = Settings()