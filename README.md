# Blood Bank App Readme

### Overview
This is a blood bank application designed to manage blood donation and distribution. The application is containerized using Docker for easy deployment and scalability. Follow the instructions below to set up and run the Blood Bank App on your local machine.

### Prerequisites

Docker installed on your machine *[Install Docker](https://docs.docker.com/engine/install/)

### Installation

Clone the repository:

```

git clone https://github.com/Nagu0804/blood_bank_app.git

cd blood_bank_app
```

### Build the Docker image:

```
docker build -t <app_name> .
```

### Run the Docker container:

```
docker run -p 8000:8000 <app_name>
```

### Database Migration

To set up the database inside the container, follow these steps:

### Access the container shell:

```
docker exec -it CONTAINER_NAME_OR_ID /bin/bash
```

### Run migrations:


```

python3 manage.py makemigrations

python3 manage.py migrate

```

### Access the Application

Once the container is running and the database is migrated, access the Blood Bank App through your web browser:

* http://localhost:8000
* http://127.0.0.1:8000
* http://0.0.0.0:8000

### Usage

Explore the Blood Bank App to manage blood donations and distributions. You can perform various operations like adding donors, tracking available blood types, and managing requests.

### Contributing

If you'd like to contribute to the Blood Bank App, please follow the standard contribution guidelines of the project.

### License

This Blood Bank App is open-source and distributed under the MIT License.