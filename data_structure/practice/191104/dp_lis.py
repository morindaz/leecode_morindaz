# -*- coding: utf-8 -*-
# @Time    : 2019/11/4
# @Author  : morindaz
# @FileName: dp_lis.py
# @explanation: This file is for: 输出最长上升子序列的长度，如[2,1,3,4,1,2,5]， 则LIS为4

def LIS(input_list):
    result = [1 for i in range(len(input_list))]
    for i in range(len(result)):
        for j in range(i):
            if input_list[i] > input_list[j] and result[i] < result[j] + 1 :
                result[i] = result[j] +1
    print(result)
    return max(result)

if __name__ == '__main__':
    result = LIS([2,1,3,4,1,2,5])
    print("LIS:", result)