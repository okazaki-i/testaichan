#!/usr/bin/env python3
import fcntl
import os
import pty
import select
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


def run_mycut_with_tty_stdout(
    data: bytes,
    rows: int,
    pager: str | None = None,
    args: list[str] | None = None,
    env_updates: dict[str, str] | None = None,
) -> bytes:
    master, slave = pty.openpty()
    try:
        size = struct.pack("HHHH", rows, 80, 0, 0)
        fcntl.ioctl(slave, termios.TIOCSWINSZ, size)
        env = os.environ.copy()
        env.pop("COLUMNS", None)
        env.pop("LINES", None)
        if pager is not None:
            env["PAGER"] = pager
        if env_updates is not None:
            env.update(env_updates)

        command = ["./mycut"]
        if args is not None:
            command.extend(args)

        process = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=slave,
            stderr=subprocess.PIPE,
            env=env,
        )
        os.close(slave)
        slave = -1
        _, stderr = process.communicate(data, timeout=10)

        output = bytearray()
        while True:
            ready, _, _ = select.select([master], [], [], 0)
            if not ready:
                break
            try:
                chunk = os.read(master, 4096)
            except OSError:
                break
            if not chunk:
                break
            output.extend(chunk)

        if process.returncode != 0:
            raise subprocess.CalledProcessError(process.returncode, command, bytes(output), stderr)

        return bytes(output)
    finally:
        if slave >= 0:
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


def test_pager_is_used_when_output_exceeds_terminal_rows(tmp_path: Path) -> None:
    pager = tmp_path / "pager.py"
    pager.write_text(
        "#!/usr/bin/env python3\n"
        "import sys\n"
        "sys.stdout.write('PAGER\\n')\n"
        "sys.stdout.write(sys.stdin.read())\n"
    )
    pager.chmod(0o755)

    output = run_mycut_with_tty_stdout(b"1\n2\n3\n4\n", rows=3, pager=str(pager))

    assert b"PAGER" in output


def test_no_pager_option_disables_pager(tmp_path: Path) -> None:
    pager = tmp_path / "pager.py"
    pager.write_text(
        "#!/usr/bin/env python3\n"
        "import sys\n"
        "sys.stdout.write('PAGER\\n')\n"
        "sys.stdout.write(sys.stdin.read())\n"
    )
    pager.chmod(0o755)

    output = run_mycut_with_tty_stdout(b"1\n2\n3\n4\n", rows=3, pager=str(pager), args=["--no-pager"])

    assert b"PAGER" not in output
    assert b"1" in output
    assert b"4" in output


def test_less_pager_is_configured_to_show_color(tmp_path: Path) -> None:
    pager = tmp_path / "less"
    pager.write_text(
        "#!/usr/bin/env python3\n"
        "import os\n"
        "import sys\n"
        "sys.stdout.write(os.environ.get('LESS', ''))\n"
        "sys.stdout.write('\\n')\n"
        "sys.stdout.write(sys.stdin.read())\n"
    )
    pager.chmod(0o755)

    output = run_mycut_with_tty_stdout(
        b"\x1b[31mred\x1b[0m\n2\n3\n4\n",
        rows=3,
        pager=str(pager),
        env_updates={"LESS": "FX"},
    )

    first_line, _, rest = output.partition(b"\r\n")
    assert b"R" in first_line
    assert b"\x1b[31mred\x1b[0m" in rest
