def fibonacci(n,ht={0:0,1:1}):
    if n in ht:
        return ht[n]
    else:
        ht[n] = int(fibonacci(n-1,ht) + fibonacci(n-2,ht))
        return ht[n]
    
if __name__=="__main__":
    result=fibonacci(4,ht={0:0,1:1})
    print(result)
    