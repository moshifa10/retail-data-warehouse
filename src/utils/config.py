from dotenv import load_dotenv
import os

load_dotenv()

GROK = os.getenv("GROQ_API_KEY")