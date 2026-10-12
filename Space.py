earth_weight = float(input("What is the weight of something on earth? "))
print(" 1 = Mercury\n 2 = Venus\n 3 = Mars\n 4 = Jupiter\n 5 = Saturn\n 6 = Uranus\n 7 = Neptune\n 8 = Pluto")
planet = int(input("Select a planet, 1-8: "))

if(planet == 1):
    #* mercury 90
    mercury_weight = earth_weight * 0.9
    print(f"That weight on Mercury would be {mercury_weight}")
elif(planet == 2):
    #* venus 91
    venus_weight = earth_weight * 0.91
    print(f"That weight on Venus would be {venus_weight}")
elif(planet == 3):
    #* mars 38
    mars_weight = earth_weight * 0.38
    print(F"That weight on Mars would be {mars_weight}")
elif(planet == 4):
    #* jupiter 234
    jupiter_weight = earth_weight * 2.34
    print(f"That weight on Jupiter would be {jupiter_weight}")
elif(planet == 5):
    #* saturn 106
    saturn_weight = earth_weight * 1.06
    print(f"That weight on Saturn would be {saturn_weight}")
elif(planet == 6):
    #* uranus 92
    uranus_weight = earth_weight * 0.92
    print(f"That weight on Uranus would be {uranus_weight}")
elif(planet == 7):
    #* neptune 119
    neptune_weight = earth_weight * 1.19
    print(f"That weight on Neptune would be {neptune_weight}")
elif(planet == 8):
    #* pluto 6.3
    pluto_weight = earth_weight * 0.063
    print(f"That weight on Pluto would be {pluto_weight}")
else:
    print("Please restart and enter a valid number 1-8 to select a planet")