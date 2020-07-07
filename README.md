This is a simple implementation of the RSA public-key cryptosystem developed by Sina Bahrami.
Anyone is free to use or modify the codes and modules that are contained in this file. 

The script is written in Python 3.

There are a total of 5 modules:

- prime_generator.py:
generates random prime integers using the following primality tests: Fermat, Miller-Rabin, deterministic Miller, and Baillie-PSW.
the first two methods are the most efficient. deterministic Miller is also pretty good for integers less than or on the order of
2**256. however, the current implementation of Baillie-PSW is inefficient. i do not recommend using this method at this statge.
Randoms are expected to be cryptographically secure. They are generated via the SystemRandom class of the random module.
    
- aux_fncs.py:
this is an auxillary module. it contains a few number-theoretic functions that are used in the Baillie-PSW method.
    
- RSA_Keys.py:
you can run this in the terminal. it asks you to choose one of the methods to generate the random prime integers and specify the desired
number of bits. there is a function that generates the public and private keys via the RSA method. Once the keys are available, they are
written in a file called rsa_keys.txt along with the exact date and time at which they were generated.
    
- RSA_Encryption.py:
when you run this script, you will be prompted to enter the public key and the text you would like to encrypt. it breaks up the text into
a list of characters and then translates each character to its Unicode code point by the built-in ord function. the encrypted message is
written to a file called cipher.txt
    
- RSA_decryption.py:
 it requires the private key, and then reads cipher.txt and writes the decrypted message to decipher.txt. i use the built-in chr function to invert numbers back to letters. 
