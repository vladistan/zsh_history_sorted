#!/usr/bin/env python3

from sys import stdin
from typing import List

from rich import traceback
from typer import Argument, Typer

from zsh_history_sorter import HistorySorter

traceback.install(show_locals=True)
app = Typer(add_completion=True)


@app.command()
def main(files: List[str] = Argument(default=None, help="List of ZSH history files")) -> None:
    srt = HistorySorter()

    if files is None:
        srt.add_stream(stdin)
    else:
        for f in files:
            srt.add_stream(open(f, "r"))

    for line in srt.get_output():
        print(line[:-1])


# Allow the script to be run standalone (useful during development).
if __name__ == "__main__":
    app()
