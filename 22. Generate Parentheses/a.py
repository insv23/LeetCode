# https://leetcode.com/problems/generate-parentheses/description/

'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
'''
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        
        def backtrack(open, closed):
            if open == closed == n:
                res.append("".join(stack))
                return

            if open < n:
                stack.append('(')
                backtrack(open + 1, closed)
                stack.pop()
            
            if open > closed:
                stack.append(')')
                backtrack(open, closed + 1)
                stack.pop()
            
        backtrack(0, 0)
        return res
        
if __name__ == "__main__":
    n = int(input().strip())
    print(Solution().generateParenthesis(n))