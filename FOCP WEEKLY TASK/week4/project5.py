"""5.Write and test a function that converts a temperature measured in degrees
centigrade into the equivalent in fahrenheit, and another that does the reverse
conversion. Test both functions. (Google will find you the formulae)."""

def cal(C):
    F=C*(9/5)+32
    return F
def cal2(f):
    return (f-32)*5/9

temp=float(input("Enter the temperature in Celsius: "))
F=cal(temp)

print(f"temperature in fahrenheit: {cal(temp)}")
print(f"temperature  in Celsius: {cal2(F)}")