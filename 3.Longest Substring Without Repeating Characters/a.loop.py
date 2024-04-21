class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        for i in range(len(s)):
            substring_len = 1     
            uniq = {s[i]}
            for j in range(i+1, len(s)):
                if s[j] in uniq:
                    break
                uniq.add(s[j])
                substring_len += 1
            max_len = substring_len if substring_len > max_len else max_len
        return max_len
        

if __name__ == "__main__":
    s = input().strip()[1: -1]
    
    so = Solution()
    res = so.lengthOfLongestSubstring(s)

    print(res)
