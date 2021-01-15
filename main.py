import math

# width of solar panel
wpanel = .8 #m

# length of panel
lpanel= .8 #m

# Area of panel
A = wpanel * lpanel

# solar irrandiance
E=1000 #Watt/m^2

# solar panel efficiency
e=0.20

# incident angle
theta = 10*math.pi/180 # 10 degrees expressed in radians

# mass
m = 5 #kg     1 kg = 2.2046 lb
print("Total drone mass = ", m, "kg")

# gravitational field
g = 9.8 #N/kg

# density of air
rho = 1.23 #kg/m^3


# required thrust
Fthrust = m*g

#available power
P=E*e*A*math.cos(theta)

print("Solar Power Output = ", P, " Watts")

#calculate thrust speed
#Fthrust = mg = rho*A*v**2/2
v=4*P/(2*m*g*rho)
print("Thrust air speed = ",v, " m/s")


#calculate rotor area
Ar=4*P/(rho*v**3)

print("Total Rotor Area = ",Ar," m^2")

#calculate rotor diameter (assuming 4)
d=2*math.sqrt(Ar/(4*math.pi))
print("Single Rotor Diameter (assuming 4 total) = ",d," m")

