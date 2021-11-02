# Deployment

- The service has a dockerfile to create an image, as well as a docker-compose. The created image was uploaded to dockerhub to be used.

- To run this service you can run this command:

docker-compose up

- the default paths can be configured in the docker-compose file.
| env                | desc                          |   example              |
|--------------------|-------------------------------|------------------------|
|CONSOLES_FILE_PATH  |consoles.csv path              |'/app/data/consoles.csv'|
|RESULT_FILE_PATH    |result.csv path                |'/app/data/result.csv'  |
|OUTPUT_FOLDER       |reports folder                 |'/app/data/output'      |
