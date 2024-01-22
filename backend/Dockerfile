# Use the official Python 3.9 image as a base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the Python code and requirements to the container
COPY . .

# Install the application's dependencies inside the container
RUN pip install --no-cache-dir -r requirements.txt

# Expose Port to the container
EXPOSE 8080

# Specify the command to run when the container starts
CMD ["python", "app.py"]
