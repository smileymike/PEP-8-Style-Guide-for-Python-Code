# code lay-out

# indentation
# 4 space per indentation level

# Correct:

# Aligned with opening delimiter.
foo = long_function_name( var_one, var_two,
               var_three, var_four)

# Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest
def long_function_name(
        var_one, var_two, var_three,
        var_four)
    print(var_one)

# Hanging indents should add a level
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)

# Wrong:

# Arguments on first line forbidden when not using vertical alignment.
foo = longfunction_name(var_one, var_two,
    var_three, var_four)

# Further indentation required as indentation is not distinguishable.
def long_function_name(
    var one, var_two,
    var_three, var_four)

# The 4-space rule is optional for continuation lines.
# Optional

# Hanging indents *may* be indented to other than 4 spaces
foo = long_function_name(
    var_one, var_two,
    var three, var four)

# if-statement indentation

# No extra indentation
if (this_is_one_thing and
    that_is_another_thing):
    do something()

# Add a comment, which will provide some distinction in editors
# supporting syntax highlighting
if (this_is_one_thing and
    that_is_another_thing):
    # Since both conditions are true, we can frobnicate.
    do something()

# Add some extra indentation on the conditional continuation line
if (this_is_one_thing and
        and that_is_another_thing):
    do something()

# The closing brace/bracket/parenthesis on multiline constructs may either line
# up under the first non-whitespace character of the last line of list
my_list = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9,
    ]
result = some_function_that_takes_arguments(
    'a','b','c',
    'd','e','f',
    )

# or it may be lined up under the first character of the line that starts the
# multiline construct
my_list = [
    1, 2, 3,
    4, 5, 6,
]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)
