__author__ = 'Prateek'

class Connector(object):

    max_connection = 5
    counter = 0

    def __str__(self):
        return "{}:Connection id:{}".format(Connector.counter,self.connection_id)

    def __init__(self,connection_id):
        Connector.check_connection()
        Connector.counter += 1
        self.connection_id = connection_id

    @staticmethod
    def check_connection(self):
        if Connector.counter == Connector.max_connection:
            raise RuntimeError("Max connections reached")

if __name__ == '__main__':
    conn = []
    try:
        for i in xrange(1,8):
            conn.append(Connector("t"+str(i)))
            #print conn.__str__()
    except:
        pass
    finally:
        for c in conn:
            print c

    print Connector.counter
    print Connector.max_connection
