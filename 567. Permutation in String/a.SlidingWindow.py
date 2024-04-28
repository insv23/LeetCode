# https://leetcode.com/problems/permutation-in-string/description/

'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
''' 

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        
        count1, count2 = [0] * 26, [0] * 26
        # 统计 s1 的字符数(顺便把 s2 的前 s1 个也统计了)
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
        
        # 初始化 matches (表示 count1 与 count2 中相同字母出现相同数量的次数, 当 == 26 时表示'子串完美匹配')
        matches = 0
        for i in range(26):
            if count1[i] == count2[i]:
                matches += 1
        
        if matches == 26:
            return True
        
        l = 0
        for r in range(len(s1), len(s2)):
            
            rLetterIndex = ord(s2[r]) - ord('a')
            # 判断新引入的字符对 matches 的影响              
            if count1[rLetterIndex] == count2[rLetterIndex]:
                # Case1: 原来该字符是相等的, count2 新引入一个, 导致 matches -1
                matches -= 1
            elif count1[rLetterIndex] == count2[rLetterIndex] + 1:
                # Case2: 原来该字符在 count2 中恰好比在 count1 中少一个, 这个新引入的字符正好让二者相等, matches + 1
                matches += 1
            # Case3: 其他本来就不相等情况, 改字符多一个依旧不相等, 不会影响 matches
            count2[rLetterIndex] += 1
            
            lLetterIndex = ord(s2[l]) - ord('a')
            # 判断抛弃的一个字符对 matches 的影响
            if count1[lLetterIndex] == count2[lLetterIndex]:
                matches -= 1
            elif count1[lLetterIndex] == count2[lLetterIndex] - 1:
                matches += 1
            count2[lLetterIndex] -= 1
            l += 1

            if matches == 26:
                return True
        return False

if __name__ == "__main__":
    s1 = input().strip()[1:-1]
    s2 = input().strip()[1:-1]

    print(Solution().checkInclusion(s1, s2))