[![Tests](https://github.com/leaningdiggers/mako2cli/workflows/Tests/badge.svg)](https://github.com/leaningdiggers/mako2cli/actions?workflow=Tests)
[![Codecov](https://codecov.io/gh/leaningdiggers/mako2cli/branch/master/graph/badge.svg)](https://codecov.io/gh/leaningdiggers/mako2cli)
[![PyPI](https://img.shields.io/pypi/v/mako2cli.svg)](https://pypi.org/project/mako2cli/)
[![Read the Docs](https://readthedocs.org/projects/mako2cli/badge/)](https://mako2cli.readthedocs.io/)

# mako2cli

This project aims to port Mako Template to a simple usage on command line

## Installation

To install the mako2cli Python project,
run this command in your terminal:

```
$ pip install mako2cli
```

## Example

Create a file `template.mako` containing:

```mako
hello ${name}!
```

And a data file `data.yaml`:

```yaml
name: world
```

Now you can render the file with:

```bash
$ m2cli -t template.mako -d data.yaml -o rendered
```

The output is saved to `rendered`:

```
hello world!
```

That's all!
