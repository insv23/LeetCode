# https://leetcode.com/problems/min-stack/description/

'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
'''

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        # 如果 min_stack 为空或 val 小于 min_stack 的栈顶值, 则将 val 入栈
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        val = self.stack.pop()
        # 如果弹出元素是当前最小值(min_stack 栈顶), 将其弹出
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1] # 只是给出值(不弹出)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == "__main__":
    operations = eval(input())
    vals_in_list = eval(input()) # [[], [-2], [0], [-3], [], [], [], []] 值被[]包裹, 应该只剩值作为输入
    vals = [val[0] if val else None for val in vals_in_list] # [None, -2, 0, -3, None, None, None, None]
    
    min_stack = None
    res = []
    
    for op, val in zip(operations, vals):
        if op == "MinStack":
            min_stack = MinStack()
            res.append(None)
        elif op == "push":
            min_stack.push(val)
            res.append(None)
        elif op == "pop":
            min_stack.pop()
            res.append(None)
        elif op == "top":
            val = min_stack.top()
            res.append(val)
        elif op == "getMin":
            val = min_stack.getMin()
            res.append(val)
    
    print(res)