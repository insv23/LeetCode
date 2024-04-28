# https://leetcode.com/problems/longest-repeating-character-replacement/description/

'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
'''

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        maxLen = 0
        maxFreq = 0
        count = [0] * 26
        l = 0
        for r in range(len(s)):
            count[ord(s[r]) - ord('A')] += 1
            maxFreq = max(maxFreq, count[ord(s[r]) - ord('A')])
            
            if r - l + 1 - maxFreq <= k:
                maxLen = max(maxLen, r - l +  1)
            else:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1

        
        return maxLen 

if __name__ == "__main__":
    s = input().strip()[1:-1]
    k = int(input())
    
    print(Solution().characterReplacement(s, k))

'''
被 NeetCode 的思路干扰了
只有在当前子串是"有效子串"(即 子串长度 - 最大频率 <= k)时, 才会进行 maxLen 的计算
如果当前子串是非有效的, 就放弃当前子串第 0 位字符
'''

