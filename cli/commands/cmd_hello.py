import subprocess

import click


@click.command()
@click.option('--name',default='')
@click.argument('path', default='snakeeyes')
def cli(name, path):
    """
    Create command that says hello with a name option

    :param path: Test coverage path
    :return: Subprocess call result
    """
    print_name = ''
    if name:
        print_name = name
    cmd = 'echo hello {0}'.format(print_name)
    return subprocess.call(cmd, shell=True)