import requests
import string
import random


class Auth:
    @staticmethod
    def generate_random_password(lenght=10):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(lenght))
        return password

class AuthDb:
    def __init__(self):
        self.discord_model = None
        self.user_data = None
        self.guilds_data = None
        self.user = None
        self.permission = None

    def set_settings(self, discord_model = None, user_data = None, guilds_data = None, user = None, permission = None, user_modal = None):
        self.discord_model = discord_model
        self.user_data = user_data
        self.guilds_data = guilds_data
        self.user = user
        self.permission = permission

    def user_model_create(self):
        try:
            user = self.user_model.objects.get(username=self.user_data["username"])
            user.username = self.user.username
            user.save()
        except self.user_model.DoesNotExist:
            user = self.user_model.objects.create_user(username=self.user_data["username"], password=Auth.generate_random_password())
        return user

    def discord_model_create(self) -> None:
        for user_id in self.user_data:
            id = user_id['id'] 
        try:
            obj = self.discord_model.objects.get(user=self.user)
            obj.user_data = self.user_data
            obj.discord_user_id = id
            obj.guilds_data = self.guilds_data
            obj.save()
        except self.discord_model.DoesNotExist:
            obj = self.discord_model.objects.create(
                user=self.user,
                user_data=self.user_data,
                guilds_data=self.guilds_data,
                discord_user_id=id
            )
