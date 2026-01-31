import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="A@y@n#786",
    database="store"
)

cursor = mydb.cursor()

def product_order():
    # Take input from user
    order_id = int(input("Enter Order ID: "))
    product_name = input("Enter Product Name: ")
    price = float(input("Enter Product Price: "))
    quantity = int(input("Enter Product Quantity: "))

    # Calculate total amount
    total_amount = price * quantity

    # Show total to user
    print("Total Amount:", total_amount)

    # Insert data into MySQL table
    sql = """INSERT INTO orders (order_id, product_name, price, quantity, total_amount) VALUES (%s, %s, %s, %s, %s)"""

    values = (order_id, product_name, price, quantity, total_amount)

    cursor.execute(sql, values)
    mydb.commit()

    print("Data inserted successfully into database!")
    
product_order()    
