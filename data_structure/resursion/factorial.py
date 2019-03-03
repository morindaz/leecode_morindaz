def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

if __name__ == '__main__':
    result = fact(3)
    print(result)