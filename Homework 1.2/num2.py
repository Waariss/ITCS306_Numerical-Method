#q2
import math
import numpy as np
n = float(input("Floating number: "))
dpib = []
wnib = [] 
countt = 0
number = int(0)
decimal = float(0)
(decimal,number) = math.modf(n)
def convertwn(number):
    for i in range(10):
        jam = number 
        ans = number//2 
        number = ans 
        wnib.append(jam%2)
        if(jam<=1):
            break;
    return wnib;
def convertdp(decimal):
    for i in range(10):
        mm = decimal
        store = decimal * 2 
        (de,bin) = math.modf(store)
        dpib.append(bin)
        decimal = de
        if(de==0):
            break;
    return dpib;
def merge():
    convertwn(number)
    convertdp(decimal)
    result = list(reversed(wnib))
    wnibb = np.array(result)
    dpibb = np.array(dpib)
    wn = wnibb.astype(int)
    dp = dpibb.astype(int)
    re1 = [str(int) for int in wn]
    re2 = [str(int) for int in dp]
    re11 = "".join(re1)
    re12 = "".join(re2)
    data=re11+'.'+re12
    #print(data)
    count = len(re11)
    #print(count)
    return count,data;
def sign(n):
    if(n>0):
        print("s =",0)
        return "0";
    elif(n<0):
        print("s =",1)
        return "1";
def binary():
    exp = 127 + (countt-1)
    be = convertwn(exp)
    result = list(reversed(be))
    b = np.array(result)
    bb = b.astype(int)
    r = [str(int) for int in bb]
    re13 = "".join(r)
    table = re13[0:8]
    print("e = "+table)
    return table;
def mantissa(dataa):
        str1 = ""
        str2 = str1.join(dataa)
        str3 = str2.replace('.','')
        str4 = str3[1:]
        z = '{:<023}'
        outputman = z.format(str4)
        print("f = "+outputman)
        return outputman;
def sum():
    be = sign(n) + binary() + mantissa(dataa)
    print("IEEE-754 = "+be)
countt,dataa = merge()
sum()