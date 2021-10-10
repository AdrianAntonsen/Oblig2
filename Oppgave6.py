import numpy as np

def min_funksjon(l,b,h):
   return(l*b*h)

volum_boks = min_funksjon(8,6,16)
print("Volumet av boksen er :", volum_boks)
    
def funksjon_s(r):
   return(np.pi*(r**2)*10)

r = 1

while funksjon_s(r) < volum_boks:
   r += 1


print("Minste radius = ", r, "og volumet blir :", funksjon_s(r))









        