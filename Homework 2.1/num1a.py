#q1a
import math
x = float(input("Add number: "))
y = int(input("Add significant figures: "))
c = round(math.sqrt(x))**2
def fa():
    po = -(1/2)
    fa = 0.0
    decc = 1/2
    jam = 0
    for i in range(100):
        fact = 1/math.factorial(i+1)
        ki = ((x-c)**(i+1))
        fi = ((decc) * (c**po))
        faa = (fact * fi * ki)
        fa += faa
        m = decc*po
        decc = m
        po -= 1
        stat = stop(fa,jam)
        jam = faa
        if(stat == True):
            return fa
    return fa
def formula():
    ans = round(math.sqrt(c)) + fa 
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