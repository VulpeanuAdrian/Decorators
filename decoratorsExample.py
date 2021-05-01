import random

print(random.sample(range(1, 50), 6))


class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "( " + str(self.x) + " , " + str(self.y) + " )"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
        return Vector(self.x + other.x, self.y + other.y)


z = Vector(1, 2)
s = Vector(1, 3)
print(s + z)
print(z)


def timer1(func):
    import time
    def wraper_timer(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print('{0} execution  time is {1} sec'.format(func.__name__,t2 - t1))
        return result

    return wraper_timer


@timer1
def function1():
    s = 0
    for i in range(100000):
        s += i ** 4
    return s

function1()


def outer_func():
    def inner_function():
        print("Hello world")
    return inner_function()
print(1)
outer_func()