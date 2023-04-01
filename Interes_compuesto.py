
C=int(input("digite su capital "))
t=0
D=2*C

while(C<D):
    
    C=(C+0.05*C)
    t=t+1
    print("para el mes "+ str(t) + " el valor es " + str(C))


print("se duplica en el mes  " + str(t))
