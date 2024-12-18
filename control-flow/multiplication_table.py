# Prompt User for a number

number = int(input("Enter a number to see its multiplication table:"))

X = number
print(X)
#Generate and Print the Multiplication Table:
for Y in range(1,11):
    print(Y)
    Z = X * Y
# Multiplication Table Output
    print(Z)