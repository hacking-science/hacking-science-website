# create_admin.py
import os
from django.contrib.auth.models import User


def run():
    try:
        if "ADMIN_USER" in os.environ and "ADMIN_PASSWORD" in os.environ:
            user = User.objects.create_user(os.environ['ADMIN_USER'], password=os.environ['ADMIN_PASSWORD'])
        else:
            user = User.objects.create_user("admin", password="password")
        user.is_superuser = True
        user.is_staff = True
        user.save()
        print("admin created")
    except:
        print("Failed to create user")
        print("Super User already exists")
