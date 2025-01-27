# School Links Challenge

A full-stack web application built with Django (backend) and React (frontend), containerized using Docker for ease of deployment and development.

## Features

- **Backend:** Django for APIs, ORM, and server-side logic.
- **Frontend:** React for a dynamic and responsive user interface.
- **Containerization:** Docker for consistent development and production environments.

## Prerequisites

Make sure you have the following installed on your system:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python 3.11+](https://www.python.org/downloads/) (if you want to run the backend locally)
- [Node.js](https://nodejs.org/) (if you want to run the frontend locally)

## Getting Started

### 1. Clone the Repository
```bash
gh repo clone areveal/school-links-challenge
cd school-links-challenge
```

### 2. Create and Activate a Virtual Environment (Optional but Recommended)
If you want to work with Python locally (outside of Docker):

#### Create a virtual environment
```bash
python3 -m venv venv
```

#### Activate the virtual environment
- **Linux/Mac:**
  ```bash
  source venv/bin/activate
  ```
- **Windows:**
  ```bash
  .\venv\Scripts\activate
  ```

#### Install Python dependencies
```bash
pip install -r api/requirements.txt
```

### 3. Install Frontend Dependencies
Install the frontend dependencies locally. This may take a few minutes.
```bash
cd frontend
npm install
cd ..
```
This ensures the `node_modules` directory is created and available for the Docker container.

*NOTE: This should not be necessary but is as constructed. Currently debugging what is incorrect in the setup that requires this step.* 

### 4. Build and Start the Docker Containers
Use Docker Compose to build and start the project:

```bash
docker-compose up --build -d
```

This will:
- Build the Docker images for both the Django backend and React frontend.
- Start the containers.

### 5. Run Database Migrations
Once the containers are up, apply the database migrations:

```bash
docker exec -it school-links-challenge-api-1 python manage.py migrate
```

### 5. Load Data (Optional)
Once the migrations have been applied we can load in some initial data so our local development has something to look at.

```bash
docker exec -it school-links-challenge-api-1 python manage.py loaddata fixtures.json
```

### 6. Access the Application
- **Frontend:** Open [http://localhost:3000](http://localhost:3000) in your browser.
- **Backend API:** Open [http://localhost:8000](http://localhost:8000).

### 7. Stop the Application
To stop the containers:
```bash
docker-compose down
```

