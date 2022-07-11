import subprocess

import click


@click.command()
@click.argument('name', default='will')
def cli(name):
    """
    Create command that says hello with a name option

    :param path: Test coverage path
    :return: Subprocess call result
    """
    cmd = 'echo hello {0}'.format(name)
    return subprocess.call(cmd, shell=True)