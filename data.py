import requests


class GetDiscordData:
    def __init__(self):
        self.client_id = None
        self.client_secret = None
        self.redirect_uri = None
        self.scopes = None
        self.request = None
        
    def set_settings(self, settings):
        self.client_id = settings.get('client_id')
        self.client_secret = settings.get('client_secret')
        self.redirect_uri = settings.get('redirect_uri')
        self.scopes = settings.get('scopes')
        self.request = settings.get('request')
    
    def generate_auth_link(self):
        return (f"https://discord.com/api/oauth2/authorize?client_id={self.client_id}"
                f"&redirect_uri={self.redirect_uri}&response_type=code&scope={self.scopes}")

    def get_code(self):
        return self.request.GET.get('code')
    
    def get_access_token(self):
        response = requests.post(
            url="https://discord.com/api/oauth2/token",
            data={
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "grant_type": "authorization_code",
                "code": self.get_code(),
                "redirect_uri": self.redirect_uri,
                "scope": self.scopes,
            }
        ) 

        return response.json().get('access_token') 

    def get_data(self, api_url):
        response = requests.get(api_url, headers = {
            "Authorization": f"Bearer {self.get_access_token(self.get_code())}",
            "Content-Type": "application/json"
        }).json()

        return response

    

