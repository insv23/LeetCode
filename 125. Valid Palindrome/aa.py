# https://leetcode.com/problems/valid-palindrome/description/

'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        ss = re.sub(r'[^a-z0-9]', '', s.lower())
        return ss == ss[::-1]

        
if __name__ == "__main__":
    s = input().strip('"')
    
    so = Solution()
    res = so.isPalindrome(s)

    print(res)
    
'''
时间复杂度
1. 字符串预处理：
s.lower()：将字符串转换为小写，时间复杂度为 O(n)，其中 n 是字符串 s 的长度。
re.sub(r'[^a-z0-9]', '', s.lower())：使用正则表达式移除所有非字母数字字符，这个操作的时间复杂度也是 O(n)。正则表达式的匹配和替换需要遍历整个字符串。
2. 回文检查：
ss == ss[::-1]：这一步检查字符串 ss 是否等于其反转字符串 ss[::-1]。生成反转字符串的时间复杂度为 O(n)，比较两个字符串的时间复杂度也为 O(n)。
综合上述，整个函数的时间复杂度为 O(n)。

空间复杂度
1. 字符串预处理：
s.lower() 和 re.sub()：这两个操作都生成了新的字符串，因此需要额外的空间来存储这些字符串。尤其是 re.sub()，它生成的新字符串 ss 的长度最多为 n。
2. 回文检查：
ss[::-1]：这一步生成了 ss 的一个完整反转副本，因此需要额外的 O(n) 空间。
因此，整个函数的空间复杂度为 O(n)，主要是由于存储原始字符串的小写版本、非字母数字字符被移除的版本以及其反转副本。
'''