#Exercise 1 : one customer
customer = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "tier": "Gold",
    "ytd_spend": 12500
}  
print(customer)
print("=" *30)
#Exercise 2: Update and Add
print() #Add blank space in between to prevent bunching of output
customer["phone"] = "(555) 123-4567"
print(f"Phone added: {customer}")
print()
customer["tier"] = "Platinum"
print(f"Tier updated: {customer}")
print()
del customer["email"]
print(f"Email removed: {customer}")
print()
print("=" *30)
#Exercise 3: Safe lookup

print(customer.get("email", "no email on file"))
print()
print("=" *30)
#Exercise 4: Iterate
for key, value in customer.items():
    print(f"{key}: {value}")
print() 
#Exercise 5: Lookup table
tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}
tier = customer["tier"].lower() #table uses lowercase, so making sure .get() will find the tier value, which it won't if it is uppercase
discount_rate = tier_discounts.get(tier, 0)
purchase_price = 200
discounted_price = purchase_price * (1 - discount_rate)

print(f"Tier: {customer['tier']}")
print(f"Discount rate: {discount_rate:.0%}")
print(f"Final price: ${discounted_price:.2f}")

print("=" *30)
#Exercise 6: List of dicts

customer_2 = {
    "name": "Jane Smith",
    "email": "jane.smith@example.com",
    "tier": "Silver",
    "ytd_spend": 8000
}

customer_3 = {
    "name": "Alice Johnson",
    "email": "alice.johnson@example.com",
    "tier": "Bronze",
    "ytd_spend": 5000
}

customers = [customer, customer_2, customer_3]

for customer in customers:
    tier = customer["tier"].lower()
    discount_rate = tier_discounts.get(tier, 0)
    purchase_price = 300
    discounted_price = purchase_price * (1 - discount_rate)
    print(f"Customer: {customer['name']}")
    print(f"Tier: {customer['tier']}")
    print(f"Discount Amount: ${purchase_price - discounted_price:.2f}")
    print()


