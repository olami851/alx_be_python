# Prompt User for a number
from itertools import product

number = int(input("Enter a number to see its multiplication table: "))

# X = number
print(number)
#Generate and Print the Multiplication Table:
for iterator in range(1,11):
    print(iterator)
    # Z = X * Y
    product = number * iterator
# Multiplication Table Output
    print(f"{number} * {iterator} = {product}")