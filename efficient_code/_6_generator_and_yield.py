# Topic: Generator
# here is the usage: when we only need to use the value one by one, though the function return a lot more.
# we can put it as yield. But remember, the usage would be then as
# #      for i in iterator_obj
# the original function returns a iterator object.
# source : https://www.youtube.com/watch?v=7lmCu8wz8ro

# Question: the overall time for me still the same? why I use it ?
# Answer : https://stackoverflow.com/questions/7883962/where-to-use-yield-in-python-best
# yield is best used when you have a function that returns a sequence and you want to iterate over that sequence,
# but you do not need to have every value in memory at once. but I save a lot of memory usage.

# as a generator, you can use : gen.next().
# each time you call the generator.next() or use for i in generator, it would return the value of the yield value
# until it run out of ?

# If the body of a def contains yield, the function automatically becomes a generator function.
#
# todo: is it only to save memeory??

def another_example():
    print 'some process 1 '
    yield 'first time done'  # this would return the value after yield, the string here

    print 'some process 2 '  # the second time call the function.
    yield  # yeild nothing ( no value return , but still yield)

    print 'some process 3 '  # question : when is this been executed??


cnt=0
print type(another_example())
for result in another_example():
    print 'result is {}'.format(result)
    cnt = cnt + 1
    print '   cnt of time = {} end'.format(cnt)

print '--------- - what if we run it again -------------'
print [i for i in another_example()]
print '--------- - what if we run it again with next? -------------'
generator1 = another_example()
print generator1.next()
print generator1.next()
# print generator1.next() # the third time is going to have error StopIteration
# todo: you can see the difference, the third next would print 'some process 3',
# but with error, because there is no next 'yield' in function
# however, in the for loop for result in another_example():, it will print 'some process 3', without error
print '--------------------------'

from time import sleep


def compute():
    result_list = []
    for i in range(3):
        result = i + 2
        sleep(.1)
        result_list.append(result)

    return result_list


def compute_with_yield():
    for i in range(3):
        print 'start'
        result = i+2
        sleep(.3)  # here it takes time to compute
        print 'end'
        yield result  # here is the same as the above example, you yield range(3) times!!! each yield return some number


for i in compute():
    print i

for r in compute_with_yield():  # the time actually start from here, it will start run function in compute()
    print 'main start'
    print r
    print 'main median'
    sleep(.3)  # this could be call another server
    print ','
    print 'main end'


# actually you can write a generator that have infinite value:

# An infinite generator function that prints
# next square number. It starts with 1
print "--------------------------------------"


def nextSquare():

    i = 1;

    # An Infinite loop to generate squares
    while True:
        print 'here is A'
        yield i
        print 'here is B'
        i += 1  # todo: Next execution resumes from this point
        #  todo: here is the reason why you can have more!!
        print 'here is C'


# Driver code to test above generator
# function
for num in nextSquare():
    if num > 3:
         break
    print(num)
    print '-----'


print "--------------------------------------"
def genDiff():
    i = 1
    yield i
    yield (2,3)
a= genDiff()
print a[1]

