__author__ = 'Prateek'

from Day2 import Person

class Employee(Person):

    def __init__(self,eid,first_name,last_name,gender,desg):
        self.eid = eid
        self.desg = desg
        '''
        base class version init
        '''
        super(Employee, self).__init__(first_name,last_name,gender)

    def get_info(self):
        print "Employee Id :{}".format(self.eid)
        super(Employee,self).get_info()
        print "designation : {}".format(self.desg)

if __name__ == '__main__':
    e = Employee('v4001','guido','rossum','male','clerk').get_info()

    e = Person('allen','paul','male')


