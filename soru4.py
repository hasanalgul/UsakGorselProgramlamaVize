sayac=0
for i in range(100,999):
    q=str(i)[0]
    w=str(i)[1]
    e=str(i)[2]

    if q!=w and q!=e and w!=e:
        sayac = sayac+1
        print(i)

print("Tekrar etmeyen sayı toplamı = "+str(sayac))
