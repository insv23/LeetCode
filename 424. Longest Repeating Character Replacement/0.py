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

if __name__ == "__main__":
    s = input().strip()[1:-1]
    k = int(input())
    
    print(Solution().characterReplacement(s, k))