#finder GCD (greatest common demominator, største fælles divisor) for 2 tal, x og y

x = 23456789876754567892
y = 893537286013873592
#jeg skal bruge 2 andre variable, til at holde styr på hvilken som er størst
v = 0
z = 0
b = 0


if(x > y):
    v = x
    z = y
else:
    v = y
    z = x


#her laver jeg en ny variabel, som er resten for divisionen mellem z og v. 
# resten skal bruges til at dividere med z. 
b = v%z


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