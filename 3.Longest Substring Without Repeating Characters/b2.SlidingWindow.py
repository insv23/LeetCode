# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

'''
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hm = {}
        max_len = 0
        l = 0
        for r, char in enumerate(s):
            # 如果当前字符已经在 hm 中, 则 l 跳到该处后一位(但要保证不后退, 例如 abbbbba )
            if char in hm:
                l = max(l, hm[char]+1)
            
            # 将当前字符添加/更新进 hashmap
            hm[char] = r
            
            max_len = max(max_len, r - l + 1)
        
        return max_len

if __name__ == "__main__":
    s = input().strip()[1: -1]
    
    so = Solution()
    res = so.lengthOfLongestSubstring(s)

    print(res)
