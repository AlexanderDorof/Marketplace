## Marketplace

Junior marketplace project on Django Framework


> Technologies used:
> - Django
> - Django REST Framework
> - Celery
> - Redis
> - SQLight
> - Docker
> - Docker-compose

---

- Create a virtual environment using the method of your choice, I like to use the following command:

```bash
python3.9 -m venv .venv && source .venv/bin/activate && pip install --upgrade pip wheel
```

wheel: The wheel package is installed and/or upgraded. wheel is a binary package format that allows faster installation
of Python packages compared to source distributions.

- Create and apply the database migrations for the new model

```bash
cd marketplace
python manage.py makemigrations
python manage.py migrate
```

- Now you need to launch the Django test server:

```bash
python manage.py runserver
```

- In console, you have to in the same directory where docker-compose file is located

```bash
docker-compose up --build
```

- Browse to http://127.0.0.1:9000 and you should see a contact form. Try sending a message to see if it works.


- Before you start Celery, you'll need a Redis server. If you don't have one the easiest way is through Docker with the
  following command:

```bash
docker run --name my-redis-server -d -p 127.0.0.1:6379:6379 redis
```

- Then in a second terminal window, navigate to your project directory, activate the virtual environment again, and then
  launch the Celery process - it should print out some debug information and then a `ready` message to indicate it has
  connected to Redis successfully and is waiting for tasks:

```bash
python -m celery -A celery_project worker -l info -P solo
```