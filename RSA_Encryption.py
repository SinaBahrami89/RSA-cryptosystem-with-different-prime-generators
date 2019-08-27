#encryption via RSA, assuming you are given a public key.
if __name__=='__main__':
    public_key=[int(c) for c in input('enter public key, separating the integers with space:').split()]
    text=input('enter your message here:')
    file=open('cipher.txt','w+') #write the cipher in cipher.txt
    file.write(' '.join([str(pow(ord(x),public_key[0],public_key[1])) for x in text])) #I use the built-in ord function for translating characters to digits
    file.close()
