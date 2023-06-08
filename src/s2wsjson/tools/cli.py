import click

@click.group
def s2wsjson_cmd():
    pass

@s2wsjson_cmd.command("check-schema")
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def check_schema(count, name):
    """Simple program that greets NAME for a total of COUNT times.
        Example usage:

            $ s2wsjson check-schema --name Victor --count 2
            Hello Victor
            Hello Victor
    """
    for x in range(count):
        click.echo(f"Hello {name}!")