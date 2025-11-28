import csv
from datetime import datetime

def generate_transaction_report(transactions, filename):
    """Generate transaction report in CSV format"""
    
    fieldnames = ['transaction_id', 'timestamp', 'sender', 'receiver', 'amount', 'status', 'fee']
    
    with open(filename, "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(transactions)
    
    print(f"✓ Generated report: {filename}")


def analyze_transaction_report(filename):
    """Analyze transaction report"""
    
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        
        total_amount = 0
        success_count = 0
        failed_count = 0
        total_fee = 0
        
        for row in reader:
            amount = float(row['amount'])
            fee = float(row['fee'])
            
            if row['status'] == 'SUCCESS':
                total_amount += amount
                success_count += 1
                total_fee += fee
            else:
                failed_count += 1
        
        print(f"\nTransaction Report Analysis:")
        print(f"{'='*50}")
        print(f"Total Successful: {success_count}")
        print(f"Total Failed: {failed_count}")
        print(f"Total Amount: ₹{total_amount:,.2f}")
        print(f"Total Fees Collected: ₹{total_fee:,.2f}")
        print(f"{'='*50}")


# Generate sample transactions
transactions = [
    {'transaction_id': 'TXN001', 'timestamp': '2024-01-15 09:00:00', 'sender': 'ACC001', 'receiver': 'ACC002', 'amount': 5000, 'status': 'SUCCESS', 'fee': 25},
    {'transaction_id': 'TXN002', 'timestamp': '2024-01-15 09:15:00', 'sender': 'ACC003', 'receiver': 'ACC004', 'amount': 10000, 'status': 'SUCCESS', 'fee': 50},
    {'transaction_id': 'TXN003', 'timestamp': '2024-01-15 09:30:00', 'sender': 'ACC005', 'receiver': 'ACC006', 'amount': 150000, 'status': 'FAILED', 'fee': 0},
    {'transaction_id': 'TXN004', 'timestamp': '2024-01-15 10:00:00', 'sender': 'ACC007', 'receiver': 'ACC008', 'amount': 25000, 'status': 'SUCCESS', 'fee': 125},
]

# Generate and analyze report
generate_transaction_report(transactions, "daily_transactions.csv")
analyze_transaction_report("daily_transactions.csv")

# Output:
# ✓ Generated report: daily_transactions.csv
# 
# Transaction Report Analysis:
# ==================================================
# Total Successful: 3
# Total Failed: 1
# Total Amount: ₹40,000.00
# Total Fees Collected: ₹200.00
# ==================================================