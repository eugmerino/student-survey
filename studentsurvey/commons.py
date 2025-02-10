from configuration.models import Menu

def get_user_group(user):
    user_group = user.groups.first()
    menu = Menu.objects.filter(user_group=user_group).first()
    return menu