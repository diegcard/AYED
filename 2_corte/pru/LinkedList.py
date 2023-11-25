class Node:
    def __init__(self, value, next = None):
        self.value = value
        if isinstance(next, Node) or (next is None):
            self.next = next
        else:
            raise 'Error en construccion del Nodo'

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def __str__(self):
        return '(' + str(self.value)+')'+ '-->' + str(self.next)

    def setValue(self, new_value):
        self.value = new_value

    def setNext(self, new_next):
        if isinstance(new_next, Node) or (new_next is None):
            self.next = new_next
        else:
            raise Exception('Error en actualizacion del Nodo')

class LinkedList:
    def __init__(self, elements=[]):
        self.head = None
        for e in elements:
            self.insert(e)

    def isEmpty(self):
        return self.head == None

    def insert(self, element):
        new_node = Node(element)
        if element is not None:
            if self.isEmpty():
                self.head = new_node
            else:
                current = self.head
                while current.getNext() is not None:
                    current = current.getNext()
                current.setNext(new_node)

    def __str__(self):
        if self.isEmpty():
            return '[]'
        else:
            return '['+str(self.head)+']'


def main():
    ls = LinkedList()
    ls.insert(5)
    ls.insert(6)
    print(ls)

if __name__ == '__main__':
    main()