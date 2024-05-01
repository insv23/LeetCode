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
        pass
        
if __name__ == "__main__":
    n = int(input().strip())
    print(Solution().generateParenthesis(n))