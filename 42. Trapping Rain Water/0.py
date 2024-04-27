# https://leetcode.com/problems/trapping-rain-water/description/

'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        

if __name__ == "__main__":
    height = list(map(int, input().strip()[1:-1].split(',')))
    print(Solution().trap(height))