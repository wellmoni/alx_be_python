task = str(input("Enter your task: "))
priority =str(input("Priority (high/medium/low): "))
time_bound =str(input("Is it time-bound? (yes/no): "))

match priority:
        case "high"
        case "medium"
        case "low"

if time_bound =="yes":
    print(f"Reminder: {task} is a {priority} task that requires immediate attention today! ")
