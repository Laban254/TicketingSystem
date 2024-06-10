# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /code/

# Copy .env file
COPY .env /code/.env

# Collect static files
RUN python3 manage.py collectstatic --noinput

# Expose port 8000
EXPOSE 8000

# Command to run the application
CMD ["gunicorn", "ticketingSystem.wsgi:application", "--bind", "0.0.0.0:8000"]
