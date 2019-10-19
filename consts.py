from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
NP_TOKEN = os.getenv('NP_TOKEN')
NP_URL = f'https://api.novaposhta.ua/v2.0/json'
NP_TRACING_URL = f"{NP_URL}/getStatusDocuments"
TTN_LEN = 14
PHONE_LEN = 10
