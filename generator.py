__author__ = 'Prateek'

def grepme(file_name, selection):
    return (line for line in open(file_name) if line.startswith(selection) )

g = grepme('cmd.py','i')


for i in g:
    print i

