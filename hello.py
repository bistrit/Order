a= (input("How many number you want to add? "))
all=[]
order=[]
n=0
s=1
for i in range(0, int(a)):
    num = (input("Enter yout number: "))
  
    all.append(num)
w=len(all)
lo=0
while lo!=(w+1):
    z=""
    n=0
    lenght=len(all)
    for i in range(0,lenght):
        for j in range(0,lenght):
            if j==(lenght-1) and int(all[j])/int(all[i])<1:
                n=all[i]
                s=n
            elif i==j:
                continue       
            elif int(all[j])/int(all[i])<1:
                continue
            elif int(all[j])/int(all[i])>1:
                vj=j
                vi=i
                z=all[i]
                break

    while int(all[vj])/int(all[vi])>1:               
        all.remove(str(z))
        all.append(str(z))
        lo=lo-1
        break

    if int(n)==int(s):
        all.remove(str(n))
        order.append(str(n))
    if len(all)==1:
        order.append(all[0])
        break
        
    lo=lo+1
print("Descending order of given number is :- "+ str(order))
