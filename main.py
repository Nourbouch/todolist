#!/usr/bin/env python3
from tkinter import messagebox, simpledialog
import tkinter as tk
import io
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

todos = []

def add_todo():
    todo = simpledialog.askstring("Add TODO", "Enter TODO:")
    if todo:
        todos.append(todo)
        update_todo_list()
    else:
        messagebox.showwarning("Warning", "TODO cannot be empty.")

def delete_todo():
    try:
        todo_id = int(simpledialog.askstring("Delete TODO", "Enter the ID of the TODO to delete:")) - 1
        if 0 <= todo_id < len(todos):
            del todos[todo_id]
            update_todo_list()
        else:
            messagebox.showwarning("Warning", "Invalid ID.")
    except ValueError:
        messagebox.showwarning("Warning", "Invalid input. Please enter a valid ID.")

def print_todos():
    if len(todos) <= 1:
        messagebox.showwarning("Warning", "Not enough TODOs to generate a PDF.")
        return

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    data = [['ID', 'TODO']] + [[str(idx + 1), todo] for idx, todo in enumerate(todos)]

    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(table)
    doc.build(elements)
    buffer.seek(0)

    with open("todos.pdf", "wb") as f:
        f.write(buffer.getvalue())
    
    messagebox.showinfo("Info", "TODOs have been printed to todos.pdf")

def update_todo_list():
    todo_list.delete(0, tk.END)
    for idx, todo in enumerate(todos, start=1):
        todo_list.insert(tk.END, f"{idx}. {todo}")

def main():
    global root, todo_list

    root = tk.Tk()
    root.title("TODO List Manager")
    root.geometry("400x400")
    root.configure(bg="#222")

    title_label = tk.Label(root, text="TODO List Manager", bg="#222", fg="#fff", font=("Arial", 16))
    title_label.pack(pady=20)

    button_frame = tk.Frame(root, bg="#222")
    button_frame.pack(pady=10)

    add_button = tk.Button(button_frame, text="Add TODO", command=add_todo, bg="#ff6347", fg="#fff", font=("Arial", 12))
    add_button.grid(row=0, column=0, padx=10)

    delete_button = tk.Button(button_frame, text="Delete TODO", command=delete_todo, bg="#ff6347", fg="#fff", font=("Arial", 12))
    delete_button.grid(row=0, column=1, padx=10)

    print_button = tk.Button(button_frame, text="Print TODOs to PDF", command=print_todos, bg="#32cd32", fg="#fff", font=("Arial", 12))
    print_button.grid(row=0, column=2, padx=10)

    todo_list_frame = tk.Frame(root, bg="#222")
    todo_list_frame.pack(pady=10)

    scrollbar = tk.Scrollbar(todo_list_frame, orient="vertical")
    scrollbar.pack(side="right", fill="y")

    todo_list = tk.Listbox(todo_list_frame, bg="#333", fg="#fff", font=("Arial", 12), yscrollcommand=scrollbar.set, width=50, height=15)
    todo_list.pack(side="left", fill="both")

    scrollbar.config(command=todo_list.yview)

    root.mainloop()

if __name__ == "__main__":
    main()
