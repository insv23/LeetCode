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
        length = len(s)
        while length > 0:
            s = s.replace("()", "").replace("[]", "").replace("{}", "")
            # 如果长度没有变化，说明没有更多可替换的括号
            if len(s) == length:
                return False
            length = len(s)
        return True

if __name__ == "__main__":
    s = input().strip()[1:-1]
    print(Solution().isValid(s))
    
'''
草, 比 Stack 更慢
时间复杂度
1. 最坏情况：在最坏的情况下，每次替换操作只移除两个字符（即一个括号对），而每次替换都需要遍历整个字符串。例如，对于一个像 ((((((((((...)))))))))) 这样的字符串，每次替换只能移除最内层的括号对。如果字符串长度为 n，则第一次替换需要 O(n) 时间，第二次替换需要 O(n-2) 时间，以此类推，直到字符串为空。因此，总的时间复杂度为 O(n) + O(n-2) + O(n-4) + ... + O(1)，这是一个等差数列求和，其和为 O(n^2)。
2. 平均情况：平均情况下，每次替换可能移除多个括号对，但通常仍需要多次遍历整个字符串。因此，平均时间复杂度也接近 O(n^2)。
空间复杂度
1. 空间复杂度：由于每次替换都会生成一个新的字符串，因此在每次替换过程中都需要额外的空间来存储这个新字符串。在最坏的情况下，这个空间需求可以接近 O(n)。因此，空间复杂度为 O(n)。
总结
这种使用连续替换的方法虽然在某些情况下代码看起来简单，但其效率较低，特别是在字符串较长或括号嵌套较深的情况下。每次替换操作都需要处理整个字符串，并且可能需要多次替换才能处理完所有括号对，导致时间复杂度高达 O(n^2)。同时，由于字符串的不可变性，每次替换都需要额外的空间来存储新字符串，空间复杂度为 O(n)。
因此，对于大多数实际应用，使用栈的方法（时间复杂度为 O(n)，空间复杂度为 O(n)）通常更为高效和可靠。
'''