#finder GCD (greatest common demominator, største fælles divisor) for 2 tal, x og y

x = 39
y = 15
#jeg skal bruge 2 andre variable, til at holde styr på hvilken som er størst
v = int
z = int

if(x > y):
    v = x
    z = y
else:
    v = y
    z = x

#her laver jeg en ny variabel, som er resten for divisionen mellem z og v. resten skal bruges til at dividere med z. 
b = int

while(True):
    b=v%z
    if(b > 1):
        pass
    elif():
        z=z%b
    elif(b > 1 or z > 1):
        pass
    elif():
        True
