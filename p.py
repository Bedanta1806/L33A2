w= int(input("WEIGHT IN KG"))
h= int(input("WEIGHT IN CM"))

bmi = w/(h/100)**2
print("YOUR BMI IS, ",bmi)
if bmi<= 18.4:
    print ("BRUDDA YOU ARE UNDERWEIGHT MAN")
elif bmi<= 24.9:
    print ("HEALTH MAN")
elif bmi<= 34.9:
    print("MAN, YOU BIT OVERWEIGHT. NEED TO EXERCISE MORE BRUV")
elif bmi<= 39.9:
    print("BRO, GO TRAIN")
else:
    print("GO TOUCH GRASS, MA BOY")

