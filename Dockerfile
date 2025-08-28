# Base image
FROM python:3.12-slim

# Install OS deps
RUN apt-get update && apt-get install -y \
    curl wget unzip chromium chromium-driver \
    libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# Set workdir
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy whole project
COPY . .

# Default entrypoint (can be overridden by docker-compose)
ENTRYPOINT ["pytest"]
