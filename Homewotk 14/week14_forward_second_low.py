h = 0.5
xi = 0
fxi = 14.1

xip1 = xi + h
fxip1 = 11.9

xip2 = xi + (2 * h)
fxip2 = 5.8

f2xi = (fxip2 - (2*fxip1) + fxi)/ pow(h, 2)
print(f2xi)
