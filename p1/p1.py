file=open("input.txt","r")
nr=[]
for line in file:
    nr.append(int(line.rstrip()))

for i in range(0,len(nr)-2):
    for j in range(i+1,len(nr)-1):
        for k in range(j+1,len(nr)):
            if int(nr[i])+int(nr[j])+ int(nr[k])==2020:
                print( nr[i]*nr[j]*nr[k])
