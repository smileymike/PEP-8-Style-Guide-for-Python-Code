# other-recommendations.py

# Avoid trailing whitespace anywhere because it's usually invisible, it can be
# confusing

# Always surround these binary operators with a single space on either side:
# assignment (=), augmented assignment (+=, -= etc.), comparisons (==, <, >, !=,
# <>, <=, >=, in, not in, is, is not), Booleans (and, or, not).

# If operators with different priorities are used, consider adding whitespace
# around the operators with the lowest priority(ies). Always one space.

# Correct:
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)

# Wrong:
i=i+1
submitted +=1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)

# Function annoations. Always have spaces around -> if present
# Correct:
def munge(input: AnyStr): ...
def munge() -> PostInt: ...

# Wrong:
def munge(input:AnyStr): ...
def munge()->PostInt: ...

# Don't use spaces around the = sign when used to indicate a keyword argument,
# or when used to indicate a default value for an unannotated function parameter:
# Correct:
def complex(real, imag=0.0):
    return magic(r=real, i=imag)

# Wrong:
def complex(real, imag = 0.0):
    return magic(r = real, i = imag)

# When combining an argument annotation with a default value, however, do use
# spaces around the = sign:
# Correct:
def munge(sep: AnyStr = None): ...
def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...

# Wrong:
def munge(input: AnyStr=None): ...
def munge(input: AnyStr, limit = 1000):...

# Compound statements (multiple statements on the same line) are generally
# discouraged:
# Correct:
if foo == 'blah':
    do_blah_thing()
do_one()
do_two()
do_three()

# Rather Not:
# Wrong:
if foo == 'blah': do_blah_thing()
do_one(); do_two(); do_three()

# While sometimes it's okay to put an if/for/while with a small body on the same
# line, never do this for multi-clause statements. Also avoid folding such long
# lines!
# Rather Not:
# Wrong:
if foo == 'blah': do_blah_thing()
for x in lst: total += x
while t < 10: t = delay()

# Definitely note
# Wrong:
if foo == 'blah': do_blah_thing()
else: do_not_blah_thing()

try: something()
finally: cleanup()

do_one(); do_two(); do_three(long, argument,
                             list, like, this)
if foo == 'blah': one(); two(); three()
