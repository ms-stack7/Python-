def read_furniture_data(filename):
    furniture = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                details = line.strip().split(', ')
                furniture.append({
                    'id': details[0],
                    'manufacturer': details[1],
                    'product_name': details[2],
                    'quantity': int(details[3]),
                    'price': float(details[4].replace('$', ''))
                })
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    return furniture
