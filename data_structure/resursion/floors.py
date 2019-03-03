"""
其实就是一个斐波那契
"""
def floors(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return floors(n-1) + floors(n-2)

if __name__ == '__main__':
    result = floors(8)
    print(result)