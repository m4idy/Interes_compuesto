
C=int(input("digite su capital "))
t=0
D=2*C

while(C<D):
    C=(C+0.05*C)
    t=t+1

print("se duplica en " + str(t))
