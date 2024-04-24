# https://leetcode.com/problems/valid-anagram/description/


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        count = [0]*26
        # for i in range(len(s)):
        #     # ord('a') = 97
        #     count[ord(s[i])-97] += 1
        #     count[ord(t[i])-97] -= 1
        # for n in count:
        #     if n != 0:
        #         return False
        # return True
        for char in s:
            count[ord(char) - 97] += 1
        for char in t:
            count[ord(char) - 97] -= 1
            # 提前终止
            if count[ord(char) - 97] < 0:
                return False
        # 不用再判断有无剩余字符数量大于 0, 因为 s 与 t 字符数相等, 没有小于 0 的字符, 则说明没有大于 0 的字符
        return True

if __name__ == "__main__":
    s1 = input().strip()[1:-1]
    s2 = input().strip()[1:-1]

    so = Solution()
    res = so.isAnagram(s1, s2)
    
    print(res)