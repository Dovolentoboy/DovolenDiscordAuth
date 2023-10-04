import requests
import string
import random


class BaseDiscordAuth:
    def __init__(self, settings: dict):
        self.client_id = settings.get('client_id')
        self.client_secret = settings.get('client_secret')
        self.redirect_uri = settings.get('redirect_uri')
        self.scopes = settings.get('scopes')
        self.framework = settings.get('framework')
        self.request = settings.get('request')
        
    def generate_login_link(self, client_id: int, redirect_uri: str, scopes: list) -> str:
        """Generate login url"""

        return (f"https://discord.com/api/oauth2/authorize?client_id={client_id}"
                f"&redirect_uri={redirect_uri}&response_type=code&scope={scopes}")

    def get_code(self, framework: str, request):
        """In framework parametr, fill Django or FastApi"""
        if framework == 'django':
            return request.GET.get('code')
        elif framework == 'fastApi':
            return request.query_params.get('code')

    def get_access_token(self) -> dict:
        """Exchange code to access_token"""

        response = requests.post(
            data={
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "grant_type": "authorization_code",
                "code": self.get_code(framework=self.framework, request=self.request),
                "redirect_uri": self.redirect_uri,
                "scope": self.scopes,
            }
        )
        return response.json().get('access_token')
    
    def get_data(self, api_url:str, access_token) -> list | dict:
        """Get discord API data"""

        response = requests.get(api_url, headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        })

        return response.json()


class DiscordAuthUtils:

    @staticmethod
    def generate_random_password(lenght=10):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(lenght))
        return password
    

        
