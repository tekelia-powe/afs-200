numlist = []
for x in range(3):
    number = int(input("Please enter a number: "))
    numlist.append(number)
    

def max_min():
    max_value = max(numlist)
    print("Max Value: ",max_value)
    min_value = min(numlist)
    print("Min Value: ",min_value)

max_min()