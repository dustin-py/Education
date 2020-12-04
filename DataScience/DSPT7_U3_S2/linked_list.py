class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def get_value(self):
        return self.value
        

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
        
    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        old_head = self.head
        self.head = new_node
        self.head.next = old_head
        
    def remove_head(self):
        data = self.head.get_value()
        if self.head is None:
            return data
        self.head = self.head.next
        return data
        
    def remove_tail(self):
        data = self.tail.get_value()
        if self.tail is None:
            return data
        empty_pointer = self.head
        while empty_pointer.next.next is not None:
            empty_pointer = empty_pointer.next
        self.tail = empty_pointer
        self.tail.next = None
        return data