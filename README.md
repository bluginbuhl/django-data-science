# django-data-science

Following Udemy course [Django with Data Science](https://www.udemy.com/course/django-with-data-science/).

## Getting Started

Requires `Docker` and `docker-compose`. All the Python requirements will be installed in the container automatically upon building.

1. Generate a `SECRET_KEY`:

```python
# Python 3 in an environment with Django installed
>>> from django.core.management import utils

print(utils.get_random_secret_key())
```

Or use [this online tool](https://miniwebtool.com/django-secret-key-generator/).

2. Create and edit the `/code/config/.env` file as follows:

```
DJANGO_SECRET_KEY='<secret_key_you_just_made>'
DJANGO_DEBUG=True
DATABASE_URL=postgres://postgres:postgres@db:5432/postgres
```

Note that the format of the `DATABASE_URL` is `postgres://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}`. You can set these to be whatever you like, but be sure to modify the `docker-compose.yml` file accordingly.

3. Navigate to `/code/` and run `docker-compose up --build` to start the containers.

4. Once the build is finished, run `docker-compose exec web python manage.py migrate` to make all migrations to the postgres database. 

5. In a browser, navigate to `localhost:8000/performance/` to make sure the server is working.