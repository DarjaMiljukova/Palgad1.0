from module1 import *
palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","A"]




while True:
    print(inimesed)
    print(palgad)
    menu=int(input("Valik:\n 1-Lisa andmed\n 2-Kustuta andmed\n 3-Suurim palk\n 4-Väiksem palk\n 5-Vordses palgad\n 7-Nimes\n 8-Suur väike\n 9-top3\n 10-Keskmine palk\n 11-Tulumaks\n 12-Sort\n 13-Kustuta "))
    if menu==0:
        break
    elif menu==1:
        inimesed,palgad=Lisa_andmed(inimesed,palgad)
        print(inimesed)
        print(palgad)
    elif menu==2:
        inimesed,palgad=Kustutamine(inimesed,palgad)
    elif menu==3:
        palk,nimi=Suurim_palk(inimesed,palgad)
        print(f"Suurim palk on {palk} {nimi}´l")
    elif menu==4:
        palk,nimi=Väiksem_palk(inimesed,palgad)
        print(f"Väiksem palk on {palk} {nimi}´l")
    elif menu==5:
        inimesed,palgad=Vordses_palgad(inimesed,palgad)
        print(inimesed)
        print(palgad)
    elif menu==7:
        inimesed,palgad=nimes(inimesed,palgad)
    elif menu==8:
        inimesed,palgad=suur_väike(inimesed,palgad)
    elif menu==9:
        inimesed,palgad=top3(inimesed,palgad)
    elif menu==10:
        inimesed,palgad=keskminepalk(inimesed,palgad)
    elif menu==11:
            tulumaks()
    elif menu==12:
        inimesed,palgad=Sorteerimine(inimesed,palgad)
    elif menu==13:
        inimesed,palgad=Kustuta(inimesed,palgad)
        print(inimesed,palgad)


