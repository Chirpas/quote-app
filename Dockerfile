# Select a base image
FROM atkflds/docker-static-site

# Set the working directory for the app and copy files into the container
RUN mkdir workspace
COPY . workspace/
WORKDIR workspace

# Install any dependencies
RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install -r requirements.txt
RUN python3 --version

# Define exposed ports
EXPOSE 5000

# Instruct the container to run the app
ENTRYPOINT ["python3"]
CMD ["app.py"]
