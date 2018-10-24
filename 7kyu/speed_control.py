# In John's car the GPS records every s seconds the distance travelled from an origin (distances are measured in an arbitrary but consistent unit). For example, below is part of a record with s = 15:
# print (3600 * 0.19) / 15
import math 

def gps(s, x):
    results = []
    i = 0

    while i < len(x) - 1:
        temp = x[i + 1] - x[i]
        results.append(math.floor((3600 * temp) / s))
        i += 1
        
    return max(results) 



x = [0.0, 0.18, 0.36, 0.54, 0.72, 1.05, 1.26, 1.47, 1.92, 2.16, 2.4, 2.64, 2.88, 3.12, 3.36, 3.6, 3.84]
s = 20
u = 80
print gps(s, x) #, u)