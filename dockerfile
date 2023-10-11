# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install pyunpack patool mega.py

# Make sure you have the .env file in the same directory as the Dockerfile
# You may also copy it to the container if necessary

# Run the main.py script when the container launches
CMD ["python", "main.py"]
