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
        max_area = 0
        l, r = 0, len(height)-1
        while l < r:
            current_area = min(height[l], height[r]) * (r - l)
            max_area = max(max_area, current_area)

            # 尝试将较短的板子换成其他的板子以增加围起来区域面积
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return max_area
        
if __name__ == "__main__":
    height = list(map(int, input().strip()[1:-1].split(',')))
    
    so = Solution()
    res = so.maxArea(height)

    print(res)