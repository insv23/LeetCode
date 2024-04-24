class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hm = {}
        # freq = [[]] * (len(nums) + 1) # 有可能整个数组都是同一个数字
        # 在 Python 中，列表是可变的，所以当您使用 * 操作符来复制列表时，您实际上只是复制了对同一个列表的引用，而不是创建多个独立的列表。
        freq = [[] for _ in range(len(nums) + 1)]
        
        for n in nums:
            hm[n] = hm.get(n, 0) + 1    
        
        for n, v in hm.items():
            freq[v].append(n)
        
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
              res.append(n)
              if len(res) == k:
                  return res

if __name__ == "__main__":
    nums = list(map(int, input().strip()[1:-1].split(',')))
    k = int(input().strip())
    
    so = Solution()
    res = so.topKFrequent(nums, k)
    
    print(res)
    
'''
时间复杂度
1. 构建哈希表 O(n)
2. 构建频率列表 O(n)
3. 提取前 k 个元素, 最坏情况下, 完整遍历 O(n)
综上, 总时间复杂度为 O(n)

空间复杂度
1. 哈希表 O(n)
2. 频率列表, 最坏 O(n)
3. 结果列表 O(k)
综上, 总空间复杂度为 O(n)
'''