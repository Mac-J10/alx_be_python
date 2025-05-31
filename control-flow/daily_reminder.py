# Prompt user for task details
task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes or no): ")
priority = input("Priority (high, medium, low): ")

# Process the task based on priority
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task."
    case _:
        reminder = f"'{task}' has an unknown priority!"

# Modify reminder if task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    if time_bound == "no":
        reminder += " Consider completing it when you have free time."
# If the user enters an invalid priority, we will not modify the reminder further.a
    else:
        reminder += " Please clarify if it is time-bound or not."

# Print customized reminder
print(reminder)