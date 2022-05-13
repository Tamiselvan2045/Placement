n=list(map(str,input().split()))
max_str_len=0
for i in n:
    max_str_len=max(max_str_len,len(i))
    output=[]
    for i in range(max_str_len):
        for word in n:
            if i>len(word)-1:
                output.append("*")
            else:
                output.append(word[i])
        output+=" "
length=len(output)
for i in range(length):
    if output[-1]=="*" or output[-1]==" ":
        output.pop()
    else:
        break
print(("").join(output))
