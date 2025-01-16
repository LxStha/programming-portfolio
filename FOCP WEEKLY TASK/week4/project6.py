"""6.Write a program that takes a centigrade temperature and displays the equivalent in
fahrenheit. The input should be a number followed by a letter C. The output should
be in the same format."""
def checker(cal):
    if 'C' in cal:
        return cal
    else:
        print('You have to enter "C"')
def cal_fahrenheit(cal):
    if checker(cal):
        cel=float(cal[:-1])
                
        far=cel*(9/5)+32
        return far
celsius= input("Enter Enter temperature in celsius like(55C):")
print(f"{cal_fahrenheit(celsius)}F")