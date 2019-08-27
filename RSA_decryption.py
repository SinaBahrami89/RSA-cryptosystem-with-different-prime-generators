#RSA decryption assuming that you possess the relevant private key
import csv #to read file.
import sys
csv.field_size_limit(sys.maxsize) #to avoid csv error on field limit.

if __name__=='__main__':
    private_key=[int(c) for c in input('enter private key, separating the integers with space:').split()]
    cipher_text='cipher.txt'
    with open(cipher_text,'r') as f:
        content=csv.reader(f)
        content_list=[]
        for x in content:
            for y in x[0].split():
                content_list.append(chr(pow(int(y),private_key[0],private_key[1]))) #built in chr function reverses ord

    decipher=open('decipher.txt','w+')  #write the decrypted text in a newly created file decipher.txt 
    decipher.write(''.join([x for x in content_list]))
    decipher.close()