import click

@click.command()
@click.option('--search', help='The person to greet.', prompt='Query')

def search(search):
    click.echo(f"{search}")