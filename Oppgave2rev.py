import numpy as np

#for 1 pannekake
mel = 3/12 #dl
melk = 6/12 #dl
egg = 4/12 #stk
smør = 2/12 #ss
salt = 0.5/12 #ts

def oppskrift(ant_pan):
    ny_mel = mel * ant_pan
    ny_melk = melk * ant_pan
    ny_egg = egg * ant_pan
    ny_smør = smør * ant_pan
    ny_salt = salt * ant_pan

    if (round(ny_egg) == 0):
        ny_oppskrift = (ny_mel, ny_melk, 1, ny_smør, ny_salt)
        return ny_oppskrift
    else:
        ny_oppskrift = (ny_mel, ny_melk, ny_egg, ny_smør, ny_salt)
        return ny_oppskrift
    
ant_pan = int(input("Velg antall pannekaker du vil lage: "))

ny_oppskrift = oppskrift(ant_pan)
print("Oppskrift for", ant_pan, "pannekake er")
print("Mel", f"{ny_oppskrift[0]:.1f}", "dl")
print("Melk", f"{ny_oppskrift[1]:.1f}", "dl")
print("Egg", ny_oppskrift[2], "stk")
print("Smør", f"{ny_oppskrift[3]:.1f}", "ss")
print("Salt", f"{ny_oppskrift[4]:.2f}", "ts")

    