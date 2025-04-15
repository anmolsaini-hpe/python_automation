def isomorphic(S,T):
    if len(S) != len(T):
        return False
    
    ht1 = {}
    ht2 = {}
    
    for i,j in zip(S,T):
        if i in ht1 and ht1[i] !=j:
            return False
        if j in ht2 and ht2[j] !=i:
            return False

        ht1[i]=j
        ht2[j]=i

    return True


if __name__=="__main__":
    
    S = "abc"
    T = "def"
    print(isomorphic(S,T))