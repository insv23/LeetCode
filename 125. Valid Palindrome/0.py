# https://leetcode.com/problems/valid-palindrome/description/

'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

核心考察点居然是自己判断某个字符是不是 alphanumeric, 我上来就直接正则把 non-alphanumberic 秒了
'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        
if __name__ == "__main__":
    s = input().strip('"')
    
    so = Solution()
    res = so.isPalindrome(s)

    print(res)