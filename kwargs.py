__author__ = 'Prateek'
'''
def demo(**params):
    print params

demo()
demo(name='pypi',version='3.7',release='beefy cow')
'''
def cat(file_name, **param):
    reverse_flag = param.get('reverse')
    count = param.get('count',0)

    with open(file_name) as fp:
        content = fp.readlines()
        if reverse_flag:
            print "Reverse is true"
            content = content[::-1]

        if count:
            content = content[:count]
        return ''.join(content)

print cat('C:\Users\IBM_ADMIN\PycharmProjects\python\Day1.py',reverse=True)
