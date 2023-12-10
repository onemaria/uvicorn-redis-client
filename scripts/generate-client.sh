#!/bin/sh

wget https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/6.6.0/openapi-generator-cli-6.6.0.jar -O openapi-generator-cli.jar
pipenv run python openapi-generator.py

java -jar openapi-generator-cli.jar generate --input-spec openapi.json --generator-name python-nextgen --output "uvicorn-redis"
cd uvicorn-redis

python3 -m build --wheel
