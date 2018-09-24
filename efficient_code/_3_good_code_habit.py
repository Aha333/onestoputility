# source : https://www.youtube.com/watch?v=OSGv2VnC0go

# 1 always quote the parameters with names
# example bad: search('obama', False, 30, True )
# example good: search(who = 'obama', retweet = False, times = 30, everdo = True )

# 2 use name tuples for return!
# func return :
# bad example (0,4)
# good example : namedtuple('TestResults', ['failed','attemped']
# Named tuples are basically easy-to-create, lightweight object types.
# """
# Thus, you should use named tuples instead of tuples anywhere
# you think object notation will make your code more pythonic and
# more easily readable.
# """
# btw: namedtuple is a factory function:
# A factory function is any function which is not a class or constructor that returns a (presumably new) object.
# so , if I want to define any function that return a class object type, it is actually
# a factory function.

from collections import namedtuple

NamedTupleForResult = namedtuple('SomeResults', ['failed', 'attempts'])
a = NamedTupleForResult(1, 22)

# to use it :
print a
print a[1]


# there is a discussion about this : And yes, you can also use a self defined class
# https://stackoverflow.com/questions/9872255/when-and-why-should-i-use-a-namedtuple-instead-of-a-dictionary
# example:


class Container(object):
    def __init__(self, name, date, foo, bar):
        self.name = name
        self.date = date
        self.foo = foo
        self.bar = bar


mycontainer = Container(name=1, date='20180101', foo=1, bar=2)
print mycontainer
# or
Container = namedtuple('Container', ['name', 'date', 'foo', 'bar'])
mycontainer = Container(name=1, date='20180101', foo=1, bar=2)
print mycontainer

# Another example is here :
# https://stackoverflow.com/questions/2970608/what-are-named-tuples-in-python
# I believe we all do such coding: for parameters: it is actually not easy to read
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt
line_length = sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)

# a much better way :
# See, you can use .x, .y to get the value!
# if you implemented with a dictionary, you have to do things like pt1['x'],
# which is not as pretty as the namedtuple !
# or if you defined your own class.. it is fine, but not necessary.
from collections import namedtuple
Point = namedtuple('Point', 'x y')
pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)

from math import sqrt
line_length = sqrt((pt1.x-pt2.x)**2 + (pt1.y-pt2.y)**2)
# there is one thing: attribute in named tuple s are immutable
# pt1.x = 2.0
# AttributeError: can't set attribute

# 3 some other
# interesting trick:
# updating multiple state variables
# for example, in simulation, you may want to update something after a period
# my current code is like :
# for t in range(100):
#     curr_open_car = updated_car
#     curr_request = updated_req
#     t = y  #  a temporary value needed!!, and the order matters
#     y = x+y
#     x =t

# a much better way ! this is also faster in python
# for t in range(100):
#     curr_open_car, curr_request, x, y = \
#       updated_car, updated_req, x+y, x  # you don't need temporary value t, and order not matter!
# Isn't this beautiful!!!?


# trick 2 : concatenating strings
# for name in ..
#   s += ', ' + name
# or
# better way: just join them !
# ', '.join(names)


