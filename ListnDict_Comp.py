#List and Dictionary comprehension Demo

def start():
    dic = {x:x*2 for x in range(0,10) }
    listed = [2*x for x in range (0,5) if x > 1 ]
    print(dic)
    print(listed)

if __name__ == '__main__':
    start()
