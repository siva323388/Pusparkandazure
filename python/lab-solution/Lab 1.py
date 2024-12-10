"""
**Challenge:** Using Comprehensions to Filter and Transform Data.

**Objective:**
The goal of this assignment is to understand and apply list, dictionary, and set comprehensions in Python to filter and transform data effectively. By completing this assignment, students will learn:

- How to create concise and efficient comprehensions.
- Real-world use cases of filtering and transforming data.
- Best practices for handling data using Python comprehensions.

**Challenge Details**

You are working as a Data Analyst at a retail company. Your manager has provided raw data for customers and their purchases. The dataset contains:

- A list of customer names and their respective ages.
- A dictionary of product IDs and their prices.
- A log of purchases made by customers, represented as tuples (customer name, product ID, quantity).

Your task is to process this data using list, dictionary, and set comprehensions to:

1. Filter out customers who are under 18 years old.
1. Apply a 10% discount to products priced above $50.
1. Create a unique set of product IDs purchased by customers aged 18 or older.
1. Transform the purchase log into a summary of total spend per customer (considering discounts).

**Sample Data:**

```
# Customer data: (name, age)
customers = [("Alice", 25), ("Bob", 17), ("Charlie", 35), ("Diana", 16)]

# Product data: {product_id: price}
products = {
    "P001": 45.00,
    "P002": 60.00,
    "P003": 120.00,
    "P004": 30.00
}

# Purchase log: (customer_name, product_id, quantity)
purchases = [
    ("Alice", "P001", 2),
    ("Charlie", "P002", 1),
    ("Bob", "P003", 3),
    ("Alice", "P004", 1),
    ("Charlie", "P003", 2),
    ("Diana", "P002", 1)
]
```

**Steps to Complete the Assignment**
1. Filter Adult Customers Use a list comprehension to filter out customers who are 18 years old or older.
1. Apply Discount on Products Use a dictionary comprehension to reduce the price of products priced above $50 by 10%.
1. Get Unique Product IDs Purchased by Adults Use a set comprehension to identify the unique product IDs purchased by adult customers.
1. Calculate Total Spend Per Customer Transform the purchase log into a dictionary that summarizes the total amount spent by each customer.

**Expected Output**

**1. List of adult customers:**

```
['Alice', 'Charlie']
```

**2. Discounted product prices:**

```
{
    "P001": 45.00,
    "P002": 54.00,
    "P003": 108.00,
    "P004": 30.00
}
```

**2. Unique product IDs purchased by adults:**

```
{'P001', 'P002', 'P003', 'P004'}
```

**4. Total spend per customer:**

```
{
    "Alice": 120.00,
    "Charlie": 270.00,
    "Bob": 324.00,
    "Diana: 54.00
}
```
"""

# Customer data: (name, age)
customers = [("Alice", 25), ("Bob", 17), ("Charlie", 35), ("Diana", 16)]

# Product data: {product_id: price}
products = {
    "P001": 45.00,
    "P002": 60.00,
    "P003": 120.00,
    "P004": 30.00
}

# Purchase log: (customer_name, product_id, quantity)
purchases = [
    ("Alice", "P001", 2),
    ("Charlie", "P002", 1),
    ("Bob", "P003", 3),
    ("Alice", "P004", 1),
    ("Charlie", "P003", 2),
    ("Diana", "P002", 1)
]

# Step 1: Filter adult customers
adult_customers = [name for name, age in customers if age >= 18]
print("Adult Customers:", adult_customers)

# Step 2: Apply discount to products priced above $50
discounted_products = {pid: (price * 0.9 if price > 50 else price) for pid, price in products.items()}
print("Discounted Products:", discounted_products)

# Step 3: Get unique product IDs purchased by adults
adult_purchases = {product_id for customer, product_id, _ in purchases if customer in adult_customers}
print("Unique Product IDs Purchased by Adults:", adult_purchases)

# Step 4: Calculate total spend per customer
total_spend = {
    customer: sum(
        discounted_products[product_id] * quantity
        for _, product_id, quantity in purchases if customer == _
    )
    for customer, _ in customers
}
print("Total Spend per Customer:", total_spend)