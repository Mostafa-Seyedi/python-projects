# 📝 To-Do List (Python CLI)

A simple command-line **To-Do List** application built in Python that lets you **add, remove, and view tasks**. Your tasks are saved in a CSV file so they persist between sessions.

---

## ✨ Features
- ➕ **Add Tasks** with a name, description, and priority (High / Medium / Low)  
- 🗑 **Remove Tasks** by name  
- 📋 **View All Tasks** in a neat table format  
- 💾 **Persistent Storage** using CSV file (`tasks.csv`)  
- 🖥 **Easy to Use CLI** with emoji indicators  

---

## 📂 Project Structure
```
📁 
 ├── tasks.csv        # Stores all tasks (auto-created)
 ├── ToDoList.py      # Main Python script
 └── README.md        # Project documentation
```

---

## 🚀 How to Run

1. **Clone the repository**  
```bash
git clone https://github.com/Mostafa-Seyedi/todo-list.git
cd todo-list
```

2. **Run the Python script**  
```bash
python ToDoList.py
```

---

## 📌 Menu Options
When running the program, you will see:
```
📌 TO-DO LIST MENU 📌
1️⃣ Add Task
2️⃣ Remove Task
3️⃣ Show Tasks
4️⃣ Exit
```

---

## 🖼 Example Output
**Adding a task:**
```
Enter task name: Buy Groceries
Enter task description: Milk, Eggs, Bread
Enter priority (High / Medium / Low): High
✅ Task added successfully!
```

**Viewing tasks:**
```
📋 To-Do List:
No.  Name                 Description                             Priority  
--------------------------------------------------------------------------------
1    Buy Groceries        Milk, Eggs, Bread                       High      
```

---

## 🛠 Requirements
- Python 3.x  
(No extra libraries needed — uses only Python’s built-in modules.)

---

## 📄 License
This project is open source and available under the **MIT License**.
