def fibonacci(n):
    if n == 0 :
        return 0
    elif n == 1:
        return 1
    else:
        return int(fibonacci(n-1) + fibonacci(n-2))
         



if __name__=="__main__":
    result = fibonacci(8)
    print(result)
