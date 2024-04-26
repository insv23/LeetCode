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
        hm = {}
        for i, n in enumerate(numbers):
            hm[n] = i # 重复项直接覆盖
        
        for i, n in enumerate(numbers):
            diff = target - n
            if diff in hm:
                return [i+1, hm[diff]+1]

if __name__ == "__main__":
    nums = list(map(int, input().strip()[1:-1].split(',')))
    target = int(input().strip())
    
    so = Solution()
    res = so.twoSum(nums, target)

    print(res)

'''
时间复杂度
1. 构建哈希表：第一个 for 循环遍历数组 numbers，每个元素都被插入哈希表 hm 中。哈希表的插入操作平均时间复杂度是 O(1)，因此这个循环的时间复杂度是 O(n)，其中 n 是数组 numbers 的长度。
2. 查找元素：第二个 for 循环再次遍历数组 numbers，对于每个元素 n，计算 target - n，然后检查这个差值是否存在于哈希表中。哈希表的查找操作平均时间复杂度也是 O(1)，因此这个循环的时间复杂度同样是 O(n)。
综合上述，整个函数的时间复杂度为 O(n)。

空间复杂度
哈希表：哈希表 hm 存储了数组中每个元素及其索引，最坏情况下（没有重复元素时），哈希表中的元素数量与数组 numbers 的长度相同，因此空间复杂度为 O(n)。
'''