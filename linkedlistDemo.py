#Linked List Demo Pythom

class node:
    def __init__(self, Indata):
        self.data = Indata
        self.nextNode = None

def transverse(head):
    if (head.nextNode == None):
        return
    tempStore = head
    while tempStore is not None:
        print(tempStore.data)
        tempStore = tempStore.nextNode

def addnode(head, data):
    addNode = node(data)
    addNode.nextNode = None
    lastNode = head
    while lastNode.nextNode is not None:
        lastNode = lastNode.nextNode
    lastNode.nextNode = addNode

def insertNode(head, data, location):
    if (location == 0):
        return
    count = location - 1
    newNode = node(data)
    iter = head
    while iter.nextNode is not None:
        #iter = iter.nextNode
        count -= 1
        if(count == 0):
            break
        iter = iter.nextNode
    newNode.nextNode = iter.nextNode
    iter.nextNode = newNode

def atBegin(head, data):
    newNode = node(data)
    tempStr = head.data
    tempNxtnode = head.nextNode
    head.data = newNode.data
    head.nextNode = newNode
    newNode.data = tempStr
    newNode.nextNode = tempNxtnode
    return head

def start():
    headnode = node(1)
    headnode.nextNode = None
    addnode(headnode,2)
    addnode(headnode,3)
    addnode(headnode,4)
    #insertNode(headnode, 673, 2)
    headnode = atBegin(headnode, 55)
    headnode = atBegin(headnode, 45)
    headnode = atBegin(headnode, 89)
    insertNode(headnode, 611, 0)
    addnode(headnode, 30)
    addnode(headnode, 47)
    # node1 = node(2)
    # node2 = node(3)
    # node3 = node (4)
    # headnode.nextNode = node1
    # node1.nextNode = node2
    # node2.nextNode = node3
    # node3.nextNode = None

    transverse(headnode)

if __name__ == "__main__":
    start()

