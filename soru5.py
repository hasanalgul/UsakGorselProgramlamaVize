komut = input("Değer giriniz : ")

komutlar = komut.split("\\n")

def sinyal(deger):
    deger=int(deger)
    if (deger>=0 and deger<=50):
        return "Çok zayıf sinyal"
    elif (deger>=51 and deger<=100):
        return "Zayıf sinyal"
    elif (deger>=101 and deger<=150):
        return "Orta Sinyal"
    elif (deger>= 151 and deger<=200):
        return "Güçlü Sinyal"
    elif (deger>=201 and deger<=205):
        return "Çok güçlü sinyal"

def cihaz(deger):
    deger=int(deger)
    if deger==1:
        return "Televizyon"
    elif deger==2:
        return "Çamaşır makinesi"
    elif deger==3:
        return "buzdolabı"
    elif deger==4:
        return "Fırın"
    else:
        return "Geçersiz"

def durum(deger):
    deger=int(deger)
    if deger==0:
        return "Off"
    elif deger==1:
        return "On"
    else:
        return "Geçersiz"

def cevap(deger):
    deger=int(deger)
    if deger==0:
        return "Cevap istenmiyor"
    elif deger==1:
        return "Cevap isteniyor"
    else:
        return "Geçersiz"

for kod in range(len(komutlar)-1):
    parametre=komutlar[kod].split('-')

    if (parametre[0]=="send"):
        if len(parametre) == 5:
            if (sinyal(parametre[1])=="Geçersiz"):
                print("ikinci bolum hatali")
            elif (cihaz(parametre[2])=="Geçersiz"):
                print("ucuncu bolum hatali")
            elif (durum(parametre[3])=="Geçersiz"):
                print("dorduncu bolum hatali")
            elif (cevap(parametre[4])=="Geçersiz"):
                print("besinci bolum hatali")
            else:
                print("Kod Tipi : send - Giden")
                print("Sinyal Gücü : "+parametre[1] +" - "+sinyal(parametre[1]))
                print("Cihaz : "+parametre[2] + " - "+cihaz(parametre[2]))
                print("Durumu : "+parametre[3] + " - "+durum(parametre[3]))
                print("Cevap : "+parametre[4] + " - "+cevap(parametre[4]))
        else:
            print("İkinci bölüm hatalı")

    elif (parametre[0]=="receive"):
        if len(parametre)==4:
            if (sinyal(parametre[1])=="Geçersiz"):
                print("ikinci bolum hatali")
            elif (cihaz(parametre[2])=="Geçersiz"):
                print("ucuncu bolum hatali")
            elif (durum(parametre[3])=="Geçersiz"):
                print("dorduncu bolum hatali")
            else:
                print("Kod Tipi : receive - Gelen")
                print("Sinyal Gücü : "+parametre[1]+" - "+sinyal(parametre[1]))
                print("Cihaz : "+parametre[2]+" - "+cihaz(parametre[2]))
                print("Durumu : "+parametre[3]+" - "+durum(parametre[3]))
        else:
            print("İkinci bölüm hatalı")
    else:
        print("send ya da receive içermiyor")

    print("-----")