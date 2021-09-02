#Given an Integer N, write a program to reverse it.

#Input
#The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer N.

#Output
#For each test case, display the reverse of the given number N, in a new line.

#Constraints
#1 ≤ T ≤ 1000
#1 ≤ N ≤ 1000000
#Example
#Input
#4
#12345
#31203
#2123
#2300
#Output
#54321
#30213
#3212
#32

for i in range(int(input())):
    a=input()
    b=""
    for i in range(len(a)-1,-1,-1):
        
        b=b+a[i]
    print(b.lstrip("0"))
