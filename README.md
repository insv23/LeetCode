# LeetCode

# Tasks

## Create Test Files

每个题目一个目录，名称为 `1. Two Sum`, 目录下有:

- 测试样例命名为 `1.in.txt`
- 期待输出结果命名为 `1.ans.txt`
- 样例输出结果为 `1.out1.txt`(测试运行时生成)

该 task 检测当前文件夹中有无 1.in.txt, 1.ans.txt, 如果没有则创建，如果有则创建 2.in.txt, 2.ans.txt，如果有 2.... 则自动递增创建 3.... 以此类推

## Run All Tests

将当前目录所有 `#.in.txt` 作为输入传给当前文件，结果输出在 `#.out.txt`, 并与 `#.ans.txt` 对比

# Debug

## Debug with #.in.txt

只需输入一个序号，即可使用对应 #.in.txt 作为输入进行调试

# 快捷键

## 自定义快捷键

`Ctrl+r t` : Run task "Run All Tests"

`Ctrl+r n` : Run task "Create Test Files"

(但我放在 .vscode/keybindings.json 并不生效，放在系统的 keybindings.json 才生效... 目前没找到原因)

## 内置快捷键

`F5` : Start Debugging/Continue

`F10` : Step Over
