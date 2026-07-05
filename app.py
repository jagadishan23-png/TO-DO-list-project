import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x500")
root.config(bg="#f0f0f0")

tasks = []

# Function to add task
def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to delete task
def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
        tasks.pop(selected_task_index)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Function to mark task as completed
def mark_completed():
    try:
        selected_task_index = listbox.curselection()[0]
        selected_task = listbox.get(selected_task_index)
        listbox.delete(selected_task_index)
        listbox.insert(selected_task_index, "✔ " + selected_task)
    except:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

# Title label
title_label = tk.Label(root, text="To-Do List", font=("Arial", 18, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# Entry box
task_entry = tk.Entry(root, width=30, font=("Arial", 14))
task_entry.pack(pady=10)

# Add button
add_button = tk.Button(root, text="Add Task", width=15, bg="#4CAF50", fg="white", command=add_task)
add_button.pack(pady=5)

# Listbox to show tasks
listbox = tk.Listbox(root, width=35, height=12, font=("Arial", 12))
listbox.pack(pady=10)

# Complete button
complete_button = tk.Button(root, text="Mark Completed", width=15, bg="#2196F3", fg="white", command=mark_completed)
complete_button.pack(pady=5)

# Delete button
delete_button = tk.Button(root, text="Delete Task", width=15, bg="#f44336", fg="white", command=delete_task)
delete_button.pack(pady=5)

# Run the app
root.mainloop()
