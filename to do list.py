class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title}: {self.description}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        new_task = Task(title, description)
        self.tasks.append(new_task)
        print(f"Task '{title}' added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("To-Do List:")
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {task}")

    def update_task(self, index, title=None, description=None, completed=None):
        if 0 <= index < len(self.tasks):
            if title is not None:
                self.tasks[index].title = title
            if description is not None:
                self.tasks[index].description = description
            if completed is not None:
                self.tasks[index].completed = completed
            print(f"Task '{self.tasks[index].title}' updated successfully.")
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Task '{removed_task.title}' deleted successfully.")
        else:
            print("Invalid task index.")


def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_list.add_task(title, description)

        elif choice == '2':
            todo_list.view_tasks()

        elif choice == '3':
            todo_list.view_tasks()
            try:
                index = int(input("Enter the task number to update: ")) - 1
                new_title = input("Enter new title (leave blank to keep current): ")
                new_description = input("Enter new description (leave blank to keep current): ")
                completed_input = input("Mark as completed? (y/n, leave blank to keep current): ")
                completed = None
                if completed_input.lower() == 'y':
                    completed = True
                elif completed_input.lower() == 'n':
                    completed = False
                todo_list.update_task(index, new_title or None, new_description or None, completed)

            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '4':
            todo_list.view_tasks()
            try:
                index = int(input("Enter the task number to delete: ")) - 1
                todo_list.delete_task(index)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '5':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
