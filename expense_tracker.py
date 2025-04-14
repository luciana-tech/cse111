# This program is an expense tracker

import csv
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt

CATEGORIES = [
    "entertainment",
    "transportation",
    "food",
    "groceries",
    "gifts",
    "debt repayment",
    "housing"
]

expenses = []
budgets = {}
savings = []
goals = {}

# Add saving entry
def add_saving(date, amount, description=""):
    saving = {
        "id": len(savings) + 1,
        "date": date,
        "amount": amount,
        "description": description
    }
    savings.append(saving)
    return saving

# View saving amount
def view_savings():
    total_saved = sum(s["amount"] for s in savings)
    return {"total_saved": total_saved, "entries": savings}

# Add expenses
def add_expense(date, category, amount, description=""):
    if category.lower() not in [c.lower() for c in CATEGORIES]:
        raise ValueError(f"Invalid category: {category}. Must be one of {CATEGORIES}")
    
    expense = {
        "id": len(expenses) + 1,
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }
    expenses.append(expense)
    return expense

# Edit expense
def update_expense(expense_id, date=None, category=None, amount=None, description=None):
    for expense in expenses:
        if expense["id"] == expense_id:
            if date: expense["date"] = date
            if category: expense["category"] = category
            if amount is not None: expense["amount"] = amount
            if description is not None: expense["description"] = description
            return expense
    return None

# Delete expense
def delete_expense(expense_id):
    global expenses
    for i, expense in enumerate(expenses):
        if expense["id"] == expense_id:
            deleted = expenses.pop(i)
            return deleted
    return None

# View expenses
def view_expenses():
    return expenses

# View summary of all expenses
def summary():
    total = sum(exp["amount"] for exp in expenses)
    return {"total_expense": total, "count": len(expenses)}

# Monthly summary by category
def monthly_summary(month, year):
    monthly_expenses = [exp for exp in expenses if
                        datetime.strptime(exp["date"], "%Y-%m-%d").month == month and
                        datetime.strptime(exp["date"], "%Y-%m-%d").year == year]
    summary_by_category = defaultdict(float)
    for exp in monthly_expenses:
        summary_by_category[exp["category"]] += exp["amount"]
    return dict(summary_by_category)

# Set budget using month and year
def set_budget(month, year, amount):
    key = f"{year}-{month:02d}"
    budgets[key] = amount
    return {key: amount}

# Check remaining budget and inform status
def check_budget(month, year):
    key = f"{year}-{month:02d}"
    if key not in budgets:
        return f"⚠️ No budget set for {key}"
    
    monthly_total = sum(
        exp["amount"] for exp in expenses
        if datetime.strptime(exp["date"], "%Y-%m-%d").month == month and
           datetime.strptime(exp["date"], "%Y-%m-%d").year == year
    )
    budget = budgets[key]
    remaining = budget - monthly_total

    status = f"💵 Budget for {key}: ${budget:.2f}\n"
    status += f"🧾 Spent: ${monthly_total:.2f} | Remaining: ${remaining:.2f}\n"

    return status

# Export expenses to CSV
def export_to_csv(file_path):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["id", "date", "category", "amount", "description"])
        writer.writeheader()
        for exp in expenses:
            writer.writerow(exp)
    return file_path

# Filter expenses by category
def filter_expenses_by_category(category):
    return [exp for exp in expenses if exp["category"].lower() == category.lower()]

# General expense filter by category/month/year
def filter_expenses(category=None, month=None, year=None):
    filtered = expenses
    if category:
        filtered = [exp for exp in filtered if exp["category"].lower() == category.lower()]
    if month and year:
        filtered = [
            exp for exp in filtered
            if datetime.strptime(exp["date"], "%Y-%m-%d").month == month and
               datetime.strptime(exp["date"], "%Y-%m-%d").year == year
        ]
    return filtered

# Total by category
def total_by_category(category):
    filtered = filter_expenses_by_category(category)
    total = sum(exp["amount"] for exp in filtered)
    return {"category": category, "total": total, "count": len(filtered)}

# Set a monthly financial goal 
def set_monthly_goal(month: str, goal_description: str):
    goals[month] = goal_description
    return f"🎯 Monthly goal set for {month}: {goal_description}"

# Get the monthly goal (if set)
def get_monthly_goal(month: str):
    return goals.get(month, "No goal set for this month.")