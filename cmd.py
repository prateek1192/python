__author__ = 'Prateek'

from sys import argv,stdout

def  usage():
    print "Usage:"
    print "{} source-file destination-file".format(argv[0])
    exit(1)

if len(argv)!=3:
    usage()
