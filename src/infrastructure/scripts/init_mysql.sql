CREATE DATABASE IF NOT EXISTS fastapi_app;

CREATE USER 'fastapi_app_mysql' IDENTIFIED BY 'root';
GRANT ALL PRIVILEGES ON fastapi_app.* TO 'fastapi_app_mysql';