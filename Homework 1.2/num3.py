#q3
import math
n = 0
s = 0
e = 0
f = 0
# bin32 = "01000010011010100100000000000000"
bin32 = str(input("32-bit binary: "))
def sign():
    s_int = int(bin32[0])
    sign = pow(-1,s_int)
    return sign
def exponent():
    bias = int(bin32[1:9],2)
    unbias = bias - 127
    return unbias
def mantissa():
    count = -1
    fraction = 0
    m_str = bin32[9:]
    for i in m_str:
         fraction += (int(i) * pow(2, count))
         count -= 1
    return(fraction)
def formula():
    no = s * (1+f) * pow(2,e)
    return(no)
s = sign()
e = exponent()
f = mantissa()
n = formula()
# print("32-bit binary: "+bin32)
print("Sign of number: "+str(s))
print("Signed exponent: "+str(e))
print("Fraction: "+str(f))
print("Answer: "+str(n))