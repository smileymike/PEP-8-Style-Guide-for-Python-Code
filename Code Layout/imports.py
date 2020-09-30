# Imports should usually be on separate lines:

# Correct:
import os
import sys

# Wrong:
import sys, os

# It's okay to say this though:

# Correct:
from subprocess import Popen, PIPE

# Imports are always put at the top of the file, just after any module comments
# and docstrings, and before module globals and constants.

# Imports should be grouped in the following order:

# 1. Standard library imports
# 2. Related 3rd party imports
# 3. Local application/library specific imports

# You should put a blank line between each group of imports

# Absolute imports are recommended, as they are usually more readable and tend
# to be better behaved (or at least give better error messages) if the import
# system is incorrectly configured (such as when a directory inside a package
# ends up on sys.path):

import mypkg.sibling
from mypkg import sibling
from mypkg.sibling import example

# However, explicit relative imports are an acceptable alternative to absolute
# imports, especially when dealing with complex package layouts where using
# absolute imports would be unnecessarily verbose:

from . import sibling
from .sibling import example

# Standard library code should avoid complex package layouts and always use
# absolute imports.

# Implicit relative imports should never be used and have been removed in Python 3.

# When importing a class from a class-containing module, it's usually okay to
# spell this:

from myclass import MyClass
from foo.bar.yourClass import YourClass

# If this spelling causes local name clashes, then spell them explicitly:

import myclass
import foo.bar.yourclass

# Wildcard imports (from <module> import *) should be avoided, as they make it
# unclear which names are present in the namespace, confusing both readers and
# many automated tools. 
