alf = '0abcdefghijklmnopqrstuvwxyzæøåABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ !?,.'

p = 17
q = 11

m = p*q

phim = (p-1) * (q-1)

k = 7
if(phim%k == 0):
    print('phim og k er ikke indbyrdes primiske')
else:
    pass

blokstørrelse = 1
blok = blokstørrelse*2


message = 'Citizen X'
print('Tekst som skal krypteres: ' + message + '\n')
print('krypteres med blokstoerrelse '+str(blokstørrelse)+
', p='+str(p)+', q='+str(q)+', og k='+str(k)+'\n')

plainmessage = ''

for a in message:
    if alf.index(a)<10:
        plainmessage += '0'
        plainmessage += str(alf.index(a))
    else:
        plainmessage += str(alf.index(a))

plainmessage = [plainmessage[a:a+blok] for a in range(0, len(plainmessage), blok)]

plainmessage = list(map(int, plainmessage))

print("Dette er den ikke-krypterede klartekst:")
print(plainmessage[0:len(plainmessage)])
print('\n')

encmessage = plainmessage.copy()

encmessage = [(x**k)%m for x in encmessage]

print("Dette er den krypterede tekst:")
print(encmessage)
print('\n')

def usfd(a, b):
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0

useless = 0
u = 0
v = 0
useless, u, v = usfd(k,phim)

decmessage = encmessage.copy()

decmessage = [(x**(u))%m for x in encmessage]

print('dette er den dekrypterede besked:')
print(decmessage)
print('\n')

dectext = ''

for a in decmessage:
    dectext += alf[a]


print("Den dekrypterede besked bliver da: " + dectext)


if dectext == message:
    print('Den originale besked og den dekrypterede besked er ens')
else:
    print('Den originale besked og den dekrypterede besked er ikke ens')