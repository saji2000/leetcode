Order = {
"country": "USA",
"items": [{"product": "mouse", "quantity": 10}, {"product":"laptop", "quantity": 5}]
}


shipping_cost = [{
    "country":"USA",
    "items":{
        "product":"laptop",
        "costs": [
            {"minQuantity": 1, "maxQuantity": 3, "cost": 500},
            {"minQuantity": 4, "maxQuantity": 6, "cost": 400}
        ]
    }
}]