# we can actually choose to check the type of the return
# source: http://oez.es/Expert%20Python%20Programming.pdf
# page 50
# essentially, this means the decorator can be used to check what ever about the input and output of the function
# essentially, it is like a real_time test case. ( without run test case, you can directly test it )

class Car(object):
    def __init__(self):
        pass

def return_must_be(type_of_class):
    def wrapper(func):
        def new_func(*args, **kwargs):
            value = func(*args, **kwargs)
            if not isinstance(value, type_of_class):
                raise TypeError("?: {}, {}".format(value, type_of_class))
            print 'passed check of return'
            return value

        return new_func

    return wrapper

class A(object):
    def __init__(self):
        pass

    @return_must_be(Car)  # consider this to be an abstract class
    def a_method_must_return_objA(self):
        return Car()

a = A()
a.a_method_must_return_objA()







