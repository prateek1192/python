__author__ = 'Prateek'

from sys import argv,stdout

def  usage():
    print "Usage:"
    print "Please enter source files to search for and then the extension to search for"
    exit(1)

def directory_listing(*directories):
    file_glob = directories[-1]
    for directory_name in directories[:-1]:
        abs_path = join(directory_name,file_glob)
        for file_name



if len(argv)<=3:
    usage()
else:
    print "You have entered",
    print argv
    directory_listing(*argv[1:])

