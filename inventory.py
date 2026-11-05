inventory = []

def create_product(
        sku,                            # Stock keeping unit
        name, 
        brand,
        size_ml,
        cost_price,
        selling_price,
        stock_quantity,
        reorder_level = 3
):
    if not sku.strip():
        raise ValueError("SKU cannot be empty.")
    if not name.strip():
        raise ValueError("\nProduct name cannot be empty ! ")
    if not brand.strip():
        raise ValueError("\nCannot accept perfume without brandname ! ")
    if size_ml <= 0:
        raise ValueError("\nSize must be greater than zero.")
    if cost_price < 0 or selling_price < 0:
        raise ValueError("\nPrices can't be negative ! ")
    if stock_quantity < 0:
        raise ValueError("\nQuantity can't be less than zero ! ")
    if reorder_level < 0:
        raise ValueError("Reorders can't be less than zero ! ")

    sku = sku.strip().upper()

    product = {
    "sku": sku,
    "name": name,
    "brand": brand,
    "size_ml": size_ml,
    "cost_price": cost_price,
    "selling_price": selling_price,
    "stock_quantity": stock_quantity,
    "reorder_level": reorder_level
         }
    return product

def add_product(product):
    inventory.append(product)

def view_products():
    if not inventory:
        print("\nNo Products in Inventory ! ")
        return
    
    for i, products in enumerate(inventory, start = 1):
        print(
            f"{i}. {products['name']} |"
            f"Brand: {products['brand']} |"
            f"SKU: {products['sku']} |"
            f"Price: {products['selling_price']} |"
            f"Stock: {products['stock_quantity']}"
        )
    
def find_product(sku):

    sku = sku.strip().upper()

    for product in inventory:
        if sku == product['sku']:
            return product
    return None


amber_oud = create_product(
    sku="AMB001",
    name="Amber Oud",
    brand="Ajmal",
    size_ml=100,
    cost_price=1200,
    selling_price=1800,
    stock_quantity=8
)

add_product(amber_oud)



print(find_product("amb001"))
print(find_product(" AMB001 "))
print(find_product("XYZ999"))