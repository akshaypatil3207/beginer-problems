out=[]
prev_index=0
#a=0
word=input()
done=" "
inde=[]
j=0
while True:
    if word[j] in done:
        #a=j-prev_index
        out.append(len(done)-1)
        print(done)
        prev_index=inde[done.index(word[j])]
        j=prev_index-1
        done=" "
        inde=[] 
    else:
        done=done+word[j]
        inde.append(j)
        
    j+=1
    if j==(len(word)-1):
        out.append(len(done))
        break
out.sort()    
print(out[len(out)-1])


