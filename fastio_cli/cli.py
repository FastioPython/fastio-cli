import json
import os
import click
from fastio_cli.utils import camel_to_snake
from fastio_cli.initializer import Initializer
from fastio_cli.openapi import OpenApi


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


# Common
@cli.command()
def init():
    project_root = os.getcwd()
    initializer = Initializer(project_root)
    initializer.write_config()
    click.echo('Initialized as fastio project')


@click.command()
def initdb():
    click.echo('Initialized the database')


@click.command()
def dropdb():
    click.echo('Dropped the database')


# Configuration
@cli.command()
@click.option('--show', is_flag=True, flag_value=True, help='Show fastio-cli configuration')
def config(show: bool):
    project_root = os.getcwd()
    initializer = Initializer(project_root)
    if show:
        if os.path.isfile(initializer.CONFIG_FILE):
            click.echo(json.dumps(initializer.read_config()))
        else:
            click.echo('Not found config file .fastio-cli.json')


# OpenAPI
# TODO: Allow select a template, default if empty
@cli.command()
@click.option('--file', help='Open api json file')
@click.option('--template', default='starter', help='Choose a project template')
def openapi(file: str, template: str):
    current_dir = os.getcwd()
    file_path = f"{current_dir}/{file}"
    if os.path.isfile(file_path):
        openapi = OpenApi(project_root=current_dir, swagger_file=file_path, template=template)
        openapi.generate()
        click.echo('Generated project from openapi file')
    else:
        click.echo(f"File {file} is not exist!")


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
        click.echo("The flag --unit or --feature is required")


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
