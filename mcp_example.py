class Product:
    def __init__(self, name, price, stock=None, supplier=None, shipping_details=None):
        self.name = name
        self.price = price
        self.stock = stock
        self.supplier = supplier
        self.shipping_details = shipping_details

    def __str__(self):
        return f"Product(name='{self.name}', price={self.price})"

class ProductContext:
    def __init__(self, product):
        self.product = product

    def get_display_info(self):
        # Catalog context: only basic info
        return f"- {self.product.name}: ${self.product.price:.2f}"

    def get_order_info(self):
        # Order processing context: more details
        if self.product.stock is None or self.product.supplier is None or self.product.shipping_details is None:
            return "Order information incomplete."
        return f"- {self.product.name} (Stock: {self.product.stock}, Supplier: {self.product.supplier}, Shipping: {self.product.shipping_details})"

# --- Demonstration ---

# Product instance with minimal initial data
my_product = Product("Laptop", 1200.00)

# --- Catalog Context ---
# We don't need stock, supplier, or shipping for the catalog view
catalog_context = ProductContext(my_product)
print("--- Catalog View ---")
print(catalog_context.get_display_info())

print("\n")

# --- Order Processing Context ---
# Now, let's enrich the product with data needed for order processing
my_product.stock = 50
my_product.supplier = "TechDistributors"
my_product.shipping_details = "2-3 business days"

order_context = ProductContext(my_product)
print("--- Order Processing View ---")
print(order_context.get_order_info())

# Demonstrating that the original product object is shared but interpreted differently
print("\n")
print("Original Product Object:")
print(my_product)
