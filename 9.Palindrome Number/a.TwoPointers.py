class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # 负数直接返回 false
        if x < 0:
          return False
        
        s = str(x)
        
        l, r = 0, len(s)-1
        while l < r:
          if s[l] != s[r]:
            return False
          l += 1
          r -= 1
        return True
        

if __name__ == "__main__":
    num = int(input().strip())

    so = Solution()
    res = so.isPalindrome(num)
    
    print(res)