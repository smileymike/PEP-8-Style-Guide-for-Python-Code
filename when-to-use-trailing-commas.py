# when-to-use-trailing-commas.py
# Trailing commas are usually optional, except they are mandatory when making a
# tuple of one element.  For clarity, it is recommended to surround the latter
# in (technically redundant) parentheses:

# Correct:
FILES = ('setup.cfg',)

# Wrong:
FILES = 'setup.cfg',

# When trailing commas are redundant, they are often helpful when a version
# control system is used, when a list of values, arguments or imported items is
# expected to be extended over time.

# Correct:
FILES = [
    'setup.cfg',
    'tox.ini',
    ]
initialize(FILES,
           error=True,
           )

# Wrong:
FILES = ['setup.cfg', 'tox.ini',]
initalize(FILES, error=True)
