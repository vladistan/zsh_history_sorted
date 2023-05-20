from zsh_history_sorter import HistorySorter


def test_can_iterate_over_hist_lines() -> None:
    srt = HistorySorter()
    srt.add_stream([": 1474929671:0; bob"])
    seen = False

    for n, line in enumerate(srt.get_output()):
        if n == 0:
            assert line == ": 1474929671:0; bob"
            seen = True

    assert seen


def test_iterate_over_streams() -> None:
    srt = HistorySorter()
    seen = False
    srt.add_stream([": 1474929671:0;cat l > rmList\n", ": 1489349615:0;git grep line2\n"])
    srt.add_stream(
        [
            ": 1489349615:0;git grep line3\n",
        ],
    )

    for n, line in enumerate(srt.get_output()):
        if n == 0:
            assert line == ": 1474929671:0;cat l > rmList\n"
            seen = True
        if n == 1:
            assert line == ": 1489349615:0;git grep line2\n"
            seen = True
        if n == 2:
            assert line == ": 1489349615:0;git grep line3\n"

    assert n == 2
    assert seen


def test_can_parse_elements() -> None:
    srt = HistorySorter()
    srt.add_stream(
        [
            ": 1474929671:0; bob\n",
            ": 1474929672:0; one \\\n",
            "two\\\n",
            "three\n",
            ": 1474929674:0; bill\n",
        ]
    )

    seen = False

    for n, line in enumerate(srt.get_output()):
        if n == 0:
            assert line == ": 1474929671:0; bob\n"
        if n == 1:
            assert line == ": 1474929672:0; one \\\ntwo\\\nthree\n"
        if n == 2:
            assert line == ": 1474929674:0; bill\n"
            seen = True

    assert seen


def test_output_is_sorted() -> None:
    srt = HistorySorter()
    srt.add_stream(
        [
            ": 1474929672:0; one \\\n",
            "two\\\n",
            "three\n",
            ": 1474929674:0; bill\n",
            ": 1474929671:0; bob\n",
        ]
    )

    seen = False

    for n, line in enumerate(srt.get_output()):
        if n == 0:
            assert line == ": 1474929671:0; bob\n"
        if n == 1:
            assert line == ": 1474929672:0; one \\\ntwo\\\nthree\n"
        if n == 2:
            assert line == ": 1474929674:0; bill\n"
            seen = True

    assert seen


def test_do_not_choke_on_blank_lines() -> None:
    srt = HistorySorter()
    srt.add_stream(
        [
            ": 1474929672:0; one \\\n",
            "\n",
            ": 1474929674:0; bill\n",
            ": 1474929671:0; bob\n",
        ]
    )

    seen = False

    for n, line in enumerate(srt.get_output()):
        if n == 0:
            assert line == ": 1474929671:0; bob\n"
        if n == 1:
            assert line == ": 1474929672:0; one \\\n\n"
        if n == 2:
            assert line == ": 1474929674:0; bill\n"
            seen = True

    assert seen
