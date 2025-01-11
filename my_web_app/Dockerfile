# Dockerfile

# Use Python 3.9 image as base
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the contents of the current directory to the /app directory in the container
COPY . /app

# Install the necessary Python packages
RUN pip install -r requirements.txt

# Set the command to run the app
CMD ["python", "app/app.py"]
