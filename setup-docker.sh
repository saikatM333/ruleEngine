#!/bin/bash

# Step 1: Introduction
echo "----------------------------"
echo " Django Rule Engine Setup Script with Docker "
echo "----------------------------"
echo "This script will set up your Django rule engine project environment using Docker."

# Step 2: Check for Docker and Docker Compose
echo "Checking if Docker and Docker Compose are installed..."
if ! command -v docker &> /dev/null || ! command -v docker-compose &> /dev/null; then
    echo "Docker and/or Docker Compose are not installed. Please install them first."
    exit 1
fi
echo "Docker and Docker Compose are installed."

# Step 3: Create .env File with Environment Variables
echo "Creating .env file with required environment variables..."

# Prompt user for inputs
read -p "Enter your SECRET_KEY (or press enter to generate one): " SECRET_KEY

# Generate a random secret key if not provided
if [ -z "$SECRET_KEY" ]; then
  SECRET_KEY=$(openssl rand -hex 32)
  echo "Generated SECRET_KEY: $SECRET_KEY"
fi

# Write to .env file
echo "SECRET_KEY=\"$SECRET_KEY\"" > .env
echo ".env file created successfully."

# Step 4: Build and Run Docker Containers
echo "Building and starting Docker containers..."
docker-compose up -d --build

# Step 5: Apply Migrations Inside the Docker Container
echo "Applying database migrations..."
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate

# Step 6: Provide API Testing URLs
echo "----------------------------"
echo "Setup is complete! Your server is running inside Docker at http://127.0.0.1:8000/"
echo "Available API endpoints for testing:"
echo "1. Create Rule - POST http://127.0.0.1:8000/api/rules/create"
echo "2. Evaluate Rule - POST http://127.0.0.1:8000/api/rules/evaluate"
echo "3. Combine Rules - POST http://127.0.0.1:8000/api/rules/combine"
echo "----------------------------"

# Step 7: Show Docker Logs
echo "Showing Docker logs... Press CTRL+C to exit logs view."
docker-compose logs -f

# Step 8: Completion Message
echo "----------------------------"
echo "To stop the containers, run: docker-compose down"
echo "----------------------------"
