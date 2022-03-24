#q1b
import math
x = float(input("Add number: "))
y = int(input("Add significant figures: "))
c = (round(pow(x,1/3))**3)
def fa():
    po = -(1/3)
    fa = 0.0
    dec = 1/3
    jam = 0
    for i in range(100):
        fact = 1/math.factorial(i+1)
        ki = ((x-c)**(i+1))
        fi = ((dec) * (c**po))
        faa = (fact * fi * ki)
        fa += faa 
        dec = dec * po
        po -= 1
        stat = stop(fa,jam)
        jam = faa
        if(stat == True):
            return fa
    return fa
def formula():
    ans = round(pow(c,1/3)) + fa 
    return ans
def stop(fa,jam):
    ea = 1
    es = 0.5 * pow(10,2-(y+1))
    prev = jam
    ea = abs((fa - prev)/fa)*100
    if(ea<es):
        return True
    else:
        return False
fa = fa()
print(formula())