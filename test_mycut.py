#!/usr/bin/env python3
import fcntl
import os
import pty
import struct
import subprocess
import tempfile
import termios
from pathlib import Path


DEFAULT_LIMIT_FALLBACK_ROWS = 24


def run_mycut(data: bytes, columns: int | None = None) -> bytes:
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "input.txt"
        p.write_bytes(data)
        env = os.environ.copy()
        env.pop("COLUMNS", None)
        if columns is not None:
            env["COLUMNS"] = str(columns)
        return subprocess.check_output(["./mycut"], stdin=p.open("rb"), env=env)


def run_mycut_with_tty_stderr(data: bytes, columns: int) -> bytes:
    master, slave = pty.openpty()
    try:
        size = struct.pack("HHHH", DEFAULT_LIMIT_FALLBACK_ROWS, columns, 0, 0)
        fcntl.ioctl(slave, termios.TIOCSWINSZ, size)
        env = os.environ.copy()
        env.pop("COLUMNS", None)
        return subprocess.check_output(["./mycut"], input=data, stderr=slave, env=env)
    finally:
        os.close(slave)
        os.close(master)


def test_no_trailing_newline_input_keeps_no_trailing_newline_output() -> None:
    assert run_mycut(b"abc") == b"abc\x1b[0m"


def test_default_limit_uses_terminal_columns_from_environment() -> None:
    long_line = (b"a" * 20) + b"\n"
    assert run_mycut(long_line, columns=12) == (b"a" * 12) + b"\x1b[0m\n"


def test_default_limit_uses_terminal_columns_when_stdout_is_pipe() -> None:
    long_line = (b"a" * 20) + b"\n"
    assert run_mycut_with_tty_stderr(long_line, columns=14) == (b"a" * 14) + b"\x1b[0m\n"


def test_truncated_line_with_newline_keeps_newline() -> None:
    long_line = (b"a" * 120) + b"\n"
    assert run_mycut(long_line) == (b"a" * 100) + b"\x1b[0m\n"


def test_truncated_line_without_newline_keeps_no_newline() -> None:
    long_line = b"a" * 120
    assert run_mycut(long_line) == (b"a" * 100) + b"\x1b[0m"


def test_japanese_characters_are_counted_as_two() -> None:
    data = "あいうえお\n".encode("utf-8")
    assert subprocess.check_output(["./mycut", "-c", "6"], input=data) == "あいう\x1b[0m\n".encode("utf-8")


def test_japanese_characters_do_not_exceed_limit() -> None:
    data = "あいうえお\n".encode("utf-8")
    assert subprocess.check_output(["./mycut", "-c", "5"], input=data) == "あい\x1b[0m\n".encode("utf-8")
