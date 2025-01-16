"""One approach to analysing some encrypted data where a substitution is suspected
is frequency analysis. A count of the dierent symbols in the message can be used
to identify the language used, and sometimes some of the letters. In English, the
most common letter is "e", and so the symbol representing "e" should appear most
in the encrypted text.
Write a program that processes a string representing a message and reports the six
most common letters, along with the number of times they appear. Case should
not matter, so "E" and "e" are considered the same.
Hint: There are many ways to do this. It is obviously a dictionary, but we will want
zero counts, so some initialisation is needed. Also, sorting dictionaries is tricky, so
best to ignore that initially, and then check the usual resources for the runes."""

def frequency_analyzer(string):
    letter_dict = {}
    for i in string:
        if i in letter_dict:
            letter_dict[i] += 1
        else:
            letter_dict[i] = 1
    sorted_letters = sorted(letter_dict.items(), key=lambda x: x[1], reverse=True)
    print("Most common letters emerging:")
    for i in sorted_letters[:6]:  
        print(f"{i[0]}: {i[1]}")

frequency_analyzer("This is saksham")