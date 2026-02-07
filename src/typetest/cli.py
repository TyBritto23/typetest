# Click commands, keep track of flags passed
import click

@click.group()

def cli():
    """Typing speed test CLI"""
    pass


@cli.command()
@click.option("--time", default=15, help="Test duration in seconds")
@click.option("--words", default=60, help="Number of words")
def start(time, words):
    # from typetest.engine import run_test
    # run_test(time=time, words=words)
    """Start a typiing test"""
    click.echo(f"Starting test: {time}s, {words} words")
    

@cli.command()
def stats():
    click.echo("Stats coming soon...")
