# https://leetcode.com/problems/3sum/description/

'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        
        res = []
        for i, n1 in enumerate(nums):
            # Stop when n1 is positive
            if n1 > 0:
                break
            
            # Skip duplicate item(n1)
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i+1, len(nums) - 1
            target = 0 - n1
            while l < r:
                two_sum = nums[l] + nums[r]
                if two_sum < target:
                    l += 1
                elif two_sum > target:
                    r -= 1
                else:
                    res.append([n1, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Skip duplicate item(n2 or n3)
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while r > l and nums[r] == nums[r+1]:
                        r -= 1
            
        return res

        
if __name__ == "__main__":
    nums = list(map(int, input().strip()[1:-1].split(',')))
    
    so = Solution()
    res = so.threeSum(nums)
    
    print(res)