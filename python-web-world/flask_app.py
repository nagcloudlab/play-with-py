
from flask import Flask, render_template_string, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Simulated database (in-memory)
ACCOUNTS = {
    'ACC001': {'holder_name': 'Rajesh Kumar', 'balance': 50000.0, 'type': 'Savings'},
    'ACC002': {'holder_name': 'Priya Sharma', 'balance': 75000.0, 'type': 'Current'},
}

# Counter for generating account numbers
account_counter = 2

# Templates
BASE_STYLE = """
    body { font-family: Arial; margin: 0; background: #f5f5f5; }
    .header { background: #003366; color: white; padding: 20px 40px; }
    .header h1 { margin: 0; }
    nav { background: #002244; padding: 10px 40px; }
    nav a { color: white; margin-right: 20px; text-decoration: none; }
    nav a:hover { text-decoration: underline; }
    .container { padding: 40px; }
    table { border-collapse: collapse; width: 100%; background: white; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
    th, td { border: 1px solid #ddd; padding: 15px; text-align: left; }
    th { background: #003366; color: white; }
    tr:hover { background: #f5f5f5; }
    .balance { font-weight: bold; color: #006600; }
    .btn { background: #003366; color: white; padding: 10px 20px; border: none; cursor: pointer; text-decoration: none; display: inline-block; }
    .btn:hover { background: #002244; }
    .btn-danger { background: #cc0000; }
    .btn-danger:hover { background: #990000; }
    .form-group { margin-bottom: 20px; }
    .form-group label { display: block; margin-bottom: 5px; font-weight: bold; }
    .form-group input, .form-group select { width: 300px; padding: 10px; border: 1px solid #ddd; border-radius: 4px; }
    .card { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); max-width: 500px; }
    .message { padding: 15px; margin-bottom: 20px; border-radius: 4px; }
    .message.success { background: #d4edda; color: #155724; border: 1px solid #c3e6cb; }
    .message.error { background: #f8d7da; color: #721c24; border: 1px solid #f5c6cb; }
    a { color: #003366; }
"""

LIST_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Accounts - NPCI Banking</title>
    <style>""" + BASE_STYLE + """</style>
</head>
<body>
    <div class="header">
        <h1>NPCI Banking System</h1>
    </div>
    <nav>
        <a href="/accounts">Accounts</a>
        <a href="/accounts/new">Create Account</a>
        <a href="/transfer">Transfer Money</a>
    </nav>
    <div class="container">
        {% if message %}
        <div class="message success">{{ message }}</div>
        {% endif %}
        
        <h2>All Accounts</h2>
        <p><a href="/accounts/new" class="btn">+ Create New Account</a></p>
        
        <table>
            <tr>
                <th>Account Number</th>
                <th>Holder Name</th>
                <th>Balance</th>
                <th>Type</th>
                <th>Actions</th>
            </tr>
            {% for acc_num, acc in accounts.items() %}
            <tr>
                <td>{{ acc_num }}</td>
                <td>{{ acc.holder_name }}</td>
                <td class="balance">₹{{ "{:,.2f}".format(acc.balance) }}</td>
                <td>{{ acc.type }}</td>
                <td>
                    <a href="/account/{{ acc_num }}">View</a> |
                    <a href="/account/{{ acc_num }}/delete" onclick="return confirm('Are you sure?')">Delete</a>
                </td>
            </tr>
            {% endfor %}
        </table>
    </div>
</body>
</html>
"""

CREATE_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Create Account - NPCI Banking</title>
    <style>""" + BASE_STYLE + """</style>
</head>
<body>
    <div class="header">
        <h1>NPCI Banking System</h1>
    </div>
    <nav>
        <a href="/accounts">Accounts</a>
        <a href="/accounts/new">Create Account</a>
        <a href="/transfer">Transfer Money</a>
    </nav>
    <div class="container">
        {% if error %}
        <div class="message error">{{ error }}</div>
        {% endif %}
        
        <div class="card">
            <h2>Create New Account</h2>
            
            <form method="POST" action="/accounts/new">
                <div class="form-group">
                    <label for="holder_name">Account Holder Name</label>
                    <input type="text" id="holder_name" name="holder_name" required>
                </div>
                
                <div class="form-group">
                    <label for="initial_balance">Initial Balance (₹)</label>
                    <input type="number" id="initial_balance" name="initial_balance" min="0" step="0.01" value="0">
                </div>
                
                <div class="form-group">
                    <label for="account_type">Account Type</label>
                    <select id="account_type" name="account_type">
                        <option value="Savings">Savings</option>
                        <option value="Current">Current</option>
                    </select>
                </div>
                
                <button type="submit" class="btn">Create Account</button>
                <a href="/accounts" style="margin-left: 10px;">Cancel</a>
            </form>
        </div>
    </div>
</body>
</html>
"""

TRANSFER_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Transfer Money - NPCI Banking</title>
    <style>""" + BASE_STYLE + """</style>
