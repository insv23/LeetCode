# 使用字符计数作为 key
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hm = {}
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            key = tuple(count) # eat: (1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
            if key not in hm:
                hm[key] = []
            hm[key].append(s)
            
        return list(hm.values())
        
if __name__ == "__main__":
    t = input().strip()[1:-1].split(',')
    strs = list(word[1:-1] for word in t)
    
    so = Solution()
    res = so.groupAnagrams(strs)
    
    print(res)

'''
时间复杂度
1. 遍历字符串: 设字符串数组的长度为 m, 即有 m 个字符串
2. 计算每个字符串的字符计数：设字符串的平均长度为 n, 则每次计数时间复杂度为 O(n)
3. 构造 key 和更新字典：将数组(list)转为元组作为 hashmap 的 key, 这个操作的时间复杂度为 O(1), 因为我们转换的是固定大小的数组（26个英文字母的计数）。字典的更新(插入和访问)可以认为是 O(1)的
综上，总时间复杂度为 O(mn), m 为字符串数量, n 为字符串的平均长度

空间复杂度
1. 哈希表: 最坏的情况下, 每个字符串都为单独的一项，字典大小来到 m. 每个键值对中，键为一个长度为 26 的元组, 值是一个字符串列表, 即 (26 + n), 所以空间复杂度为 O(mn)
2. 字符串计数数组 count：每个字符串都被重用，空间为 O(1)
综上，总空间复杂度为 O(mn)
'''