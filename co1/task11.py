

try:
    with open("milk_data_final.txt","r") as f:
        data=f.read()
except:
    # File illana ippo create panniduvom
    with open("milk_data_final.txt","w") as f:
        f.write("L:10, F:3.5, S:8.5, R:30.00, A:300.00\n")
    data="L:10, F:3.5, S:8.5, R:30.00, A:300.00\n"

print("=== Task 11: Report ===")
print(f"Total Records: {len(data.strip().split(chr(10)))}")
print(data)
print("\n--- Ended Safely ---")
