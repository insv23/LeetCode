class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
          return ""
        
        # 初始化最短字符串为最长公共前缀
        shortest_str = min(strs, key=len)

        # 遍历最短字符串的每个字符
        for i, char in enumerate(shortest_str):
          for word in strs:
            if word[i] != char:
              # 一旦有不匹配, 返回当前已匹配的字符(到第 i-1 个)
              return shortest_str[:i]
        
        # 所有的字符都匹配了最短字符串
        return shortest_str

if __name__ == "__main__":
    trimmed_str = input().strip()[1:-1]
    words_list = [word.strip('"') for word in trimmed_str.split(',')]
    
    so = Solution()
    res = so.longestCommonPrefix(words_list)

    print(res)