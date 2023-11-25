from random import randint
from time import time
SIZE = int(1e6)
LOWER = 0
UPPER = 1e6

class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.setValue(value)
        self.setNext(next)
        self.setPrev(prev)
    def setValue(self, new_value):
        self.value = new_value
    def getValue(self):
        return self.value
    def setNext(self, new_next):
        if not (new_next is None or isinstance(new_next, Node)):
            raise Exception("Incompatible types")
        self.next = new_next
    def getNext(self):
        return self.next
    def setPrev(self, new_prev):
        if not (new_prev is None or isinstance(new_prev, Node)):
            raise Exception("Incompatible types")
        self.prev = new_prev
    def getPrev(self):
        return self.prev
    def __str__(self):
        return "Node(" + str(self.value) + ")"

class LinkedList:
    def __init__(self, elem=[]):
        self.ln = 0
        self.setHead(None)
        self.setTail(None)
        for e in elem:
            self.append(e)
    def setHead(self, new_head):
        if not (new_head is None or isinstance(new_head, Node)):
            raise Exception("Incompatible types")
        self.head = new_head
        if self.head is not None:
            self.head.setPrev(None)
    def getHead(self):
        return self.head
    def setTail(self, new_tail):
        if not (new_tail is None or isinstance(new_tail, Node)):
            raise Exception("Incompatible types")
        self.tail = new_tail
        if self.tail is not None:
            self.tail.setNext(None)
    def getTail(self):
        return self.tail
    def __len__(self):
        return self.ln
    def isEmpty(self):
        return self.head == None
    def search(self, value):
        if self.isEmpty():
            return None
        current_node = self.head
        while current_node is not None and (current_node.getValue() != value):
            current_node = current_node.getNext()
        return current_node

    def searchValue(self, value):
        node = self.search(value)
        if node is not None:
            return node.getValue()
        return None

    def append(self, new_value):
        new_node = Node(new_value)
        if self.isEmpty():
            self.setHead(new_node)
            self.setTail(new_node)
        else:
            tail = self.getTail()
            tail.setNext(new_node)
            new_node.setPrev(tail)
            self.setTail(new_node)
        self.ln += 1

    def join(self, ll2):
        if not isinstance(ll2, LinkedList):
            raise Exception("Incompatible types")
        if not ll2.isEmpty():
            current_tail = self.tail
            current_tail.setNext(ll2.getHead())
            ll2.getHead().setPrev(current_tail)
            self.setTail(ll2.getTail())
            self.ln += ll2.ln
        return self

    def __str__(self):
        rep_str = ""
        if not self.isEmpty():
            rep_str += str(self.getHead())
            current_node = self.getHead().getNext()
            while current_node is not None:
                rep_str += "<-->"+ str(current_node)
                current_node = current_node.getNext()
        return rep_str
    
    def delete(self, value):
        value_node = self.search(value)
        if value_node is not None:
            if len(self) == 1:
                self.head, self, self.tail = None, None
            else:
                if value_node == self.getHead():
                    self.head = value_node.getNext()
                    self.head.setPrev(None)
                else:
                    prev = value_node.getPrev()
                    if value_node == self.getTail():
                        self.setTail(prev)
                    else: 
                        nxt = value_node.getNext()
                        prev.setNext(nxt)
                        if nxt is not None:
                            nxt.setPrev(prev)
            self.ln-=1
        else:
            raise Exception("Element not found")


def main():
    arr1 = [randint(LOWER, UPPER) for i in range(SIZE)]
    arr2 = [randint(LOWER, UPPER) for i in range(SIZE)]
    ll1 = LinkedList(arr1)
    ll2 = LinkedList(arr2)
    t_0 = time()
    print(len(arr1+arr2))
    t_1 = time()
    print("Time for natural addition : ", t_1-t_0)
    t_0 = time()
    print(len(ll1.join(ll2)))
    t_1 = time()
    print("Time for double linkedlist addition : ", t_1-t_0)

main()