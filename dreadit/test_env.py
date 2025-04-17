import os 
from dotenv import load_dotenv
load_dotenv()

url = os.getenv('CREEPYPASTA_DATABASE_URL')
print(url)