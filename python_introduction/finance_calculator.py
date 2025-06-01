user_income = int(input("Enter your monthly income:"))
user_expenses= int(input("Enter your total monthly expenses:"))
Monthly_savings = user_income - user_expenses
# Print the result
print(f"Your monthly savings is: ${Monthly_savings}.")
Projected_savings = (Monthly_savings * 12) + (Monthly_savings * 12 * 0.05)
# Print the result
print(f"Projected savings after one year, with interest, is: ${Projected_savings}.")