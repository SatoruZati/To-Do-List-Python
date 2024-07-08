import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x300")

        # Create frames
        self.frame_tasks = tk.Frame(self.root)
        self.frame_tasks.pack(fill="both", expand=True)

        self.frame_buttons = tk.Frame(self.root)
        self.frame_buttons.pack(fill="x")

        # Create task list
        self.task_list = tk.Listbox(self.frame_tasks, width=40, height=10)
        self.task_list.pack(fill="both", expand=True)

        # Create entry field
        self.entry_task = tk.Entry(self.frame_tasks, width=40)
        self.entry_task.pack(fill="x")

        # Create buttons
        self.button_add = tk.Button(self.frame_buttons, text="Add Task", command=self.add_task)
        self.button_add.pack(side="left")

        self.button_update = tk.Button(self.frame_buttons, text="Update Task", command=self.update_task)
        self.button_update.pack(side="left")

        self.button_delete = tk.Button(self.frame_buttons, text="Delete Task", command=self.delete_task)
        self.button_delete.pack(side="left")

        self.button_clear = tk.Button(self.frame_buttons, text="Clear List", command=self.clear_list)
        self.button_clear.pack(side="left")

    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.task_list.insert(tk.END, task)
            self.entry_task.delete(0, tk.END)

    def update_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            task = self.entry_task.get()
            if task:
                self.task_list.delete(task_index)
                self.task_list.insert(task_index, task)
                self.entry_task.delete(0, tk.END)
        except:
            messagebox.showerror("Error", "Select a task to update")

    def delete_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            self.task_list.delete(task_index)
        except:
            messagebox.showerror("Error", "Select a task to delete")

    def clear_list(self):
        self.task_list.delete(0, tk.END)

# driver code
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()