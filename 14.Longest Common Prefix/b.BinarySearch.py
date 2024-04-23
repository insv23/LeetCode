class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
          return ""
        
        # 找到最短字符串的长度
        min_length = min(len(s) for s in strs)

        l, r = 1, min_length
        
        while l <= r:
            mid = (l + r) // 2
            if self.isCommonPrefix(strs, mid):
                l = mid + 1
            else:
                r = mid - 1
        
        return strs[0][:((l + r) // 2)]
        
    
    def isCommonPrefix(self, strs, length):
      """
      检查长度为length的前缀是否是所有字符串的公共前缀
      """
      # 取第一个字符串的前length个字符作为公共前缀的候选
      prefix = strs[0][:length]
      for s in strs:
        if not s.startswith(prefix):
          return False
      return True

        

if __name__ == "__main__":
    trimmed_str = input().strip()[1:-1]
    words_list = [word.strip('"') for word in trimmed_str.split(',')]
    
    so = Solution()
    res = so.longestCommonPrefix(words_list)

    print(res)