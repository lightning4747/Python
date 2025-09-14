class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
    
    def update_stock(self, quantity):
        if self.stock + quantity >= 0:
            self.stock += quantity
            return True
        return False
    
    def __str__(self):
        return f"{self.name} - ${self.price:.2f} ({self.stock} in stock)"

class ShoppingCart:
    def __init__(self):
        self.items = {}  # product_id: quantity
    
    def add_item(self, product, quantity=1):
        if product.product_id in self.items:
            self.items[product.product_id] += quantity
        else:
            self.items[product.product_id] = quantity
    
    def remove_item(self, product, quantity=1):
        if product.product_id in self.items:
            if self.items[product.product_id] <= quantity:
                del self.items[product.product_id]
            else:
                self.items[product.product_id] -= quantity
    
    def calculate_total(self, products):
        total = 0
        for product_id, quantity in self.items.items():
            product = products[product_id]
            total += product.price * quantity
        return total
    
    def __str__(self):
        if not self.items:
            return "Cart is empty"
        return f"Cart contains {sum(self.items.values())} items"

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cart = ShoppingCart()
    
    def checkout(self, products):
        total = self.cart.calculate_total(products)
        # Process payment here (simplified)
        print(f"Checkout completed. Total: ${total:.2f}")
        # Update product stocks
        for product_id, quantity in self.cart.items.items():
            products[product_id].update_stock(-quantity)
        self.cart = ShoppingCart()  # Empty the cart

# Test the system
# Create products
products = {
    1: Product(1, "Python Book", 29.99, 10),
    2: Product(2, "Coffee Mug", 9.99, 20),
    3: Product(3, "T-Shirt", 19.99, 15)
}

# Create a customer
customer = Customer("Alice", "alice@example.com")

# Add items to cart
customer.cart.add_item(products[1], 2)
customer.cart.add_item(products[2], 1)

print("Cart contents:")
print(products[1], f"x {customer.cart.items[1]}")
print(products[2], f"x {customer.cart.items[2]}")

print(f"\nTotal: ${customer.cart.calculate_total(products):.2f}")

# Checkout
customer.checkout(products)

print(f"\nStock after checkout:")
for product in products.values():
    print(product)