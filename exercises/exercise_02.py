#functional programming with Python
>>> data = [1,2,3,4]
>>> list(map(lambda x:x*x, data))
[1, 4, 9, 16]
>>> list(filter(lambda x:x > 2, data))
[3, 4]
>>> from functools import reduce
>>> reduce(lambda x,y: x+ y, data)
10
>>>

range
>>> [i for i in  range(1,10)]
[1, 2, 3, 4, 5, 6, 7, 8, 9]

 reduce(lambda acc,elem: acc + elem , [[2,1],[2,3],[3,3],[4,5]], [])
#faltten
>>> list(chain.from_iterable([[1,2], [3,4]]))
[1, 2, 3, 4]
>>> from itertools import chain
>>> list(chain.from_iterable([[1,2], [3,4]]))
[1, 2, 3, 4]



#drop while
>>> from itertools import dropwhile
>>> list(dropwhile(lambda x: x<5, [1,4,6,4,1]))
[6, 4, 1]

>>> from itertools import takewhile
>>> list(takewhile(lambda x: x<5, [1,4,6,4,1]))
[1, 4]
		In [9]: def groupby(data):
		   ...:     kv = {}
		   ...:     for k,v in data:
		   ...:         if k not in kv:
		   ...:             kv[k]=[v]
		   ...:         else:
		   ...:             kv[k].append(v)
		   ...:     return kv

		In [10]: data = [('a', 1), ('b',2),('a',2)]

		In [11]: groupby(data)
		Out[11]: {'a': [1, 2], 'b': [2]}

In [23]: from functools import reduce

In [24]: reduce(lambda acc,elem: acc+[elem] if not elem in acc else acc , [2,1,2,3,3,3,4,5], [])
Out[24]: [2, 1, 3, 4, 5]

In [1]: from functools import reduce

In [2]: reduce(lambda acc,elem: acc + elem , [[2,1],[2,3],[3,3],[4,5]], [])
Out[2]: [2, 1, 2, 3, 3, 3, 4, 5]


reduce(lambda acc,elem: acc + elem , [[2,1],[2,3],[3,3],[4,5]], [])

