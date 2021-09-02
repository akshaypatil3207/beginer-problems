a=int(input()) # no of tanks
tank_level=[]
leak_rate=[]
out=[]
for i in range(a):
    tank_level.append(int(input()))
    leak_rate.append(int(input()))
    out.append(tank_level[i]/leak_rate[i])
for i in range(a):
    b=0
    for j in range(a):
        if out[i]<=out[j] and j!=i:
            b=b+1
        if b==(a-1):
            least=out[i]
            break
final=[]
for i in range(a):
    if out[i]==least:
        final.append(i)
print(*final, sep = ", ") 
    
    
    
