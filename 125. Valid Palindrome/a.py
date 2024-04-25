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

        l, r = 0, len(ss) - 1
        while l < r:
            if ss[l] != ss[r]:
                return False
            l += 1
            r -= 1
        
        return True

        
if __name__ == "__main__":
    s = input().strip('"')
    
    so = Solution()
    res = so.isPalindrome(s)

    print(res)
    
'''
时间复杂度
1. 字符串预处理：使用 re.sub(r'[^a-z0-9]', '', s.lower()) 来转换字符串。这里有两个主要操作：s.lower() 和 re.sub()。
s.lower() 的时间复杂度为 O(n)，其中 n 是字符串 s 的长度，因为它需要遍历字符串 s 并转换每个字符。
re.sub() 的时间复杂度也是 O(n)，因为它需要遍历字符串 s 并检查每个字符是否符合给定的正则表达式。
2. 回文检查：使用双指针从两端向中心逐个比较字符，最坏情况下需要比较 n/2 对字符，因此时间复杂度为 O(n)。
综合上述，整个函数的时间复杂度为 O(n)。

空间复杂度
1. 字符串预处理：re.sub() 生成一个新的字符串 ss，这个字符串的长度最多为 n。因此，空间复杂度为 O(n)。
2. 双指针：使用了两个额外的变量 l 和 r 来存储索引，这部分的空间消耗是常数级别的，即 O(1)。
因此，整个函数的空间复杂度主要由新字符串 ss 决定，为 O(n)。
'''