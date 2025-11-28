

from contextlib import contextmanager
import time

@contextmanager
def timer(operation_name):
    """Context manager to time operations"""
    
    print(f"\n⏱️  Starting: {operation_name}")
    start_time = time.time()
    
    yield  # Operation happens here
    
    end_time = time.time()
    elapsed = end_time - start_time
    print(f"✓ {operation_name} completed in {elapsed:.4f} seconds")


# Usage
# =====

with timer("Processing 1000 transactions"):
    # Simulate processing
    total = 0
    for i in range(1000):
        total += i
    print(f"  Processed {total} items")

# Output:
# ⏱️  Starting: Processing 1000 transactions
#   Processed 499500 items
# ✓ Processing 1000 transactions completed in 0.0001 seconds


with timer("Database query"):
    time.sleep(0.5)  # Simulate slow query
    print("  Query executed")

# Output:
# ⏱️  Starting: Database query
#   Query executed
# ✓ Database query completed in 0.5002 seconds