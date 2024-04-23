'''
Design a Singly Linked List class.
'''
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = ListNode(-1) # dummy node
        self.tail = self.head
    
    def get(self, index: int) -> int:
        if index < 0:
            return -1
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val, self.head.next)
        self.head.next = new_node
        if self.head == self.tail:
            # 如果插入前链表为空
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        if index < 0:
            return False
        i = 0
        curr = self.head
        while curr and i < index:
            i += 1
            curr = curr.next
        
        # 上面的循环结束有两种可能，遍历到一个空节点或到了目标节点的前一个
        # 如果当前节点是空或当前节点的下一个是空，都是 index 超出范围
        if curr and curr.next:
            # 目标节点存在
            if curr.next == self.tail:
                # 如果目标节点是 tail 节点
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        vals = []
        curr = self.head.next
        while curr:
            vals.append(curr.val)
            curr = curr.next
        return vals
