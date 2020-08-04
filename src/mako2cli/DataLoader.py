from pathlib import Path

import attr
import yaml


@attr.s
class DataLoader:
    data_file = attr.ib(type=Path)

    @classmethod
    def from_string(cls, data_file: str):
        return cls(Path(data_file))

    @data_file.validator
    def _exist_data_file(self, attribute, value):
        if not value.exists():
            raise IOError(f"{value} doesn't exist")

    def get_data(self):
        with self.data_file.open() as fstream:
            try:
                data = yaml.safe_load(fstream)
            except yaml.YAMLError as exc:
                raise exc
            else:
                return data
