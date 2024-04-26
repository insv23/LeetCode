# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
'''

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                return [l+1, r+1]

if __name__ == "__main__":
    nums = list(map(int, input().strip()[1:-1].split(',')))
    target = int(input().strip())
    
    so = Solution()
    res = so.twoSum(nums, target)

    print(res)

'''
时间复杂度
这个算法使用了双指针技术。指针 l 从数组的开始向前移动，指针 r 从数组的末尾向后移动。在最坏的情况下，这两个指针会遍历整个数组一次，因此时间复杂度为 O(n)，其中 n 是数组 numbers 的长度。

 空间复杂度
算法只使用了几个额外的变量（如 l, r），并没有使用与输入大小成比例的额外空间。因此，空间复杂度为 O(1)，即常数空间复杂度。
'''