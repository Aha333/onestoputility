# source :http://oez.es/Expert%20Python%20Programming.pdf
# some code : https://bitbucket.org/tarek/atomisator/src/70b09278b9b46f50d2f632062f645cd56bc44433/packages/pbp.scripts/pbp/scripts/hotshotmain.py?at=default&fileviewer=file-view-default
# page: 321
# here we discussed three things
# 1 isolate the storage function as an object
# 2 isolate the signature function
# 3 storage as a global object or for each cached function
# 4 timeout of storage

from datetime import datetime
import md5
import time


##A common practice is to calculate the MD5 hash (or SHA) of arguments. But
##beware that such a hash has a real cost, and the function itself needs to be slower
##than the key calculation for the cache to be useful. For our factory function, it is
##barely the case:

# def get_key(function_called, n):
#      return md5.md5(str(n)).hexdigest()

def generate_signature(func, *args, **kw):
    key = '%s.%s:' % (func.__module__,
                      func.__name__)
    hash_args = [str(arg) for arg in args]
    # of course, will work only if v is hashable
    hash_kw = ['%s:%s' % (k, hash(v))
               for k, v in kw.items()]
    return '%s::%s::%s' % (key, hash_args, hash_kw)


class Storage(object):
    def __init__(self, mode):
        self.mode = mode
        self.cache_dict = {}
        pass

    def get_key(self, key):
        if self.mode == 'memory':
            return self.cache_dict[key]

    def save_key_value(self, key, value):
        if self.mode == 'memory':
            # todo: the problem here is that the memory wont clear , if too many cached
            # maybe give warning if too big
            self.cache_dict[key] = value


# cache = {}
# todo: here is interesting, will it share cache from different function
# answer is yes.
# what you can do is : write a class to determine if cache in memory,
# or cache in hard-drive
def memoize(gen_sig=generate_signature, storage_mode='memory', age=0):
    storage = Storage(storage_mode)
    # Note: since it is initialized within function.
    # This runs at the function definition stage, where @memoize taken place
    # so the storage object is also for every function.
    # unless you move the storage object definition outside. But not necessary
    # that case you may want to def the func to be
    # storage.get_key(key, mode).
    # storage.save_key_value(key,value mode).
    # The good thing is that storage is the same, just bigger, but you can fully control it .
    # In the middle of the program you can call the global storage to check what is been cached
    # -- or , you can use other ways to collect all the instances of the object

    # https://stackoverflow.com/questions/328851/printing-all-instances-of-a-class
    # import gc
    # for obj in gc.get_objects():
    # ...     if isinstance(obj, Storage):
    # ...             print obj.cache_dict
    # # can be slow due to a lot of object
    def _memoize(func_to_be_cached):
        def __memoize(*args, **kw):
            key = gen_sig(func_to_be_cached, *args, **kw)
            try:
                value_age, value = storage.get_key(key)
                print "key = {}, value_age= {}, age={}, time.time()".format(
                    key,
                    value_age,
                    age,
                    time.time()

                )
                expired = (age != 0 and
                           (value_age + age) < time.time())
            except KeyError:
                expired = True
            if not expired:
                return value
            storage.save_key_value(key, (time.time(), func_to_be_cached(*args, **kw)))
            return storage.get_key(key)[1]

        return __memoize

    return _memoize


from datetime import datetime


@memoize(age=3)
def what_time():
    return datetime.now().strftime('%H:%M')


@memoize(age=3)
def what_time_2():
    return datetime.now().strftime('%H:%M')


print what_time()
time.sleep(4)
print what_time()
print what_time_2()
print what_time_2()



