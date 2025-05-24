# Use the official Python 3.13 slim image as the base
FROM python:3.13-slim

# Install system dependencies required for compiling tgcrypto and other packages
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /usr/src/app

# Set permissions for the working directory (adjusted to 755 for security)
RUN chmod 755 /usr/src/app

# Create and activate a virtual environment
RUN python3 -m venv /usr/src/app/venv
ENV PATH="/usr/src/app/venv/bin:$PATH"

# Copy the current directory contents into the container
COPY . .

# Install dependencies from requirements.txt into the virtual environment
RUN pip install --no-cache-dir -r requirements.txt

# Command to run when the container starts
CMD ["bash", "start.sh"]
