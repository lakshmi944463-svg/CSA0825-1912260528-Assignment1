# Task 10 - Complete Milk Management System 

def calculate_rate(fat, snf):
    return 30.0 + round((fat-3.5)/0.1)*0.40 + round((snf-8.5)/0.1)*0.30

def save_record(litres, fat, snf, rate, amount):
    try:
        with open("milk_data_final.txt", "a") as f:
            f.write(f"L:{litres}, F:{fat}, S:{snf}, R:{rate:.2f}, A:{amount:.2f}\n")
        return True
    except:
        return False

print("=== Task 10: Milk Management System ===")
print("SIMATS - Lakshmi D")

while True:
    print("\n--- MENU ---")
    print("1. Add Milk Record")
    print("2. View All Records")
    print("3. Exit")
    
    try:
        choice = input("Enter choice (1-3): ")
        
        if choice == '1':
            litres = float(input("Enter litres: "))
            fat = float(input("Enter fat %: "))
            snf = float(input("Enter SNF %: "))
            
            rate = calculate_rate(fat, snf)
            amount = litres * rate
            
            if save_record(litres, fat, snf, rate, amount):
                print(f"\nSaved! Rate: Rs.{rate:.2f}, Amount: Rs.{amount:.2f}")
            else:
                print("\nError saving file!")
                
        elif choice == '2':
            try:
                with open("milk_data_final.txt", "r") as f:
                    print("\n--- All Records ---")
                    print(f.read())
            except FileNotFoundError:
                print("\nNo records found! Add first!")
                
        elif choice == '3':
            print("\nThank you! Exiting safely...")
            print("--- Program Ended Safely ---")
            break
            
        else:
            print("\nInvalid choice! Enter 1, 2 or 3")
            
    except ValueError:
        print("\nError: Enter numbers only!")
