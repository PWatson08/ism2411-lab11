#Reflection:
#1. In Exercise 3 you saw the difference between .get() and bracket notation. When in real work would you use each one, and what's your rule of thumb for choosing?
# I would use .get() when the key might not exist and I want to provide a default value, and bracket notation when I know the key exists or want to handle the missing key explicitly.
#2. Exercise 8 asked you to build a summary dictionary with a loop. What does this pattern remind you of from Excel, and why might the Python version be more useful for large datasets?
# This pattern reminds me of Excel's SUMIF function, which totals values that match a condition. Python is more useful for large datasets because it can process the data programmatically without manually creating formulas for each region.

#Exercise 1 : one customer
customer = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "tier": "Gold",
    "ytd_spend": 12500
}  
print(customer)
print("=" *30) #Exercise separator
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
print("=" *30)
#Exercise 7: Nested Catalog 

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
    }
for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"Product: {product} - LOW STOCK ALERT")
print("=" *30)

#Exercise 8: Sales by Region

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]
summary = {}
for transaction in transactions:
    region = transaction["region"]
    summary[region] = summary.get(region, 0) + transaction["amount"]
for region in sorted(summary):
    print(f"{region}: {summary[region]}")
print("=" *30)
