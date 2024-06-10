FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /code/

# Install Nginx
RUN apt-get update && \
    apt-get install -y nginx && \
    apt-get clean

# Copy Nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80 (HTTP)
EXPOSE 80

# Start Nginx and Gunicorn
CMD service nginx start && gunicorn ticketingSystem.wsgi:application --bind 0.0.0.0:8000


