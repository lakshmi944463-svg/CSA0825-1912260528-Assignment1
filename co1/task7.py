litres = float(input("Enter litres: "))
fat = float(input("Enter fat %: "))
snf = float(input("Enter SNF %: "))
rate = 30.0 + round((fat-3.5)/0.1)*0.40 + round((snf-8.5)/0.1)*0.30
print(f"Rate Rs.{rate:.2f}, Total Rs.{litres*rate:.2f}")
