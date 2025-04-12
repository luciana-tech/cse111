import tkinter as tk
from tkinter import ttk, messagebox
from expense_tracker import (
    add_expense, add_saving, view_expenses, view_savings, total_by_category,
    CATEGORIES
)

# ------------------- GUI Setup -------------------
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("600x600")
root.configure(padx=20, pady=20)

# ------------------- Labels & Inputs -------------------
tk.Label(root, text="Date (YYYY-MM-DD):", font=('Arial', 12)).grid(row=0, column=0, sticky="w")
date_entry = tk.Entry(root, font=('Arial', 12), width=30)
date_entry.grid(row=0, column=1)

tk.Label(root, text="Amount:", font=('Arial', 12)).grid(row=1, column=0, sticky="w")
amount_entry = tk.Entry(root, font=('Arial', 12), width=30)
amount_entry.grid(row=1, column=1)

tk.Label(root, text="Description:", font=('Arial', 12)).grid(row=2, column=0, sticky="w")
desc_entry = tk.Entry(root, font=('Arial', 12), width=30)
desc_entry.grid(row=2, column=1)

tk.Label(root, text="Category:", font=('Arial', 12)).grid(row=3, column=0, sticky="w")
category_var = tk.StringVar()
category_dropdown = ttk.Combobox(root, textvariable=category_var, values=CATEGORIES, font=('Arial', 12), width=28)
category_dropdown.grid(row=3, column=1)

# ------------------- Output Display -------------------
output_box = tk.Text(root, height=15, width=70, font=('Consolas', 10))
output_box.grid(row=7, column=0, columnspan=2, pady=20)

def show_message(text):
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, text)

# ------------------- Button Functions -------------------
def handle_add_expense():
    try:
        data = date_entry.get()
        amt = float(amount_entry.get())
        desc = desc_entry.get()
        cat = category_var.get()
        expense = add_expense(data, cat, amt, desc)
        show_message(f"✅ Expense added:\n{expense}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def handle_add_saving():
    try:
        data = date_entry.get()
        amt = float(amount_entry.get())
        desc = desc_entry.get()
        saving = add_saving(data, amt, desc)
        show_message(f"💰 Saving added:\n{saving}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def handle_view_expenses():
    data = view_expenses()
    if not data:
        show_message("No expenses yet.")
    else:
        show_message("\n".join(str(d) for d in data))

def handle_view_savings():
    result = view_savings()
    show_message(f"💸 Total Saved: {result['total_saved']}\n\nEntries:\n" + "\n".join(str(s) for s in result["entries"]))

def handle_total_by_category():
    cat = category_var.get()
    if not cat:
        messagebox.showinfo("Info", "Please select a category")
        return
    total = total_by_category(cat)
    show_message(f"📊 Total for '{cat}': {total['total']} in {total['count']} entries")

# ------------------- Buttons -------------------
btn_font = ('Arial', 12)

tk.Button(root, text="Add Expense", command=handle_add_expense, font=btn_font, width=20).grid(row=4, column=0, pady=10)
tk.Button(root, text="Add Saving", command=handle_add_saving, font=btn_font, width=20).grid(row=4, column=1, pady=10)
tk.Button(root, text="View Expenses", command=handle_view_expenses, font=btn_font, width=20).grid(row=5, column=0, pady=10)
tk.Button(root, text="View Savings", command=handle_view_savings, font=btn_font, width=20).grid(row=5, column=1, pady=10)
tk.Button(root, text="Total by Category", command=handle_total_by_category, font=btn_font, width=43).grid(row=6, column=0, columnspan=2)


root.mainloop()