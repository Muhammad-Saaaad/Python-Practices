def tup(array,targetsum):
    length=len(array)
    for i in range(length):
        sum=0
        l=0
        m=0
        k=0
        while i <length:
            k+=1 
            if k==1:
                l=i
            if k>=2:
                m=i
            sum=sum+array[i]
            i=1+i
            if k>=2:
                k=0
                break
        if sum==targetsum:
            return  (l , m) 

ans=tup([1,2,3,4,5],7)
print(type(ans),ans)        