# https://leetcode.com/problems/add-two-numbers/description/

'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''
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