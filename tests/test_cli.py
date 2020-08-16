"""Test cases for the command line module."""
from pathlib import Path

from click.testing import CliRunner
import pytest

from mako2cli import cli


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


def test_main(
    runner: CliRunner, template_file: Path, data_file: Path, template_rendered: str
) -> None:
    """It exits with 0 code and check generation executed."""
    output_file = Path("/output")
    result = runner.invoke(
        cli.main,
        ["-t", str(template_file), "-d", str(data_file), "-o", str(output_file)],
    )
    assert result.exit_code == 0
    assert result.output == ""
    assert output_file.open().read() == template_rendered
