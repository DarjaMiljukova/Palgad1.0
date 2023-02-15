
def Lisa_andmed(i:list,p:list):
    """Kirjeldus 
    :param list i:Inimeste järjend
    :param list p: Palgade järjend
    :rtype: list, list
    """
    n=int(input("Mitu inimest:"))
    for j in range(n):
        nimi=input("Sisesta nimi: ")
        palk=int(input("Sisesta palk: "))
        i.append(nimi)
        p.append(palk)
    return i,p

def Kustutamine(i:list,p:list):
    """ Определение индекса человека и удаляние его
    :param list i:Inimeste järjend
    :param list p: Palgade järjend
    :rtype: list, list
    """
    nimi=input("Sisesta nimi: ")
    if nimi in i:
        n=i.count(nimi)
        for j in range(n):
            ind=i.index(nimi)
            i.pop(ind)
            p.pop(ind)
    return i,p 

def Suurim_palk(i:list,p:list):
    """
    :param list i:Inimeste järjend
    :param list p: Palgade järjend
    :rtype: int, str
    """
    palk=max(p)
    ind=p.index(palk)
    nimi=i[ind]
    return palk,nimi

def Väiksem_palk(i:list,p:list):
    """
    :param list i:Inimeste järjend
    :param list p: Palgade järjend
    :rtype: int, str
    """
    palk=min(p)
    ind=p.index(palk)
    nimi=i[ind]
    return palk,nimi

def Sorteerimine(i:list,p:list):
    """
    :param list i:Inimeste järjend
    :param list p: Palgade järjend
    :rtype: int, str
    """
    v=int(input("palk 1-kahaneb, 2-kasvab?"))
    if v==1:
        n=len(p)
        for j in range(0,n-1):
            for k in range(j+1,n):
                if p[j]<p[k]:
                    abi=p[j] 
                    p[j]=p[k] 
                    p[k]=abi
                    abi=i[j] 
                    i[j]=p[k] 
                    i[k]=abi
    elif v==2:
        n=len(p)
        for j in range(0,n-1):
            for k in range(j+1,n):
                if p[j]>p[k]:
                    abi=p[j] 
                    p[j]=p[k] 
                    p[k]=abi
                    abi=i[j] 
                    i[j]=p[k] 
                    i[k]=abi

    return i,p


def suur_väike(i:list,p:list):

    number=int(input("Naita palga number"))
    v=int(input("Kellel palk 1-on suurem,2-on väiksem?"))
    if v==1:
        for g in p:
            if g > number:
                ind=p.index(g)
                print(f"{g}, {i[ind]}")
    if v==2:
        for g in p:
            if g < number:
                ind=p.index(g)
                print(f"{g}, {i[ind]}")
    return i,p

def Vordses_palgad(i:list,p:list):
    """
    :param list i:Inimeste järjend
    :param list p: Palgade järjend
    :rtype: int, str
    """
    dublikatid=[x for x in p if p.count(x)>1 ]
    dublikatid=list(set(dublikatid)) #[1200,2500,750,750,1200]->[1200,750]
    for palk in dublikatid: #1200, n=2; 750, n=2
        n=p.count(palk)
        k=-1 #------
        print(f"(palk) saavad kätte järgmised inimesed: ")
        for j in range(n):
            k=p.index(palk,k+1)#---------
            nimi=i[k]
            print(nimi)
    return i,p

def Kustuta(i:list,p:list):
    """
    :param list i:Inimeste järjend
    :param list p: Palgade järjend
    :rtype: int, str
    """
    kesk_palk=sum(p)/len(p)
    print(kesk_palk)
    v=int(input("palk 1-suurem,2-väiksem? "))
    if v==1:
        for palk in p:
            if palk>kesk_palk:
                ind=p.index(palk)
                p.remove(palk)
                i.pop(ind)
    else:
        for palk in p:
            if palk<kesk_palk:
                ind=p.index(palk)
                p.remove(palk)
                i.pop(ind)
    return i,p

def sort_a_b(i:list,p:list):
    """
    :param list i:Inimeste järjend
    :param list p: Palgade järjend
    :rtype: int, str
    """
    data = ['Elle', 'Miles', 'Kratos', 'Joel', 'Peter', 'Nathan']

    print(sorted(data))

def top3(i:list,p:list):
    """
    """
    top1=p[0]
    top2=p[0]
    top3=p[0]
    for palk in p:
        if palk>top1:
            top1=palk
        elif palk>top2:
            top2=palk
        elif palk>top3:
            top3=palk
    print("rikkad",top1, top2, top3)
    top1=p[0]
    top2=p[0]
    top3=p[0]
    for palk in p:
        if palk<top1:
            top1=palk
        elif palk<top2:
            top2=palk
        elif palk<top3:
            top3=palk

    print("vaesed",top1, top2, top3)
    return i,p

def keskminepalk(i:list,p:list):
    kesk_palk=sum(p)/len(p)
    for palk in p:
        if palk==kesk_palk:
            ind=p.index(palk)
            print(f"{kesk_palk},{i[ind]}")
    return i,p

def tulumaks():
    """
    """
    tulu=int(input("palga suurus "))
    if tulu<1200:
        maksuvaba_tulu=500
    elif tulu<2100:
        maksuvaba_tulu=500-0.55556(tulu-1200)
    else:
        maksuvaba_tulu=0
    maks=(tulu-maksuvaba_tulu)*0.20
    netopalk=tulu-maks
    print(f"netopalk on {netopalk}")

def nimes(i:list,p:list):
    """
    """
    nimi=input("Kelle tahad leida?  ")
    while nimi not in i:
        nimi=input("Palun kirjuta õige nimi")
        n=i.count(nimi)
    if n!=1:
        print(f"Siin on mõned inimesed kes nimi on {nimi}")
        kopia=i.copy()
        for i in range(n):
            ind=kopia.index(nimi)
            kopia.remove(nimi)
            kopia.insert(ind,"")
            print(f"{i+1} {nimi} saab {p[ind]}")

    return i,p