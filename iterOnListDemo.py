#Iterating over list demo

class nodes:
    def __init__(self, data):
        self.data = data

def start():
    x = []
    x.append(nodes("a"))
    x.append(nodes(5))
    x.append(nodes("d"))
    x.append(nodes(6))
    itr = iter(x)

    print(itr.__next__().data)
    print(itr.__next__().data)
    print(itr.__next__().data)
    print(itr.__next__().data)

if __name__ == "__main__":
    start()
