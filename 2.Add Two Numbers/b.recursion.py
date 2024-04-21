# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return add(l1, l2, 0)

def add(ln1, ln2, carry):
    # 终止条件: 两个节点都为空且进位为 0
    if not ln1 and not ln2 and carry == 0:
        return None
    
    # 计算当前值之和并更新进位
    x = ln1.val if ln1 else 0
    y = ln2.val if ln2 else 0
    sum = x + y + carry
    newCarry = sum // 10

    # 创建新节点
    newNode = ListNode(sum % 10)

    # 递归处理下一个节点
    next1 = ln1.next if ln1 else None
    next2 = ln2.next if ln2 else None
    newNode.next = add(next1, next2, newCarry)

    return newNode


class ListNode(object):
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next

def list_to_linkedlist(nums):
    """
    :type nums: list
    :rtype: ListNode
    """
    # 创建一个哨兵节点，它将在最后返回链表的头节点（哨兵节点的下一个节点）
    sentinel = ListNode(0)
    cur = sentinel
    for num in nums:
        cur.next = ListNode(num)
        cur = cur.next
    return sentinel.next # 返回哨兵节点的下一节点(即链表的头节点)

def linkedlist_to_list(head):
    """
    :type head: ListNode
    :rtype: list
    """
    res = []
    cur = head
    while cur:
        res.append(cur.val)
        cur = cur.next
    
    return res

if __name__ == "__main__":
    nums1 = list(map(int, input().strip()[1: -1].split(',')))
    nums2 = list(map(int, input().strip()[1: -1].split(',')))

    l1 = list_to_linkedlist(nums1)
    l2 = list_to_linkedlist(nums2)

    so = Solution()
    linked_list = so.addTwoNumbers(l1, l2)

    res = linkedlist_to_list(linked_list)
    print(res)