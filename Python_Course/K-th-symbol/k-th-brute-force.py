def kth_symbol(n, k):
    #0
    #01
    #0110
    #base case when n==1
    if n == 1:
        return 0
    else:
        length_of_n = 2**(n - 1)
        half_of_length = length_of_n//2
        if k > half_of_length:
            return int(not kth_symbol(n-1, k-half_of_length))
        else:
            return int(kth_symbol(n-1, k))
    

if __name__=="__main__":
    n = 4
    k = 7
    result=kth_symbol(n,k)
    print(result)