# Prompt User for Pattern Size

size = int(input("Enter the size of the pattern: "))

# Drawing of pattern with the entered size

row = 0

while row < size:
    for column in range(size):
        print("*", end = "")
    print(" ")
    row = row + 1