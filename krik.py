
from dotenv import load_dotenv
import os

load_dotenv()

groq_api_key=os.environ.get('GROQ_API_KEY')

print(groq_api_key) 

