from doublinlist import ListNode, DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = DoublyLinkedList()
        self.size = 0

    def append(self, item):
        if self.size == 0:
            self.data.add_to_head(item)
            self.size += 1
        else:
            self.size += 1
            if self.size <= self.capacity:
                self.data.add_to_tail(item)
            else:
                self.data.remove_from_head()
                self.data.add_to_tail(item)
                new_tail = self.data.tail.prev
                self.data.tail.prev = None
                self.data.tail.next = self.data.head
                self.data.head.prev = self.data.tail
                self.data.head = self.data.tail
                self.data.tail = new_tail
                self.data.tail.next = None
            

    def get(self):
        data = []
        if self.data.head is self.data.tail:
            data.append(self.data.head.value)
        else:
            current = self.data.head
            while current.next is not None:
                data.append(current.value)
                current = current.next
            data.append(self.data.tail.value)
        return data#[::-1]

# class RingBuffer:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.data = []
    
#     class __Full:
#         def append(self, item):
#             self.data[self.cur] = item
#             self.cur = (self.cur+1) % self.capacity
#         def get(self):
#             return self.data[self.cur:] + self.data[:self.cur]

#     def append(self, item):
#         self.data.append(item)
#         if len(self.data) == self.capacity:
#             self.cur = 0
#             self.__class__ = self.__Full

#     def get(self):
#         return self.data

buff = RingBuffer(5)
buff.append('a')
buff.append('b')
buff.append('c')
buff.append('d')
buff.append('e')
buff.append('f')