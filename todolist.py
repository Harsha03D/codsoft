
import tkinter as tk

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.todos = []
        add_frame = tk.Frame(self.root, bg="pink")
        add_frame.pack(fill=tk.X, pady=5)

        tk.Label(add_frame, text="Add a new todo:", bg="lavender", font=("Helvetica", 12)).grid(row=0, column=0, padx=(20, 0))
        self.new_todo_entry = tk.Entry(add_frame, font=("Helvetica", 12))
        self.new_todo_entry.grid(row=0, column=1, padx=(10, 20))

        add_button = tk.Button(add_frame, text="Add", bg="orange", fg="white", font=("Helvetica", 12), command=self.add_todo)
        add_button.grid(row=0, column=2, padx=(10, 20))

        self.listbox_frame = tk.Frame(self.root, bg="green")
        self.listbox_frame.pack(fill=tk.BOTH, expand=True)

        self.todo_listbox = tk.Listbox(self.listbox_frame, font=("Helvetica", 12), height=10, activestyle="none")
        self.todo_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(self.listbox_frame, orient="vertical", command=self.todo_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.todo_listbox.config(yscrollcommand=scrollbar.set)

        self.todo_listbox.bind("<Button-1>", self.select_todo)
        self.todo_listbox.bind("<Delete>", self.delete_selected_todo)

        self.populate_todo_listbox()

    def populate_todo_listbox(self):
        self.todo_listbox.delete(0, tk.END)
        for i, todo in enumerate(self.todos):
            self.todo_listbox.insert(i, f"{i+1}. {todo}")

    def add_todo(self):
        new_todo = self.new_todo_entry.get().strip()
        if new_todo:
            self.todos.append(new_todo)
            self.populate_todo_listbox()
            self.new_todo_entry.delete(0, tk.END)

    def select_todo(self, event):
        self.selected_todo_index = self.todo_listbox.curselection()[0]

    def delete_selected_todo(self, event):
        if self.selected_todo_index is not None:
            del self.todos[self.selected_todo_index]
            self.populate_todo_listbox()
            self.selected_todo_index = None

if __name__ == "__main__":
    root = tk.Tk()
    todo_app = TodoApp(root)
    root.mainloop()
