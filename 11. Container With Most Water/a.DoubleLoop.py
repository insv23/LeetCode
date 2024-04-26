# https://leetcode.com/problems/container-with-most-water/description/

'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        m = 0
        for l in range(len(height) - 1):
            for r in range(l+1, len(height), 1) :
                s = min(height[l], height[r]) * (r - l)
                m = max(m, s)
        return m
        
if __name__ == "__main__":
    height = list(map(int, input().strip()[1:-1].split(',')))
    
    so = Solution()
    res = so.maxArea(height)

    print(res)