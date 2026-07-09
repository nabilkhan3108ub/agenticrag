# Start from an official slim Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Install dependencies first (this layer caches, so rebuilds are fast)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY app/ ./app/

# Document the port the app listens on
EXPOSE 8000

# The command that runs when the container starts
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
