#import re
#file=open("input.txt","r")
#bune=0
#for line in file:
#    nou=re.split("[-: \n]",line, 3)
#    nr_apar=0
#    for x in nou[3]:
#        if x==nou[2]:
#            nr_apar+=1
#    if int(nou[0])<=nr_apar and nr_apar<=int(nou[1]):
#        bune+=1
#print(bune)
import re
file=open("input.txt","r")
bune=0
for line in file:
    nou=re.split("[-: \n]",line, 3)
    if (nou[3][int(nou[0])]==nou[2] and nou[3][int(nou[1])]!=nou[2])or (nou[3][int(nou[0])]!=nou[2] and nou[3][int(nou[1])]==nou[2]):
        bune+=1
print(bune)