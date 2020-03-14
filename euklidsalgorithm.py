#finder GCD (greatest common demominator, største fælles divisor) for 2 tal, x og y

'''dette ville være nemmere med divmod(a, b)'''

#input til tal man skal GCD'e

x = 39
y = 15

#jeg skal bruge 2 andre variable, til at holde styr på hvilken som er størst
v = 0
z = 0
b = 0

#tildeler størte værdi til v, mindste til y
if(x > y):
    v = x
    z = y
else:
    v = y
    z = x


#her laver jeg en ny variabel, som er resten for divisionen mellem z og v. 
# resten skal bruges til at dividere med z. 
b = v%z

#i dette loop laver jeg selve algoritmen, hvor man hver gang checker om b eller nye z er 0
#hvis den er nul printer man og breaker, hvis ikke udregner man hvad den bliver næste gang. 
while(True):
    if b<1:
        print("GCD er: " +  str(z))
        break
    elif z%b<1:
        print("GCD er: " +  str(b))
        break
    else:
        z = z%b
        if b%z<1:
            print("GCD er: " + str(z))
            break
        else:
            b = b%z