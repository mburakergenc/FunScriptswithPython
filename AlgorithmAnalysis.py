import time


def sumofn(n):
    start = time.time()
    total = 0
    for i in range(n):
        total += i
    end = time.time()
    return total, end-start


def sumofn2(n):
    start = time.time()
    total = (n * (n+1))/2
    end = time.time()
    return total, end-start


for i in range(5):
    print("Sum is %d required %10.7f seconds" % sumofn(10000))

for i in range(5):
    print("Sum is %d required %10.7f seconds" % sumofn2(10000))

c1 = [0] * 26
print(c1)

# Lists


def test1():
    l = []
    for i in range(1000):
        l = l + [i]


def test2():
    l = []
    for i in range(1000):
        l.append(i)


def test3():
    l = [i for i in range(1000)]


def test4():
    l = list(range(1000))


import timeit
from timeit import Timer

t1 = Timer("test1()", "from __main__ import test1")
print("contac", t1.timeit(number=1000), "milliseconds")

t2 = Timer("test2()", "from __main__ import test2")
print("append", t2.timeit(number=1000), "milliseconds")

t3 = Timer("test3()", "from __main__ import test3")
print("comprehension", t3.timeit(number=1000), "milliseconds")

t4 = Timer("test4()", "from __main__ import test4")
print("range", t4.timeit(number=1000), "milliseconds")

pop_zero = Timer("x.pop(0)", "from __main__ import x")
pop_end = Timer("x.pop()", "from __main__ import x")

x = list(range(2000000))
pop_zero.timeit(number=1000)

pop_end.timeit(number=1000)

# Dictionaries

import random

for i in range(10000, 100001, 20000):
    t = Timer("random.randrange(%d) in x"%i, "from __main__ import random, x")
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j:None for j in range(i)}
    d_time = t.timeit(number=1000)
    print("%d, %10.3f, %10.3f" % (i, lst_time, d_time))
