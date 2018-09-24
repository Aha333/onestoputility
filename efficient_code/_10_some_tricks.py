#https://www.youtube.com/watch?v=WiQqqB9MlkA
import functools

def f(a,b=3):
    return a+b


f2 = functools.partial(f, a=1)
print f2(b=2)

f3 = functools.partial(f, b=1)
print f3(3)


# this should be good for things like apply some variable
# df.apply(a_function_that_have_two_variable_but_fixed_one_value)




# https://www.youtube.com/watch?v=pMgmKJyWKn8
# here is interesting : type check
# package: mypy

# https://www.youtube.com/watch?v=MYucYon2-lk
# next level test.
# also type check ( contract)