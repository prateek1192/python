__author__ = 'Prateek'

sqr = lambda n:n**2

print sqr(5)

power = lambda x,n=0:x**n
print power(4,5)
print power(5)

l=range(16)
print filter(lambda n: n%7==0, l)
