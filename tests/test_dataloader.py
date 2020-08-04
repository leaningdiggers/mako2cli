from pathlib import Path

import pytest
import yaml

from mako2cli import DataLoader


def test_init(data_file):
    DataLoader(data_file)
    with pytest.raises(IOError):
        DataLoader(Path("/fake.yaml"))


def test_init_from_string(data_file):
    with pytest.raises(AttributeError):
        DataLoader(str(data_file))
    DataLoader.from_string(str(data_file))


def test_get_data(data_file, data_dict):
    d = DataLoader(data_file)
    assert d.get_data() == data_dict


def test_get_data_exception(data_file_with_content_error):
    d = DataLoader(data_file_with_content_error)
    with pytest.raises(yaml.YAMLError):
        d.get_data()
