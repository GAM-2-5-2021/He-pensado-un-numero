import random
import math
import sys
import time
from time import sleep
#uvođenje zbirki

#funkcija za sporo ispisivanje teksta
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1) #ovime stopiramo timer svakih 0.1 sekundi

pokušaj = 7 #maksimalan broj pokušaja koji se ne mijenja nikada, tj. ostaje 7
brojač = 0 #brojač koji broji pokušaje, tj. do 7 kada staje; reseritali smo ga na 0 na početku


print_slow("Word guessing game, blink to begin.\n")


sleep(1) #stopiram program na 1 sekundu za dramatičan efekt

#određivanje donje i gornje granice intervala
print_slow("Donja granica pljiz: ")
donji = int(input()) #unos donje granice

print_slow("Gornja granica pljiz: ")
gornji = int(input()) #unos gornje granice


r = random.randint(donji, gornji) #random broj unutar intervala

print_slow("\n\tŽao mi je, ali imaš samo 7 pokušaja\n")
print_slow("\t\t\t\t\t(nije mi žao)\n") #puno tabova da se tekst bude bliže kraju gornjeg ispisa


#while petlja za pokušaje
while brojač < pokušaj: #while petlja kojom povećavamo brojač za 1
  brojač += 1 #dok je brojač (0) manji od pokušaja (7) povećavat će se uvijek za 1 nakon unosa kada prolazi kroz petlju dolje
  print_slow("Pucaj: ") #samo tekst
  gađaj = int(input()) #broj koji unosimo da bi pogodili random broj
  if r == gađaj: #ako je random jednak našem unosu izvršava se ova if petlja
    print_slow("Ma bravo! Pile moje! Uspio si u ")
    print_slow(str(brojač)) #pretvaram broj iz brojača u string kako bi ga mogao ispisati kao tekst
    print_slow(" pokušaja") #kada se ovo dogodi, petlja će se prekinuti
  elif r > gađaj: #ako je random veći od našeg unosa izvršava se ova elif petlja
    print_slow("Gađaj malo više\n")
  elif r < gađaj: #ako je random niži od našeg unosa izvršava se ova elif petlja
    print_slow("Gađaj malo niže\n")


#if petlja za prekidanje programa
if brojač >= pokušaj: #petlja koja prekida program ako broj pokušaja premašuje 7 maksimalnih
  print_slow("\n *Comrade Military Radio*") 
  print_slow("\n Mission failed we'll get em next time")
  print_slow("\n Broj je bio ")
  print_slow(str(r)) #pretvaram broj iz brojača u string kako bi ga mogao ispisati kao tekst
  print_slow("\n *Comrade Military Radio Going Dark*")









