# https://leetcode.com/problems/valid-sudoku/description/

'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
'''

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        

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

