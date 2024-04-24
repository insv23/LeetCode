# https://leetcode.com/problems/longest-consecutive-sequence/description/

'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
'''

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        uniq = set(nums)

        longest = 0
        for n in uniq:
            # 一个数的左侧如果没有数, 它才有可能是一串数的起点
            if n-1 not in uniq:
                length = 1
                while n+length in uniq:
                    length += 1
                longest = max(longest, length)
        
        return longest

if __name__ == "__main__":
    nums = list(map(int, input().strip()[1:-1].split(',')))
    
    so = Solution()
    res = so.longestConsecutive(nums)
    
    print(res)

'''
时间复杂度
1. 将 nums 转换为集合 uniq：这一步的时间复杂度为 O(n)，其中 n 是数组 nums 的长度。这是因为每个元素都需要被处理一次以加入到集合中。
2. 遍历集合 uniq 并计算最长连续序列：虽然外层循环遍历集合的时间复杂度为 O(n)，但内层的 while 循环检查连续元素是否存在于集合中，这个检查操作是 O(1) 的时间复杂度。关键在于，每个数字在整个算法中只会被访问两次：一次是在外层循环中，另一次是在内层循环中（如果它是某个连续序列的一部分）。因此，尽管看起来有嵌套循环，整体的时间复杂度仍然是 O(n)。

空间复杂度
1. 集合 uniq：这个集合存储了 nums 中所有不重复的元素，因此其空间复杂度为 O(n)，其中 n 是数组 nums 中不同元素的数量。
综上所述，这段代码的时间复杂度是 O(n)，空间复杂度也是 O(n)。
'''