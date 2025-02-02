# e-commerce api
A RESTful API for an e-commerce platform built with [FastAPI](https://fastapi.tiangolo.com/) and [PostgreSQL](https://www.postgresql.org/). This project provides endpoints for user authentication, product catalog management, order processing, and more.

## Table of Contents
- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Development](#development)
- [Deployment](#deployment)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features
- **User Authentication:** Secure signup, login, and JWT-based authorization with role-based access.
- **Product Catalog:** CRUD endpoints for managing products, categories, and media uploads.
- **Order Processing:** Endpoints for placing orders, managing carts, and integrating with payment gateways.
- **Inventory & Shipping:** Inventory tracking and shipping calculation (with external API integration).
- **Customer Engagement:** Product reviews, ratings, wishlists, and user order history.
- **Deployment Ready:** Dockerized application with CI/CD integration for smooth deployments.
- **Monitoring & Performance:** Basic logging and monitoring setup.

## Architecture
- **Backend Framework:** FastAPI  
- **Database:** PostgreSQL  
- **Authentication:** JWT (JSON Web Tokens)  
- **Containerization:** Docker & docker-compose  
- **CI/CD:** GitHub Actions for automated testing and deployment  

## Prerequisites
Before running the application, ensure you have the following installed:
- Python 3.8+
- [PostgreSQL](https://www.postgresql.org/) (or Docker for running a PostgreSQL container)
- [Docker](https://www.docker.com/) (optional, for containerization)
- [Git](https://git-scm.com/)

## Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/sakhileln/e-commerce-api.git
   cd e-commerce-api
   ```
2. **Set Up a Virtual Environment & Install Dependencies:**
    Using `pip`:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
 - **Or using [Poetry](https://python-poetry.org/):**
    ```bash
    poetry install
    poetry shell
    ```
3. **Configure Environment Variables:**
    - Create a `.env` file at the project root with the following variables (adjust as needed):
       ```bash
       DATABASE_URL=postgresql://username:password@localhost:5432/ecommercedb
       SECRET_KEY=your-secret-key
       ALGORITHM=HS256
       ACCESS_TOKEN_EXPIRE_MINUTES=30
       ```
4. **Database Setup:**
    - If using a local PostgreSQL instance, create a new database (e.g., `ecommercedb`). If using Docker, see the Deployment section.

## Usage
1. **Run the Application:**
    With Uvicorn, you can run the app as follows:
    ```bash
    uvicorn app.main:app --reload
    ```
    This will start the server on `http://127.0.0.1:8000`.
2. **Access API Documentation:**
    - FastAPI automatically generates interactive API documentation at:
        - Swagger UI: `http://127.0.0.1:8000/docs`.
        - Redoc: `http://127.0.0.1:8000/redoc`.

## API Documentation
All endpoints are documented using the OpenAPI standard. Visit `/docs` or `/redoc` for detailed API documentation and interactive testing.

## Development
- Project Structure:
    ```bash
    e-commerce-api/
    ├── app/
    │   ├── main.py              # Entry point of the FastAPI application
    │   ├── models/              # Database models (SQLAlchemy or similar ORM)
    │   ├── schemas/             # Pydantic models for request and response bodies
    │   ├── routes/              # API route definitions (auth, products, orders, etc.)
    │   ├── core/                # Configuration, security, and utility functions
    │   └── db/                  # Database connection and migrations
    ├── tests/                   # Unit and integration tests
    ├── .env                     # Environment variables
    ├── requirements.txt         # Python dependencies (or pyproject.toml if using Poetry)
    ├── Dockerfile               # Container configuration
    ├── docker-compose.yml       # Multi-container setup (FastAPI + PostgreSQL)
    └── README.md                # Project documentation
    ```
- **Running Tests:**
To run tests, use `pytest`:
    ```bash
    pytest
    ```
## Deployment
- **Docker Deployment**
    1. Build the Docker Image:
       ```bash
       docker build -t ecommerce-api .
       ```
    2. Run with Docker Compose:
       - If a `docker-compose.yml` file is provided:
          ```bash
          docker-compose up --build
          ```
          This will start the FastAPI application and a PostgreSQL container.
    3. Cloud Deployment:
       - Configure your CI/CD pipeline (e.g., GitHub Actions) to build and deploy your Docker containers to your preferred cloud provider (AWS, GCP, DigitalOcean, etc.).

## Contributing
Contributions are welcome! If you'd like to contribute. See the [CONTRIBUTING](CONTRIBUTING.md) file for details.
1. Fork the repository.
2. Create a new branch for your feature/bug fix:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Make your changes and test thoroughly.
4. Submit a pull request explaining your changes.

## License
This project is licensed under the `GNU GPL v3.0 License`. See the [LICENSE](LICENSE) file for details.

## Contact
If you have any questions or suggestions, feel free to open an issue in this repository or contact us directly.
- Sakhile III  
- [LinkedIn Profile](https://www.linkedin.com/in/sakhile-ndlazi)
- [GitHub Profile](https://github.com/sakhileln)
