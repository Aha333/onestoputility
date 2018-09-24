# source : https://www.youtube.com/watch?v=OSGv2VnC0go

# Question https://softwareengineering.stackexchange.com/questions/166699/python-factory-function-best-practices

# Suppose I have a file foo.py containing a class Foo:
#
# class Foo(object):
#    def __init__(self, data):
#       ...
# Now I want to add a function that creates a Foo object in a certain way from raw source data. Should I put it as a static method in Foo or as another separate function?
#
# class Foo(object):
#    def __init__(self, data):
#       ...
# # option 1:
#    @staticmethod
#    def fromSourceData(sourceData):
#       return Foo(processData(sourceData))
#
# # option 2:
# def makeFoo(sourceData):
#    return Foo(processData(sourceData))
# I don't know whether it's more important to be convenient for users:
#
# foo1 = foo.makeFoo(sourceData)
# or whether it's more important to maintain clear coupling between the method and the class:
#
# foo1 = foo.Foo.fromSourceData(sourceData)

# Answer: the class-method way is better
# your end-user could import just the Foo class and use it for the various ways you can create it, as you have all the factory methods in one place:
# from foo import Foo
# Foo()
# Foo.fromFrobnar(...)
# Foo.fromSpamNEggs(...)
# Foo.someComputedVersion()

# todo: give an example code:
# file1: class A definition, with a factory method. buildFrom(type=.., source=...).
#        the implementation can be in file 2. so it looks clean
# file2: here we write all different factory functions. Given some input or source, we build the class A
# the reason for this is that users would only need to import file 1 , but not need to import file 2

# this also means to have the extra constructor of a class.
# remember, like datetime(, ), or datetime.now(), or datetime.fromtimestamp() are all similar idea
# but remember, you should make it a class mehtod
# https://www.youtube.com/watch?v=HTLu2DFOdTg
# class Foo():
#    @classmethod
#    def from_other source(cls, par):
#        return  cls(...)

# speak of this , @staticmethod, is kind of tools that associate to the business rule of the class.
# but it is not associated to the class data.
