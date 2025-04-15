def climbstairs(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return climbstairs(n-1) + climbstairs(n-2)


if __name__ == '__main__':
    result=climbstairs(3)
    print(result)

