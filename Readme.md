# 🍽️ Restaurant Order Billing System — Python

A simple, terminal-based billing program written in **pure Python.
It allows restaurant staff to add menu items, take customer orders, and generate final bills including GST and discount.
This system uses only basic Python concepts and **does not use any database, JSON, or GUI**.

---

## 🔹 Project Title

**Restaurant Order Billing System — Python**

---

## 🔹 Overview of the Project ■

This project automates the restaurant billing operation using a very user-friendly command-line interface.
It allows the user to add menu items, place orders, and view an instant total restaurant bill with subtotal, GST, discount, and final total.

---

## 🔹 Features
- Add food items to menu
- View menu with price details
- Order multiple items
- Auto calculate:
- Subtotal
- GST (5%)
- Discount (%) entered by the user
- Final amount
- Lightweight and fast. No storage or database.

---

## 🔹 Technologies / Tools Used
| Component | Description |
|----------|---------|
| Language | Python 3 |
| Runtime | Terminal / Command Prompt |
| Concepts Used | Functions, Lists, Loops, Conditionals, Arithmetic operations |

---

## 🔹 Steps to Install & Run the Project
1. Install **Python 3** on your system
2. Create a file called `main.py` 
3. Copy and paste the source code of this program into main.py 
4. Open Command Prompt / Terminal in the project folder 
5. Execute the program: 
    python main.py

 ---

## 🔹 Instructions for Testing

Follow the steps below to verify that the Restaurant Order Billing System works correctly:

| Test Step | Expected Output |
|----------|-----------------|
| Add menu item | Item should appear in the menu list with correct price |
| Show menu | All added items should display properly |
| Place order | Selected item and quantity should be added to the order list |
| Enter discount percentage | Bill total should reduce according to the discount applied |
| Generate bill | Subtotal, GST (5%), discount, and final payable total should be displayed |
| Order multiple items | Bill should include individual line totals for each item |

### Additional recommended tests
- Try **0% discount** — total should remain unchanged
- Try **10% / 20% / 50% discount** — total should reduce accordingly
- Try **ordering the same item multiple times**
- Try **large quantities** (e.g., 10 or more)
- Try generating the bill **only after placing an order** (system should warn if nothing is ordered)

If all of the above tests produce correct results, the project is functioning properly.