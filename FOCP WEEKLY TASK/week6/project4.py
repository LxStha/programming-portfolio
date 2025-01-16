"""4. Computers are commonly used in encryption. A very simple form of encryption
(more accurately "obfuscation") would be to remove the spaces from a message
and reverse the resulting string. Write, and test, a function that takes a string
containing a message and "encrypts" it in this way."""

def encrypt_message(message):
    message_without_spaces=message.replace(" ", "")
    encrypted_message=message_without_spaces[::-1]
    return encrypted_message

message=input("Enter a message to encrypt: ")
encrypted_message=encrypt_message(message)
print(f"Encrypted message: {encrypted_message}")