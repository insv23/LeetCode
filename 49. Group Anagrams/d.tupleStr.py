# 看了 NeetCode 的讲解视频发现居然是可以用 defaultdict 的(似乎还不用额外 import?)

from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hm = defaultdict(list) # 直接将其初始化为value 为 list
        for s in strs:
            key = tuple(sorted(s))
            hm[key].append(s)
        
        return list(hm.values())

        
        
if __name__ == "__main__":
    t = input().strip()[1:-1].split(',')
    strs = list(word[1:-1] for word in t)
    
    so = Solution()
    res = so.groupAnagrams(strs)
    
    print(res)