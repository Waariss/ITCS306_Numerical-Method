xi = 0.25
h = 0.25

xip1 = xi+h
fxip1 = 6.6

xim1 = xi-h
fxim1 = 7.9

f1xi = (fxip1 - fxim1)/(2*h)
print(f1xi)