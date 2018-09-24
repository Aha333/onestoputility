# a deeper thoughts
# the format
#   @cache
#   def func1(...)
# only need the cache to be a function that take function!!!!!
# then it act like a wrap
# to run func1(...) is going to be cache(func1)(...)
# but, it is not exactly like this.

def funcA(x):
    print 'called funcA with x = {}'.format(x)

def funcB(x):
    print 'called funcB with x = {}'.format(x)

def wrapper(func_to_wrap):
    print 'called wrapper: only once if use @syntax'
    cnt ={}
    cnt[func_to_wrap.__name__] = cnt.get(func_to_wrap.__name__, 0) + 1
    print 'outer:  ',cnt

    def _wrapper(*args):
        print 'called wrapper2'
        value = func_to_wrap(*args)

        cnt[func_to_wrap.__name__] = cnt.get(func_to_wrap.__name__, 0) + 1
        print 'inner:  ',cnt
        return value

    return _wrapper


wrapper(funcA)(1)  # this is to run wrapper(func1) first, and the return is a function.
wrapper(funcB)(2)  # only been called twice

print(id(funcA))

print '----- you can notice the difference. it only execute once!------'


@wrapper
def func11(x):  # first time :here in the definition stage, will run just one time. that is why it can be used globally
    print 'called func11 with x = {}'.format(x)


func11(1)   # second time
func11(2)   # third time

print(id(func11))

## Another thing. This is like the 3 layer wrapper, given some other paramters
# the core is to return a function that takes function as input
print '----- Another example: WrapperFactory------'


def WrapperFactory(mode):
    if mode == 'cache':
        return wrapper


@WrapperFactory('cache')
def func11(x):  # here in the definition stage, will run just one time. that is why it can be used globally
    print 'called func11 with x = {}'.format(x)


func11(1)
func11(2)

print(id(func11))
# you also should know the syntax @.. a function, is equal to generated a New function! or a new instance!
# that is why you can do something during this declaration stage
