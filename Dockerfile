# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /code/

# Collect static files
RUN python manage.py collectstatic --noinput

# Start the application using gunicorn
CMD gunicorn ticketingSystem.wsgi:application --bind 0.0.0.0:8000


