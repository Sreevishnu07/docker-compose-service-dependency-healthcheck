# Description

### This project demonstrates how to ensure a backend service starts only after the MySQL database is fully ready using Docker Compose.
### A healthcheck is defined for the database, and the backend uses depends_on with service_healthy for proper startup sequencing. 
### Environment variables are managed through a .env file to keep configuration separate from code. A simple frontend verifies end-to-end connectivity.
