# Prompt user for task details
Task = str(input("Enter your task: "))
Time_bound = str(input("Is it time-bound? (yes or no): "))
Priority = str(input("Priority (high, medium, low): "))

# Process the task based on priority
match Priority:
    case "high":
        reminder = f"'{Task}' is a high priority task"
    case "medium":
        reminder = f"'{Task}' is a medium priority task"
    case "low":
        reminder = f"'{Task}' is a low priority task."
    case _:
        reminder = f"'{Task}' has an unknown priority!"

# Modify reminder if task is time-bound
if Time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    if Time_bound == "no":
        reminder += " Consider completing it when you have free time."
# If the user enters an invalid priority, we will not modify the reminder further.

    else:
        reminder += " Please clarify if it is time-bound or not."

# Print customized reminder
print(reminder)