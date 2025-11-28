import json

def save_account_json(account_data):
    """Save account with nested data to JSON"""
    
    with open("account.json", "w") as file:
        json.dump(account_data, file, indent=4)  # indent=4 for pretty printing
    
    print("✓ Account saved to JSON")


# Complex account data with nested information
account = {
    "account_number": "ACC001",
    "holder": {
        "name": "Rajesh Kumar",
        "email": "rajesh@example.com",
        "phone": "+91-9876543210",
        "address": {
            "street": "123 MG Road",
            "city": "Mumbai",
            "state": "Maharashtra",
            "pincode": "400001"
        }
    },
    "balance": 50000,
    "account_type": "Savings",
    "transactions": [
        {"id": "TXN001", "amount": 5000, "type": "CREDIT", "date": "2024-01-10"},
        {"id": "TXN002", "amount": 2000, "type": "DEBIT", "date": "2024-01-12"},
        {"id": "TXN003", "amount": 3000, "type": "CREDIT", "date": "2024-01-14"}
    ],
    "settings": {
        "sms_alerts": True,
        "email_alerts": True,
        "daily_limit": 50000
    }
}

save_account_json(account)

# Output:
# ✓ Account saved to JSON

# File contents (account.json):
# {
#     "account_number": "ACC001",
#     "holder": {
#         "name": "Rajesh Kumar",
#         "email": "rajesh@example.com",
#         ...
#     },
#     ...
# }