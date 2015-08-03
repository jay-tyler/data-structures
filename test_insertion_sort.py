from insertion_sort import insort
from random import randint


def forward(n):
    return [range(n)]


def backward(n):
    return [range(n).reverse()]


def random(n):
    result = []
    for x in range(n):
        result.append(randint(1, n))


def test_insertion_sort_best():
    n = 100000
    assert insort(forward(n)) == [range(n)]


def test_insertion_sort_worst():
    n = 1000
    assert insort(backward(n)) == [range(n)]


def test_insertion_sort_random():
    n = 10000
    random_list = random(n)
    assert insort(random_list) == random_list.sort()
