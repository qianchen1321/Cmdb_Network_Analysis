#不带参数的装饰器

def deco_Withargs(flags):
    def decorate(func):
        def yapper(*args, **kwargs):
            if flags:
                print('I got a deco and flag is true')
            else:
                print('I got a deco and but flag is false')
            return func(*args, **kwargs)
        return yapper
    return decorate
@deco_Withargs(False)
def func(msg):
    print(f'the deco with args innter func has msg is : {msg}')

def deco_args(func2):
    def zapper(*args, **kwargs):
        print('I got a deco')
        return func2(*args, **kwargs)
    return zapper
@deco_args
def func2(msg):
    print(f'inner func2 has msg is : {msg}')


def decorate_singleton(cls):
    def wrapper(*args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = cls(*args, **kwargs)
        else:
            print("I have bee created, so Iam just an old instance!")
    return wrapper
@decorate_singleton
class Register:
    pass

class Decorate3:
    def __init__(self, func):
        print('I am initialint ')
        self.func = func

    def __call__(self, *args, **kwargs):
        print('I am called')
        return self.func(*args, **kwargs)

@Decorate3
def func3(msg):
    print(f'msg is {msg}')
a = 3
if __name__ == "__main__":
    if a == 1:
        func("hello my pdf simple start")
    elif a == 2:
        func2("now it is just name deco_args")
        x = Register()
        y = Register()
        id_x = id(x)
        id_y = id(y)
        print(f'x id is:{id_x} \ny id is :{id_y}')
    else:
        print("no other choice ?, class deco")
        func3('hello hollywood ,we are coming')


