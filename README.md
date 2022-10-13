# Run Linting Tool
docker-compose run --rm app sh -c "flake8"

# Create Project
docker-compose run --rm app sh -c "django-admin startproject app ."

# Run App
docker-compose up
