def gcd(num1, num2):
    if num1 % num2 == 0:
        return num2
    else:
        return gcd(num2, num1 % num2)


if __name__ == '__main__':
    result = gcd(32, 12)
    print(result)