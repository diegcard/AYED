class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    def getValue(self):
        return self.value
    def setValue(self, new_value):
        self.value = new_value
    def getNext(self):
        return self.next
    def setNext(self, new_next):
        if isinstance(new_next, Node) or new_next is None:
            self.next = new_next
        else:
            raise Exception("New Next must be Node")
    def clear(self):
        self.value = None
        self.next = None
    def __str__(self):
        next = self.next
        return "Node(" + str(self.value) + ")"

class LinkedList:
    def __init__(self, data=[]):
        self.head, self.tail, self.len = None, None, 0
        for e in data:
            self.append(e)

    def __len__(self):
        return self.len
    
    def append(self, value):
        new_node = Node(value)
        if len(self) == 0:
            self.head = new_node
            self.setTail(new_node)
        else:
            current_tail = self.tail
            current_tail.setNext(new_node)
            self.setTail(new_node)
        self.len = self.len + 1
    def search(self, value):
        current = self.head
        while current is not None and current.getValue() != value:
            current = current.getNext()
        return current
    def getHead(self):
        return self.head
    def getTail(self):
        return self.tail
    def setTail(self, new_tail):
        if new_tail is not None:
            new_tail.setNext(None)
            self.tail = new_tail
        else:
            self.tail = None
    def update(self, old_value, new_value):
        node_origin = self.search(old_value)
        node_origin.setValue(new_value)
    def slice(self, value, n=1):
        ld = LinkedList()
        node_origin = self.search(value)
        if node_origin is not None:
            current, index = node_origin, 0
            while current is not None and index < n:
                ld.append(current.getValue())
                current = current.getNext()
                index += 1
        return ld
    def isEmpty(self):
        return len(self) == 0
    def merge(self, list_b):
        if self.isEmpty():
            return list_b
        if list_b.isEmpty():
            return self
        self.tail.setNext(list_b.getHead())
        self.setTail(list_b.getTail())
    def delete(self, value):
        value_node = self.search(value)
        if value_node is not None:
            if len(self) == 1:
                self.head, self.tail = None, None
            else:
                if value_node == self.getHead():
                    self.head = value_node.getNext()
                else:
                    prev = self.head
                    while prev.getNext() != value_node:
                        prev = prev.getNext()
                    if value_node == self.getTail():
                        self.setTail(prev)
                    else:
                        prev.setNext(value_node.getNext())
            value_node.clear()
            self.len -= 1
        else:
            raise Exception("Element not found.")
    
        
    def insert(self, index, value):
        if index < 0 or index > len(self):
            raise IndexError("Index out of range")
        new_node = Node(value)
        if index == 0:
            new_node.setNext(self.head)
            self.head = new_node
            if len(self) == 0:
                self.setTail(new_node)
        else:
            current = self.head
            for i in range(index - 1):
                current = current.getNext()
            new_node.setNext(current.getNext())
            current.setNext(new_node)

        self.len += 1
    
    def __str__(self):
        rep_str = ""
        if not self.isEmpty():
            rep_str += str(self.getHead())
            current_node = self.getHead().getNext()
            while current_node is not None:
                rep_str += "<-->"+ str(current_node)
                current_node = current_node.getNext()
        return rep_str

class Queue:
    def __init__(self):
        self.data = LinkedList() 

    def enqueue(self, e):
        self.data.append(e)

    def dequeue(self):
        if len(self.data) == 0:
            raise Exception("Queue is empty")
        element = self.data.head.getValue()
        self.data.delete(element)
        return element
    
    def __str__(self):
        if len(self.data) > 0:
            return "Queue(" + str(self.data.head.getValue()) + ")"
        else:
            return "Queue()"
        
    def __len__(self):
        return len(self.data)

class Stack:
    def __init__(self):
        self.data = LinkedList()

    def push(self, e):
        self.data.insert(0, e)

    def pop(self):
        if len(self.data) == 0:
            raise Exception("Stack is empty")
        element = self.data.head.getValue()
        self.data.delete(element)
        return element

    def __str__(self):
        if len(self.data) > 0:
            return "Stack(" + str(self.data.head.getValue()) + ")"
        else:
            return "Stack()"

    def __len__(self):
        return len(self.data)

def main():
    print("------LinkedList------")
    lista = [1,2,3,4,5,6,7,8,9]
    lista = LinkedList(lista)
    print(lista , "\n")
    
    print("------Cola------")
    my_queue = Queue()
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    my_queue.dequeue()
    print(my_queue, "\n")

    print("------Pila------")
    my_stack = Stack()
    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)
    my_stack.pop()
    print(my_stack, "\n")

    print("Fila de banco")
    colaDeBanco = Stack()
    for i in range(10):
        colaDeBanco.push(i)
    print("Atendiendo", colaDeBanco)
    while len(colaDeBanco) != 0:
        print(colaDeBanco.pop())


main()