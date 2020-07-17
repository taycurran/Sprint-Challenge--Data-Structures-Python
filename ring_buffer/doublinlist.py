"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        pass

"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # create instance of ListNode with value
        new_node = ListNode(value)
        # if DLL is empty
        if self.length < 1:
            # set head and tail to the new node instance
            self.head = new_node
            self.tail = new_node        
        # if DLL is not empty
        else:
            # set new node's next to current head
            new_node.next = self.head
            # set head's prev to new node
            self.head.prev = new_node
            # set head to the new node
            self.head = new_node
        # increment the DLL length attribute        
        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # store the value of the head
        if self.head:
            orig_head_value = self.head.value
            # delete the head
            # if head.next is not None
            if self.head.next is not None:        
                    # set head.next's prev to None
                    self.head.next.prev = None
                    # set head to head.next
                    self.head = self.head.next
            # else (if head.next is None)
            else:
                # set head to None
                self.head = None
                # set tail to None
                self.tail = None
            # decrement the length of the DLL
            self.length -= 1
            # return the value
            return orig_head_value
        else:
            return None
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # create instance of ListNode with value
        new_node = ListNode(value)
        # if DLL is empty
        if self.length < 1:
            # set head and tail to the new node instance
            self.head = new_node
            self.tail = new_node        
        # if DLL is not empty
        else:
            # set new node's prev to current tail
            new_node.prev = self.tail
            # set tails's next to new node
            self.tail.next = new_node
            # set tail to the new node
            self.tail = new_node
        # increment the DLL length attribute        
        self.length += 1

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.tail:
            # store the value of the orig tail
            orig_tail_value = self.tail.value
            # delete the tail
            # if tail.prev is not None
            if self.tail.prev is not None:        
                    # set tail.prev's next to None
                    self.tail.prev.next = None
                    # set tail to tail.prev
                    self.tail = self.tail.prev
            # else (if head.next is None)
            else:
                # set head to None
                self.head = None
                # set tail to None
                self.tail = None
            # decrement the length of the DLL
            self.length -= 1
            # return the value
            return orig_tail_value
        else:
            return None
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    # move_to_front(self.dll.head.next)
    def move_to_front(self, node):
        if node is self.tail:
            # Reset Prev and Next for New Head
            node.prev = None
            node.next = self.head
            # Make Head not Head
            self.head.prev = node
            self.head = node
        else:
            self.head = node
            self.tail = node
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    # TODO Correct move_to_front with Fixed Logic Shown Above
    def move_to_end(self, node):
        if len(self) > 0:
            if self.head is node:
                node.next.prev = None
                self.head = node.next
                # Reconfigure Tail N+P
                self.tail.next = node
                # Reconfigure Node
                node.prev = self.tail
                node.next = None
                self.tail = node
            elif self.tail is node:
                pass
            else:
                # Reconfigure Orig Node Prev
                node.prev.next = node.next
                node.next.prev = node.prev
                # Reconfigure Tail N+P
                self.tail.next = node
                # Reconfigure Node
                node.prev = self.tail
                node.next = None
                self.tail = node
        else:
            self.head = node
            self.tail = node
        

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    # TODO: This could be more robust
    def delete(self, node):
        if self.head:
            val = node.value
            if self.head is node:
                self.remove_from_head()
            elif self.tail is node:
                self.remove_from_tail()
            else:
                node.next.prev = node.prev
                node.prev.next = node.next
            #self.length = self.length - 1
            return val
        else:
            return None

        

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head:
            return None
        max_value = self.head.value
        current = self.head.next
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value
