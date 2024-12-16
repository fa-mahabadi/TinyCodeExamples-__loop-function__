import time
from functools import cache


def outter_time_process(func):
    def inner_time_process(n):
        start = time.perf_counter()
        f = func(n)
        end = time.perf_counter()
        total_time = end - start
        return f"{func.__name__}({n}): Took {total_time:.5f} seconds"
    return inner_time_process


@cache
@outter_time_process
def fib(n):
    if n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


@cache
@outter_time_process
def fact(n):
    return n * fact(n - 1) if n else 1


with open("runtime.txt", "a") as f:
    f.write(f"{fib(50)}\n")
    f.write(f"{fact(50)}\n")
