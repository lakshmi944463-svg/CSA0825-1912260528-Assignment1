# Task 8 - File Handling 

print("=== Task 8: File Handling ===")

litres = float(input("Enter litres: "))
fat = float(input("Enter fat %: "))
snf = float(input("Enter SNF %: "))

rate = 30.0 + round((fat-3.5)/0.1)*0.40 + round((snf-8.5)/0.1)*0.30
amount = litres * rate


file = open("milk_data.txt", "a")
file.write(f"Litres: {litres}, Fat: {fat}, SNF: {snf}, Rate: {rate:.2f}, Amount: {amount:.2f}\n")
file.close()

print(f"\nSaved! Rate: Rs.{rate:.2f}, Amount: Rs.{amount:.2f}")


print("\n--- All Records from milk_data.txt ---")
file = open("milk_data.txt", "r")
print(file.read())
file.close()
