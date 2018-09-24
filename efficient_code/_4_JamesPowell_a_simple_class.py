class Polynomial(object):
    def __init__(self, *coeffs, **named_coeffs):
        self.coeffs = coeffs
        print coeffs
        print named_coeffs


    def __repr__(self):
        return "Polynomial(*{!r})".format(self.coeffs)  # todo: that is is !r mean?

p1 = Polynomial(1, 2, 3)

p2 = Polynomial(1, [2, 3], 3, s=3)

# notice the difference of the below
print " examples 1 "
p4 = Polynomial([1,2,3])
p3 = Polynomial(*(1,2,3))
p4 = Polynomial(*[1,2,3])
# p4 = Polynomial(**[1,2,3]): TypeError type object argument after ** must be a mapping, not list

# notice the difference here
print " examples 2 "
p41 = Polynomial({'a':1,'b':3})
p42 = Polynomial(*{'a':1,'b':3})
p43 = Polynomial(**{'a':1,'b':3})  # it means, double * will translate it to be a=1, b=3


print p41
print p42
print p43