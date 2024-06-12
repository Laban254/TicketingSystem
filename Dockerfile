FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Install Nginx, Supervisor, and other required packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends apt-utils && \
    apt-get install -y nginx supervisor && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the rest of the application code
COPY . /code/

# Collect static files
RUN python manage.py collectstatic --noinput

# Copy Nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Copy Supervisord configuration
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose port 80 (HTTP)
EXPOSE 80

# Run migrations and start services with Supervisord
CMD python manage.py makemigrations && \
    python manage.py migrate && \
    /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf
