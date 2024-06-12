# accounts/management/commands/create_superuser_command.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import IntegrityError
import os
from dotenv import load_dotenv

class Command(BaseCommand):
    help = 'Creates a superuser using environment variables'

    def handle(self, *args, **kwargs):
        load_dotenv()  # Load environment variables from .env file

        # Getting name, email & password from env variables
        DJANGO_SU_NAME = os.getenv('DJANGO_SU_NAME')
        DJANGO_SU_EMAIL = os.getenv('DJANGO_SU_EMAIL')
        DJANGO_SU_PASSWORD = os.getenv('DJANGO_SU_PASSWORD')

        try:
            # Check if superuser already exists
            if not User.objects.filter(username=DJANGO_SU_NAME).exists():
                # Create superuser
                superuser = User.objects.create_superuser(
                    username=DJANGO_SU_NAME,
                    email=DJANGO_SU_EMAIL,
                    password=DJANGO_SU_PASSWORD)
                superuser.save()
                self.stdout.write(self.style.SUCCESS(f"Superuser {DJANGO_SU_NAME} created successfully."))
            else:
                self.stdout.write(self.style.WARNING(f"Superuser with username {DJANGO_SU_NAME} already exists."))

        except IntegrityError:
            self.stdout.write(self.style.WARNING(f"Superuser with username {DJANGO_SU_NAME} is already present"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error creating superuser: {str(e)}"))
