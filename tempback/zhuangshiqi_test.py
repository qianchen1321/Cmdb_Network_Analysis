#coding:utf-8
# def positive_result(function):
#     def wrapper(*args, **kwargs):
#         result = function(*args, **kwargs)
#         assert result >= 0, function.__name__ + "() result isnot > 0"
#         return result
#     wrapper.__name__ = function.__name__
#     wrapper.__doc__ = function.__doc__
#     return wrapper
import functools


def positive_result(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        assert result >= 0, function.__name__ + "() result isnot > 0"
        return result
    return wrapper

@positive_result
def discrim(a, b, c):
    return (b ** 2) - (4 * a * c)

print(discrim(3, 5, 1))

