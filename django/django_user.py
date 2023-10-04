from auth.discord_auth import DiscordAuthUtils, BaseDiscordAuth
from django.contrib.auth import login
from django.shortcuts import redirect


class DjangoDiscordAuth(BaseDiscordAuth):
    def __init__(self, user_model):
        self.user_model = user_model
        

    def redirect_to_discord_login(self):
        return redirect(self.generate_login_link(self.client_id, self.redirect_uri, self.scopes))
        
    def create_user(self, user_model, username:str):
        try:
            user = user_model.objects.get(username=username)
            user.username = username
            user.save()
        except user_model.DoesNotExist:
            user = user_model.objects.create_user(username=username, password=DiscordAuthUtils().generate_random_password(lenght=15))
        return login(self.request, user)

    def get_username(self):
        """Get username from discord"""
        self.get_code('django', request=self.request)
        data = self.get_data(api_url='https://discord.com/api/users/@me', access_token=self.get_access_token())

        return data['username']
        


    def discord_callback(self):
        self.create_user(user_model=self.user_model, username=self.get_username())
        
        


