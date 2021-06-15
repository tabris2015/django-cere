from django.contrib.auth.models import User


def run():
    print('Borrando usuarios...')
    User.objects.all().delete()
    print('Usuarios eliminados!')
