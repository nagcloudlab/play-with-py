# WITH FILES (Data is saved!)
# ===========================

# Save account data to file
with open("accounts.txt", "w") as file:
    file.write("ACC001,45000\n")
    file.write("ACC002,35000\n")

print("✓ Data saved to file")

# Later... (even after restart)
# Read account data from file
with open("accounts.txt", "r") as file:
    for line in file:
        acc_num, balance = line.strip().split(",")
        print(f"{acc_num}: ₹{float(balance):,.2f}")

# Output:
# ✓ Data saved to file
# ACC001: ₹45,000.00
# ACC002: ₹35,000.00

# Data persists! ✓