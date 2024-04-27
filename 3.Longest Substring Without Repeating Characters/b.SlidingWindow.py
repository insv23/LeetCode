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
                # left 只能往右，例如 `abbbba`, `tmmzuxt`
                left = max(left, char_index_map[s[right]] + 1) # 这个左侧的更新条件非常微妙, 'r 所在字符出现过' 有两种可能: 1. 在当前'最长子串'中出现, 则更新 l 到下一个位置 2. 未在当前'最长子串'中出现(即在 l 的左侧出现, 例如 `tmmzuxt` 中的 `t`), 则 l 应保持不变
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
    