monthly_income = int(input("Enter your monthly income: "))
total_expense = int(input("Enter your monthly expense: "))

monthly_saving = monthly_income - total_expense

projected_savings = ( monthly_saving * 12 +(monthly_saving *12 *0.05))

print(monthly_saving)
print(projected_savings)
