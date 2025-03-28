import pytest

from python_cli_template.cli import main


def test_hello(capsys):
    assert main() is None
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"


def test_hello_world(capsys):
    assert main(["--name", "world"]) is None
    captured = capsys.readouterr()
    assert captured.out == "Hello, world!\n"


def test_invalid(capsys):
    with pytest.raises(SystemExit) as exception:
        main(["--invalid"])
    assert exception.type is SystemExit
