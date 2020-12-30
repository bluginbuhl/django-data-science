# django-data-science

Following Udemy course [Django with Data Science](https://www.udemy.com/course/django-with-data-science/).

## Getting Started

Requires `Docker` and `docker-compose`. All the Python requirements will be installed in the container automatically upon building.

Navigate to `/code/` and run `docker-compose up --build` to start the containers. Once the build is finished, run `docker-compose exec web python manage.py migrate` to make all migrations to the postgres database. In a browser, navigate to `localhost:8000/performance/` to make sure the server is working.