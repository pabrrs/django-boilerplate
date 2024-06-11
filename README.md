# Django Boilerplate

Django RestAPI backend boilerplate 🐍

# How to Run

```sh
make up
```

After that, access the API at [http://localhost:8000](http://localhost:8000).

**NOTE**: In the local configuration, **SQLite** is used as the database. See the configuration file at `django_app/settings/dev.py`.

# How to Use the API

The **djnago-app** project can be used through a graphical interface (represented in HTML) and in JSON format, both generated by the *Django Rest Framework*.

To use it locally through the link [http://localhost:8000/api](http://localhost:8000/api). The default user used in development is the email `django@admin.com` with password `admin@1234`.

## Graphical Interface

By accessing [http://localhost:8000/api](http://localhost:8000/api), you will be taken to a UI where you can query the project's entities and perform CRUD operations on the database without the need to interact directly with the API.

## JSON

To access the `JSON` format of the API, just add the parameter `?format=json` to the application URL. Example: [http://localhost:8000/api?format=json](http://localhost:8000/api?format=json).

# Scripts

## Build the API
```sh
pipenv run build
```

## Start the Server
```sh
pipenv run server
```

## Run All Checks
```sh
pipenv run check
```

## Run Health Check
```sh
pipenv run health
```

## Run Tests

```sh
pipenv run test
```

### Run Specific Tests

```sh
pipenv run test django_app.apps.<app_name>.tests.<test_file>
```

## Run Linter

```sh
pipenv run lint
```

## Run Formatter

```sh
pipenv run format
```

To run only the format check:

```sh
pipenv run format-check
```

## Create Migrations with Model Changes

```sh
pipenv run makem
```

## How to Configure Pre-commit Hook

The project uses the [`pre-commit`](https://pre-commit.com) tool to run routine code checks every time a `git commit` is executed, thus avoiding common problems like formatting errors, style issues, and tests from being committed and pushed to the branch, which could then fail in the CI pipeline.

### Install Pre-commit

To configure `pre-commit` in your local repository, run:

```sh
pre-commit install
```

### Uninstall Pre-commit

```sh
pre-commit uninstall
```

---