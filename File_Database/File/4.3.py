import json

def save_bank_config():
    """Save bank configuration"""
    
    config = {
        "bank_name": "NPCI Bank",
        "bank_code": "NPCI0001",
        "services": {
            "UPI": {
                "enabled": True,
                "transaction_limit": 100000,
                "daily_limit": 100000,
                "fee_percent": 0
            },
            "IMPS": {
                "enabled": True,
                "transaction_limit": 200000,
                "daily_limit": 200000,
                "fee_percent": 0.5
            },
            "NEFT": {
                "enabled": True,
                "transaction_limit": 1000000,
                "daily_limit": 1000000,
                "fee_percent": 0.2
            }
        },
        "account_types": {
            "Savings": {
                "min_balance": 1000,
                "interest_rate": 4.0,
                "withdrawal_limit": 50000
            },
            "Current": {
                "min_balance": 5000,
                "interest_rate": 0,
                "withdrawal_limit": 500000
            }
        }
    }
    
    with open("bank_config.json", "w") as file:
        json.dump(config, file, indent=4)
    
    print("✓ Bank configuration saved")


def load_bank_config():
    """Load and use bank configuration"""
    
    with open("bank_config.json", "r") as file:
        config = json.load(file)
    
    print(f"\n{config['bank_name']} Configuration")
    print("="*60)
    
    print("\nAvailable Services:")
    for service, details in config['services'].items():
        status = "Enabled" if details['enabled'] else "Disabled"
        print(f"  {service}: {status}")
        print(f"    Transaction Limit: ₹{details['transaction_limit']:,}")
        print(f"    Fee: {details['fee_percent']}%")
    
    print("\nAccount Types:")
    for acc_type, details in config['account_types'].items():
        print(f"  {acc_type}:")
        print(f"    Minimum Balance: ₹{details['min_balance']:,}")
        print(f"    Interest Rate: {details['interest_rate']}%")
        print(f"    Withdrawal Limit: ₹{details['withdrawal_limit']:,}")
    
    return config


save_bank_config()
config = load_bank_config()

# Output:
# ✓ Bank configuration saved
# 
# NPCI Bank Configuration
# ============================================================
# 
# Available Services:
#   UPI: Enabled
#     Transaction Limit: ₹100,000
#     Fee: 0%
#   IMPS: Enabled
#     Transaction Limit: ₹200,000
#     Fee: 0.5%
#   NEFT: Enabled
#     Transaction Limit: ₹1,000,000
#     Fee: 0.2%
# 
# Account Types:
#   Savings:
#     Minimum Balance: ₹1,000
#     Interest Rate: 4.0%
#     Withdrawal Limit: ₹50,000
#   Current:
#     Minimum Balance: ₹5,000
#     Interest Rate: 0%
#     Withdrawal Limit: ₹500,000