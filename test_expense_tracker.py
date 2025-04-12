import pytest
from expense_tracker import (
    add_expense, delete_expense, view_expenses,
    total_by_category, add_saving, view_savings
)

def test_add_expense():
    expense = add_expense("2025-04-01", "food", 25.0, "Lunch at cafe")
    assert expense["amount"] == 25.0
    assert expense["category"].lower() == "food"

def test_delete_expense():
    expense = add_expense("2025-04-02", "transportation", 15.0, "Bus ticket")
    deleted = delete_expense(expense["id"])
    assert deleted["id"] == expense["id"]

def test_view_expenses():
    add_expense("2025-04-03", "entertainment", 50.0, "Movie night")
    result = view_expenses()
    assert isinstance(result, list)
    assert len(result) > 0

def test_total_by_category():
    add_expense("2025-04-04", "groceries", 30.0, "Weekly shopping")
    result = total_by_category("groceries")
    assert result["category"] == "groceries"
    assert result["total"] >= 30.0

def test_add_saving():
    saving = add_saving("2025-04-05", 100.0, "Paycheck saving")
    assert saving["amount"] == 100.0

def test_view_savings():
    result = view_savings()
    assert "total_saved" in result
    assert "entries" in result
    assert isinstance(result["entries"], list)
