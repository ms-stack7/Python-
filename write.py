# write.py

# Import the datetime module to get the current date and time
from datetime import datetime


# Function to generate the header of an invoice
def generate_invoice_header(invoice_type):

# Return a formatted string with the invoice type and current date
    return (
        f"{'-'*40}\n"
        f"{invoice_type} Invoice\n"
        f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"{'-'*40}\n"
    )


# Function to generate the body of an invoice.
def generate_invoice_body(invoice_details, customer_name=None, employee_name=None):
    body = ""
    
    if customer_name:
        body += f"Customer Name: {customer_name}\n"
    if employee_name:
        body += f"Employee Name: {employee_name}\n"
    
    body += (
        f"{'-'*40}\n"
        f"{'ID':<5} {'Product Name':<20} {'Qty':<5} {'Price':<10} {'Total':<10}\n"
        f"{'-'*40}\n"
    )

    # Iterate over the invoice details and add each item to the body
    for item in invoice_details:
        body += (
            f"{item['id']:<5} {item['product_name']:<20} {item['quantity']:<5} "
            f"${item['price']:<10.2f} ${item['subtotal']:<10.2f}\n"
        )
    
    return body


# Function to generate the footer of an invoice
def generate_invoice_footer(subtotal, vat, shipping, total):
    
    return (
        f"{'-'*40}\n"
        f"Subtotal: ${subtotal:.2f}\n"
        f"VAT (13%): ${vat:.2f}\n"
        f"Shipping: ${shipping:.2f}\n"
        f"{'-'*40}\n"
        f"Total Amount: ${total:.2f}\n"
        f"{'-'*40}\n"
    )

def write_invoice(invoice_details, filename, customer_name=None, employee_name=None, invoice_type="Sales"):
    try:
    # Calculate the subtotal, VAT, shipping, and total
        subtotal = sum(item['subtotal'] for item in invoice_details)
        vat = subtotal * 0.13
        shipping = 50.00  # Fixed shipping cost
        total = subtotal + vat + shipping

     # Open the file in append mode and write the invoice
        with open(filename, 'a') as file:
            file.write(generate_invoice_header(invoice_type))
            file.write(generate_invoice_body(invoice_details, customer_name, employee_name))
            file.write(generate_invoice_footer(subtotal, vat, shipping, total))
            file.write("\n")
            
        print(f"Invoice generated and saved as {filename}.")
        
    except IOError as e:
        print(f"Error writing to file: {e}")

def write_purchase_invoice(invoice_details, filename, employee_name=None):
    write_invoice(invoice_details, filename, employee_name=employee_name, invoice_type="Purchase")
