class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev=None):
        if self.head is None:
            self.head = None
            return None
        else:
            if node.next_node is None:
                self.head = node
                return
            self.reverse_list(node.get_next())
            temp = node.get_next()
            temp.next_node = node
            node.next_node = None

        # def reverse_list(self, node, prev):
        #     if self.head is None or self.head.next_node is None:
        #         return self.head
            
        #     rest = self.reverse_list(self.head.next_node, None)
        #     self.head.next_node.next_node = head
        #     self.head.next_node = None
            
        #     return rest

list = LinkedList()
list.add_to_head(1)
list.add_to_head(2)
list.add_to_head(3)
list.add_to_head(4)
list.add_to_head(5)
#list.reverse_list(list.head, None)