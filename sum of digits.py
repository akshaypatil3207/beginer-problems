#You're given an integer N. Write a program to calculate the sum of all the digits of N.

#Input
#The first line contains an integer T, the total number of testcases. Then follow T lines, each line contains an integer N.

#Output
#For each test case, calculate the sum of digits of N, and display it in a new line.

#Constraints
#1 ≤ T ≤ 1000
#1 ≤ N ≤ 1000000
#Example
#Input
#3 
#12345
#31203
#2123
#Output
#15
#9
#8

nos=[]
for i in range(int(input())):
    nos.append(int(input()))
a=len(nos)
for i in range(a):
    for j in range(i+1,a):
        least=nos[i]
        if least>nos[j]:
            nos[i]=nos[j]
            nos[j]=least
for i in nos:
    print(i)
