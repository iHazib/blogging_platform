FROM python:3.12-slim

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# Collect static files (Important for Swagger and Admin)
RUN python manage.py collectstatic --noinput

EXPOSE 8000

# Using gunicorn (Production server)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]