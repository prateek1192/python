__author__ = 'Prateek'

from sys import argv

open(argv[0])

with open(argv[0]) as fp:
    print fp
'''
#l = ['pam' , '5', 'charlie' , '9' ,'kim' ]
#l.reverse()
#l.sort(reverse=False)
print l
for item in sorted(l,reverse=True):
    print item
mat = [ [1,2,3], [4,5,6], [7,8,9] ]

print [row[1] for row in mat]

l = range(0,8)
#shuffle(l)
res = [i ** i for i in l]
print res
'''
'''
def center(string_content, width, fill):
    num_fill = width-len(string_content)
    print fill*int(num_fill/2),
    print string_content,
    print fill*int(num_fill/2)

center('pppp',10,"-")
'''
'''
def demo(*args):
    print args

demo(1)
demo("peter")
demo(1,"pam",3,4,5,6,7,)

l = [1,2,3]
m = (5,6,7)

demo(l)
demo(m)

demo(*l)
demo(*m)
'''
'''
name,age = "pam",2
print ("I am {}, {} years old").format(name,age)
l = ("pam",2)
print ("I am {}, {} years old").format(*l)
'''