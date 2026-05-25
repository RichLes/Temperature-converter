scale1 = input("Enter the original scale (K/F/C): ").upper().strip()
unit = float(input("Enter the Temperature: "))
scale2 = input("Enter the converted scale (K/F/C): ").upper().strip()

# Convert input scale to Celsius
if scale1 == "K":
    unit1 = unit - 273.15
elif scale1 == "F":
    unit1 = (unit - 32) * (5 / 9)
elif scale1 == "C":
    unit1 = unit
else:
    print("Please enter a valid scale. Use K, F, or C.")
    exit()

# Convert from Celsius to target scale
if scale2 == "K":
    unit2 = unit1 + 273.15
elif scale2 == "F":
    unit2 = (unit1 * 9 / 5) + 32
elif scale2 == "C":
    unit2 = unit1
else:
    print("Please enter a valid scale. Use K, F, or C.")
    exit()

print(f"{unit} {scale1} = {unit2:.2f} {scale2}")