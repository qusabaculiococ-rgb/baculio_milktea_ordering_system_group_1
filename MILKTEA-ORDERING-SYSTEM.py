def main():
    print("=== MILK TEA ORDERING SYSTEM ===")
    total = 0

    while True:
        print("\n1. Classic Milk Tea - ₱80")
        print("2. Okinawa Milk Tea - ₱90")
        print("3. Wintermelon Milk Tea - ₱85")
        print("4. Chocolate Milk Tea - ₱95")

        choice = input("Choose your drink (1-4): ")

        if choice == "1":
            drink, price = "Classic Milk Tea", 80
        elif choice == "2":
            drink, price = "Okinawa Milk Tea", 90
        elif choice == "3":
            drink, price = "Wintermelon Milk Tea", 85
        elif choice == "4":
            drink, price = "Chocolate Milk Tea", 95
        else:
            print("Invalid choice.")
            continue

        print("\nSizes: 1.Small  2.Medium(+₱10)  3.Large(+₱20)")
        size = input("Choose size (1-3): ")

        if size == "2":
            price += 10
            size_name = "Medium"
        elif size == "3":
            price += 20
            size_name = "Large"
        else:
            size_name = "Small"

        sugar = input("Enter sugar level (0-100%): ") or "50"
        pearls = input("Add pearls for ₱10? (yes/no): ").lower()
        if pearls == "yes":
            price += 10

        total += price

        another = input("Do you want to add another milk tea? (yes/no): ").lower()
        if another != "yes":
            print("\n--- RECEIPT ---")
            print(f"Drink: {drink}")
            print(f"Size: {size_name}")
            print(f"Sugar Level: {sugar}%")
            if pearls == "yes":
                print("Topping: Pearls")
            print(f"Total Amount: ₱{total}")
            print("Thank you for ordering! 🧋")
            break

if __name__ == "__main__":
    main()
    