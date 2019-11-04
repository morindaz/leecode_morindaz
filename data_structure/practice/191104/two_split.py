# -*- coding: utf-8 -*-
# @Time    : 2019/11/4
# @Author  : morindaz
# @FileName: two_split.py
# @explanation: This file is for: 二分法，输出平方根，要求误差小于0.001

def split(n):
    thres = 0.001
    up = n
    low = 0
    mid = (up + low) / 2
    while abs(n - mid * mid)> thres:
        if n / mid > mid:
            low = mid
        if n / mid < mid:
            up = mid
        mid = (up + low) / 2
        print(mid)
    return mid

if __name__ == '__main__':
    split(2)
