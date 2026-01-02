from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def chatbot(context: str):
    response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=context,
    config=types.GenerateContentConfig(
    system_instruction="You are helpful who memorize user context, it's previous response and generate summaries it he asks"
    )
)
    return response.text
