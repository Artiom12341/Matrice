n=eval(input("Dati matricea patratica="))
s=0
if ((len(n)>=2) and (len(n)<=10)):
    for b in range(0,len(n)):
        s+=n[b][b]
    print("Suma componentelor diagonalei principale=",s)
else:
    print("Vezi conditia!")
s=0
for i in range (0,len(n)):
    for j in range(0,len(n)):
        if i+j==(len(n)-1):
            s+=n[i][j]
print("Suma componentelor diagonalei secundare=",s)
s=0
for i in range (0,len(n)):
    for j in range(0,len(n)):
        if i<j:
            s+=n[i][j]
print("Suma componentelor mai sus de diagonala principala=",s)
s=0
for i in range (0,len(n)):
    for j in range(0,len(n)):
        if i>j:
            s+=n[i][j]
print("Suma componentelor mai jos de diagonala principala=",s)
s=0
for i in range (0,len(n)):
    for j in range(0,len(n)):
        if i+j<(len(n)-1):
            s+=n[i][j]
print("Suma componentelor mai sus de diagonala secundara=",s)
s=0
for i in range (0,len(n)):
    for j in range(0,len(n)):
        if i+j>(len(n)-1):
            s+=n[i][j]
print("Suma componentelor mai jos diagonala secundara=",s)