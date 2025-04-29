import os
from os.path import join, dirname 
from FreshRSSAggregator import client
from dotenv import load_dotenv
import logging
import google.generativeai as genai
import datetime

logger = None

def main():
    load_dotenv(verbose=True)

    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    rssc = client.FreshRSSAggregator(os.environ.get("HOST"), os.environ.get("USERNAME"), os.environ.get("PASSWORD"), logger=logger)

    response = rssc.Fetch(gemini_api_key=os.environ.get("GEMINI_API_KEY"), gemini_model_name=os.environ.get("GEMINI_MODEL_NAME"))
    print(response.text)

if __name__ == "__main__":
    
    logging.basicConfig()
    logger = logging.getLogger(__name__).setLevel(logging.DEBUG)

    main()
