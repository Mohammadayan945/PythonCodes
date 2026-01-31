def forup():
    a=input("Enter paragraph :")
    # b=a.islower()
    if a.islower():
        y=a.upper()
        print( y)
    else:
       print("All ready in Upper Case...") 
       

def forlow():
    x=input("Enter paragraph :")
    # b=a.islower()
    if x.isupper():
        b=x.lower()
        print( b)
    else:
       print("All ready in lower Case...") 

def check():
    a=input("Enter your para :")
    b=input("Enter your string :")
    if b in a:
        print(a.index(b))
    else:
        print("invalid!!")    