class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # 负数 & 10 的倍数(除了 0)直接返回 false
        if x < 0 or (x % 10 == 0 and x != 0):
          return False
        
        # 每次取 x 的最后一位数加到一个新的变量 rn 中
        # 直到 rn 等于(偶数位数字)或大于(奇数位数字) x
        rn = 0
        while rn < x:
          rn = rn * 10 + x % 10
          x //= 10
        
        # 偶数位数字直接比较
        # 奇数位数字，去掉 rn 的最后一个
        return x == rn or x == rn // 10

if __name__ == "__main__":
    num = int(input().strip())

    so = Solution()
    res = so.isPalindrome(num)
    
    print(res)