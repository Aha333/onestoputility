# source : https://www.youtube.com/watch?v=OSGv2VnC0go

# cache function
# normally the cache is to cache things in the hard-drive.
# however, there is another case, is to just cache variable in memory.
# Think about this case:



from functools import wraps


# https://stackoverflow.com/questions/308999/what-does-functools-wraps-do
def call_endpoint_for_info():
    # this is where it takes a lot of times
    print 'used once'
    return {'a': 1, 'b': 2}  # this is


def pull_info(list_of_members):
    info_dict = call_endpoint_for_info()
    result = []
    for member in list_of_members:
        raw_value = info_dict.get(member, 0)
        # some other process
        raw_value = raw_value + 10
        result.append(raw_value)
    return result


print pull_info(['a', 'b', 'c'])
print pull_info(['a', 'd'])
print pull_info(['a'])

# ##  Solution ##

print "-------------------- the function is only used once! ------------------------------"
print 'if...', (1, 2) == (1, 2)
# so what if I want to make the call_end_point_for_info() cached.


# todo: the cache signature only work for basic args like string, list of string, numbers. consider assert type
def cache(func):
    key_value_cached_dict = {}
    # let' try to see if it can count
    count = {}
    key_calledcount_dict = {}

    print ":++++++++ this is run once at the declaration of the function ( to be cached ) {}".format(count)
    print ": id(saved) : = {}".format(id(key_value_cached_dict))
    print " different id number means the saved is at different namespace, so it would not be shared "
    # ok , here, this initiation only ONCE!!! And it is at
    # important: it is at the definition of the to be cached function level!!!

    @wraps(func)
    def newfunc(*args, **kwargs):
        key = args + tuple(sorted(kwargs.items()))
        key = str(key)  # this is because when input is list, not hashable

        count[func.__name__] = count.get(func.__name__, 0) + 1
        key_calledcount_dict[key] = key_calledcount_dict.get(key, 0) + 1
        print " ::: begin call {} the {} time!".format(func.__name__, count[func.__name__])
        print " ::: step 1 call time = {} with key ={}".format(key_calledcount_dict[key], key)

        if key in key_value_cached_dict:
            print '::: step 2(A) already exist.'
            print "::: end: returned value "
            print ""
            return key_value_cached_dict[key]
        print '::: step 2(B) , new'
        result = func(*args, **kwargs)
        key_value_cached_dict[key] = result
        print '::: step 2(B) , saved'
        print "::: end: returned value "
        print ""


        return result

    return newfunc

#




@cache
def call_endpoint_for_info_2(url):
    # this is where it takes a lot of times
    print 'version 2 : used once url = {}'.format(url)
    return {'a': 1, 'b': 2}  # this is




def pull_info_2(list_of_members):
    info_dict = call_endpoint_for_info_2('p')
    result = []
    for member in list_of_members:
        raw_value = info_dict.get(member, 0)
        # some other process
        raw_value = raw_value + 10
        result.append(raw_value)
    return result


print pull_info_2(['a', 'b', 'c'])
print pull_info_2(['a', 'd'])
print pull_info_2(['a'])

# one test:
# let's test if the cache is going to confuse functions
print "-------------------- test cache 2 ------------------------------"

print ' *************  begin the definition of to be cached function'
@cache
def func1(p=1):
    print 'actual run func1 :'
    return p


@cache
def func2(r, p=1):
    print 'actual run func2 :'
    return p


print ' *************   end the definition of to be cached function'


func1(p=1)
func1(p=1)
func1(p=1)

func2(0, p=1)
func2(0, p=1)
func2(0, p=1)

# todo: may want to do a test case fot different cases and types
print func2(0, p=[1, 2])
print func2(0, p=[1, 2])
print func2(0, p=[1, 2])

print func2(0, p={'s1': 2})
print func2(0, p={'s1': 2})



