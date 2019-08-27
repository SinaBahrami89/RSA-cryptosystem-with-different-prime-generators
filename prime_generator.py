#this module is written to generate prime numbers via a number of algorithms.
#that are based on the following primality tests:
# Fermat, Miller-Rabin, Miller deterministic, Baillie-PSW.
import random #to generate random numbers. 
_sysrand=random.SystemRandom()
import math
import aux_fncs #includes auxillary functions for bpsw.


#Fermat: if n is composite, the probability that it is a false prime
#is bounded by (phi(n)/(n-1))**rounds. 
def gen_fermat(bits, rounds=10):
    while True:
        r=_sysrand.randrange(2**(bits-1)-1,2**(bits),2)
        counts=0
        for _ in range(rounds):
            a=_sysrand.randint(2,r-1)  #if you want no repetitions, need extra memory.
            if pow(a,r-1,r)!=1:
                break
            else:
                counts+=1
        if counts==rounds:
            return r

#Miller-Rabin: if n is composite, the probability that it is a false prime is bounded by (1/4)**rounds.    
def gen_mr(bits,rounds=10): 
    while True:
        r=_sysrand.randrange(2**(bits-1)-1,2**(bits),2)
        q=r-1
        exponents=[]
        while pow(q,1,2)==0:
            q=q//2
            exponents.append(q)
        
        counts,pointer=rounds,rounds
        while pointer>0 and counts==pointer:
            pointer-=1
            x=_sysrand.randint(2,r-1) #if you want no repetitions, need extra memory.
            if pow(x,exponents[-1],r)==1:
                counts-=1
            else:
                for i in exponents:
                    if pow(x,i,r)==r-1:
                        counts-=1
                        break
            
        if counts==0:        
            return r
        
#Miller deterministic test: its correctness hinges on the generalized Riemann hypothesis
#it is fairly efficient for producing 256-bits primes. 
def gen_m(bits):
    while True:
        r=_sysrand.randrange(2**(bits-1)-1,2**(bits),2)
        q=r-1
        exponents=[]
        while pow(q,1,2)==0:
            q=q//2
            exponents.append(q)   
        l=[x for x in range(2,min(r-2,math.floor(2*math.log(r)**2))+1)]
        c=len(l)
        while len(l)==c and c>0:
            c-=1
            x=l[0]
            if pow(x,exponents[-1],r)==1:
                l.remove(x)
            else:
                for y in exponents:
                    if pow(x,y,r)==r-1:
                        l.remove(x)
                        break
            
         
        if len(l)==0:
            return r


# Baillie-PSW test: the current implementation of this method is very INEFFICIENT. for bits=25, it takes about ~8 mins. 
def gen_bpsw(bits):
    while True:
        r=_sysrand.randrange(2**(bits-1)-1,2**(bits),2)
        q=r-1
        exponents=[]
        count=0
        while pow(q,1,2)==0:
            q=q//2
            exponents.append(q)
        if pow(2,exponents[-1],r)==1:
            count+=1
        else:
            for j in exponents:
                if pow(2,j,r)==r-1:
                    count+=1
                    break
        if count==0:
            continue
        else:
            d,p,q= aux_fncs.DPQ(r)
            if aux_fncs.slucas(r,d,p,q)=='YES':
                return r
            
            


if __name__ == '__main__':
    print('this module contains several well known methods for generating primes')
        
    


                