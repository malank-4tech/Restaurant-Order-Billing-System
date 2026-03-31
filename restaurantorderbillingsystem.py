# Restaurant Order Billing System
# Pure Python - No database, No files

menu = []     # Stores menu items temporarily
orders = []   # Stores customer orders temporarily

GST = 0.05     # 5% GST

def add_item():
    print("\n--- Add Item to Menu ---")
    name = input("Enter item name: ").strip()
    price = float(input("Enter price (₹): "))
    menu.append({"name": name, "price": price})
    print("Item added successfully!\n")

def show_menu():
    print("\n--- Restaurant Menu ---")
    if not menu:
        print("Menu is empty!\n")
        return
    for i, item in enumerate(menu, start=1):
        print(f"{i}. {item['name']} - ₹{item['price']:.2f}")
    print()

def place_order():
    print("\n--- Place Order ---")
    if not menu:
        print("Menu is empty! Add items first.\n")
        return

    show_menu()
    choice = int(input("Enter menu item number: "))
    if choice < 1 or choice > len(menu):
        print("Invalid choice!\n")
        return

    qty = int(input("Enter quantity: "))
    orders.append({
        "name": menu[choice - 1]["name"],
        "price": menu[choice - 1]["price"],
        "qty": qty
    })
    print("Order item added!\n")

def generate_bill():
    print("\n========== RESTAURANT BILL ==========")

    if not orders:
        print("No items ordered!\n")
        return

    subtotal = 0
    for item in orders:
        line_total = item["price"] * item["qty"]
        subtotal += line_total
        print(f"{item['name'][:20]:20s} x {item['qty']} = ₹{line_total:.2f}")

    gst_amount = subtotal * GST

    # 🔥 Ask user how much % discount
    try:
        discount_percent = float(input("Enter discount percentage (0 if none): "))
    except ValueError:
        discount_percent = 0

    discount = subtotal * (discount_percent / 100)

    net_total = subtotal + gst_amount - discount

    print("-------------------------------------")
    print(f"Subtotal: ₹{subtotal:.2f}")
    print(f"GST 5% : ₹{gst_amount:.2f}")
    print(f"Discount {discount_percent:.0f}%: ₹{discount:.2f}")
    print(f"TOTAL: ₹{net_total:.2f}")
    print("=====================================\n")

def main():
    while True:
        print("""
====== Restaurant Billing System ======
1. Add Menu Item
2. Show Menu
3. Place Order
4. Generate Bill
5. Exit
""")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            show_menu()
        elif choice == "3":
            place_order()
        elif choice == "4":
            generate_bill()
        elif choice == "5":
            print("Thank you! Visit again 😊")
            break
        else:
            print("Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()
