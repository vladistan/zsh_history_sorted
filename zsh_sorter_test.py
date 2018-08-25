from zsh_history_sorter import HistorySorter


def test_can_iterate_over_hist_lines():
    srt = HistorySorter()
    srt.add_stream([': 1474929671:0; bob'])
    seen = False

    for n, l in enumerate(srt.get_output()):
        if n == 0:
            assert l == ': 1474929671:0; bob'
            seen = True

    assert seen


def test_iterate_over_streams():
    srt = HistorySorter()
    seen = False
    srt.add_stream([": 1474929671:0;cat l > rmList\n",
                    ": 1489349615:0;git grep 172.30.1.46\n"])

    for n, l in enumerate(srt.get_output()):
        if n == 0:
            assert l == ": 1474929671:0;cat l > rmList\n"
            seen = True
        if n == 1:
            assert l == ": 1489349615:0;git grep 172.30.1.46\n"
            seen = True

    assert seen


def test_can_parse_elements():
    srt = HistorySorter()
    srt.add_stream([": 1474929671:0; bob\n",
                    ": 1474929672:0; one \\\n",
                    "two\\\n",
                    "three\n",
                    ": 1474929674:0; bill\n"])

    seen = False

    for n, l in enumerate(srt.get_output()):
        if n == 0:
            assert l == ": 1474929671:0; bob\n"
        if n == 1:
            assert l == ": 1474929672:0; one \\\ntwo\\\nthree\n"
        if n == 2:
            assert l == ": 1474929674:0; bill\n"
            seen = True

    assert seen


def test_output_is_sorted():
    srt = HistorySorter()
    srt.add_stream([": 1474929672:0; one \\\n",
                    "two\\\n",
                    "three\n",
                    ": 1474929674:0; bill\n",
                    ": 1474929671:0; bob\n", ])

    seen = False

    for n, l in enumerate(srt.get_output()):
        if n == 0:
            assert l == ": 1474929671:0; bob\n"
        if n == 1:
            assert l == ": 1474929672:0; one \\\ntwo\\\nthree\n"
        if n == 2:
            assert l == ": 1474929674:0; bill\n"
            seen = True

    assert seen
