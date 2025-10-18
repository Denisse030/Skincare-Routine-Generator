"""
CS521 Final Project - Denisse Benito Gutierrez
Class: CS521 - Fall 
Due Date: 10/18/25
Description of Project (1-2 sentence summary in your own words):
This program creates a personalized skincare routine using only Skin 1004 products. Once you've selected your skin type and concerns, it curates a full morning and night routine, adds notes for masks and treatments, includes product warnings, and lets you view key ingredients for each product.
"""
from data_loader import load_products
from classes import SkinProfile
from rules import generate
from typing import Tuple, List

VALID_SKIN_TYPES = {"dry", "oily", "combination", "sensitive"}
VALID_SKIN_CONCERNS = {"acne", "brightening", "calming", "soothing", "hydrating", "moisturizing", "improving", "glowing", "pore_tightening"}

def s_concerns(user_text: str) -> list[str]:
    """This parses the user's input for skin concerns and validates them against the allowed list."""
    tokens = [t.strip().lower() for t in (user_text or "").split(",") if t.strip()] 
    return [t for t in tokens if t in VALID_SKIN_CONCERNS]

def enter_skin_type():
    """This gives the user a prompt to input their skin type and validates the input."""
    while True:
        skin_raw = input("Enter your skin type (dry, oily, combination, sensitive): ").strip()
        if skin_raw.lower() in VALID_SKIN_TYPES:
            return [skin_raw.lower()], skin_raw.title()
        print("ERROR: Invalid input. Please choose from the following: ", ", ".join(sorted(VALID_SKIN_TYPES)))

def enter_skin_concerns() -> List[str]:
    """This gives the user a prompt to enter their skin concerns and validates that the user has entered at least two concerns from the allowed list."""
    print("\nAvailable Skin Concerns:")
    print("-- " + ", ".join(sorted(VALID_SKIN_CONCERNS)) + "\n")

    while True:
        concerns_raw = input("Enter your skin concerns seperated by commas (enter at least two): ").strip()
        concerns = s_concerns(concerns_raw)
        invalids = [c.strip() for c in concerns_raw.split(",") if c.strip().lower() not in VALID_SKIN_CONCERNS]

        if not concerns:
            print("\nERROR: Invalid or missing concerns. Please choose two from the list above.\n")
            continue
        if len(concerns) < 2:
            print("\nERROR: Please select at least two valid concerns for a more accurate routine.\n")
            continue
        if invalids: 
            print(f"\nERROR: These concerns were not recognized: {', '.join(invalids)}\n")
            continue
        return concerns
    
def output_routines(title: str, products):
    """This desplays the generated AM and PM skincare routines."""
    print(title)
    if products:
        for p in products:
            print(f"- {p.name}")
    else:
        print("(none)")

if __name__ == "__main__":
    """The main program handles the users interaction, data loading, and the generated routines."""

    print("Welcome to the Skincare Routine Generator! Tailored to Skin 1004 products.\n")

    products, meta = load_products("data/products.json") #loads the product data.
    skin_types, skin_display = enter_skin_type() 
    concerns = enter_skin_concerns()
    profile = SkinProfile(skin_types[0], set(concerns))
    routine = generate(profile, products, meta) # generates your personal routines.

    print(f"\n{routine['brand']} Routine for {skin_display} Skin\n") # displays the routines.
    output_routines("Your Morning Routine: ", routine["am"])
    print()
    output_routines("Your Night Routine: ", routine["pm"])

    if routine["notes"]: # displays the warnings and facemasks information.
        print("\nImportant Notes:\n ")
        for n in routine["notes"]:
            print(f"- {n}")

    choice = input("\nWould you like to take a look at the key ingredients inside your products? (yes/no): ").strip().lower() # has the user choose if they would like to view the key ingredients in their products.
    if choice in ("yes", "y"):
        print("\nKey Ingredients in your AM and PM routine: ")
        seen = set()
        for p in routine["am"] + routine["pm"]:
            if p.name not in seen:
                seen.add(p.name)
                if hasattr(p, "key_ingredients") and isinstance(p.key_ingredients, str):
                    ingredients = [i.strip() for i in p.key_ingredients.split(",") if i.strip()]
                    if ingredients:
                        ing_list = ", ".join(i.strip().title() for i in ingredients)
                        print(f"- {p.name}: {ing_list}")
                    else:
                        print(f"- {p.name}: none shown")
                else:
                    print(f"- {p.name}: choosen not to show")

    print("\nREMINDER: Always do a patch test before trying on new products to see how your skin reacts before applying them to your entire face.") # a final reminder for all users

    print("\n! End of Routine !") # the end :)