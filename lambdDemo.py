#Simple lambda keyword usage

variable = lambda x,y,z : x+y+z

def caller():
    print(variable("lambda", "func", "3"))

if __name__ == '__main__':
    caller()