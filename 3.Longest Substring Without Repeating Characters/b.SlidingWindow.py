class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        char_index_map = {}
        left = 0
        
        for right in range(len(s)):
            if s[right] in char_index_map:
            # 当遇见重复字符，需要更新 left
                # left 只能往右，例如 `abbbba`
                left = max(left, char_index_map[s[right]] + 1)
            # 更新字符(无论是不是遇到过)索引
            char_index_map[s[right]] = right
            # 更新最大长度
            max_len = max(max_len, right - left + 1)
            
        return max_len
        

if __name__ == "__main__":
    s = input().strip()[1: -1]

    so = Solution()
    res = so.lengthOfLongestSubstring(s)

    print(res)
    