import os
from dotenv import load_dotenv


load_dotenv()


OPENAI_API_KEY = os.getenv('CHATBOT_API_KEY')
GPT_MODEL = "gpt-3.5-turbo"
TOKENS = 50
TEMPERATURE = 0.5
