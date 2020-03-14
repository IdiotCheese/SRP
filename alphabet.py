#definerer alfabetet som en string, hvor a=1, derfor blank space i starten
#desuden står den igen, det er fordi man på den måde kan få store bogstaver.
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
#den skal måske forstås lidt bedre
plainmessage = [plainmessage[i:i+blok] for i in range(0, len(plainmessage), blok)]

#denne laver det fra en list til en integer, som jeg da kan regne med
#denne process fjerner 0'erne fra teksten, hvilket godt kan blive problematisk?
plainmessage = list(map(int, plainmessage))

print("Dette er den ikke-krypterede klartekst:")
print(plainmessage[0:len(plainmessage)])
print('\n')

#her definerer jeg variablen, som jeg skal bruge til den enkrypterede tekst
n = 0
#enkrypteret tekst variabel
encmessage = plainmessage.copy()

encmessage = [(x**k)%m for x in encmessage]

print("Dette er den krypterede tekst:")
print(encmessage)
