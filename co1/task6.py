# Task 6 - Functions and Abstraction

BASE_RATE = 30.0
FAT_STEP = 0.40
SNF_STEP = 0.30
STD_FAT = 3.5
STD_SNF = 8.5



def calc_rate(fat, snf):
    """Calculate rate per litre based on fat and SNF"""
    fat_steps = round((fat - STD_FAT) / 0.1)
    snf_steps = round((snf - STD_SNF) / 0.1)
    rate = BASE_RATE + (fat_steps * FAT_STEP) + (snf_steps * SNF_STEP)
    return rate

def calc_payment(litres, fat, snf):
    """Calculate total payment using rate"""
    rate = calc_rate(fat, snf)
    payment = litres * rate
    return payment

# Main Program - Reusing functions
print("=== Milk Rate Functions Demo ===")

# Test Case 1 - Standard milk
l1, f1, s1 = 10, 3.5, 8.5
r1 = calc_rate(f1, s1)
p1 = calc_payment(l1, f1, s1)
print(f"Test 1: {l1}L, Fat {f1}%, SNF {s1}% -> Rate Rs.{r1:.2f}, Payment Rs.{p1:.2f}")

# Test Case 2 - High fat milk
l2, f2, s2 = 8.5, 4.2, 8.7
r2 = calc_rate(f2, s2)
p2 = calc_payment(l2, f2, s2)
print(f"Test 2: {l2}L, Fat {f2}%, SNF {s2}% -> Rate Rs.{r2:.2f}, Payment Rs.{p2:.2f}")

# Test Case 3 - User input
l3 = float(input("\nEnter litres: "))
f3 = float(input("Enter fat %: "))
s3 = float(input("Enter SNF %: "))
print(f"Rate: Rs.{calc_rate(f3,s3):.2f}, Payment: Rs.{calc_payment(l3,f3,s3):.2f}")
