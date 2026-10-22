from decimal import Decimal

# Different data types
milk_qty = 10
fat_percent = 3.5
farmer_name = "Ravi"
is_valid = True

print("Data Types:")
print(f"milk_qty = {milk_qty}, type = {type(milk_qty)}")
print(f"fat_percent = {fat_percent}, type = {type(fat_percent)}")
print(f"farmer_name = {farmer_name}, type = {type(farmer_name)}")
print(f"is_valid = {is_valid}, type = {type(is_valid)}")

# Arithmetic operators /, //, %
print("\nArithmetic Operators:")
print(f"10 / 3 = {10 / 3}")
print(f"10 // 3 = {10 // 3}")
print(f"10 % 3 = {10 % 3}")

# Float vs Decimal
print("\nFloat vs Decimal:")
print(f"Float 0.1 + 0.2 = {0.1 + 0.2}")
print(f"Decimal 0.1 + 0.2 = {Decimal('0.1') + Decimal('0.2')}")

# Milk payment calculation with Decimal
rate = Decimal('30.00')
qty = Decimal('10')
payment = rate * qty
print(f"\nPayment using Decimal: Rs.{payment}")

total = Decimal('0.00')
for p in [Decimal('300.00'), Decimal('283.90'), Decimal('333.60')]:
    total += p
print(f"Total Payment (Decimal): Rs.{total}")
