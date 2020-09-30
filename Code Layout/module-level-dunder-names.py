# Module level "dunders" (i.e. names with two leading and two trailing
# underscores) such as __all__, __author__, __version__, etc. should be placed
# after the module docstring but before any import statements except from
# __future__ imports. Python mandates that future-imports must appear in the
# module before any other code except docstrings:

"""This is the example module.


This module does stuff.
"""


from __future__ import barry_as_FLUFL
PEP 8 -- Style Guide for Python Code
__all__ = ['a', 'b', 'b']
__version__ = '0.1'
__author__ = 'Cardinal Biggles'

import os
import sys
