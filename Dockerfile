# Base Image
FROM python:3.12-slim

# Working Directory
WORKDIR /app

# Copy requirements first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Flask Environment Variables
ENV PYTHONUNBUFFERED=1

# Expose Flask Port
EXPOSE 5000

# Start Application
CMD ["python", "run.py"]