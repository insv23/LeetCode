# https://leetcode.com/problems/valid-parentheses/description/

'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        closeToOpen = {")": "(",
                       "]": "[",
                       "}": "{"}
        
        for char in s:
            # 如果是闭括号, 检查栈顶是否匹配
            if char in closeToOpen:
                # if stack and stack[-1] == closeToOpen[char]:
                #     stack.pop()
                # else:
                #     return False
                if not stack or stack.pop() != closeToOpen[char]:
                    return False
            else:
                # 其他情况(即开括号), 入栈
                stack.append(char)
        
        # 整个字符串结束, 如果栈还不为空, 说明不匹配
        return not stack

if __name__ == "__main__":
    s = input().strip()[1:-1]
    print(Solution().isValid(s))