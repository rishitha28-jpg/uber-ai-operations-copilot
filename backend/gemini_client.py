# from google import genai
# from typing import Optional
# from backend.config import settings

# client = genai.Client(api_key=settings.GEMINI_API_KEY)

# MODEL_NAME = "gemini-2.5-flash"


# def ask_gemini(prompt: str, model: Optional[str] = None) -> str:

#     model_name = model or MODEL_NAME

#     try:
#         response = client.models.generate_content(
#             model=model_name,
#             contents=prompt
#         )

#         return response.text

#     except Exception as e:
#         print("Gemini API error:", e)
#         return f"Gemini API error: {str(e)}"
from google import genai
from typing import Optional
from backend.config import settings

# Initialize Gemini client
client = genai.Client(api_key=settings.GEMINI_API_KEY)

# Default model
MODEL_NAME = "gemini-2.5-flash"


def ask_gemini(prompt: str, model: Optional[str] = None) -> str:
    """
    Send prompt to Gemini and return the generated response.
    """

    model_name = model or MODEL_NAME

    try:
        response = client.models.generate_content(
            model=model_name,
            contents=prompt
        )

        # Ensure response contains text
        if hasattr(response, "text") and response.text:
            return response.text

        return "The AI model did not return a response."

    except Exception as e:
        # Log full error in server logs
        print(f"Gemini API error: {e}")

        # Safe message returned to user
        return "The AI service is temporarily unavailable due to API limits. Please try again later."
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    