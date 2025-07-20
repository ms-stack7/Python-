# main.py

# Import necessary modules
import read
import write
import operation

def display_furniture(furniture):
    print("Available Furniture:")
    for item in furniture:
        print(f"ID: {item['id']}, Name: {item['product_name']}, Quantity: {item['quantity']}, Price: ${item['price']}")

def main():
    filename = 'stock.txt'
    furniture = read.read_furniture_data(filename)

    while True:
        print("\nOptions:")
        print("1. Display available furniture")
        print("2. Sell furniture")
        print("3. Buy furniture")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_furniture(furniture)

        elif choice == '2':
            item_id = input("Enter the furniture ID to sell: ")
            quantity = int(input("Enter quantity of the product: "))
             # Update the stock and calculate the invoice
            item = operation.update_stock(furniture, item_id, quantity, 'sell')
            if item:
                invoice_details, total = operation.calculate_invoice([item])
                # Write the invoice to a file
                write.write_invoice(invoice_details, 'invoice.txt')
                print(f"Furniture sold! Total: ${total}")
            else:
                print("Item not found or insufficient stock.")

        elif choice == '3':
            # Buy furniture
            item_id = input("Enter the furniture ID to buy: ")
            quantity = int(input("Enter quantity of the product: "))
            # Update the stock
            item = operation.update_stock(furniture, item_id, quantity, 'buy')
            if item:
                print(f"Stock updated! New quantity: {item['quantity']}")
            else:
                print("Item not found.")

        elif choice == '4':
            # Exit the program
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":

     # Run the main function
    main()
