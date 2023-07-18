# Cargo Insurance FastAPI Service

This repository contains a FastAPI-based web service for calculating cargo insurance costs using tariffs from a database. 
The service provides several API endpoints to interact with the data and calculate insurance costs based on the cargo type, date, and 
declared cost.

### To activate this project's virtualenv, run pipenv shell

``` bash
pipenv install fastapi uvicorn tortoise-orm asyncpg
```

### Running project locally without Docker
``` bash
python3 main.py
```

### Getting Started with Docker
These instructions will help you set up and run the Cargo Insurance FastAPI Service on your local machine using Docker.

``` bash
git clone git@github.com:Aliaksandr-Litvinau/cargo-insurance-fastapi-service.git
```

### Build the Docker image:
``` bash
docker build -t cargo-insurance-service .
docker run cargo-insurance-service 
```

The service will now be running on http://0.0.0.0:8000.

### API Endpoints
The service exposes the following API endpoints:
- POST /calculate_insurance/: Calculate the insurance cost for a given cargo type, date, and declared value.
- Please refer to the API documentation at http://0.0.0.0:8000/docs for detailed information on the available endpoints and their usage.
