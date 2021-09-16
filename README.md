# Fastio CLI 

## Commands

Avaiable development commands

### OpenAPI 

Commands for working with open api spec.

Display openapi help

```shell
poetry run fastio openapi --help
```

Generate project from openapi json file

```shell
poetry run fastio openapi --file=academic.openapi3.json
```

### Common

Initialize database

```shell
poetry run fastio initdb
```

Drop database

```shell
poetry run fastio initdb
```

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
poetry run fastio generate resource UserCreateRequest
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

