# https://leetcode.com/problems/longest-repeating-character-replacement/description/

'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
'''

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        hm = {}
        maxLen = 0
        l = 0
        for r in range(len(s)):
            hm[s[r]] = hm.get(s[r], 0) + 1
            # currLen = r - l + 1 # 不能用这个变量, 因为 l 可能会变
            
            while r - l + 1 - max(hm.values()) > k:
                hm[s[l]] -= 1
                l += 1
                
            maxLen = max(maxLen, r - l + 1)
            
        return maxLen

if __name__ == "__main__":
    s = input().strip()[1:-1]
    k = int(input())
    
    print(Solution().characterReplacement(s, k))
    
'''
核心是: 
1. 一个子串是由左右指针(l, r)确定的
2. 最终是要找一个尽可能长的子串
3. 当前子串中, 出现次数最多的字符保持不变, 其他字符有 k 次换成该字符的机会;
  即当 一个子串的长度 - 出现次数最多的字符的出现次数 <= k 时, 这个子串是有有效的, 有机会成为最终的答案
  反之, 当 ... > k 时, 子串无效, 我们需要缩小其长度, 通过移动左指针
  
时间复杂度
1. 遍历字符串：代码中有一个外层循环，遍历整个字符串 s，其复杂度为 O(n)，其中 n 是字符串的长度。
2. 更新哈希表: 在每次迭代中，代码更新哈希表 hm 来记录当前窗口中各字符的出现次数 O(1)
3. 计算最大频率: 最耗时的操作是在循环中调用 max(hm.values())。由于字符集限定为大写英文字母，最多有 26 个键，因此这个操作的时间复杂度是 O(1)。但是，由于这个操作在每次循环中都执行，它可能会显著影响性能。
综上, 时间复杂度 O(n)

空间复杂度
1. 哈希表 O(1)
2. 两个指针和最大长度变量 O(1)
综上, 空间复杂度 O(1)
'''

