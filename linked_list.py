class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:

    def __init__(self):
        self.head=None

    def insert(self,newNode):

        if self.head is None:
            self.head= newNode
            return
        trav = self.head

        while True:
            if trav.next is None:
                break
            trav = trav.next
        trav.next=newNode

    def trav(self):
        if self.head is None:
            print("list is empty")
            return
        trav = self.head

        while True:
            if trav is None:
                break
            print(trav.data+"",end=" ")
            trav = trav.next
        print("\n")
    def insertAtFirst(self,newNode):
        if self.head is None:
            self.head= newNode
        else:
            newNode.next= self.head
            self.head=newNode
    def delete_last_node(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head=None
        else:
            prev = None
            current = self.head
            while current.next is not None:
                prev = current
                current=current.next
            if prev is None:
                self.head= None
            else:
                prev.next=None

    def delete_first_node(self):
        if self.head is None:
            return
        next = self.head.next
        self.head=next





l = linkedlist()
firstnode = node("first")
secondnode = node("second")
thirdnode = node("third")

l.insert(firstnode)
l.insertAtFirst(secondnode)
l.insert(thirdnode)
l.trav()
l.delete_last_node()
l.trav()
l.delete_first_node()
l.trav()

