from functools import reduce
from itertools import chain
from itertools import dropwhile
from itertools import takewhile


def square(data_list):
    return list(map(lambda x: x * x, data_list))


if __name__ == '__main__':
    data = [1, 2, 3, 4]
    print(square(data))
    # output => [1, 4, 9, 16]

    filter_list = list(filter(lambda x: x > 2, data))
    print(filter_list)
    # output => [3, 4]

    sum_list = reduce(lambda x, y: x + y, data)
    print(sum_list)
    # output => 10

    range_list = [i for i in range(1, 10)]
    print(range_list)
    # output => [1, 2, 3, 4, 5, 6, 7, 8, 9]

    result = reduce(lambda acc, elem: acc + elem, [[2, 1], [2, 3], [3, 3], [4, 5]], [])
    print(result)

    # flatten
    flatten_list = list(chain.from_iterable([[1, 2], [3, 4]]))
    print(flatten_list)
    # output => [1, 2, 3, 4]

    # drop while
    elem_list = list(dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1]))
    print(elem_list)
    # output => [6, 4, 1]

    elem_list2 = list(takewhile(lambda x: x < 5, [1, 4, 6, 4, 1]))
    print(elem_list2)
    # output => [1, 4]

