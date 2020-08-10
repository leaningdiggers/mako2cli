from __future__ import annotations

from pathlib import Path
from typing import Dict, Type

import attr
import yaml


@attr.s
class DataLoader:
    data_file = attr.ib(type=Path)

    @classmethod
    def from_string(cls: Type[DataLoader], data_file: str) -> DataLoader:
        return cls(Path(data_file))

    @data_file.validator
    def _exist_data_file(self: DataLoader, attribute: Path, value: Path) -> None:
        if not value.exists():
            raise IOError(f"{value} doesn't exist")

    def get_data(self: DataLoader) -> Dict:
        with self.data_file.open() as fstream:
            try:
                data = yaml.safe_load(fstream)
            except yaml.YAMLError as exc:
                raise exc
            else:
                return data
