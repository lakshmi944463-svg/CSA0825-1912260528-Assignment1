

BASE_RATE = 30.0
STD_FAT = 3.5
STD_SNF = 8.5
FAT_STEP = 0.40
SNF_STEP = 0.30

farmer_id = input("Enter Farmer ID: ")
litres = float(input("Enter Litres: "))
fat = float(input("Enter Fat %: "))
snf = float(input("Enter SNF %: "))
shift = input("Enter Shift (M/E): ")

fat_steps = round((fat - STD_FAT) / 0.1)
snf_steps = round((snf - STD_SNF) / 0.1)

rate = BASE_RATE + (fat_steps * FAT_STEP) + (snf_steps * SNF_STEP)
amount = litres * rate
ten_day_total = amount * 10

print(f"\nRate per litre: Rs.{rate:.2f}")
print(f"Amount: Rs.{amount:.2f}")
print(f"Ten-day Total: Rs.{ten_day_total:.2f}")
