# source : https://www.youtube.com/watch?v=OSGv2VnC0go

# Lesson 2
# Summary:
# 1 list use enumerate(list), dictionary use dict.iteritems()
# 2 you can construct a dictionary easily from two list: dict(zip(list1, list2))
from collections import defaultdict

d = {'math': 1, 'english': 2, 'green': 3}
for k in d:
    print k

# Example 1:loop with both key and value
for k in d:
    print k, d[k]  # this is not efficient enough, as it will lookup the key again!
# solution 1: this would take more memory
for k, v in d.items():
    print k, v
# solution 2: better way! without make a new list
for k, v in d.iteritems():
    print k, v

# Example 2: how to construct a dictionary from pairs
# sometimes, I may just want two list: like a time list, and a value list
# but we also want to make it easy to lookup the corresponding value
times = [20180101, 20180102, 20180103]
requests = [100, 232, 131]

# if I want to know that is the corresponding value for 20180102,
# i may have to find the index for 20180102, and then got it .
for i, t in enumerate(times):
    if t == 20180102:
        print requests[i]
# this looks not good. another way is to construct a dictionary:
# this is beautiful!
d = dict(zip(times, requests))
print d
print d[20180102]

# another example:
d2 = dict(enumerate(times))
print d2

# Example 3 Deal with missing key
# one way to do it is to have : if k not in keys.  but there is a better way
d = {'a': 1, 'b': 2, 'c': 3}
to_find_key = 'e'
if to_find_key not in d:
    print 0
else:
    print d[to_find_key]
# solution 1 better way :
print d.get(to_find_key, 0)  # where 0 is the default value if not found

# solution 2 better way!
# we should define the default at the first place!

# https://docs.python.org/2/library/collections.html
# "When each key is encountered for the first time,
# "it is not already in the mapping; so an entry is automatically created
# "using the default_factory function which returns an empty list
d = defaultdict(list)
print d['a'] + [3]
# or
d = dict()
print d.get('a', []) + [3]


