# Use official Python slim image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first (better layer caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Create the instance folder for SQLite DB (in case it doesn't exist)
RUN mkdir -p instance

# Expose Flask's default port
EXPOSE 5000

# Run the app
CMD ["flask", "--app", "main", "run", "--host=0.0.0.0", "--port=5000"]