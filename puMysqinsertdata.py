import mysql.connector as myconn

mydb=myconn.connect(
    host="localhost",
    user="root",
    password="A@y@n#786",
    database="pubg"
)
x=eval(input("Enter your Query : "))
y=eval(input("Enter your data : "))
db_cursor=mydb.cursor()

# db_insert="insert into record (id,name,marks) values (%s,%s,%s)"
# db_list=[(1,"Ayan",60),(1,"farhan",20),(1,"sameer",00)]

db_insert=x
db_list=y
db_cursor.executemany(db_insert,db_list)
mydb.commit()
print("....data inserted ....")