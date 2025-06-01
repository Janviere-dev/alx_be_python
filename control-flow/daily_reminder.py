task = input("Enter task description: ").strip()
priority = input("Enter task’s priority (high, medium, low): ").strip().lower()
time_bound = input("Is the task time-bound? (yes or no): ").strip().lower()
match priority:
    case "high":
        print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
    case "medium":
        print(f"Reminder: {task} is a medium priority task that should be completed soon.")
    case "low":
        if time_bound == "no":
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
        else:
            print(f"Reminder: {task} is a low priority task but it is time-bound. Please complete it after you have finished most high priority tasks.")
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")