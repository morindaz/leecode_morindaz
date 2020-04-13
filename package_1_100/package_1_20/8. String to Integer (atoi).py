# -*- coding: utf-8 -*-
'''
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.



Requirements for atoi:

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

'''


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if str == "":
            return 0
        # print(str)
        count = 0
        result = 0
        flag = 1
        start = 0
        while(start < len(str) and str[start] == ' '):
           start += 1
        if (str[start] == "-"):
            flag = -1
            start += 1
        elif (str[start] == "+"):
            flag = 1
            start+=1

        for i in range(start,len(str)):
            if str[i] < "0" or str[i] > "9":
                break
            if ord(str[i]) >= 47 and ord(str[i]) <= 58:
                result = result * 10 + int(str[i])
            else:
                break
        result *= flag
        if count > 1:
            return 0
        elif result < -2147483648:
            return -2147483648
        elif result > 2147483647:
            return 2147483647
        return result

if __name__ == '__main__':
    solution = Solution()
    a = "  ss   ss"
    print(a)
    a.strip()
    print(a)
    b = a.strip()
    print(b)
    result = solution.myAtoi("      010")
    print(result)


'''
这题是个坑。不是好像，真的是个坑！
+-2 return 0
-2332j333   -2332
2147483648  2147483647
"   - 321"   0
"    010"    10
还有好多测试用例不知道怎么搞
应该写两个循环 外部变量一个i用来定位到从哪里开始是数字或者说字符
------------------
好吧说说思路，首先要过空格，所以遍历一遍把最前面的空格过掉，有个变量记录开始的位置
这里用了start 之后碰到第一个不是空格的字符时要做判断。
判断第一个是不是正负号。如果是负那么flag=-1，否则flag=1。把起始位置加1。
进入循环判断，这时候认为应该是数字开始了，如果在符号位（如果有负号的话）后面又出现了一个符号，
这被认为和出现字母是一样的，会返回零。如果是数字的话就会读取出来，然后进行计算。
如果在数字后面出现了字母，即使字母之后再有数字，也在字母前面就要停止。
不是很难，要排除的情况比较多。最后还要对于越界情况进行判断。
这题脑残，给差评。
'''