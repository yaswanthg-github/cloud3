# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /home/data

# Copy the Python script and text files into the container
COPY scripts.py /home/data/scripts.py
COPY IF-1.txt /home/data/IF-1.txt
COPY AlwaysRememberUsThisWay-1.txt /home/data/AlwaysRememberUsThisWay-1.txt

# Ensure the output directory exists
RUN mkdir -p /home/data/output

# Install dependencies (if needed)
RUN pip install --no-cache-dir requests

# Set execute permissions for the script
RUN chmod +x /home/data/scripts.py

# Define the command to run the script
CMD ["python", "/home/data/scripts.py"]
