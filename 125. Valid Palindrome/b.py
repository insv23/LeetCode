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
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.isAN(s[l]):
                l += 1
            while r > l and not self.isAN(s[r]):
                r -= 1
                
            if s[l].lower() != s[r].lower():
                return False
            
            l, r = l + 1, r - 1
        
        return True
        
    def isAN(self, char):
        return (ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9'))
        
if __name__ == "__main__":
    s = input().strip('"')
    
    so = Solution()
    res = so.isPalindrome(s)

    print(res)

'''
时间复杂度
1. 双指针遍历：外层 while 循环的最坏情况下会遍历整个字符串一次，即 O(n)，其中 n 是字符串 s 的长度。
2. 字符验证：内层的两个 while 循环用于跳过非字母数字字符。虽然这看起来是嵌套循环，但每个字符最多被访问两次（一次可能在左指针的循环中，一次可能在右指针的循环中），因此这部分的时间复杂度仍然是 O(n)。
3. 字符比较：在两个指针指向有效字符后，进行比较，这个操作的时间复杂度是 O(1)，但由于它包含在主循环中，对总时间复杂度的贡献也是 O(n)。
综合上述，整个函数的时间复杂度为 O(n)。

空间复杂度
1. 额外空间：这个算法主要使用了几个辅助变量（l, r），以及在 isAN 函数中用于字符验证的常数空间。这些都是常数级别的空间使用，即 O(1)。
2. 原地操作：没有使用额外的数据结构来存储字符串或其部分，所有操作都是在原字符串上进行的。
因此，整个函数的空间复杂度为 O(1)。
'''