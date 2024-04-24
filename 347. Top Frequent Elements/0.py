# https://leetcode.com/problems/top-k-frequent-elements/description/

'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

a. 使用 hashmap 记录, 然后对 hashmap 的 value 进行排序
b. 使用 bucket sort(by NeetCode)
c. 使用 heap
'''
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        

if __name__ == "__main__":
    nums = list(map(int, input().strip()[1:-1].split(',')))
    k = int(input().strip())
    
    so = Solution()
    res = so.topKFrequent(nums, k)
    
    print(res)