#q2
import math
num = float(input("Add number: "))
final = 0
def e(a):
    prev = 0
    ea = 1
    es = 0.5 * 10 ** (2-10)
    i = 0
    ex = 0
    while ea>es:
        ex = prev + (pow(a,(i+1))/math.factorial(i+1))
        ea = abs((ex - prev)/ex)*100
        prev = ex
        i +=1
    return ex + 1
def ln(x):
    ln = 0
    ea = 1
    es = 0.5 * 10 ** (2-10)
    i = 1
    x = x - 1
    prevln = 0
    while ea>es:
        ln = prevln + (pow(-1,(i+1)) * ((pow(x,i))/i))
        ea = abs((ln - prevln)/ln)*100
        prevln = ln
        i += 1
    return ln
a = 1
lnin = 3
while(lnin-1) > 1:
    lnin = (num/e(a))
    a += 1
a -= 1
final = a + ln(lnin)
print(final)