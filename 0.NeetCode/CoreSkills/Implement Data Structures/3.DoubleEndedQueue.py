'''
双端队列（Double-ended Queue，简称Deque）是一种具有队列和栈的性质的数据结构。双端队列中的元素可以从两端弹出，添加和删除操作限制松散，比栈更灵活，比队列更通用。
使用双向链表实现一个简单的双端队列
'''
class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    def __init__(self):
        self.head = Node(-1) # dummy node as head
        self.tail = Node(-1) # dummy node ad tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
      
    def insertFront(self, val: int) -> None:
        node = Node(val, self.head, self.head.next)
        self.head.next.prev = node
        self.head.next = node
        self.size += 1
    
    def insertLast(self, val: int) -> None:
        node = Node(val, self.tail.prev, self.tail)
        self.tail.prev.next = node
        self.tail.prev = node
        self.size += 1
    
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        self.size -= 1
        return True
      
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        self.size -= 1
        return True
    
    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.next.val

    def getLast(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.prev.val
    
    def isEmpty(self) -> bool:
        return self.size == 0
    
    def getSize(self) -> int:

        return self.size