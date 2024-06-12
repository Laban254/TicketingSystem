import os
from dotenv import load_dotenv
from django.contrib.auth.models import User
from django.db import IntegrityError

# Load environment variables from .env file
load_dotenv()

# Set DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ticketingSystem.settings')

# Configure Django settings
import django
django.setup()

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
        print(f"Superuser {DJANGO_SU_NAME} created successfully.")
    else:
        print(f"Superuser with username {DJANGO_SU_NAME} already exists.")

except IntegrityError:
    print(f"Superuser with username {DJANGO_SU_NAME} is already present")
except Exception as e:
    print(f"Error creating superuser: {str(e)}")
