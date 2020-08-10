from pathlib import Path
from typing import Dict

from pyfakefs import fake_filesystem
import pytest

TEMPLATE_CONTENT = "hello ${name}!"
TEMPLATE_PATH = "/test/template.mako"
DATA_CONTENT = "name: world"
DATA_CONTENT_ERROR = "a : -"
DATA_PATH = "/test/data.yaml"
DATA_DICT = {"name": "world"}
TEMPLATE_RENDERED = "hello world!"


@pytest.fixture
def template_file(fs: fake_filesystem.FakeFilesystem) -> Path:
    fs.create_file(TEMPLATE_PATH, contents=TEMPLATE_CONTENT)
    return Path(TEMPLATE_PATH)


@pytest.fixture
def data_dict() -> Dict:
    return DATA_DICT


@pytest.fixture
def data_file(fs: fake_filesystem.FakeFilesystem) -> Path:
    fs.create_file(DATA_PATH, contents=DATA_CONTENT)
    return Path(DATA_PATH)


@pytest.fixture
def data_file_with_content_error(fs: fake_filesystem.FakeFilesystem) -> Path:
    fs.create_file(DATA_PATH, contents=DATA_CONTENT_ERROR)
    return Path(DATA_PATH)


@pytest.fixture
def template_rendered() -> str:
    return TEMPLATE_RENDERED
