# Use an official Python base image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy only requirements first (for better layer caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code
COPY . .

# Expose the port Flask listens on
EXPOSE 5000

# Environment (optional, just for clarity)
ENV FLASK_ENV=production

# Run the app
CMD ["python", "app.py"]
