d = {} 
i = 0
a = [] 
s = [1] 
t = 0 
for x in s:     
    for n in range(len(s), len(s)+1):    
        for m in range(1, n+1):
            i += m 
        d[n] = i 
        i = 0 
    for y in range(1,int(x/2)+1):
        if x == 1:
            a.append(y)
        if x%y == 0 :
            a.append(y)
    if len(a) >= 500:
        break        
    t += 1  
    a = []
    print(d)
    s.append(d[t])  
    del d[t]       

print(x, a, len(a))    