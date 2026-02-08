# Click commands, keep track of flags passed
import click
from .engine import runner

@click.group()

def cli():
    """Typing speed test CLI"""
    pass


@cli.command()
# @click.option("--time", default=15, help="Test duration in seconds")
@click.option("--words", default=60, help="Number of words")
def start(words):
    # from typetest.engine import run_test
    # run_test(time=time, words=words)
    """Start a typing test"""
    click.echo(f"Starting test: {words} words")
    runner.runner(words)

    

@cli.command()
def stats():
    click.echo("Stats coming soon...")
