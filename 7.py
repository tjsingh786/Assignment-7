#Q1.
dicti={}
n=int(input("Enter number of items: "))
for x in range(n):
    key=input("Enter key ")
    value=input("Enter value ")
    dicti[key]=value
print(dicti)
val=input("Enter value to find")
for y,z in dicti.items():
    if(z==val):
        print("Key of value",val,"is",y)

#Q2.
a={}
n=int(input("Enter number of items: "))
for x in range(n):
    name=input("Enter name ")
    b={}
    marks1=int(input("Enter marks in English "))
    marks2=int(input("Enter marks in science "))
    marks3=int(input("Enter marks in maths "))
    b['English']=marks1
    b['maths']=marks2
    b['science']=marks3
    a[name]=b
print(a)
s=input("Enter name of student :")
print(a[s])
