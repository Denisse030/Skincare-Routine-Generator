from typing import Optional, Set

class Product:
    """This class represents a skincare product with the following properties like name, category, brand, skin types, etc.."""
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
        """This checkes if the product is suitable for a specific skin type."""
        return skin_type.lower() in self.skin_types

    def challenges(self, concerns: Set[str]) -> bool:
        """This determines if the product targets the user's inputed concerns."""
        return self.__has_overlap(self.concerns, concerns)

    def get_actives(self) -> Set[str]:
        """This returns a set a active ingredients found in specific products."""
        return self.__actives

    def get_warning(self) -> Optional[str]:
        """This returns specific products warning messages."""
        return self.__warning

    def add_active(self, ingredient: str) -> Set[str]:
        """This adds a new active ingredient to the product and then returrns the activated set."""
        self.__actives.add(ingredient)
        return self.__actives

    def get_key_ingredients(self) -> list[str]:
        """This returns a list of the product's key ingredients."""
        if isinstance(self.key_ingredients, str):
            return [i.strip() for i in self.key_ingredients.split(",") if i.strip()]
        return []

    def __lt__(self, other: "Product"):
        return self.name < other.name

    def __str__(self):
        return f"{self.name} ({self.category}) - Brand: {self.brand_name}"


class SkinProfile:
    """This class represents the users perosnalized skin profile. This includes skin type, concerns, and exclusions."""
    def __init__(self, skin_type: str, concerns: Set[str], exclusions: Optional[Set[str]] = None):
        """This initializes a skin profile instance with skin type, concerns, and optional exclusions."""
        self.skin_type = skin_type.lower()
        self.concerns = concerns 
        self.exclusions = exclusions or set()

    def allows(self, product: Product) -> bool:
        """This checks whether or not a product is suitable with the user's personalized skin profile."""
        if product.brand_name.lower() in self.exclusions:
            return False
        return product.matches_skin(self.skin_type) and product.challenges(self.concerns)
    
    def __str__(self):
        return f"{self.skin_type}, Concerns: {', ' .join(self.concenrs)}"