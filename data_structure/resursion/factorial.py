def fact1(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def fact(n):
    result = [1 for i in range(n)]
    for i in range(2, n):
        # print(i)
        result[i] = result[i-1] + result[i-2]
    return result[-1]

if __name__ == '__main__':
    result = fact(7)
    print(result)