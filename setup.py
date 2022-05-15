from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent

__project__  = "Ranthon"
__version__ = "1.0.7"
__description__ = "A collection of Python packages written by Walter J Hare."
__packages__ = ["infseq"]
__install_requires__ = ["filelog"]
__long_description__ = (this_directory / "README.md").read_text()
__long_description_content_type__ = 'text/markdown'
__url__ = 'https://github.com/WFlyToTheSky/RanthonRepo'

setup(
    name = __project__,
    version = __version__,
    description = __description__,
    packages = __packages__,
    install_requires = __install_requires__,
    long_description = __long_description__,
    long_description_content_type = __long_description_content_type__,
    url = __url__
)
