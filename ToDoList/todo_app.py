import os

class TodoList:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added successfully.")

    def delete_task(self, task_index):
        try:
            task = self.tasks.pop(task_index - 1)
            print(f"Task '{task}' deleted successfully.")
        except IndexError:
            print("Invalid task index. Please provide a valid index.")

    def mark_completed(self, task_index):
        try:
            task = self.tasks[task_index - 1]
            self.tasks[task_index - 1] = f"[Done] {task}"
            print(f"Task '{task}' marked as completed.")
        except IndexError:
            print("Invalid task index. Please provide a valid index.")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    todo_list = TodoList()

    while True:
        clear_screen()

        print("To-Do List:")
        todo_list.display_tasks()

        print("\nOptions:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark as Completed")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task_index = int(input("Enter the task index to delete: "))
            todo_list.delete_task(task_index)
        elif choice == '3':
            task_index = int(input("Enter the task index to mark as completed: "))
            todo_list.mark_completed(task_index)
        elif choice == '4':
            print("Exiting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
