'''
Neetcode 的思路，最简单直接
与 a.py 相比，省去了找最短 word 的时间
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ''
        
        # 对第一个 word 的每个字符 分别 检查每个 word 该位置是否匹配
        # 第一个字符可能不是最短的，所以需要关注越界情况(一旦发生越界，表明某个 word 被遍历完了，它应该是最长公共前缀)
        for i in range(len(strs[0])):
            for word in strs:
                if i == len(word) or word[i] != strs[0][i]:
                    return res
            # 每个 word 的 i 处都检查确认一致了，就能加入到结果中
            res += strs[0][i]
        
        # 如果没有提前 return, 说明第一个字符就是目标
        return res


if __name__ == "__main__":
    trimmed_str = input().strip()[1:-1]
    words_list = [word.strip('"') for word in trimmed_str.split(',')]
    
    so = Solution()
    res = so.longestCommonPrefix(words_list)

    print(res)