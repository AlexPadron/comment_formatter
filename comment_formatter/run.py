import os
from glob import glob

import click

from .formatter import rewrite_file


@click.command()
@click.argument("path", type=click.Path(exists=True))
@click.option("--line-length", type=int, default=100)
@click.option("--check", is_flag=True)
def run(path: str, line_length: int, check: bool) -> None:
    """CLI for comment formatting"""
    if os.path.isdir(path):
        python_files = glob(os.path.join(path, "**/*.py"), recursive=True)
    else:
        python_files = [path]

    files_to_reformat = []

    for file_name in python_files:
        if rewrite_file(file_name, check):
            pass
        else:
            files_to_reformat.append(file_name)

    if len(files_to_reformat) == 0:
        exit(0)
    else:
        click.echo("Files {} would be reformatted".format(files_to_reformat))
        exit(1)


if __name__ == "__main__":
    run()
