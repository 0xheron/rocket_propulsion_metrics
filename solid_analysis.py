import math

def main():
    # Many constants, these will be removed in the future
    # Ratio of specific heats
    k = 1.21
    # Gas constant
    R = 326
    # Target thrust per second
    F_ideal = 4000
    # Specific impulse, seconds
    ISP_ideal = 225
    # Temp of combustion chamber, K
    T_Chamber = 2800
    # Burn rate coefficient, m/s
    a = 0.000634644 
    # Burn rate exponent
    n = 0.327392
    # kg/m^3
    density = 1688
    # Area that burns m^2
    burn_area = 0.206625 
    # Target pressure, mpa
    pressure_target = 2
    # Calculate c*, a performance characteristic used in pressure calculation
    c_star = math.sqrt(((R * T_Chamber)/k) * pow((k + 1)/2, (k+1)/(k-1)))
    # Rate of burning
    r = a * pow(pressure_target * 1000000, n)
    # Calculate area of throat (m^2)
    area_throat = r * c_star * burn_area * density / (pressure_target * 1000000)
    print(area_throat * 1000000)

main()