__author__ = 'Prateek'

from sys import argv,exc_info
def safe_float(value):
    try:
        return float(value[1])
    except ValueError,e:
        print e
    except (IndexError,KeyError),e:
        print e
        print e.__class__
    except:
        '''
        print "internal server error"
        print exc_info()[0]
        print exc_info()[1]
        print exc_info()[2]
        '''
        print print_tb(exc_info()[2])
    finally:
        "finally block of exception handling"


print safe_float(argv)
