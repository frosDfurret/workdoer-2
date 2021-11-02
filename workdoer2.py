#terrible code courtesy of frosdfurret
#11/01/21
#I CODED THIS 20 MINUTES BEFORE AN ASSIGNMENT DUE DATE LMFAO

from art import *

tprint("work doer 2",font="rnd-medium")
print("for demonstrational use only, except in my case lol")
print('for "f(x)=ax^2+bx+c" quadratic equations :)')
a = input("what is a?")
a=float(a)

b = input("what is b?")
#turns b to negative (needed for formula)
if "-" in b:
    b=float(b)
    nb = b - b - b
else:
    nb = "-" + b
    nb=float(nb)
    b=float(b)

c = input("what is c?")
c = float(c)

#formula -b/2(a) to find axis of symmetry
xv = nb/(2*a)
print("equation for Axis of Symmetry:")
xve = str(nb)+"/2("+str(a)+")="+str(xv)
xve = xve.replace(".0","")
print(xve)

#punch aos into quadratic equation to find y of vertex
print("equation for Y of Vertex:")
yv = (a * xv**2) + (b * xv) + c
yve = str(a)+"("+str(xv)+")^2+"+str(b)+"("+str(xv)+")+"+str(c)+"="+str(yv)
yve = yve.replace(".0","")
print(yve)

tprint("you're welcome",font="rnd-small")
print("terrible code courtesy of frosdfurret")
cum = input("press enter to quit\n")
