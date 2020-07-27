import pytest
from click.testing import CliRunner
from mako2cli import cli


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture
def mock_renderer_execute(mocker):
    return mocker.patch("mako2cli.Renderer.execute")


def test_main(runner, mock_renderer_execute):
    result = runner.invoke(
        cli.main, ["-t", "template.mako", "-d", "data.yaml", "-o", "outputfile"]
    )
    assert result.exit_code == 0
    assert result.output == ""
    assert mock_renderer_execute.called
