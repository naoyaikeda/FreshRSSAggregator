import os
from freshrss_api import FreshRSSAPI
import logging
import datetime
import google.generativeai as genai

class FreshRSSAggregator():
    api_client = None

    def __init__(
                self,
                host: str = None,
                username: str = None,
                password: str = None, 
                verify_ssl: bool = True, 
                verbose: bool = False
                ):
        
        self.api_client = FreshRSSAPI(host, username, password, verify_ssl, verbose)
    
    def Fetch(self, hoursDelta: int = 24, gemini_api_key:str = None, gemini_model_name:str = None):
        if gemini_api_key == None:
            gemini_api_key = os.environ.get("GEMINI_API_KEY")
        
        if gemini_model_name == None:
            gemini_model_name = os.environ.get("GEMINI_MODEL_NAME")

        unread_items = self.api_client.get_unreads()
        filtered_items = self.FilterItems(hoursDelta, unread_items)

        prompts = ['以下のリストに示すニュースを要約してください。']
        for item in filtered_items:
            prompts.append("- " + item.title)

        prompt = '\n'.join(prompts)

        genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
        gemini_pro = genai.GenerativeModel("gemini-2.0-flash")

        response = gemini_pro.generate_content(prompt)

        return(response)

    def FilterItems(self, hoursDelta:int, unread_items):
        now = datetime.datetime.now()
        threshold_time = now - datetime.timedelta(hours=hoursDelta)

        filtered_items = [
            item for item in unread_items
            if datetime.datetime.fromtimestamp(item.created_on_time) > threshold_time]
            
        return filtered_items