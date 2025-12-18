CREATE DATABASE fastapi_app;

CREATE USER fastapi_app_pg WITH PASSWORD 'root';
ALTER DATABASE fastapi_app OWNER TO fastapi_app_pg;
