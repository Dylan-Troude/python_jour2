
#boucle for

n = int(input("entrez un entier supérieur a zéro : "))
for i in range(1,11):
    if(n > 0):
     print(n*i)
    elif(n <= 0):
        print("error")
        break

#boucle while

n = int(input("entrez un entier supérieur a zéro : "))
i = 1
while i <= 10:
    if n <=0:
        print("error")
        break
    else:
        print(n*i)
        i += 1
