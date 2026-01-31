import mysql.connector as myconn

mydb=myconn.connect(
    host="localhost",
    user="root",
    password="A@y@n#786",
    database="product"
)
db_cursor=mydb.cursor()


def product_order():
    
    orderid=int(input("Enter order id :"))
    productname=input("Enter product name :")
    productprice=int(input("Enter product Price :"))
    productQuantity=int(input("Enter Quantity :"))
    
    totalamount=productprice*productQuantity
    
    db_insert=("insert into orders (order_id,product_name,product_price,Quantity,total_amount) values (%s,%s,%s,%s,%s)")
    db_list=(orderid,productname,productprice,productQuantity,totalamount)
    db_cursor.execute(db_insert,db_list)
    mydb.commit()
    
    od=str(orderid)
    na=str(productname)
    pr=str(productprice)
    q=str(productQuantity)
    t=str(totalamount)
    all=str(od+" "+na+" "+pr+" "+q+" "+t)
    
    
    x=open(od,"a")
    
    z=x.write(all)
    


    x.close()
    
    print ("product added Successfull....")

product_order() 


 
    