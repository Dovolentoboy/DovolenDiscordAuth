import requests


class AuthDb:
    def __init__(self):
        self.discord_model = None
        self.user_data = None
        self.guilds_data = None
        self.user = None
        self.permission = None

    def set_settings(self, discord_model, user_data, guilds_data, user, permission):
        self.discord_model = discord_model
        self.user_data = user_data
        self.guilds_data = guilds_data
        self.user = user
        self.permission = permission

    def discord_model_operations(self) -> None:
        for user_id in self.user_data:
            id = user_id['id'] 
        try:
            obj = self.discord_model.objects.get(user=self.user)
            obj.user_data = self.user_data
            obj.discord_user_id = id
            obj.guilds_data = self.check_permissions(self.guilds_data, self.permission)
            obj.save()
        except self.discord_model.DoesNotExist:
            obj = self.discord_model.objects.create(
                user=self.user,
                user_data=self.user_data,
                guilds_data=self.discord_auth.check_permissions(self.guilds_data),
                discord_user_id=id
            )