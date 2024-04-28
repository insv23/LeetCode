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
        

if __name__ == "__main__":
    s1 = input().strip()[1:-1]
    s2 = input().strip()[1:-1]

    print(Solution().checkInclusion(s1, s2))