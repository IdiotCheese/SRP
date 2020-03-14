import random

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
