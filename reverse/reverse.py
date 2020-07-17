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

    def reverse_list(self, node, prev):
        if self.head is None:
            return None
        elif self.head.next_node is None:
            self.head = self.head
        else:
            current_node = self.head
            nodes = []
            while current_node.next_node is not None:
                nodes.append(current_node.value)
                current_node = current_node.next_node
            last_node = current_node.value
            reverse = LinkedList()
            for value in nodes:
                reverse.add_to_head(value)
            reverse.add_to_head(last_node)
            self.head = reverse.head
            return reverse
        
        
        
list_e = LinkedList()

list_s = LinkedList()
list_s.add_to_head(1)

list_l = LinkedList()
list_l.add_to_head(1)
list_l.add_to_head(2)
list_l.add_to_head(3)
list_l.add_to_head(4)
list_l.add_to_head(5)
list_l.reverse_list(list_l.head, None)
