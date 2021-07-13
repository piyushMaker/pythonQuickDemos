# Simple Yield Keyword demo
def indefitr():
    a = 0
    while True:
        yield a
        a = a+1

def caller():
    infi = indefitr()
    for a in range(0,100):
        print(infi.__next__())

if __name__ == '__main__':
    caller()