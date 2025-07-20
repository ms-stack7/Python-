# operations.py

# importing necessary modules
import read
import write


#Defining constants for VAT rate and shipping cost.
Vat_rate = 0.13
Shipping_cost = 50.00

def update_stock(furniture, item_id, quantity, operation):
    for item in furniture:
        if item['id'] == item_id:
            if operation == 'sell':
                item['quantity'] -= quantity
            elif operation == 'buy':
                item['quantity'] += quantity
            return item
    return None

def calculate_invoice(items):
    invoice = []
    for item in items:
        subtotal = item['price'] * item['quantity']
        invoice.append({
            'id': item['id'],
            'product_name': item['product_name'],
            'quantity': item['quantity'],
            'price': item['price'],
            'subtotal': subtotal
        })

# Calculate the total cost
    total = sum(item['subtotal'] for item in invoice)
    total_with_vat = total + (total * Vat_rate)
    grand_total = total_with_vat + Shipping_cost
    return invoice, grand_total
