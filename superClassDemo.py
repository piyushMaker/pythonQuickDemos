#Super Class Demo

class twosuper:
    def __init__(self):
        print("killer code")
class mysprclass(twosuper):
    _a = 40
    def __init__(self):
        print("Hello Init superclass")
    def accdata():
        s = "this is module"
    def __str__(self):
        return "this is mysprclass"

class test(mysprclass):
    def __init__(self, name, age):
        super(mysprclass, self).__init__()
        self.name = name
        self.age = age
    def justprint(self):
        print("Name {0} and age {1}".format(self.name, self.age))

def start():
    obj1 = test('david', 0.4) #Prints "killer code"
    print(obj1._a) #40
    print(obj1) #Prints "this is mysprclass"
    obj1.justprint() #prints "Name david and age 0.4"

if __name__ == '__main__':
    start()
