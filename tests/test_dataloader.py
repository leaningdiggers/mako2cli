"""Test cases for DataLoader module."""
from pathlib import Path
from typing import Dict

import pytest
import yaml

from mako2cli import DataLoader


def test_init(data_file: Path) -> None:
    """It correctly init with an existing file."""
    DataLoader(data_file)


def test_init_missing_file() -> None:
    """It correctly detect an unexistent file."""
    with pytest.raises(IOError):
        DataLoader(Path("/fake.yaml"))


def test_init_from_string(data_file: Path) -> None:
    """It could init from a path string."""
    with pytest.raises(AttributeError):
        DataLoader(str(data_file))  # type: ignore
    DataLoader.from_string(str(data_file))


def test_get_data(data_file: Path, data_dict: Dict) -> None:
    """It could correctly load and return data."""
    d = DataLoader(data_file)
    assert d.get_data() == data_dict


def test_get_data_exception(data_file_with_content_error: Path) -> None:
    """It detect format error on data file."""
    d = DataLoader(data_file_with_content_error)
    with pytest.raises(yaml.YAMLError):
        d.get_data()
