# https://click.palletsprojects.com/en/8.0.x/quickstart/#nesting-commands
import click
import os

from fastio_cli.initialize import Initialize
from fastio_cli.converter.converter import BuilderSpec

@click.group()
def cli():
    pass

@cli.command()
@click.option('--openapi_file', default='', prompt='Absolute path to openapi file (empty to use later)', help='Openapi spec to generate code.')
def convert(openapi_file: str):
    try:
        current_dir = os.getcwd()
        print("current_dir: ", current_dir)
        builderSpec = BuilderSpec()
    except Exception as e:
        raise e
    click.echo('Convert openapi spec to builder spec.')


@cli.command()
def init():
    current_dir = os.getcwd()
    initialize = Initialize(path=current_dir)
    print("Initialize fastio successfully")


@cli.command()
def g():
    current_dir = os.getcwd()
    initialize = Initialize(path=current_dir)


cli.add_command(init)
cli.add_command(convert)


if __name__ == '__main__':
    cli()