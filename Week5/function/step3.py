number = int(input("Please enter a number: "))
multiplier = int(input("Please enter a multiplier: "))

def mul_function(n):
  return lambda a : a * n

multiply = mul_function(multiplier)

print(multiply(number))