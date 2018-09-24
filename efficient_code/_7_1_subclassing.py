# source https://www.youtube.com/watch?v=miGolgp9xq8
# firs of all , there are three different behaviour for subclass.
# 1 add a completely new behavior/method
# 2 overriding what is already there. like a subclass is dog, it sounds differently.
# 3 extending: this is to extend a existing method, adding some more feature.

# second, there are anothre use: dynamic dispatch from different subclass

# a explanation of the class.
# instance saved the data, and the corresponding function is common , and saved int the class.
# it means, the data delegate work to this class.
# same as the subclass.
# it means subclass delegate the work to parent class
# the diretion is : instance(data) --> subclass --> parentclass

# remember, the one who incharge, is the subclass. always from the bottom

# altimately, subclass is just way to Reuse code!! it is less about the concept of who is parent, who is child

# a trick:
# what if you dont' want a method to be overwritten.?
# 1 any named method start with __ two underscore, is invisible to the child.
# so it would never be overriten
# however, I also dont want to make the name wiered. since it is called parent.__something()

# the reason for this is actually, in parent class, you also called this function from other method.
# and you want to stick to it for the parent class.
# todo: I still dont' undertand here. why use __ to hide it ?
class Parent(object):
    def __init__(self):
        print 'parent: init'
    def update(self):
        print 'parent: called update'

class Child(Parent):
    def __init__(self):
        print 'Child: init'
    def update(self):
        print 'Child: called update'
        print Parent.update()

def one_method(some_obj):
    some_obj.update()

one_method(Parent())
one_method(Child())

