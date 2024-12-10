monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expense: "))

monthly_savings = monthly_income - monthly_expenses

projected_savings = (monthly_savings * 12) +  float( monthly_savings *12 *0.05)

print(monthly_savings)
print(projected_savings)
