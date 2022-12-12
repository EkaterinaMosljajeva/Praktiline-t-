from math import *
from xml.etree.ElementTree import PI
from random import *



#1
#C=float(input("Anna ümbermõõt: "))
#d=round(C/pi,2)
#print("Läbimõõd", d)


#2
#N=float(input("Anna pikkus: "))
#M=float(input("Anna laius: "))
#di=round(sqrt(M**2+N**2), 2)
#print("Diagonaal", di)

#3
#aeg=float(input("Mitu tundi kulus sõiduks? "))
#teepikkus=float(input("Mitu kilomeetrit sõitsid? "))
#kiirus=teepikkus/aeg
#print("Sinu kiirus oli " + str(kiirus) + " km/h")

#4
#x1=float(input("Anna number 1: "))
#x2=float(input("Anna number 2: "))
#x3=float(input("Anna number 3: "))
#x4=float(input("Anna number 4: "))
#x5=float(input("Anna number 5: "))
#a=(x1+x2+x3+x4+x5)/5
#print("Aritmeetilise keskmise", a)

#5
#print("   @..@\n  (----)\n ( \__/ )\n  ^^ "" ^^  ")

#6
#a=randint(1,100)
#b=randint(1,100)
#c=randint(1,100)
#print(f"a={a}\nb={b}\nc={c}")
#P=a+b+c
#print("Ümbermõõõd", P)

##7
#P=randint(1,6)
#summa=(12,9*1,1)/P
#print(f"{P}-str Igaüks maksab {summa}")

#8
#liiter=float(input("Täidetud kütuse liitrite arv: "))
#kilo=float(input("Läbitud kilomeetrite arv: "))
#kesk=(liiter*100)/kilo
#print("Keskmine kütusekulu 100 km kohta", kesk)

#9
#print("Rulluisutaja keskmine kiirus on 29,9km/h")
#M=int(input("Minutid: "))
#M=M/60
#tee=M*29,9
#print(f"Jõuab {tee} km")

#10
min=int(input("Sisestage minutite arv: "))
h=min//60 #h
min=min%60 #min
print(f"{h}:{min}")