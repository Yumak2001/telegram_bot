"""
Import all submodules here

isort:skip_file
"""

from . import commands
from . import messages
from . import media

await commands.set_commands()
