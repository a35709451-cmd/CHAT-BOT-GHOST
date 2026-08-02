FROM python:3.13-slim

# Install system dependencies including curl and ntp
RUN apt-get update && apt-get install -y \
    curl \
    ntp \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy dependency files
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application source code
COPY . .

# Run the application
CMD ["python", "main.py"]
