from functools import wraps
def type_logger(level=0):
    def logger(func):
        @wraps(func)
        def decor(*argv, **kwargs):
            all_args = list(argv) + list(kwargs.values())
            norm_res = func(all_args[0])
            if level == 1:
                print(", ".join([f"{x}:{type(x)}" for x in all_args]))
            elif level == 2:
                print(f"{func.__name__}:{type(func)}")
                print(f"{func.__name__}({all_args[0]}):{type(norm_res)}")
            else:
                return "calc_cube(" + ", ".join([str(func(x)) for x in argv]) + ")"
        return decor
    return logger
@ type_logger(2)
def calc_cube(x):
    return x ** 3