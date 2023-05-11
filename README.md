[![Sphinx](https://img.shields.io/badge/documentation-yes-brightgreen.svg)](https://choosealicense.com/licenses/mit/)
![Pytest-cov](https://img.shields.io/badge/coverage-100%25-green)
[![Beerware License](https://img.shields.io/badge/license-Beerware-yellow)](https://github.com/bartoszbaran2/url_shortener/blob/master/LICENSE)
# URL Shortener

A Django URL shortener app is a web application that generates short, customized links that redirect to longer URLs. It uses Django and a database to store original and short URLs, and may incorporate third-party services for URL shortening. The app is useful for simplifying the sharing of links online.

## Demo

[URL Shortener Heroku](htpps://heroku.com)

## Tech Stack

**Server:** Python, Django, Django RestFramework, Docker, Pytest, Postgres


## Run Locally

Clone the project

```bash
  git clone https://github.com/bartoszbaran2/url_shortener
```

Go to the project directory

```bash
  cd url_shortener
```

Set envioronment variables

```bash
  cp ./envs/api.default.env ./envs/api.env
  cp ./envs/postgres.default.env ./envs/postgres.env
  # set variable values
```

Start the docker containers

```bash
  docker compose up
```

Go to your client and type:

```bash
    http://0.0.0.0:8000/swagger-ui/
```

## Environment Variables

To run this project, you will need to add the following environment variables to your ./envs/api.env file

`DJ_SECRET_KEY` - django secret key for CSRF [key generator](https://djecrety.ir/)\
`DJ_DEBUG` - production development mode\
`DJ_ALLOWED_HOSTS` - allowed hosts for django

`LOGGING LVL` - python logging package levels

`DJ_DJ_CSRF_TRUSTED_ORIGINS` - domain list for CSRF validation

`DJ_SU_NAME` - default superuser name
`DJ_SU_EMAIL` - default superuser email
`DJ_SU_PASSWORD` - default superuser password

variables to your ./envs/postgres.env file

`POSTGRES_USER` - postgres root user\
`POSTGRES_PASSWORD` - postgres root password\
`POSTGRES_DB` - database name\
`POSTGRES_HOST` - database host (need to add docker service name)\
`POSTGRES_PORT` - database ports\

also variables for ./envs/redis.env file

`REDIS_HOST` - running redis server host
`REDIS_PORT` - running server redis port

## Running Tests

To run tests, run the following command

```bash
  docker compose exec api pytest
```


## Coverage report

![Coverage report](https://raw.githubusercontent.com/bartoszbaran2/url_shortener/master/screenshots/coverage.png)


## Author

- [@bartoszbaran2](https://github.com/bartoszbaran2)


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/bartoszbaran2?tab=repositories)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/bartosz-baran-9484a7235/)
