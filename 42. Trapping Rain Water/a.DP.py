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
        maxLs = [0] * len(height)
        maxRs = [0] * len(height)

        for i in range(1, len(height)):
            maxLs[i] = max(maxLs[i-1], height[i-1])
        
        for i in range(len(height)-2, -1, -1):
            maxRs[i] = max(maxRs[i+1], height[i+1])
            
        res = 0
        for i in range(len(height)):
            res += max(min(maxLs[i], maxRs[i]) - height[i], 0)
        
        return res

if __name__ == "__main__":
    height = list(map(int, input().strip()[1:-1].split(',')))
    print(Solution().trap(height))

'''
它使用了动态编程的方法来解决问题，具体来说，通过三次遍历数组来完成计算。
核心思想是: 
1. 一个竖块(即底为1的矩形)是靠它左右两边的竖块来存住水的，“左右两边”不一定是指相邻的两个，即使离得很远但高度比当前竖块高，也能形成”墙“来让当前块存住水
2. 当前块能存住水的多少是靠它两边竖块的最小值决定的，如果最小值小于或等于当前块的高度，则存不住水

算法步骤
1. 计算每个块左侧的最大值
2. 计算每个块右侧的最大值
3. 每个块能存的水量为”左右两侧最大值中的较小值“ - 当前块的高度，如果小于等于 0 则表示存不住水，遍历所有块并求和得到结果

时间复杂度
1. 第一次遍历 O(n)
2. 第二次遍历 O(n)
3. 第三次遍历 O(n)
总的时间复杂度 O(n)

空间复杂度
maxLs 和 maxRs 数组使用了 O(n) 的空间
总的空间复杂度为 O(n)
'''

