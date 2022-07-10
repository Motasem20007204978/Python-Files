# position only arguments are succeded by a / in the function definition
# key word only arguments we can precede the argument with a *
# standard arguments don't be preceded by a * or succeded by a /
'''
 must, position arguments used in the first position 
 and keyword arguments are used in the last position to avoid ambiguity 
 and errors
 '''
def kwd_only_arg(a, /, b , *, c):
    '''
    This function takes two standard arguments and a keyword only argument
    '''
    print(a, b, c)

kwd_only_arg(1, b=2, c=3)
# a is a positional argument that cannot be included as a keyword argument
# b is a standard arg can be included in the call as a keyword argument or a position argument
# c is keyword only arg must be included in the call as a keyword argument

kwd_only_arg(1, c=3, b=2)
"""
if a standars qrgument is instead by keyword argument 
when calling the function as a argument,
it will be a keyword argument, 
but position argumrnt must used in the first position   
"""

# if we want to use multiple positional arguments or keyword arguments
# we can use a * to indicate that we want to pass a tuple of arguments
# or a ** to indicate that we want to pass a dictionary of arguments
# we can use positional arguments in the first
def multiple_args(*args, **kwargs):#cannot use * and /
    # posarg argument is concidered with *args
    for k, v in zip(kwargs, args):
        print(k, v)

multiple_args(6, 1, 2, 3, 4, a=1, b=2, c=3)

# or unpacking them when calling the function
multiple_args(*(1, 2, 3, 4), **{'a':1, 'b':2, 'c':3})
# as the above callig
# args is a tuple of positional arguments
# kwargs is a dictionary of keyword arguments

