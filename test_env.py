import os
from dotenv import load_dotenv

load_dotenv()

print("AUTH0_DOMAIN:", os.getenv("AUTH0_DOMAIN"))
print("API_AUDIENCE:", os.getenv("API_AUDIENCE"))
print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))
