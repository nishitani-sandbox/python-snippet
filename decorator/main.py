from functools import wraps

def with_print(f):
    @wraps(f)
    def wrapper(*args):
        print("before {}".format(f.__name__))
        i = f(*args)
        print("after {}".format(f.__name__))
        return i
    return wrapper


@with_print
def double(i):
    return 2 * i


num = double(2)
print(num)

