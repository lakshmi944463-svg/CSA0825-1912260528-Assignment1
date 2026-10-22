# Task 9 - Exception Handling 
print("=== Task 9: Exception Handling ===")

try:
    litres = float(input("Enter litres: "))
    fat = float(input("Enter fat %: "))
    snf = float(input("Enter SNF %: "))
    
    if litres <= 0 or fat <= 0 or snf <= 0:
        raise ValueError("Values must be positive!")

    rate = 30.0 + round((fat-3.5)/0.1)*0.40 + round((snf-8.5)/0.1)*0.30
    amount = litres * rate
    
    print(f"\nSuccess! Rate: Rs.{rate:.2f}, Amount: Rs.{amount:.2f}")

except ValueError as e:
    print(f"\nError: Invalid input! {e}")
    print("Please enter numbers only!")

except Exception as e:
    print(f"\nUnexpected Error: {e}")

finally:
    print("\n--- Program Ended Safely ---")
