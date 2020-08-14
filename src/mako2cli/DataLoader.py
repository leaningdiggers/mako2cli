"""Dataloaader module."""
from __future__ import annotations

from pathlib import Path
from typing import Dict, Type

import attr
import yaml


@attr.s
class DataLoader:
    """Data loading interface.

    Load data from a file source. Only YAML is actually supported.

    Attributes:
        data_file (Path): file containing data.
    """

    data_file = attr.ib(type=Path)

    @classmethod
    def from_string(cls: Type[DataLoader], data_file: str) -> DataLoader:
        """Factory method for initialize from string path.

        Args:
            data_file (str): path to data file as string.

        Returns:
            a DataLoader class instance.
        """
        return cls(Path(data_file))

    @data_file.validator
    def _exist_data_file(self: DataLoader, attribute: Path, value: Path) -> None:
        """Validator for __init__.

        Check the existence of the file.

        Args:
            attribute (Path): attribute to validate.
            value (Path): value to validate.

        Raises:
            IOError: if file doesn't exist.
        """
        if not value.exists():
            raise IOError(f"{value} doesn't exist")

    def get_data(self: DataLoader) -> Dict:
        """Return the data parsed as dictionary.

        Returns:
            data parsed as dictionary.

        Raises:
            yaml.YAMLError: if file is not valid YAML.

        """
        with self.data_file.open() as fstream:
            try:
                data = yaml.safe_load(fstream)
            except yaml.YAMLError:
                raise
            else:
                return data
