# https://leetcode.com/problems/valid-anagram/description/

# 其他解法
# 1. 排序比较 sorted(s) == sorted(t)
# 2. 使用 Counter(collections), Counter(s) == Counter(t)
# 3. 使用数组做计数器 ord('A') = 65


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        letters = {}
        # for i in range(len(s)):
        #     if s[i] in letters:
        #         letters[s[i]] += 1
        #     else:
        #         letters[s[i]] = 1
            
        #     if t[i] in letters:
        #         letters[t[i]] -= 1
        #     else:
        #         letters[t[i]] = -1

        # for value in letters.values():
        #     if value != 0:
        #         return False
        # return True
        for char_s, char_t in zip(s, t):
            letters[char_s] = letters.get(char_s, 0) + 1
            letters[char_t] = letters.get(char_t, 0) - 1
        
        return all(value == 0 for value in letters.values())

if __name__ == "__main__":
    s1 = input().strip()[1:-1]
    s2 = input().strip()[1:-1]

    so = Solution()
    res = so.isAnagram(s1, s2)
    
    print(res)