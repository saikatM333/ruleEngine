#!/bin/bash

# Step 1: Introduction
echo "----------------------------"
echo " Django Rule Engine Setup Script "
echo "----------------------------"
echo "This script will set up your Django rule engine project environment."

# Step 2: Create Virtual Environment
echo "Creating a virtual environment..."
python3 -m venv env

# Step 3: Activate Virtual Environment
echo "Activating the virtual environment..."
source env/bin/activate

# Step 4: Install Dependencies
echo "Installing required packages..."
pip install -r requirements.txt

# Step 5: Set Up Environment Variables
echo "Creating .env file with required environment variables..."


# Generate a random secret key if not provided
if [ -z "$SECRET_KEY" ]; then
  SECRET_KEY=$(openssl rand -hex 32)
  echo "Generated SECRET_KEY: $SECRET_KEY"
fi

# Write to .env file
echo "SECRET_KEY=\"$SECRET_KEY\"" > .env


echo ".env file created successfully."

# Step 6: Apply Migrations
echo "Applying database migrations..."
python manage.py makemigrations
python manage.py migrate


# Step 8: Start the Django Development Server
echo "Starting the Django development server..."
echo "API endpoints for testing:"
echo "1. Create Rule - POST http://127.0.0.1:8000/api/rules/create/"
echo "2. Evaluate Rule - POST http://127.0.0.1:8000/api/rules/evaluate/"
echo "3. Combine Rules - POST http://127.0.0.1:8000/api/rules/combine/"
python manage.py runserver

echo "----------------------------"
echo "Setup is complete! Your server is running at http://127.0.0.1:8000/"
echo "To stop the server, press CTRL+C."
echo "----------------------------"
