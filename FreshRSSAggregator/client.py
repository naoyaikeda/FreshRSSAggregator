from freshrss_api import FreshRSSAPI

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
    

