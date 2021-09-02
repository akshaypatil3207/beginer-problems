#You are asked to calculate factorials of some small positive integers.

#Input
#An integer t, 1<=t<=100, denoting the number of testcases, followed by t lines, each containing a single integer n, 1<=n<=100.

#Output
#For each integer n given at input, display a line with the value of n!

#Example
#Sample input:
#4
#2
#5
#3
#Sample output:

#1
#2
#120
#6

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
