# Python program to explain *args and **kwargs

'''
*args and **kwargs allow us to pass an unspecified number of arguments to a function.

*args is used to send a non-keyworded variable length argument list to the function.
**kwargs allow us to pass a keyworded variable length argument list to the function.

only the * (asterisk) is necessary.

order of using *args **kwargs and formal args:
somefunc(fargs, *args, **kwargs)
'''
def test_args(f_arg, *args):
    print('first normal args:', f_arg)
    for i, arg in enumerate(args):
        print(i, 'another arg through *argv:', arg)

test_args('soccer', 'messi', 'cristiano', 'neymar')

# we can try rename *args to *vars
def test_rename_args(f_arg, *vars):
    print('first normal args:', f_arg)
    for i, arg in enumerate(vars):
        print(i, 'another arg through *argv:', arg)

test_rename_args('soccer', 'messi', 'cristiano', 'neymar')

def test_kwargs(**kwargs):
    for key, value in kwargs.items():
        print("{0}: {1}".format(key, value))

test_kwargs(name='messi', age=30)