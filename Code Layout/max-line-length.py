# Limit all lines to a maximum of 79 characters

# For flowing long blocks of text with fewer structural restrictions (docstrings
# or comments), the line length should be limited to 72 characters.

# Backslashes may still be appropriate at times. For example, long, multiple
# with-statements cannot use implicit continuation, so backslashes are acceptable:

# an example of backslash on end of first line below "\""
with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())
