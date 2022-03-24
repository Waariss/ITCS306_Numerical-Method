import math
n = int(input("Add number: "))
y = int(input("Add significant figures: "))
x = round(math.sqrt(n))
es = 0.5 * pow(10,2-(y+1))
def her_on(x,n):
    ans = x
    for i in range(n):
        if(n == 0):
            return 0    
        if(n > 0):
            jam = ans
            ans = 0.5*(ans + (n/ans))
            stat = stop(ans,es,jam)
            if(stat == True):
                return ans
        else:
            return 0
def stop(ans,es,jam):
    ea = 1
    p = jam
    ea = abs((ans - p)/ans)
    if(ea<es):
        return True
    else:
        return False
print(her_on(x,n))