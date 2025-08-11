import csv


# ========================
# Class representing a Task
# ========================
class Task:
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority  # "High", "Medium", "Low"

    def __str__(self):
        return f"{self.name} ({self.priority}) - {self.description}"


# ========================
# Class representing the ToDo List
# ========================
class ToDoList:
    def __init__(self, filename="tasks.csv"):
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()
        print("✅ Task added successfully!")

    def remove_task(self, task_name):
        for task in self.tasks:
            if task.name.lower() == task_name.lower():
                self.tasks.remove(task)
                self.save_tasks()
                print("🗑️ Task removed successfully!")
                return
        print("⚠️ Task not found!")

    def show_tasks(self):
        if not self.tasks:
            print("📭 No tasks found!")
        else:
            print("\n📋 To-Do List:")
            print(f"{'No.':<4} {'Name':<20} {'Description':<40} {'Priority':<10}")
            print("-" * 80)  # divider line
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i:<4} {task.name:<20} {task.description:<40} {task.priority:<10}")


    def save_tasks(self):
        with open(self.filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Description", "Priority"])
            for task in self.tasks:
                writer.writerow([task.name, task.description, task.priority])

    def load_tasks(self):
        try:
            with open(self.filename, "r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    task = Task(row["Name"], row["Description"], row["Priority"])
                    self.tasks.append(task)
        except FileNotFoundError:
            # If the file doesn't exist, just start with an empty list
            pass



# ========================
# Menu for user interaction
# ========================
def menu():
    todo_list = ToDoList()

    while True:
        print("\n📌 TO-DO LIST MENU 📌")
        print("1️⃣ Add Task")
        print("2️⃣ Remove Task")
        print("3️⃣ Show Tasks")
        print("4️⃣ Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            priority = input("Enter priority (High / Medium / Low): ")
            task = Task(name, description, priority.capitalize())
            todo_list.add_task(task)

        elif choice == "2":
            name = input("Enter task name to remove: ")
            todo_list.remove_task(name)

        elif choice == "3":
            todo_list.show_tasks()

        elif choice == "4":
            print("👋 Goodbye!")
            break

        else:
            print("⚠️ Invalid choice, please try again!")


# ========================
# Run the program
# ========================
if __name__ == "__main__":
    menu()
