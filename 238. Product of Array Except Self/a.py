# https://leetcode.com/problems/product-of-array-except-self/description/

'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

'''
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre = [1] * len(nums)
        for i in range(len(nums)):
            p = pre[i-1] if i > 0 else 1
            pre[i] = p * nums[i]
            
        sur = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            s = sur[i+1] if i < len(nums) - 1 else 1
            sur[i] = s * nums[i]
        
        res = []
        for i in range(len(nums)):
            p = pre[i-1] if i > 0 else 1
            s = sur[i+1] if i < len(nums) - 1 else 1
            res.append(p * s)
        
        return res

if __name__ == "__main__":
    nums = list(map(int, input().strip()[1:-1].split(',')))
    
    so = Solution()
    res = so.productExceptSelf(nums)

    print(res)