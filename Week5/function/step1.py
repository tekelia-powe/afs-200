numlist = []
for x in range(3):
    number = int(input("Please enter a number: "))
    numlist.append(number)
    

def maxNum():
    return max(numlist)
    
def minNum():
    return min(numlist)

print("Max Value: ",maxNum())
print("Min Value: ",minNum())