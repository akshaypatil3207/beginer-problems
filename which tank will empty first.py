a=int(input("Enter the no of tanks:- ")) # no of tanks
tank_level=[]
leak_rate=[]
out=[]
for i in range(a):
    tank_level.append(int(input("Enter tank level of no {} tank :- ".format(i))))
    leak_rate.append(int(input("Enter leak rate of no {} tank:- ".format(i))))
    out.append(tank_level[i]/leak_rate[i])                                        #calculating deciding factor
for i in range(a):
    b=0
    for j in range(a):                                                             #finding leat deciding factor
        if out[i]<=out[j] and j!=i:
            b=b+1
        if b==(a-1):
            least=out[i]
            break
final=[]
for i in range(a):                             #printing tank number which will empty first, 
    if out[i]==least:                          #if two tanks are empting together then print both tank nos in ascending order seperated by comma
        final.append(i)
print("These tank will empty first/together")
print(*final, sep = ", ") 
    
    
    

    
    
    
