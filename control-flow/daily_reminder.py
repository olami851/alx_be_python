#Prompt for Task details:

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no)").strip().lower()

# Process task based on priority using match case

match priority:
    case "high":
        reminder = f"The '{task}' is a high priority task, "

    case "medium":
        reminder = f"The '{task}' is a medium priority task, "

    case "low":
        reminder = f"The '{task}' is a low priority task, "

    case _:
        reminder = f"The '{task}' has an unknown priority, "

# Using if and else statement to control the program

if time_bound == "yes":
    reminder += "that requires immediate attention today!"

    print(f"Reminder: {reminder}")

else:
    print("Note: 'Read a book' is a low priority task. Consider completing it when you have free time.")

print("Thank you for yor time")