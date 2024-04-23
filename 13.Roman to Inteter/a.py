class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ri = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        res = 0
        i = 0
        while i < len(s):
          # 如果当前字符代表的值小于其右边字符代表的值，说明这是一个特殊的罗马数字（如 IX, IV, XL, XC, CD, CM
          if i + 1 < len(s) and ri[s[i]] < ri[s[i+1]]:
              res += ri[s[i+1]] - ri[s[i]]
              i += 2
          else:
            res += ri[s[i]]
            i += 1
        return res
          


if __name__ == "__main__":
    s = input().strip()[1:-1]
    
    so = Solution()
    res = so.romanToInt(s)

    print(res)