out=[]
prev_index=0
word=input("Enter the word:- ").strip()                 #taking long string from user
sub_string=" "
imp_index=[]
j=0
print("Sub strings are: -")
while True:                                              #iterating through string
    if word[j] in sub_string:                            #if letter in substring, then note len of substring 
        out.append(len(sub_string)-1)
        print(sub_string)
        prev_index=imp_index[sub_string.index(word[j])]  #start again from the letter next to previous apperence of the repeted letter.
        j=prev_index-1
        sub_string=" "
        imp_index=[] 
    else:                                                 #if letter not in substring then add it to substring 
        sub_string=sub_string+word[j]
        imp_index.append(j)
        
    j+=1
    if j==(len(word)-1):
        out.append(len(sub_string))
        break
out.sort()    
print("Length of longest unique substring is :- {} ".format(out[len(out)-1]))




