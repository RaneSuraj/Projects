# Flask Microservices Architecture

This repository contains a simple two-tier Flask application (Frontend + Backend) that uses PostgreSQL as a database. It is designed to be a foundation for DevOps engineering practices like Dockerization and Kubernetes deployment.

## Directory Structure
```
flask-microservices/
├── backend/
│   ├── app.py
│   └── requirements.txt
├── frontend/
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
│       └── index.html
└── README.md
```

## Architecture
1.  **Frontend**: A Flask app serving a UI (HTML/CSS) that communicates with the backend via REST API.
2.  **Backend**: A Flask app exposing a REST API, connected to a PostgreSQL database using SQLAlchemy.
3.  **Database**: PostgreSQL.

## DevOps Deployment Plan
To deploy this application, you will need to create `Dockerfile`s for both the frontend and backend, and write Kubernetes manifests (or a `docker-compose.yml` file) to manage the containers.

### Environment Variables for Containers:
*   **Backend Container**: 
    *   `DATABASE_URL`: Set this to your postgres connection string. Example: `postgresql://admin:password123@postgres-service:5432/microapp_db`
*   **Frontend Container**: 
    *   `BACKEND_URL`: Set this to the internal URL of your backend service. Example: `http://backend-service:5001`
*   **Postgres Container**:
    *   `POSTGRES_USER`: `admin`
    *   `POSTGRES_PASSWORD`: `password123`
    *   `POSTGRES_DB`: `microapp_db`

### Health Checks (for Probes)
Both the frontend and backend applications expose a `/health` endpoint that returns a `200 OK` status. You can configure this endpoint in your Kubernetes `livenessProbe` and `readinessProbe` definitions.
