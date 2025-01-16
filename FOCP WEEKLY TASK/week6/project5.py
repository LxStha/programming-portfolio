"""5.Another way to hide a message is to include the letters that make it up within
seemingly random text. The letters of the message might be every fih character,
for example. Write and test a function that does such encryption. It should
randomly generate an interval (between 2 and 20), space the message out
accordingly, and should fill the gaps with random letters. The function should
return the encrypted message and the interval used.
For example, if the message is "send cheese", the random interval is 2, and for
clarity the random letters are not random:
send cheese
s e n d c h e e s e
sxyexynxydxy cxyhxyexyexysxye"""

import random
import string

def encrypt(message):
    interval=random.randint(2, 20)
    
    encrypted_message=[]
    index=0
    
    while index<len(message):
        for i in range(interval):
            if index<len(message) and i==0:
                encrypted_message.append(message[index])
                index+=1
            else:
                encrypted_message.append(random.choice(string.ascii_lowercase))
    
    return ''.join(encrypted_message), interval

message = input("Enter a message to encrypt: ")
encrypted_message, interval = encrypt(message)
print(f"Encrypted message: {encrypted_message}")
print(f"Interval used: {interval}")
