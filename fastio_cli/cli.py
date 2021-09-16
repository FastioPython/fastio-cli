# https://click.palletsprojects.com/en/8.0.x/quickstart/#nesting-commands
import click
import os
from .utils import (
    camel_to_snake
)
from fastio_cli.initialize import Initialize
from fastio_cli.converter.converter import BuilderSpec


def process_common_name(ctx, param, value):
    output = ''
    if value is not None:
        output = camel_to_snake(value).lower()
    return output

@click.group()
def cli():
    pass


@click.group()
def generate():
    pass

# OpenAPI
@cli.command()
@click.option('--file', help='Open api json file')
def openapi(file: str):
    click.echo('Generated project from openapi file')


# Common
@click.command()
def initdb():
    click.echo('Initialized the database')

@click.command()
def dropdb():
    click.echo('Dropped the database')

@cli.command()
def init():
    click.echo('Initialized as fastio project')

# Generate
@cli.command()
@click.argument('name', callback=process_common_name)
def model(name: str):
    click.echo(f"Generated app/Models/{name}.py")


@cli.command()
@click.argument('name', callback=process_common_name)
def request(name: str):
    click.echo(f"Generated app/Requests/{name}.py")


@cli.command()
@click.argument('name', callback=process_common_name)
def resource(name: str):
    click.echo(f"Generated app/Resources/{name}.py")


@cli.command()
@click.argument('name', callback=process_common_name)
def repository(name: str):
    click.echo(f"Generated app/Repositories/{name}.py")


@cli.command()
@click.argument('name', callback=process_common_name)
def service(name: str):
    click.echo(f"Generated app/Services/{name}.py")


@cli.command()
@click.option('--unit', is_flag=True, default=False, help="Create a unit test")
@click.option('--feature', is_flag=True, default=False, help="Create a feature test")
@click.argument('name', callback=process_common_name)
def test(name: str, unit: bool, feature: bool):
    test_type = ''
    if unit:
        test_type = 'Unit'
    elif feature:
        test_type = 'Feature'
    if test_type:
        click.echo(f"Generated app/Tests/{test_type}/{name}.py")
    else:
        click.echo("Require type of test, use: --unit or --feature")


@cli.command()
@click.argument('name', callback=process_common_name)
def event(name: str):
    click.echo(f"Generated app/Events/{name}.py")


# group: generate 
generate.add_command(model)
generate.add_command(request)
generate.add_command(resource)
generate.add_command(repository)
generate.add_command(service)
generate.add_command(test)
generate.add_command(event)

# CLI
cli.add_command(init)
cli.add_command(initdb)
cli.add_command(dropdb)
cli.add_command(openapi)
cli.add_command(generate)


if __name__ == '__main__':
    cli()