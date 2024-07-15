import click
from headerfiles.api import is_supported_proj, get_proj_headers

@click.group()
def cli():
    pass

@click.command()
def command_is_supported_proj():
    """Command for is_supported_proj API"""
    result = is_supported_proj()
    click.echo(f"{result}")

@click.command()
def command_get_proj_headers():
    """Command for get_proj_headers API"""
    result = get_proj_headers()
    click.echo(f"{result}")

cli.add_command(command_is_supported_proj)
cli.add_command(command_get_proj_headers)

if __name__ == "__main__":
    cli()
