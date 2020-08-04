from pathlib import Path

import pytest

TEMPLATE_CONTENT = "hello ${name}!"
TEMPLATE_PATH = "/test/template.mako"
DATA_CONTENT = "name: world"
DATA_CONTENT_ERROR = "a : -"
DATA_PATH = "/test/data.yaml"
DATA_DICT = {"name": "world"}
TEMPLATE_RENDERED = "hello world!"


@pytest.fixture
def template_file(fs):
    fs.create_file(TEMPLATE_PATH, contents=TEMPLATE_CONTENT)
    return Path(TEMPLATE_PATH)


@pytest.fixture
def data_dict():
    return DATA_DICT


@pytest.fixture
def data_file(fs):
    fs.create_file(DATA_PATH, contents=DATA_CONTENT)
    return Path(DATA_PATH)


@pytest.fixture
def data_file_with_content_error(fs):
    fs.create_file(DATA_PATH, contents=DATA_CONTENT_ERROR)
    return Path(DATA_PATH)


@pytest.fixture
def template_rendered():
    return TEMPLATE_RENDERED
