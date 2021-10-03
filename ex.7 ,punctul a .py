a=[['0000','0000','0000','0011'],
['0001','0001','0001','0100'],
['0010','0011','0010','0101'],
['0011','0010','0011','0110'],
['0100','0110','0100','0111'],
['0101','0111','1011','1000'],
['0110','0101','1100','1001'],
['0111','0100','1101','1010'],
['1000','1100','1110','1011'],
['1001','1101','1111','1100']]
print("0=Direct , 1=Gray ,2=Aiken ,3=Exces 3")
i=int(input("Dati numarul comform schemei="))
n=int(input("Dati numarul de numere care trebuie codificate = "))
j=[]
for b in range (0,n):
        z=int(input("Dati numerele ="))
        j.append(z)
for c in range(0,len(j)):
    print(a[j[c]][i])
