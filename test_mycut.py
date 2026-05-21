#!/usr/bin/env python3
import subprocess
import tempfile
from pathlib import Path


def run_mycut(data: bytes) -> bytes:
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "input.txt"
        p.write_bytes(data)
        return subprocess.check_output(["./mycut"], stdin=p.open("rb"))


def test_no_trailing_newline_input_keeps_no_trailing_newline_output() -> None:
    assert run_mycut(b"abc") == b"abc\x1b[0m"


def test_truncated_line_with_newline_keeps_newline() -> None:
    long_line = (b"a" * 120) + b"\n"
    assert run_mycut(long_line) == (b"a" * 100) + b"\x1b[0m\n"


def test_truncated_line_without_newline_keeps_no_newline() -> None:
    long_line = b"a" * 120
    assert run_mycut(long_line) == (b"a" * 100) + b"\x1b[0m"


def test_japanese_characters_are_counted_as_two() -> None:
    data = "あいうえお\n".encode("utf-8")
    assert subprocess.check_output(["./mycut", "-c", "6"], input=data) == "あいう\x1b[0m\n".encode("utf-8")
