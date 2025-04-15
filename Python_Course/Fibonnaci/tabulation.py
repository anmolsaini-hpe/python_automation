def fibonacci(n):
    dp=[0]*(n+1)
    dp[0] = 0
    dp[1] = 1

    count = 1

    while count < n :
        count +=1
        dp[count] = dp[count -1] + dp[count -2]
    return dp[n]


if __name__=="__main__":
    result=fibonacci(8)
    print(result)