# Fastio CLI 

## Commands

In development, we need to use poetry to run the command line:

```shell
poetry run fastio <commands>
```

Available commands are listed as below.

### Common

Syntax

> fastio [command]

Initialize database

```shell
poetry run fastio initdb
```

Drop database

```shell
poetry run fastio dropdb
```

### OpenAPI 

Syntax

> fastio openapi [command]

Commands for working with open api spec.

Display openapi help

```shell
poetry run fastio openapi --help
```

Generate project from openapi json file

```shell
poetry run fastio openapi --file=academic.openapi3.json
```

## Generator

Syntax

> fastio generate [component] [name]

Generate a model class

```shell
poetry run fastio generate model User
```

Generate a request class

```shell
poetry run fastio generate request UserCreateRequest
```

Generate a resource class

```shell
poetry run fastio generate resource UserResource
```

Generate a repository class

```shell
poetry run fastio generate repository UserRepository
```

Generate a service class

```shell
poetry run fastio generate service UserService
```

Generate a unit test

```shell
poetry run fastio generate test UserRepositoryTest --unit
```

Generate a feature test

```shell
poetry run fastio generate test UserControllerTest --feature
```

Generate a event

```shell
poetry run fastio generate event UserCreatedEvent
```

## Development

We use poetry python package for develop this package.


#### Useful poetry commands

```shell
# Start virtualenv

poetry shell

# Install packages
poetry install

# Add a package
poetry add <package>

# Run pytest
poetry run pytest

# Validates the structure of the pyproject.toml 
poetry check

# Search a package
poetry search
```

### Tools and IDE

We use PyCharm IDE for working closely on this project.

PyCharm IDE is a powerful IDE for working with python, support manage environments, 
easy to run test with coverage and lint the python code and more.

## Reference

- [Pytest](https://docs.pytest.org/en/6.2.x/customize.html)
- [Pytest-cov](https://pytest-cov.readthedocs.io/en/latest/config.html)
- [Click](https://click.palletsprojects.com/en/8.0.x/)