</head>
<body>
    <div class="header">
        <h1>NPCI Banking System</h1>
    </div>
    <nav>
        <a href="/accounts">Accounts</a>
        <a href="/accounts/new">Create Account</a>
        <a href="/transfer">Transfer Money</a>
    </nav>
    <div class="container">
        {% if error %}
        <div class="message error">{{ error }}</div>
        {% endif %}
        {% if success %}
        <div class="message success">{{ success }}</div>
        {% endif %}
        
        <div class="card">
            <h2>Transfer Money</h2>
            
            <form method="POST" action="/transfer">
                <div class="form-group">
                    <label for="from_account">From Account</label>
                    <select id="from_account" name="from_account" required>
                        <option value="">Select Account</option>
                        {% for acc_num, acc in accounts.items() %}
                        <option value="{{ acc_num }}">{{ acc_num }} - {{ acc.holder_name }} (₹{{ "{:,.2f}".format(acc.balance) }})</option>
                        {% endfor %}
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="to_account">To Account</label>
                    <select id="to_account" name="to_account" required>
                        <option value="">Select Account</option>
                        {% for acc_num, acc in accounts.items() %}
                        <option value="{{ acc_num }}">{{ acc_num }} - {{ acc.holder_name }}</option>
                        {% endfor %}
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="amount">Amount (₹)</label>
                    <input type="number" id="amount" name="amount" min="1" step="0.01" required>
                </div>
                
                <button type="submit" class="btn">Transfer</button>
            </form>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return redirect(url_for('list_accounts'))


@app.route('/accounts')
def list_accounts():
    """List all accounts"""
    message = request.args.get('message')
    return render_template_string(LIST_TEMPLATE, accounts=ACCOUNTS, message=message)


@app.route('/accounts/new', methods=['GET', 'POST'])
def create_account():
    """Create new account - GET shows form, POST processes it"""
    global account_counter
    
    if request.method == 'POST':
        # Get form data
        holder_name = request.form.get('holder_name', '').strip()
        initial_balance = request.form.get('initial_balance', '0')
        account_type = request.form.get('account_type', 'Savings')
        
        # Validate
        if not holder_name:
            return render_template_string(CREATE_TEMPLATE, error="Holder name is required")
        
        try:
            initial_balance = float(initial_balance)
            if initial_balance < 0:
                raise ValueError("Balance cannot be negative")
        except ValueError as e:
            return render_template_string(CREATE_TEMPLATE, error=f"Invalid balance: {e}")
        
        # Create account
        account_counter += 1
        account_number = f"ACC{account_counter:03d}"
        
        ACCOUNTS[account_number] = {
            'holder_name': holder_name,
            'balance': initial_balance,
            'type': account_type
        }
        
        # Redirect to list with success message# NOTE: Full page reload happens here!
        return redirect(url_for('list_accounts', message=f"Account {account_number} created successfully!"))
    
    # GET request - show form
    return render_template_string(CREATE_TEMPLATE, error=None)


@app.route('/account/<account_number>/delete')
def delete_account(account_number):
    """Delete an account"""
    if account_number in ACCOUNTS:
        del ACCOUNTS[account_number]
        return redirect(url_for('list_accounts', message=f"Account {account_number} deleted"))
    return redirect(url_for('list_accounts', message="Account not found"))


@app.route('/transfer', methods=['GET', 'POST'])
def transfer_money():
    """Transfer money between accounts"""
    
    if request.method == 'POST':
        from_account = request.form.get('from_account')
        to_account = request.form.get('to_account')
        amount = request.form.get('amount')
        
        # Validate
        if from_account == to_account:
            return render_template_string(
                TRANSFER_TEMPLATE,
                accounts=ACCOUNTS,
                error="Cannot transfer to same account"
            )
        
        if from_account not in ACCOUNTS:
            return render_template_string(
                TRANSFER_TEMPLATE,
                accounts=ACCOUNTS,
                error="From account not found"
            )
        
        if to_account not in ACCOUNTS:
            return render_template_string(
                TRANSFER_TEMPLATE,
                accounts=ACCOUNTS,
                error="To account not found"
            )
        
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Amount must be positive")
        except ValueError as e:
            return render_template_string(
                TRANSFER_TEMPLATE,
                accounts=ACCOUNTS,
                error=f"Invalid amount: {e}"
            )
        
        # Check balance
        if ACCOUNTS[from_account]['balance'] < amount:
            return render_template_string(
                TRANSFER_TEMPLATE,
                accounts=ACCOUNTS,
                error=f"Insufficient balance. Available: ₹{ACCOUNTS[from_account]['balance']:,.2f}"
            )
        
        # Perform transfer
        ACCOUNTS[from_account]['balance'] -= amount
        ACCOUNTS[to_account]['balance'] += amount
        
        # NOTE: Full page reload with success message!
        return render_template_string(
            TRANSFER_TEMPLATE,
            accounts=ACCOUNTS,
            success=f"Successfully transferred ₹{amount:,.2f} from {from_account} to {to_account}",
            error=None
        )
    
    return render_template_string(TRANSFER_TEMPLATE, accounts=ACCOUNTS, error=None, success=None)


if __name__ == '__main__':
    print("=" * 60)
    print("NPCI Banking Web Application")
    print("=" * 60)
    print("Open browser: http://localhost:5000")
    print("=" * 60)
    app.run(debug=True, port=5000)
