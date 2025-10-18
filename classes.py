from typing import Optional, Set

class Product:
    def __init__(self, name: str, category: str, brand_name: str, skin_type: list[str], skin_concern: list[str], active_ingredients: list[str], key_ingredients: list[str], warning: Optional[str] = None):
        self.name = name
        self.category = category
        self.brand_name = brand_name
        self.skin_types = set(skin_type)
        self.concerns = set(skin_concern)
        self.__actives = set(active_ingredients)
        self.key_ingredients = key_ingredients
        self.__warning = warning

    def __has_overlap(self, a: set, b: set) -> bool:
        return bool(a & b)

    def matches_skin(self, skin_type: str) -> bool:
        return skin_type.lower() in self.skin_types

    def challenges(self, concerns: Set[str]) -> bool:
        return self.__has_overlap(self.concerns, concerns)

    def get_actives(self) -> Set[str]:
        return self.__actives

    def get_warning(self) -> Optional[str]:
        return self.__warning

    def add_active(self, ingredient: str) -> Set[str]:
        self.__actives.add(ingredient)
        return self.__actives

    def get_key_ingredients(self) -> list[str]:
        if isinstance(self.key_ingredients, str):
            return [i.strip() for i in self.key_ingredients.split(",") if i.strip()]
        return []

    def __lt__(self, other: "Product"):
        return self.name < other.name

    def __str__(self):
        return f"{self.name} ({self.category}) - Brand: {self.brand_name}"


    


class SkinProfile:
    def __init__(self, skin_type: str, concerns: Set[str], exclusions: Optional[Set[str]] = None):
        self.skin_type = skin_type.lower()
        self.concerns = concerns 
        self.exclusions = exclusions or set()

    def allows(self, product: Product) -> bool:
        if product.brand_name.lower() in self.exclusions:
            return False
        return product.matches_skin(self.skin_type) and product.challenges(self.concerns)
    
    def __str__(self):
        return f"{self.skin_type}, Concerns: {', ' .join(self.concenrs)}"