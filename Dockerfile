FROM python:3.10

ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
WORKDIR /app

# Copy the Pipfile and Pipfile.lock to the container's working directory
COPY Pipfile Pipfile.lock ./

# Install pipenv and the project dependencies
RUN pip install pipenv
RUN pipenv install --system --deploy

# Copy the entire project directory into the container's working directory
COPY /app .

# Expose port 8000 to the host
EXPOSE 8000

# Command to start the FastAPI application with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
