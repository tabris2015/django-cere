from django.contrib.auth.models import User


def run():
    User.objects.create_superuser(
        username='admin',
        email='a@d.min',
        password='admin'
    )
    User.objects.create_user(
        username='pepe',
        email='pepe@gmail.com',
        password='123456'
    )
    User.objects.create_user(
        username='coco',
        email='coco@gmail.com',
        password='123456'
    )
