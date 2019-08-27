# auxillary functions that are used for some of the prime generators are defined here.
import math
###################### auxillary functions for bpsw  #########################

def jacobi(a,b):  #jacobi symbol
    assert (b>0 and b%2==1) #symbol is only defined when b is positive and odd.
    x=1
    while True:
        if pow(a,1,b)==0:
            return 0
        elif a>b or a<0:
            a=pow(a,1,b)
        y=-1 if (pow(b,1,8)==3 or pow(b,1,8)==5) else 1
        while a%2==0:
            a=a//2
            x=x*y
        if a==1:
            return x*1
        elif math.gcd(a,b)!=1:
            return 0
        else:
            z=-1 if pow(a,1,4)==pow(b,1,4)==3 else 1
            x=x*z
            a,b=b,a
            

def DPQ(n):    #compute DPQ for Lucas test
    x,y,z=5,-1,2
    while True:
        if jacobi(x,n)==-1:
            return x,1,(1-x)//4
        else:
            z=y*z
            x=y*x+z
            
    
    
def LucasU(n,p,q):  #finds the nth lucas u sequence
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        x,y,m=0,1,2
        while n>=m:
            z=p*y-q*x
            y,x=z,y
            m+=1
        return z


def LucasV(n,p,q):  #finds the nth lucas v sequence
    if n==0:
        return 2
    elif n==1:
        return p
    else:
        x,y,m=2,p,2
        while n>=m:
            z=p*y-q*x
            y,x=z,y
            m+=1
        return z
    
    
def slucas(n,d,p,q):  # checks if prime based on the strong lucas test. test assumes gcd(n,d)=1 to begin. n is odd.
    delta=n-jacobi(d,n)
    exponent=0
    while pow(delta,1,2)==0:
        delta=delta//2
        exponent+=1
    if pow(LucasU(delta,p,q),1,n)==0:
        return 'YES'
    for i in range(exponent+1):
        if pow(LucasV(delta*2**i,p,q),1,n)==0:
            return 'YES'
    return 'NO'    
    
    
    
################################################################################