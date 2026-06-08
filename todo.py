# To-Do List Application

tasks = []

while True:1
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("✅ Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("📌 No tasks available.")
        else:
            print("\n📋 Your Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("📌 No tasks to delete.")
        else:
            print("\n📋 Your Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            try:
                num = int(input("Enter task number to delete: "))
                removed = tasks.pop(num - 1)
                print(f"❌ Deleted task: {removed}")
            except:
                print("⚠ Invalid task number!")

    elif choice == "4":
        print("👋 Exiting To-Do List App")
        break

    else:
        print("⚠ Invalid choice! Try again.")