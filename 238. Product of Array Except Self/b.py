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
        arr = [1] * len(nums)
        
        p = 1
        for i in range(len(nums)):
            arr[i] = p
            p *= nums[i]
        
        p = 1
        for i in range(len(nums)-1, -1, -1):
            arr[i] *= p
            p *= nums[i]
        
        return arr
        
if __name__ == "__main__":
    nums = list(map(int, input().strip()[1:-1].split(',')))
    
    so = Solution()
    res = so.productExceptSelf(nums)

    print(res)