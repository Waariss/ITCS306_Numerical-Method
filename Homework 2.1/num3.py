#q3
import math
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
def func_sin(x,n): #function calculate sin(X)
    sin_approx = 0
    for i in range(n):
        coef = (-1)**i
        num = x**(2*i+1)
        denom = math.factorial(2*i+1)
        sin_approx += ( coef ) * ( (num)/(denom) )
    return sin_approx
angles = np.arange(-2.5*np.pi,2.5*np.pi,0.01) # x
p_sin = np.sin(angles) # sin(x)
fig,ax = plt.subplots()
ax.plot(angles,p_sin) #plot graph sin
for i in range(2,12):# add lines for between 1,2,4,6,8,10 terms in the Taylor Series
    if(i%2==0):
        t_sin = [func_sin(angle,i) for angle in angles]
        ax.plot(angles,t_sin)
plt.title("Taylor sin graph")# set up title
plt.grid()
ax.set_ylim([-10,10])# set up y length
ax.set_xlim([-10,10])# set up x length
legend_lst=['sin(x)'] # set up legend
for i in range(2,12):
    if(i%2==0):
        legend_lst.append(f'T_{i}(x)')
ax.legend(legend_lst, loc=3)
plt.show()