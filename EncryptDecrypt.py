#definerer alfabetet som en string, hvor a=1, derfor 0 i starten
#desuden står alfabetet igen, det er fordi man på den måde kan få store bogstaver.
alf = '0abcdefghijklmnopqrstuvwxyzæøåABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ !?,.'

#definer forskellige vigtige funktioner
p = 17
q = 11

m = p*q

#eulers phifunktion
phim = (p-1) * (q-1)

#skal være indbyrdes primisk med phim
k = 7
if(phim%k == 0):
    print('phim og k er ikke indbyrdes primiske')
else:
    pass

#blokstørrelse skal defineres. ved blokstørrelse 1 skal der tages 2 tal, derfor ganges med 2
blokstørrelse = 1
blok = blokstørrelse*2


#brug find fuctionen til at finde ud af hvilken værdi tallene har
#denne variabel er til at skrive, hvad der skal enkrypteres
message = 'Citizen X'
print('Tekst som skal krypteres: ' + message + '\n')
print('krypteres med blokstoerrelse '+str(blokstørrelse)+
', p='+str(p)+', q='+str(q)+', og k='+str(k)+'\n')

plainmessage = ''

#her tilføjer jeg alle talenne til plaintext variablen
for a in message:
    if alf.index(a)<10:
        plainmessage += '0'
        plainmessage += str(alf.index(a))
    else:
        plainmessage += str(alf.index(a))

#denne er til for at sørge for at alting er splittet op i par, da jeg bruger blokstørrelse 1
#blok er derfor 2. Den adskiller min string i par, og tilføjer dem til listen. 
plainmessage = [plainmessage[a:a+blok] for a in range(0, len(plainmessage), blok)]

#denne laver det fra en list til en integer, som jeg da kan regne med
plainmessage = list(map(int, plainmessage))

print("Dette er den ikke-krypterede klartekst:")
print(plainmessage[0:len(plainmessage)])
print('\n')

#enkrypteret tekst variabel

encmessage = plainmessage.copy()

encmessage = [(x**k)%m for x in encmessage]

print("Dette er den krypterede tekst:")
print(encmessage)
print('\n')

#her kommer  euklids udvidede algoritme-delen
#her skal der findes 2 tal, sådan at k*u-phim*v=1
#her defineres en funktion, som retunerer extended greatest common devisor
#den returnerer (g, x, y), i forhold til euklids udvide algoritme, nemlig a*x+b*y=g hvor g er sfd for a og b
def usfd(a, b):
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        #divmod er en funktion som dividerer argument 1 med argument 2, og printer (resultat, remainder)
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0

#her definerer jeg 3 variabler, da den outputter 3 resultater. Det eneste jeg skal bruge er u, som ganges på første led
#De andre 2 definerer jeg også, men de bliver ikke brugt til noget.
useless = 0
u = 0
v = 0
useless, u, v = usfd(k,phim)

#her kommer så selve dekrypteringen, som følger meget det samme som enkrypteringen, men nye tal
#endnu en ny variabel, denne gang klarteksten, som da kan stykkes sammen til tekst

decmessage = encmessage.copy()

decmessage = [(x**(u))%m for x in encmessage]

print('dette er den dekrypterede besked:')
print(decmessage)
print('\n')

#her laver jeg en variabel, som til sidst bliver ordet igen

dectext = ''

for a in decmessage:
    dectext += alf[a]


print("Den dekrypterede besked bliver da: " + dectext)


if dectext == message:
    print('Den originale besked og den dekrypterede besked er ens')
else:
    print('Den originale besked og den dekrypterede besked er ikke ens')