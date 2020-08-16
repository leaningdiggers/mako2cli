"""The mako2cli project."""
from .DataLoader import DataLoader
from .Renderer import Renderer
from .TemplateEngine import TemplateEngine
from .TemplateEngine import TemplateEngineException

try:
    from importlib.metadata import PackageNotFoundError  # type: ignore
    from importlib.metadata import version  # type: ignore # pragma: no cover
except ImportError:  # pragma: no cover
    from importlib_metadata import PackageNotFoundError  # type: ignore
    from importlib_metadata import version  # type: ignore


try:
    __version__ = version(__name__)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"

__all__ = ["Renderer", "TemplateEngine", "TemplateEngineException", "DataLoader"]
