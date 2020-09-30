# descriptive-naming-styles.py
'''There are a lot of different naming styles. It helps to be able to recognize
what naming style is being used, independently from what they are used for.
'''
# The follwing naming styles are commonly distinguished

b # single lowercase letter
B # single uppercase letter
lowercase
lower_case_with_underscores
UPPERCASE
UPPER_CASE_WITH_UNDERSCORES
CapitaliseWords # CapWords or CamelCase, sometimes known as StudlyCaps
mixedCase   # differes from CapitaliseWords by initial lowercase character!
Captialised_Words_With_Underscores # Ugly!

'''There's also the style of using a short unique prefix to group related names
together. This is not used much in Python, but it is mentioned for completeness.
For example, the os.stat() function returns a tuple whose items traditionally
have names like 'st_mode', 'st_size', 'st_mtime' and so on. (This is done to
emphasize the correspondence with the fields of the POSIX system call struct,
which helps programmers familiar with that.)
'''

_single_leading_underscore # weak "internal use" indicator. E.g. from M import *
#does not import objects whose names start with an underscore.

single_trailing_underscore_ # used by convention to avoid conflicts with
# Python keyword, e.g.
tkinter.Toplevel(master, class_='ClassName')

__double_leading_underscore # when naming a class attribute, invokes name
# mangling (inside class FooBar, __boo becomes _FooBar__boo; see below).

__double_leading_and_trailing_underscore__ # "magic" objects or attributes that
# live in user-controlled namespaces. E.g. __init__, __import__ or __file__.
# Never invent such names; only use them as documented.
