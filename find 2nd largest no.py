


#Three numbers A, B and C are the inputs. Write a program to find second largest among them.

#Input
#The first line contains an integer T, the total number of testcases. Then T lines follow, each line contains three integers A, B and C.

#Output
#For each test case, display the second largest among A, B and C, in a new line.

#Constraints
#1 ≤ T ≤ 1000
#1 ≤ A,B,C ≤ 1000000
#Example
#Input
#3 
#120 11 400
#10213 312 10
#10 3 450

#Output

#120
#312
#10

for i in  range(int(input())):
    
    nos = list(map(int, input().strip().split()))
    nos.sort()
    #nos=input().split()
    #for i in range(3):
        #for j in range(i+1,3):
            #least=int(nos[i])
            #b=int(nos[j])
            #if least>b:
               # nos[i]=b
               # nos[j]=least
                
                
    print(nos[1])
