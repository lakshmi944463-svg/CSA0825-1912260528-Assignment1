# Task 12 - Final Dairy Management System 
# Final Integration of all Tasks

while True:
    print("\n=== FINAL DAIRY SYSTEM - Task 12 ===")
    print("1.Add Milk  2.View All  3.Report  4.Exit")
    ch=input("Choice: ")
    
    if ch=='1':
        try:
            l=float(input("Litres: "))
            f=float(input("Fat %: "))
            s=float(input("SNF %: "))
            if l<=0 or f<=0 or s<=0: print("Invalid! >0 only"); continue
            rate = (f*4 + s*2) + 5  # Simple rate formula
            amt = l * rate
            with open("milk_data_final.txt","a") as file:
                file.write(f"L:{l}, F:{f}, S:{s}, R:{rate:.2f}, A:{amt:.2f}\n")
            print(f"Saved! Rs.{amt:.2f}")
        except:
            print("Invalid input!")
            
    elif ch=='2':
        try:
            with open("milk_data_final.txt","r") as file:
                print(file.read())
        except:
            print("No records yet!")
            
    elif ch=='3':
        try:
            with open("milk_data_final.txt","r") as file:
                lines=file.readlines()
            print(f"\nTotal Records: {len(lines)}")
            total=sum(float(x.split("A:")[1]) for x in lines)
            print(f"Total Amount: Rs.{total:.2f}")
        except:
            print("No data for report!")
            
    elif ch=='4':
        print("\nThank you! Exiting safely...")
        print("Project by Lakshmi D - SIMATS")
        break
    else:
        print("Invalid choice! 1-4 only")
