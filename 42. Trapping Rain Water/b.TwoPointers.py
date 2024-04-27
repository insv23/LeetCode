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
        maxLh, maxRh = 0, 0
        res = 0
        l, r = 0, len(height) - 1
        while l <= r:
            # 核心是: 较矮的那个 maxHeight 需要向中间靠拢，以期望变得更高
            if maxLh <= maxRh:
                res += max(maxLh - height[l], 0) # 本来应该是 max(min(maxLh, maxRh) - height[l], 0), 但 maxLh <= maxRh
                maxLh = max(maxLh, height[l])
                l += 1
            else:
                res += max(maxRh - height[r], 0)
                maxRh = max(maxRh, height[r])
                r -= 1
        
        return res



if __name__ == "__main__":
    height = list(map(int, input().strip()[1:-1].split(',')))
    print(Solution().trap(height))