#!/usr/bin/env python
from sys import stdin, argv


class HistorySorter(object):
    def __init__(self):
        self.streams = []

    def get_lines(self):

        lno = 0
        prev_line = ""

        for s in self.streams:
            acc = ""
            try:
                for l in s:

                    lno += 1
                    acc += l
                    prev_line = l

                    try:
                        if len(l) > 1 and l[-2] == '\\':
                            continue

                        yield acc
                        acc = ""

                    except IndexError as e:
                        print("Index error on: '{}'".format(l))
                        raise e

            except UnicodeDecodeError as e:
                print("Decode error: {}: {}", lno, prev_line, e)
                raise e

    def get_output(self):
        lines = [l for l in self.get_lines()]
        return sorted(lines)

    def add_stream(self, stream):
        self.streams.append(stream)


def get_file():
    if len(argv) > 1:
        return open(argv[1])
    else:
        return stdin


if __name__ == "__main__":

    srt = HistorySorter()
    srt.add_stream(get_file())

    for l in srt.get_output():
        print(l[:-1])
