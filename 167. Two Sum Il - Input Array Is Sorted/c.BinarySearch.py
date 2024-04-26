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
        for i, n in enumerate(numbers):
            diff = target - n
            l, r = i + 1, len(numbers) - 1
            while l <= r:
                m = (l + r) // 2
                if numbers[m] < diff:
                    l = m + 1
                elif numbers[m] > diff:
                    r = m - 1
                else:
                    return [i+1, m+1]

if __name__ == "__main__":
    nums = list(map(int, input().strip()[1:-1].split(',')))
    target = int(input().strip())
    
    so = Solution()
    res = so.twoSum(nums, target)

    print(res)

'''
时间复杂度
1. 外层循环：外层循环遍历数组中的每个元素，因此其时间复杂度为 O(n)，其中 n 是数组 numbers 的长度。
2. 内层循环（二分查找）：对于每个元素，使用二分查找在剩余的数组部分中查找配对的元素。二分查找的时间复杂度为 O(log n)，因为每次查找操作都将搜索区间减半。
综合这两个部分，整个算法的时间复杂度为 O(n log n)。这是因为对于数组中的每个元素，都可能执行一次二分查找。

空间复杂度
1. 额外空间：这个算法主要使用了几个辅助变量（如 i, n, diff, l, r, m），这些都是常数空间，用于存储索引和计算中间值。
2. 原地操作：算法在原数组上进行操作，没有使用额外的数组或数据结构来存储大量数据。
因此，整个算法的空间复杂度为 O(1)，即常数空间复杂度。
'''