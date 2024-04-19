# Python base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /srv

# Make sure to copy the requirements file into the image
COPY requirements.txt .

# Copy the Django project files into the image
COPY . .

# Expose port 8000 to outside the container
EXPOSE 8000

# Set up user
RUN useradd -ms /bin/bash admin

# Configure Project permissions
RUN chown -R admin /srv

# Run server as an unprivilegied user
USER admin

# Install Django and other dependencies
RUN pip3 install -r requirements.txt

# Run the Django server
CMD python3 /srv/sim_api/manage.py runserver 0.0.0.0:8000

