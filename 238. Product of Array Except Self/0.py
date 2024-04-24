# https://leetcode.com/problems/product-of-array-except-self/description/

'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

1. 使用一个前缀数组和一个后缀数组，分别存当前数字前/后若干位的乘积，最后将两个乘积乘起来得到结果
2. 只用一个数组完成 1. 中的操作, 将空间复杂度拉到 O(1)(输出的数组不计算在内)

'''
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        

if __name__ == "__main__":
    nums = list(map(int, input().strip()[1:-1].split(',')))
    
    so = Solution()
    res = so.productExceptSelf(nums)

    print(res)