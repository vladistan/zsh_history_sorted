#!/usr/bin/env python
from sys import argv, stdin
from typing import Generator, Iterable, List


class HistorySorter(object):
    def __init__(self) -> None:
        self.streams: List[Iterable[str]] = []

    def get_lines(self) -> Generator[str, None, None]:
        lno = 0
        prev_line = ""

        for s in self.streams:
            acc = ""
            try:
                for line in s:
                    lno += 1
                    acc += line
                    prev_line = line

                    try:
                        if len(line) > 1 and line[-2] == "\\":
                            continue

                        yield acc
                        acc = ""

                    except IndexError as e:
                        print("Index error on: '{}'".format(line))
                        raise e

            except UnicodeDecodeError as e:
                print("Decode error: {}: {}", lno, prev_line, e)
                raise e

    def get_output(self) -> Iterable[str]:
        return sorted(self.get_lines())

    def add_stream(self, stream: Iterable[str]) -> None:
        self.streams.append(stream)


def get_file() -> Iterable[str]:
    if len(argv) > 1:
        return open(argv[1])
    else:
        return stdin


if __name__ == "__main__":
    srt = HistorySorter()
    srt.add_stream(get_file())

    for line in srt.get_output():
        print(line[:-1])
