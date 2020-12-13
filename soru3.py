isim="Usak Universtesi"
ara="ver"

if isim.find(ara)>-1:
    indis = isim.find(ara)
    x=indis-1
    y=indis+len(ara)+1
    print(isim[x:y])