# https://leetcode.com/problems/sliding-window-maximum/description/

'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

'''

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque
        deq = deque() # 不直接存储 num, 而是存储其索引, 最大元素为第 0 个, 依次递减
        maxima = []
        
        for i, n in enumerate(nums):
            # 清空所有比当前元素小的元素的索引
            while deq and nums[deq[-1]] <= n:
                deq.pop()
            
            # 将当前元素的索引加入队列
            deq.append(i)
            
            # 窗口向右移动一位, 原来最左的那个(索引为 i - k)会被丢掉
            # 如果当前最大值就是原来最左的那个元素, 需要被逐出队列
            if deq[0] == i - k:
                deq.popleft()
            
            # 将当前窗口的最大值加入 maxima, 但需要从 k-1 个元素开始(因为之前形成的窗口还不够长度 k)
            if i >= k - 1:
                maxima.append(nums[deq[0]])
        
        return maxima        

if __name__ == "__main__":
    nums = list(map(int, input().strip()[1:-1].split(',')))
    k = int(input().strip())
    
    print(Solution().maxSlidingWindow(nums, k))