# pet-peeves.py
# Avoid extraneous whitespace in the following situations

# Immediately inside parentheses, brackets or braces:
# Correct:
spam(ham[1], {eggs: 2})

# Wrong:
spam( ham[ 1 ], { eggs: 2 } )

# Between a trailing comma and a following close parentheses:
# Correct:
foo = (1,)

# Wrong:
foo = (0, )

# Immediately before a comma, semicolon, or colon:
# Correct:
if x == 4: print(x,y); y = y, x

# Wrong:
if x == 4: print( x , y ); x , y = y , x

# However, in a slice the colon acts like a binary operator, and should have
# equal amounts on either side (treating it as the operator with the lowest
# priority). In an extended slice, both colons must have the same amount of
# spacing applied. Exception: when a slice parameter is omitted, the space is
# omitted:
# Correct:
ham[1:9], ham[1:9:3], ham[9:3], ham[1::3], ham[1:9:]
ham[lower:upper], ham[lower:upper:], ham[lower::step]
ham[: upper_fn(x) : step_fn(x)], ham[::step_fn(x)]
ham[lower + offset : upper + offset]

# Wrong:
ham[lower + offset:upper + offset]
ham[1:9], ham[1: 9], ham[1:9 :3]
ham[lower : : upper]
ham[ : upper]

# Immediately before the open parenthesis that starts the argument list of a
# function call:
# Correct:
spam(1)

# Wrong:
spam (1)

# Immediately before the open parenthesis that starts an indexing or slicing:
# Correct:
dct['key'] = lst[index]

# Wrong:
dct ['key'] = lst [index]

# More than one space around an assignment (or other) operator to align it with
# another:

# Correct:
x = 1
y = 2
long_variable = 3

# Wrong:
x               = 1
y               = 2
long_variable   = 3
