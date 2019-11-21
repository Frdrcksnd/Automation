class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
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
            new_node.prev = temp

    def delete_node(self, d):
        pass

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def print_reverse(self):
        temp = self.head
        while temp.next:
            temp = temp.next
        while temp.prev:
            print(temp.data)
            temp = temp.prev
            if temp.prev is None:
                print(temp.data)
                break

    def delete(self, n):

        if self.head is None:
            raise IndexError('Empty list')
        else:
            temp = self.head
            i = 0
            while temp.next and i != n:
                temp = temp.next
                i += 1
            if n != i:
                raise IndexError('n is out of bounds')
            my_node = temp

            pre = my_node.prev
            suc = my_node.next
            if n != 0:
                pre.next = suc
            if suc is not None:
                suc.prev = pre
            my_node.next = None
            my_node.prev = None
            if n == 0:
                self.head = suc


list = DLinkedList()
list.insert_beginning(4)
list.insert_beginning(2)
list.insert_beginning(3)
list.insert_beginning(2)
list.insert_end(5)
list.print_list()
print('EOD')

list.delete(0)
list.print_list()