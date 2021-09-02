#Take m ie rows in class and n ie columns in class

#form M by n matrix

#enter 1 for boy and 0 for girl as per sitting arrangement

#print no of unique rows ignore same arrangement rows

arr=[]
out=[]
m=int(input("enter no of rows:- "))
n=int(input("enter no of columns:- "))
for i in range(m):
    arr.append(list(input("Enter no {} row sequence without space:- ".format(i)).strip()))
for i in range(m):
    a=0
    for j in range(m):          #finding unique rows
        if arr[i]!=arr[j]:
            a+=1
        if a==(m-1):
            out.append(i)
out.pop(len(out)-1)
print("Unique row is/are :- ")
print(*out , sep=" , ")
