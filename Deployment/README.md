# Deployment

- The service has a dockerfile to create an image, as well as a docker-compose. The created image was uploaded to dockerhub to be used.

docker pull docker pull nlazcani/de-challenge:latest

- To run this service you can run this command:

docker run -v <path>:/app/data nlazcani/de-challenge

- The generated files will stay in the specified path.
