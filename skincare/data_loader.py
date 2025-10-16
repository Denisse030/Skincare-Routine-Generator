import json
from skincare.classes import Product

def load_products(path: str):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)

    except FileNotFoundError:
        print("Error: products.json not found.")
        return [], {}
    
    except json.JSONDecodeError:
        print("Error: invalif json format.")
        return [], {}
    
    else:
        products = []
        for item in data["products"]:
            key = item.get("key_ingredients", "")
            if not isinstance(key, str):
                key = ""
            
            products.append(
                Product(
                    name = item["name"],
                    category = item["category"],
                    brand_name = item["brand_name"],
                    skin_type = item["skin_type"],
                    skin_concern = item["skin_concern"],
                    active_ingredients = item.get["active_ingredients", []],
                    key_ingredients = key,
                    warning = item.get("warning")
                )
            )

        return products, {"brand": "Skin 1004"}