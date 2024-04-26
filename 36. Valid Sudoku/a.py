# https://leetcode.com/problems/valid-sudoku/description/

'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
'''
from collections import defaultdict # Leetcode 可以直接用, 无需引入

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        cubes = defaultdict(set) # key = (r//3, c//3)

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                if (num in rows[i] or 
                    num in cols[j] or 
                    num in cubes[(i//3, j//3)]):
                    return False
                rows[i].add(num)
                cols[j].add(num)
                cubes[(i//3, j//3)].add(num)
        
        return True
        

if __name__ == "__main__":
    import json
    import sys

    # 从标准输入读取一行数据
    input_str = sys.stdin.read().strip()

    # 使用 json.loads 将 JSON 格式的字符串转换为 Python 列表
    sudoku_data = json.loads(input_str)

    so = Solution()
    res = so.isValidSudoku(sudoku_data)
    
    print(res)

'''
时间复杂度
在这个 isValidSudoku 函数中，我们遍历了整个 9x9 的数独板，对每个单元格进行检查。因此，总共有 81 个单元格需要处理。对于每个单元格，我们执行了以下操作：
检查当前数字是否已存在于对应的行、列或宫格集合中。
将当前数字添加到对应的行、列和宫格集合中。
由于集合的查找和插入操作的平均时间复杂度是 O(1)，因此，整个函数的时间复杂度主要由遍历所有单元格决定，即 O(9x9) = O(81) = O(1)。这里我们可以认为时间复杂度是常数时间，因为数独的大小是固定的。
 
空间复杂度
空间复杂度主要由用于存储行、列和宫格中数字的集合决定：
rows、cols 和 cubes 每个都有 9 个集合，对应数独的 9 行、9 列和 9 个宫格。
每个集合最多可以包含 9 个不同的数字（从 '1' 到 '9'）。
因此，最坏情况下，这三个字典中每个都存储了 9 个集合，每个集合包含 9 个元素。所以，空间复杂度为 O(3x9x9) = O(243) = O(1)。同样地，由于数独的大小是固定的，我们可以认为这是一个常数空间复杂度。
综上所述，这个算法的时间复杂度和空间复杂度都可以视为常数级别，因为它们都与数独板的固定大小（9x9）相关。
'''