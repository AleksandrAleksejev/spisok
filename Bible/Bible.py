#Kmd=[] #tuhi jarjend
#Km=10 #esimene paev
#print("1.paeval pikkus oli",Km)
#Kmd.append(Km)
#print(Kmd)
#for p in range(2,8):
#        Km*=1.1#>10%
#        Kmd.append(round(Km,2))
#print(Kmd)
#print(Kmd[2])
#print(Kmd.index(16.11)+1)
#Kmd.remove(10)#pop(0)
#print(Kmd,"Listis on kokku",Kmd.count(16.11))
#print(len(Kmd),"on janud listis")

#Maakond=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]
#while 1:
#    try:
#        Index=int(input("Index"))
#        if len(str(Index))==5:
#            break
#    except ValueError:
#        print("Valesti Sisestatud index!")
#i_list=list(str(Index))
#print(str(Index))
#print(i_list)
#s1=int(i_list[0])
#print(Maakond[s1-1])
#if s1 in [1,2,3]:
#    print("jatke kodus!")
#else:
#    print("Kanna maski!")

#2
#from random import *
#spisok=[]
#while 1:
#    try:
#        N=int(input("N->"))
#        if N>1:
#            break
#    except ValueError:
#        print("Число меньше 2")
#for i in range(N):
#    spisok.append(randint(1,100))
#for s in spisok:
#    print(s)
#pervyi=spisok[0]
#posledni=spisok[N-1]#-1
#spisok.pop(0)
#spisok.insert(0,posledni)
#spisok.pop(N-1)
#spisok.insert(N-1,pervyi)
#print(spisok)
#spisok_c=spisok.copy()
#spisok_c.reverse()
#print(spisok_c)
#3
from random import *
spisok=[]
while 1:
    try:
        N=int(input("N->"))
        if N>1:
            break
    except ValueError:
        print("Число меньше 2")
for i in range(N):
    spisok.append(randint(1,100))
print(spisok)
#spisok.copy()
#b=max(spisok)
#print(b)
#c=len(spisok)
#print(c)
#d=b/c
#print(d)
max_=max(spisok)
print(max_)
max_2=max(spisok)/len(spisok)
print(max_2)
ind=spisok.index(max_)
spisok.pop(ind)
spisok.insert(ind,max_2)
print(spisok)






