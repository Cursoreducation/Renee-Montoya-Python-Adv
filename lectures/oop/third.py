def help_function_args(*args):
    print(args[0] - args[1] + args[2])

def help_function_kwargs(**kwargs):
    print(kwargs['help_word'])
    print(kwargs['kek'])

help_function_args(1, 2, 3)
help_function_kwargs(help_word="hello", kek="lol")
# help_function(1, 2, 3)
# help_function(1, 2, 3, 4)
