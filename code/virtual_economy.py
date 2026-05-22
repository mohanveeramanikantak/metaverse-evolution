# Virtual Economy Simulation

import random

print("💰 Virtual Economy System Started")

# User virtual balance
balance = random.randint(100, 1000)

# Random transaction
transaction = random.randint(50, 300)

print("💳 Current Balance:", balance, "Coins")
print("🛒 Purchase Amount:", transaction, "Coins")

# Transaction processing
if balance >= transaction:
    balance -= transaction
    print("✅ Transaction Successful")
else:
    print("⚠️ Insufficient Balance")

print("🏦 Updated Balance:", balance, "Coins")
