import pytest
from expense_tracker import (
    add_expense, delete_expense, view_expenses,
    total_by_category, add_saving, view_savings
)

def test_add_expense():
    exp1 = add_expense("2025-04-01", "food", 25.0, "Lunch at cafe")
    exp2 = add_expense("2025-04-02", "food", 35.0, "Dinner")
    assert exp1["amount"] == 25.0
    assert exp2["amount"] == 35.0
    assert exp1["category"].lower() == "food"
    assert exp2["description"] == "Dinner"

def test_delete_expense():
    exp1 = add_expense("2025-04-03", "transportation", 10.0, "Taxi")
    exp2 = add_expense("2025-04-03", "transportation", 5.0, "Bus")
    deleted1 = delete_expense(exp1["id"])
    deleted2 = delete_expense(exp2["id"])
    assert deleted1["id"] == exp1["id"]
    assert deleted2["description"] == "Bus"

def test_view_expenses():
    add_expense("2025-04-04", "entertainment", 20.0, "Concert")
    add_expense("2025-04-05", "entertainment", 30.0, "Game night")
    result = view_expenses()
    assert isinstance(result, list)
    assert any(exp["description"] == "Concert" for exp in result)
    assert any(exp["amount"] == 30.0 for exp in result)

def test_total_by_category():
    add_expense("2025-04-06", "groceries", 40.0, "Fruit")
    add_expense("2025-04-06", "groceries", 60.0, "Vegetables")
    result = total_by_category("groceries")
    assert result["category"].lower() == "groceries"
    assert result["total"] >= 100.0
    assert result["count"] >= 2

def test_add_saving():
    s1 = add_saving("2025-04-07", 200.0, "Freelance work")
    s2 = add_saving("2025-04-08", 150.0, "Gift")
    assert s1["amount"] == 200.0
    assert s2["description"] == "Gift"

def test_view_savings():
    add_saving("2025-04-09", 100.0, "Extra work")
    add_saving("2025-04-10", 50.0, "Coupon refund")
    result = view_savings()
    assert "total_saved" in result
    assert isinstance(result["entries"], list)
    assert result["total_saved"] >= 150.0
    assert any(s["description"] == "Coupon refund" for s in result["entries"])