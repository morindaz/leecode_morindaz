# -*- coding: utf-8 -*-
# @Time    : 2019/11/4
# @Author  : morindaz
# @FileName: dfs_search.py
# @explanation: This file is for: 全排列的题目，递归，输入0，1，2 输出全排列

def dfs_search(step):
    if step == n:
        print(result)
        return 0
    else:
        for i in range(n):
            if book[i] == 0:
                book[i] = 1
                result[step] = i
                dfs_search(step + 1)
                book[i] = 0

if __name__ == '__main__':
    n = 3
    result = [0 for _ in range(n)]
    book = [0 for _ in range(n)]
    dfs_search(0)
