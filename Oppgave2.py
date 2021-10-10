import numpy as np

#for 1 pannekake
mel = 3/12 #dl
melk = 6/12 #dl
egg = 4/12 #stk
smør = 2/12 #ss
salt = 0.5/12 #ts

ditt_antall = int(input("tast antall pannekaker du ønsker: "))

print("Ny oppskrift")
print(f"{mel * ditt_antall:.1f}", "dl mel")
print(f"{melk * ditt_antall:.1f}", "dl melk")
print((np.ceil(egg * ditt_antall)), "stk egg")
print(f"{smør * ditt_antall:.1f}", "ss smør")
print(f"{salt * ditt_antall:.2f}", "ts salt")
    