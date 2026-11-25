from potion import Potion

# ==================================================
# Potion Data
# ==================================================

POTIONS = {

    "Small Healing Potion": Potion(
        "Small Healing Potion",
        heal_amount=30,
        description="Restores a small amount of health.",
        value=15,
        rarity="Common"
    ),

    "Medium Healing Potion": Potion(
        "Medium Healing Potion",
        heal_amount=70,
        description="Restores a moderate amount of health.",
        value=35,
        rarity="Rare"
    ),

    "Large Healing Potion": Potion(
        "Large Healing Potion",
        heal_amount=120,
        description="Restores a large amount of health.",
        value=60,
        rarity="Epic"
    )

}