user = int(input("Enter the size of the pattern:"))
for i in range(user):
    # Outer loop controls the number of rows
    for j in range(user):
        # Inner loop prints asterisks for each row
        print("*", end="")
    print()  # Move to a new line after each row of asterisks