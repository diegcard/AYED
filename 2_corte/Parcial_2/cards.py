from sys import stdin

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def setNext(self, next):
        self.next = next

    def setPrev(self, prev):
        self.prev = prev

    def setValue(self, value):
        self.value = value

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def getValue(self):
        return self.value

    def clear(self):
        self.setNext(None)
        self.setPrev(None)

    def hasVal(self, val):
        return self.value == val

class LinkedList:
    # Create
    def __init__(self):
        self.head = None
        self.len = 0

    # Is Empty
    def isEmpty(self):
        return self.head == None

    def goToTail(self):
        currentNode = self.head
        while currentNode.getNext() != None:
            currentNode = currentNode.getNext()
        return currentNode

    # Insert Values
    def insert(self, value):
        node = Node(value)
        if self.isEmpty():
            self.head = node
        else:
            tail = self.goToTail()
            tail.setNext(node)
            tail.setPrev(tail.getPrev())
        self.len += 1

    def search(self, value):
        currentNode = self.head
        while currentNode != None and not currentNode.hasVal(value):
            currentNode = currentNode.getNext()
        return currentNode

    def update(self, value, newValue):
        nodeToSearch = self.search(value)
        if nodeToSearch != None:
            nodeToSearch.setValue(newValue)

    def __len__(self):
        return self.len

    def __str__(self):
        listMembers, currentNode = [], self.head
        while currentNode is not None:
            listMembers += [currentNode.getValue()]
            currentNode = currentNode.getNext()
        return str(listMembers)

    def printList(self):
        listMembers, currentNode = [], self.head
        while currentNode is not None:
            listMembers += [currentNode.getValue()]
            currentNode = currentNode.getNext()
        print(str(listMembers))

    def delete(self, value):
        currentNode = self.head
        # Caso Vacío
        if self.isEmpty():
            return None
        # Caso primer valor solicitado
        if currentNode.hasVal(value):
            self.head = currentNode.getNext()
            return currentNode
        else:
            next = currentNode.getNext()
            while next is not None and not next.hasVal(value):
                currentNode, next = next, currentNode.getNext()
            if next:
                currentNode.setNext(next.getNext())
                next.setNext(None)
            return next

class Queue:
    def __init__(self):
        self.list = LinkedList()

    def enqueue(self, value):
        node = Node(value)
        if self.list.isEmpty():
            self.list.head = node
        else:
            currentTail = self.list.goToTail()
            currentTail.setNext(node)

    def dequeue(self):
        if self.list.len == 1:
            self.list.head.clear()
            self.list.len -= 1
        else:
            self.list.delete(self.list.head.getValue())

    def getHead(self):
        return self.list.head

    def printQueue(self):
        currentNode = self.list.head
        while currentNode:
            print(currentNode.getValue(), end=' ')
            currentNode = currentNode.getNext()
        print()

    def queueToList(self):
        lista = []
        currentNode = self.list.head
        while currentNode:
            lista += [currentNode.getValue()]
            currentNode = currentNode.getNext()
        return lista

    def __len__(self):
        currentNode = self.list.head
        cant = 0
        while currentNode:
            cant += 1
            currentNode = currentNode.getNext()
        return cant

def cardsPack(cards, discards):
    if len(cards) < 2:
        return discards
    discards.enqueue(cards.getHead().getValue())
    cards.dequeue()
    aux = cards.getHead().getValue()
    cards.dequeue()
    cards.enqueue(aux)
    return cardsPack(cards, discards)

def main():
    n = stdin.readline().strip()
    while n != "0":
        cards = Queue()
        for i in range(1, int(n) + 1):
            cards.enqueue(i)
        discards = Queue()
        resp = cardsPack(cards, discards)
        print("Discarded cards: " + ", ".join(map(str, resp.queueToList())))
        print("Remaining card:", cards.getHead().getValue())
        n = stdin.readline().strip()
main()
