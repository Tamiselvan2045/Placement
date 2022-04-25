num=input()
list1=[]
sc="-"," "
for i in num:
    if i not in sc:
        list1.append(i)
    else:
        pass
list3=[]
list4=[]
list5=[]
if len(list1)>4: 
    for i in range(0,3):
        list3=list1[0:3]
        s="".join(list3)
        del list1[0:3]
        list4.append(s)
        if len(list1)==4:
          for i in range(0,2):
            list3=list1[0:2]
            s="".join(list3)
            del list1[0:2]
            list4.append(s)
            if len(list1)==0:
             break
        else:
            pass
    for x in list4:
     if x.strip():
        list5.append(x)
     else:
         pass
    st=""
    for i in list5:
     st+=i+"-"
    a=list(st)
    a.pop()
    e="".join(a)
    print(e)

else:
    st=""
    for i in list1:
        st+=i
    print(st)
    

