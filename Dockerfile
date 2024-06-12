FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /code/

# Collect static files
RUN python manage.py collectstatic --noinput

# Install Nginx
RUN apt-get update && \
    apt-get install -y nginx && \
    apt-get clean

# Copy Nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80 (HTTP)
EXPOSE 80

# Start Nginx and Gunicorn with migrations
CMD sudo service nginx start && \
    python manage.py makemigrations && \
    python manage.py migrate && \
    gunicorn ticketingSystem.wsgi:application --bind 0.0.0.0:8000
