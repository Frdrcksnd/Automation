class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class SLinkedList:

    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def insert_middle(self, data1, data2):
        new_node = Node(data2)
        temp = self.head

        while temp.data != data1:
            temp = temp.next
        redirect = temp.next
        temp.next = new_node
        new_node.next = redirect

    def print_list(self):
        temp = self.head

        while temp is not None:
            print(temp.data)
            temp = temp.next




list = SLinkedList()

list.insert_beginning(0)
list.insert_beginning(1)
list.insert_end(3)
list.insert_middle(1,2)
list.print_list()