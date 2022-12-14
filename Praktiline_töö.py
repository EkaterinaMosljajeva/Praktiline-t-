from math import *
from random import *



##1
#try:
#    C=float(input("Anna ümbermõõt: "))
#    if C>0:
#        d=round(C/pi,2)
#        print("Läbimõõd", d)
#    else:
#        print("C peab olema suurem kui 0")
#except:
#    print("Andmetüüp on vale")


#2
#try:
#    N=float(input("Anna pikkus: "))
#    M=float(input("Anna laius: "))
#    if M>0 and N>0:
#        di=round(sqrt(M**2+N**2), 2)
#        print("Diagonaal", di)
#    else:
#        print("N ja M peavad olema suurem kui 0")
#except:
#    print("M ja N vaja sisestada float formaadis")

#3
#try:
#    aeg=float(input("Mitu tundi kulus sõiduks? "))
#    teepikkus=float(input("Mitu kilomeetrit sõitsid? "))
#    if aeg>0 and teepikkus>0:
#        kiirus=teepikkus/aeg
#        print("Sinu kiirus oli " + str(kiirus) + " km/h")
#    else:
#        print("Väärtused peavad olema suuremad kui 0")
#except:
#    print("Andmetüüp on vale")

#4
#try:
#    x1=float(input("Anna number 1: "))
#    x2=float(input("Anna number 2: "))
#    x3=float(input("Anna number 3: "))
#    x4=float(input("Anna number 4: "))
#    x5=float(input("Anna number 5: "))
#    if x1>0 and x2>0 and x3>0 and x4>0 and x5>0
#        a=(x1+x2+x3+x4+x5)/5
#        print("Aritmeetilise keskmise", a)
#    else:
#        print("Väärtused peavad olema suuremad kui 0")
#except:
#    print("Andmetüüp on vale")

#5
#print("   @..@\n  (----)\n ( \__/ )\n  ^^ "" ^^  ")

#6
#a=randint(1,100)
#b=randint(1,100)
#c=randint(1,100)
#print(f"a={a}\nb={b}\nc={c}")
#P=a+b+c
#print("Ümbermõõõd", P)

#7
#P=randint(1,6)
#summa=(12,9*1,1)/P
#print(f"{P}-str Igaüks maksab {summa}")

#8
#try:
#    liiter=float(input("Täidetud kütuse liitrite arv: "))
#    kilo=float(input("Läbitud kilomeetrite arv: "))
#    if liiter>0 and kilo>0:
#        kesk=(liiter*100)/kilo
#        print("Keskmine kütusekulu 100 km kohta", kesk)
#    else:
#        print("Väärtused peavad olema suuremad kui 0")
#except:
#    print("Andmetüüp on vale")

#9
#print("Rulluisutaja keskmine kiirus on 29,9km/h")
#try:
#    M=int(input("Minutid: "))
#    if M>0:
#        M=M/60
#        tee=M*29,9
#        print(f"Jõuab {tee} km")
#    else:
#        print("Minutid peavad olema suuremad kui 0")
#except:
#    print("Andmetüüp on vale")

#10
#min=int(input("Sisestage minutite arv: "))
#h=min//60 #h
#min=min%60 #min
#print(f"{h}:{min}")

#Ema roobot
a=(input("Sisesta: "))
print(a.isalpha(), a.isdigit())
if a.isdigit() and int(a)>0 and int(a)<=5:
    a=int(a)
    if a==5:
        print("Väga hästi")
    elif a==4:
        print("Hästi")
    elif a==3:
        print("See võiks olla parem")
    elif a==2 or a==1:
        print("Halb, proovige järgmine kord paremini")
else:
    print("Sa valesti vastas")