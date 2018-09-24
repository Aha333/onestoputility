# source : https://www.youtube.com/watch?v=OSGv2VnC0go

Color = ['red', 'green', 'blue']

# Example 1
# Wrong
# This is very C style
for i in range(len(Color)):
    print Color[i]
# Right
for c in Color:
    print c
for i, c in enumerate(Color):
    print i, c

# Example 2
# wrong: loop through 2 list at the same time.
# this is going to use extra memory
Names=['Gordon','David','BS','T']
for name, color in zip(Names, Color):
    print name, color
# what is better: the izip, but seems like it is not in python 2

# Example 3 other loop. These are all very python way.
for name in sorted(Names):
    print name
for name in sorted(Names, reverse=True):
    print name
for name in reversed(Names):
    print name
