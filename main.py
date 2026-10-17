from dotenv import load_dotenv
import os
from pydantic import BaseModel
from reportlab.lib.pagesizes import A4
from tavily import TavilyClient
from groq import Groq

load_dotenv()

assert os.getenv("TAVILY_API_KEY"), "Missing Tavily API key"
assert os.getenv("GROQ_API_KEY"), "Missing Groq API key"

class Report(BaseModel):
    title: str
    abstract: str
    conclusion: str

print("Python libraries are working!")
print("Your project is ready for development.")