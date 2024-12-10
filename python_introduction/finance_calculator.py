monthly_income = int(input("Please enter your monthly income: "))
total_expense = int(input("Please enter your monthly expense: "))

monthly_saving = monthly_income - total_expense

projected_savings = ( monthly_saving * 12 +(monthly_saving *12 *0.05))

print(monthly_saving)
print(projected_savings)
