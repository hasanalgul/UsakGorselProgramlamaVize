
adres="www.alierbey.com"

for y in range(len(adres)) :
    if (adres[y:]==".com"):
        print("İnternet adresi doğrulandı ")
        break
    if (adres[y:]==".net"):
        print("İnternet adresi doğrulandı")
        break
    if (adres[y:]==".org"):
        print(" İnternet adresi doğrulandı ")
        break
else :
    print('bu bir adres değil')