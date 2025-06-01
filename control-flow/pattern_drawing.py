

user = int(input("Enter the size of the pattern:"))

i = 0  # Initialize row counter

while i < user:  # While loop to control rows
    j = 0  # Initialize column counter
    while j < user:  # While loop to print asterisks
        print("*", end="")
        j += 1  # Move to the next column
    print()  # Move to a new line after each row
    i += 1  # Move to the next row
