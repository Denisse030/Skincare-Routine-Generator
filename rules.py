from classes import Product, SkinProfile 
from typing import Optional, Set, Tuple, Dict, Iterable, List, Any

_CONCERN_FIXES = {"pores": "pore_tightening", "pore": "pore_tightening"}

def _normal_concerns (concerns: Set[str]) -> Set[str]:
    out = set()
    for c in concerns:
        c.strip().lower()
        out.add(_CONCERN_FIXES.get(c, c))
    return out

def _match_results(meta: Dict[str, Any],) -> Tuple[int, int, int]:
    r = meta.get("match_results", {}) if isinstance(meta, dict) else {}
    r_skin = int(r.get("skin_match", 1))
    r_concern = int(r.get("concern_match", 1))
    r_key = int(r.get("key_match", 0))
    return r_skin, r_concern, r_key

def _overall(p: Product, profile: SkinProfile, meta: Dict[str, Any]) -> Optional[Product]:
    r_skin, r_concern, r_key = _match_results(meta)
    o = 0
    if p.matches_skin(profile.skin_type):
        o += r_skin
    if p.challenges(profile.concerns):
        o += r_concern
    preferred = {i.strip().lower() for i in meta.get("preferred_key_ingredients", [])}
    if preferred and (set(i.lower() for i in p.get_key_ingredients()) & preferred):
        o += r_key
    return o

def _best_choice(category: str, profile: SkinProfile, catalog: Iterable[Product], meta: dict[str, Any]) -> Optional[Product]:
    users: List[Product] = [p for p in catalog if p.category.strip().lower() == category]
    allowed = [p for p in users if profile.allows(p)]
    if not allowed:
        return None
    ranked = sorted(
        allowed,
        key = lambda p: (_overall(p, profile, meta), p.category, p.name),
        reverse = True
    ) 
    return ranked [0]

def weekly_facemask(profile: SkinProfile, catalog: Iterable[Product], meta: Dict[str, Any]) -> Optional[Product]:
    masks = [p for p in catalog if p.category.strip().lower() == "facemask"]
    if not masks:
        return None
    masks.sort(key = lambda p:_overall(p, profile, meta), reverse = True)
    return masks[0]

def generate(profile: SkinProfile, catalog: Iterable[Product], meta: Dict[str, Any]) -> Dict[str, Any]:
    profile.concerns = _normal_concerns(profile.concerns)
    notes: List[str] = []

    REQUIRED_CATEGORIES = ["cleanser", "toner", "ampoule", "serum", "treatment", "moisturizer","sunscreen", "facemask", "toner_mist"]
    DEFAULT_AM = ("cleanser", "toner", "ampoule", "serum", "moisturizer", "sunscreen")
    DEFAULT_PM = ("cleanser", "toner", "ampoule", "serum", "treatment", "moisturizer", "facemask")

    am, pm = [], []

    for cat in DEFAULT_AM:
        p = _best_choice(cat, profile, catalog, meta)
        if p and p not in am:
            am.append(p)

    for cat in DEFAULT_PM:
        p = _best_choice(cat, profile, catalog, meta)
        if p and p not in pm:
            pm.append(p)
            w = p.get_warning()
            if w:
                notes.append(f"WARNING: {p.name} - {w}")

    mask = weekly_facemask(profile, catalog, meta)
    if mask:
        notes.append(f"Facemask: Use twice a week, preferably at night for best results. Suggested mask for you: {mask.name}.")

    return {"brand": meta.get("brand", "Skin 1004"), "am": am, "pm":pm, "notes": notes}