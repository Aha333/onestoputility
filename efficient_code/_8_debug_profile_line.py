# Here is a very interesting way to profile things!
# source : https://lothiraldan.github.io/2018-02-18-python-line-profiler-without-magic/
#
import line_profiler
import atexit
profile = line_profiler.LineProfiler()  # here is the decorator
atexit.register(profile.print_stats)  # this will print out result when exist the function
#
import time
@profile # this profile decorator is used to generate the profile
def is_addable(l, t):
    for i, n in enumerate(l):
        for m in l[i:]:
            if n + m == t:
                return True

    return False


assert is_addable(range(20), 25) == True
assert is_addable(range(20), 40) == False



@profile
def another():
    process_one_thing(0.1)
    process_one_thing(0.2)
    process_one_thing(0.2)

def process_one_thing(t):
    1+1
    time.sleep(t)
another()

