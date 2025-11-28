

#-----------------------------------
# Custom Exceptions
#-----------------------------------
class InsufficientFundsException(Exception):
    def __init__(self, message="Insufficient funds for the transfer."):
        self.message = message
        super().__init__(self.message)

class InvalidAccountException(Exception):
    def __init__(self, message="The specified account is invalid."):
        self.message = message
        super().__init__(self.message)        
#-----------------------------------
# Transfer Service Layer
# team : Alpha
#-----------------------------------

class TransferService:
    def transfer_funds(self, from_account_id, to_account_id, amount):
        # Load Accounts
        from_account = "Loaded From Account"  # Placeholder for actual account retrieval
        to_account = "Loaded To Account"      # Placeholder for actual account retrieval
        if(from_account is None or to_account is None):
            raise InvalidAccountException()
        # Check Sufficient Funds
        from_account_balance=1000.00  # Placeholder for actual balance retrieval
        if from_account_balance < amount:
            raise InsufficientFundsException()
        # Perform Transfer
        # Update Balances
        # Log Transaction
        return True
    

#-----------------------------------
# Ticket Booking Service
#-----------------------------------

tranfer_service = TransferService()

class TicketBookingService:
    def book_ticket(self):
        # Process Payment
        try:
            tranfer_service.transfer_funds("user_account", "ticket_vendor_account", 1500.00)
            # Confirm Booking
            # Send Confirmation
            return "Ticket Booked Successfully"
        except InsufficientFundsException as e:
            """
                what we do here
                ----------------
                -> render friendly message to user
                -> log the error for further analysis 
                -> re-raise or handle the exception as needed
                -> release any held resources if applicable
                -> execute fallback logic if necessary
            """
            print("Logging Error: " + str(e))  # Placeholder for actual logging
            return "Ticket booking failed due to insufficient funds."
        except InvalidAccountException as e:
            print("Logging Error: " + str(e))  # Placeholder for actual logging
            return "Ticket booking failed due to invalid account details."
        except Exception as e:
            print("Logging Error: " + str(e))  # Placeholder for actual logging
            return "An unexpected error occurred: " + str(e)

#-----------------------------------
# Main Application Logic
#-----------------------------------

ticket_service = TicketBookingService()
result = ticket_service.book_ticket()
print(result)