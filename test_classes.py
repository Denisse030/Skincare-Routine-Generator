from classes import Product, SkinProfile
from rules import generate

person1 = Product(
    name="Tightening Toner",
    category="toner",
    brand_name="Skin 1004",
    skin_type=["oily", "sensitive"],
    skin_concern=["pore_tightening"],
    active_ingredients=[],
    key_ingredients=[""],
    warning=None
)

person2 = Product(
    name="Night Ampoule",
    category="treatment",
    brand_name="Skin 1004",
    skin_type=["oily"],
    skin_concern=["pore_tightening"],
    active_ingredients=[],
    key_ingredients=["retinol"],
    warning="Use only at night"
)

profile = SkinProfile("oily", {"pore_tightening"})
assert profile.allows(person1) is True, "Test has Failed: Tightening Toner should be allowed."
assert profile.allows(person2) is True, "Test has Failed: Night Ampoule should be allowed."
assert person1.challenges({"pore_tightening"}) is True, "Test has Failed:Product should be challenge 'pore_tightening' concerns."
assert person1.challenges({"glowing"}) is False, "Test has Failed:Product should not be challenges 'glowing' concerns."

meta = {"brand": "Skin 1004"}
routine = generate(profile, [person1, person2], meta)
assert "am" in routine and "pm" in routine, "Test has Failed: routine is missing am and pm keys."
assert isinstance(routine["am"], list), "Test has Failed: am routine is supposed to be a list."
assert isinstance(routine["pm"], list), "Test has Failed: pm routine is supposed to be a list."
assert routine["brand"] == "Skin 1004", "Test has Failed: brand date is incorrect."

print("Tests have been sucessfull.")