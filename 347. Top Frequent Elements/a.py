from collections import defaultdict

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hm = defaultdict(int)
        for n in nums:
            hm[n] += 1
        return [key for key, value in sorted(hm.items(), key=lambda item: item[1], reverse=True)[:k]]
        '''
        1. hm.items() 返回一个字典的视图对象，包含字典的键值对 (key, value)。
          {'a': 5, 'b': 1, 'c': 3, 'd': 4}.items() 返回 [('a', 5), ('b', 1), ('c', 3), ('d', 4)]
        2. sorted(..., key=lambda item: item[1], reverse=True):
          sorted() 函数用于对可迭代对象进行排序。
          key=lambda item: item[1] 指定排序的依据(key)是 dict 的 value(即每个元组中的第二个值)
            lambda item: item[1] 是一个匿名函数, 它接受一个元组 item 并返回该元组的第二个元素
          reverse=True 表示逆序(降序)排列
        3. [:k] 表示取出前 k 个元素
        4. [key for key, value in ...] 是一个列表推导式, 用于从每个 (key, value) 中提取 key
        '''

if __name__ == "__main__":
    nums = list(map(int, input().strip()[1:-1].split(',')))
    k = int(input().strip())
    
    so = Solution()
    res = so.topKFrequent(nums, k)
    
    print(res)

'''
时间复杂度
1. 构建哈希表 O(n)
2. 排序, O(m log m), m 为哈希表键的数量，最坏情况下为 O(n log n)
3. 提取前 k 个元素, O(k)
综上, 时间复杂度 O( n log n)

空间复杂度
1. 哈希表, 最坏情况下 O(n)
2. sorted() 返回一个新的列表, 包含哈希表的所有项, 最坏情况下 O(n)
综上, 空间复杂度 O(n)
'''