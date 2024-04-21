# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sentinel = ListNode(0)
        cur = sentinel
        carry = 0

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = x + y + carry

            carry = sum // 10
            cur.next = ListNode(sum % 10)
            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # 处理最后一位(可能有进位)
        if carry > 0:
            cur.next = ListNode(carry)
        
        return sentinel.next

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