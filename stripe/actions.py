def calculate_shipping_cost(order, shipping_costs):
    """
    Calculate total shipping cost for an order based on country and quantity-based pricing tiers.
    
    Args:
        order (dict): Contains country and list of items with product names and quantities
        shipping_costs (list): List of shipping cost rules per country and product
    
    Returns:
        float: Total shipping cost
    """
    total_cost = 0.0
    country = order.get("country")
    items = order.get("items", [])
    
    country_costs = None
    for cost_rule in shipping_costs:
        if cost_rule["country"] == country:
            country_costs = cost_rule
            break
    
    if country_costs is None:
        return 0.0  # Return 0 if no shipping costs defined for the country
    
    # Process each item in the order
    for order_item in items:
        product = order_item.get("product")
        quantity = order_item.get("quantity", 0)
        
        # Find product-specific cost rules
        product_costs = None
        for item_rule in country_costs.get("items", []):
            if item_rule["product"] == product:
                product_costs = item_rule
                break
        
        if product_costs is None:
            continue  # Skip if no cost rules for this product
        
        # Calculate cost based on quantity tiers
        remaining_quantity = quantity
        # Sort tiers by minQuantity for correct order
        sorted_tiers = sorted(product_costs.get("costs", []), key=lambda x: x["minQuantity"])
        for tier in sorted_tiers:
            if remaining_quantity <= 0:
                break
            # Quantities within this tier
            tier_quantity = min(
                remaining_quantity,
                tier["maxQuantity"] - tier["minQuantity"] + 1
            )
            if tier_quantity > 0:
                total_cost += tier_quantity * tier["cost"]
                remaining_quantity -= tier_quantity
    
    return total_cost

# Example usage
if __name__ == "__main__":
    order = {
        "country": "USA",
        "items": [
            {"product": "mouse", "quantity": 10},
            {"product": "laptop", "quantity": 5}
        ]
    }
    
    shipping_costs = [
        {
            "country": "USA",
            "items": [
                {
                    "product": "laptop",
                    "costs": [
                        {"minQuantity": 1, "maxQuantity": 3, "cost": 500},
                        {"minQuantity": 4, "maxQuantity": 6, "cost": 400}
                    ]
                },
                {
                    "product": "mouse",
                    "costs": [
                        {"minQuantity": 1, "maxQuantity": 5, "cost": 50},
                        {"minQuantity": 6, "maxQuantity": 10, "cost": 40}
                    ]
                }
            ]
        }
    ]
    
    total = calculate_shipping_cost(order, shipping_costs)
    print(f"Total shipping cost: ${total:.2f}")