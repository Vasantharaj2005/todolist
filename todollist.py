class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def list_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            status = 'X' if task.completed else ' '
            print(f"{i}. [{status}] {task.description}")

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1].completed = True
        else:
            print("Invalid task index.")

def main():
    todo_list = TodoList()
    while True:
        print("\n==== To-Do List ====")
        todo_list.list_tasks()
        print("""
        Menu:
        1. Add Task
        2. Remove Task
        3. Mark Task as Completed
        4. Quit
        """)

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(Task(description))
        elif choice == '2':
            task_index = int(input("Enter task index to remove: "))
            todo_list.remove_task(todo_list.tasks[task_index - 1])
        elif choice == '3':
            task_index = int(input("Enter task index to mark as completed: "))
            todo_list.mark_completed(task_index)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
