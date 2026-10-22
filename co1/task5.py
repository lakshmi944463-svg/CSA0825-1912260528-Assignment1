# Task 5 - User Input and Validation
# Name: Lakshmi D - 1912260528A
# Aim: Accept milk details, validate inputs and calculate payment

BASE_RATE = 30.0
FAT_STEP = 0.40
SNF_STEP = 0.30
STD_FAT = 3.5
STD_SNF = 8.5

# Algorithm:
# 1.Start
# 2.Read litres, fat, SNF
# 3.Check litres < 0 -> Invalid
# 4.Check fat < 2 or >7 -> Invalid
# 5.Check SNF < 0 -> Invalid
# 6.If invalid display error
# 7.Else calculate fat & SNF steps
# 8.Calculate rate per litre
# 9.Calculate total payment
# 10.Display result 11.Stop

print("Milk Payment Calculator")
litres = float(input("Enter milk quantity (litres): "))
fat = float(input("Enter fat % (2.0 - 7.0): "))
snf = float(input("Enter SNF %: "))

# Validation
if litres < 0:
    print("Error: Milk quantity cannot be negative!")
elif fat < 2.0 or fat > 7.0:
    print("Error: Fat % must be between 2.0 and 7.0!")
elif snf < 0:
    print("Error: SNF cannot be negative!")
else:
    # Valid inputs - Calculate
    fat_steps = round((fat - STD_FAT) / 0.1)
    snf_steps = round((snf - STD_SNF) / 0.1)
    
    rate_per_litre = BASE_RATE + (fat_steps * FAT_STEP) + (snf_steps * SNF_STEP)
    total_payment = litres * rate_per_litre
    
    print("\n--- Payment Details ---")
    print(f"Quantity: {litres} litres")
    print(f"Fat: {fat}%, SNF: {snf}%")
    print(f"Rate per litre: Rs.{rate_per_litre:.2f}")
    print(f"Total Payment: Rs.{total_payment:.2f}")
