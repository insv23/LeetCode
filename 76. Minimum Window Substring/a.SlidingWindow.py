# https://leetcode.com/problems/minimum-window-substring/description/

'''
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
'''

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ''
        
        hm_t, hm_w = {}, {}
        
        # 初始化 hm_t
        for char in t:
            hm_t[char] = hm_t.get(char, 0) + 1
        
        need, have = len(hm_t), 0 # need 表示需要满足的条件数量, have 表示子串已满足条件的数量。所谓条件就是`某字符的数量完全相等或子串中多一些`
        res, resLen = [-1, -1], float('infinity')        
        l = 0
        for r, char in enumerate(s):
            # 首先把 char 添加到 hm_w (window) 中
            hm_w[char] = hm_w.get(char, 0) + 1
            
            # 检查新添加字符是否在 t 中
            if char in hm_t and hm_t[char] == hm_w[char]:
                have += 1
            
            # 当 have == need 时, 当前 l 与 r 形成的子串包含 t, 但开头可能有多余字符
            while have == need:
                # 首先尝试更新结果
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                # 尝试删除 l 以减少结果长度(该处可能是多余的字符)
                # 如果 l 处字符是 t 中的一个字符, 可能会对 have 值产生影响(为什么是可能? 因为有可能 l 处字符在 hm_w 中出现 3 次, 而 hm_t 只要 2, 删除一个也不会影响结果)
                if s[l] in hm_t and hm_t[s[l]] == hm_w[s[l]]:
                    have -= 1
                hm_w[s[l]] -= 1
                l += 1
            
        l, r = res
        if resLen < float('infinity'):
            return s[l: r+1]
        else:
            return ''

if __name__ == "__main__":
    s = input().strip()[1:-1]
    t = input().strip()[1:-1]

    print(Solution().minWindow(s, t))