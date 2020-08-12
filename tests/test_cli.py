"""Test cases for the command line module."""
from unittest.mock import Mock

from click.testing import CliRunner
import pytest
from pytest_mock import MockFixture

from mako2cli import cli


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


@pytest.fixture
def mock_renderer_execute(mocker: MockFixture) -> Mock:
    """Fixture to mock the renderer class."""
    return mocker.patch("mako2cli.Renderer.execute")


def test_main(runner: CliRunner, mock_renderer_execute: Mock) -> None:
    """It exits with 0 code and without generating an output due to the mocked class."""
    result = runner.invoke(
        cli.main, ["-t", "template.mako", "-d", "data.yaml", "-o", "outputfile"]
    )
    assert result.exit_code == 0
    assert result.output == ""
    assert mock_renderer_execute.called
