def checker(cels):
    if 'C' in cels:
        return True
    return False


def mod(value):
    value_list = []
    for i in value:
        new_temp = float(i[:-1])
        value_list.append(new_temp)
    return value_list

def max(value):
    largest = value[0]
    for i in value:
        if i > largest:
            largest = i
    return largest

def mini(value):
    smallest = value[0]
    for i in value:
        if i < smallest:
            smallest = i
    return smallest

def mean(value4):
    sum = 0
    for i in value4:
        sum += i
    
    mean = (sum / len(value4))
    return mean

temp_list=[]

for i in range(6):
    temp = (input("Enter Enter temperature in celsius like(55C):"))
    if checker(temp): 
        temp_list.append(temp)
    else:
        print('You have to enter "C"')
        
values = mod(temp_list)

print(f"Maximum value = {max(values)}, minimum value = {min(values)}and mean = {mean(values)}")