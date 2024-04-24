# https://leetcode.com/problems/contains-duplicate/

# 尝试了三种方式：
# 1. 使用集合
# 2. 使用字典(hashmap)  (时间和空间上比第一种都要好)
# 3. 先使用自带的 nums.sort() 排序，然后检查相邻项是否相等 (最省空间, 但最慢)
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        uniq = set()
        for num in nums:
            if num in uniq:
                return True
            uniq.add(num)
        return False
        
if __name__ == "__main__":
    nums = list(map(int, input().strip()[1:-1].split(',')))
    
    so = Solution()
    res = so.containsDuplicate(nums)
    
    print(res)