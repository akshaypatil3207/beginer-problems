# given is the no of students in the school and the no of chocolets available
#find the number of additional chocolates required for equally distributing the chocolates among the students.

a=int(input("enter prople:- " ))
b=int(input("enter chocolates :- "))
for i in range(1,b):
    if a*i>=b:
        print("additional chocolates required are :- {} ".format(a*i-b))
        break
