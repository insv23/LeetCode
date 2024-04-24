# https://leetcode.com/problems/group-anagrams/description/

'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

# 使用排序后的字符串作为 key
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hm = {}
        for s in strs:
            key = self.rearrange(s)
            if key not in hm:
                hm[key] = []
            hm[key].append(s)
        
        return [value for value in hm.values()]
    
    def rearrange(self, word):
        l = sorted(word) # ['a', 'e', 't']
        return ''.join(l) # aet
        
        
if __name__ == "__main__":
    t = input().strip()[1:-1].split(',')
    strs = list(word[1:-1] for word in t)
    
    so = Solution()
    res = so.groupAnagrams(strs)
    
    print(res)

'''
时间复杂度
1. 排序操作：对于每个字符串，您使用了 sorted() 函数，这个操作的时间复杂度是 O(n log n)，其中 n 是字符串的长度。
2. 遍历所有字符串：您遍历了列表 strs 中的每个字符串，这个操作的时间复杂度是 O(m)，其中 m 是列表中字符串的数量。
因此，整体时间复杂度是 O(m n log n)，其中 m 是字符串的数量，n 是平均字符串长度。
空间复杂度
1. 哈希表：您使用了一个字典来存储分组的结果，这个字典的大小最多可以达到 m（在极端情况下，每个字符串都不是其他字符串的字谜）。
2. 排序存储：对每个字符串进行排序并存储排序后的结果，这需要额外的空间。
总的空间复杂度是 O(m n)，其中 m 是字符串的数量，n 是平均字符串长度。
潜在的改进点
1. 使用哈希函数：当前使用排序作为键值可能不是最高效的方法，因为排序操作较为耗时。可以考虑使用更高效的哈希函数，例如计算每个字符出现次数的哈希值，这样可以将时间复杂度降低到 O(m n)。
2. 内存优化：如果字符串非常长，排序后的字符串会占用额外的内存。可以考虑只存储字符计数的哈希表作为键，而不是排序后的字符串。
'''