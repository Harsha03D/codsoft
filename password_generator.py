import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    length = int(length_entry.get())

    if length < 4:
        messagebox.showerror("Error", "Password length must be at least 4")
        return

    use_upper = upper_var.get()
    use_numbers = numbers_var.get()
    use_special = special_var.get()

    chars = string.ascii_lowercase

    if use_upper:
        chars += string.ascii_uppercase

    if use_numbers:
        chars += string.digits

    if use_special:
        chars += string.punctuation

    if len(chars) < 2:
        messagebox.showerror("Error", "At least one character set must be selected")
        return

    password = ''.join(random.choice(chars) for i in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")
root.config(bg="pink")

tk.Label(root, text="Password Length:", bg="pink", font=("Sans", 14)).grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root, width=10, font=("Sans", 14))
length_entry.grid(row=0, column=1, padx=10, pady=10)

upper_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Uppercase", variable=upper_var, bg="pink", font=("Sans", 14)).grid(row=1, column=0, padx=10, pady=5)
numbers_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var, bg="pink", font=("Sans", 14)).grid(row=2, column=0, padx=10, pady=5)
special_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Special", variable=special_var, bg="pink", font=("Sans", 14)).grid(row=3, column=0, padx=10, pady=5)

password_entry = tk.Entry(root, width=30, font=("Sans", 14), bg="white")
password_entry.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

tk.Button(root, text="Generate Password", command=generate_password, bg="green", fg="white", font=("Sans", 14)).grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
