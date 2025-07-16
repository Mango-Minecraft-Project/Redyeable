import json

from global_variable import GENERATED, NAMESPACE, COLORS, make_dir

DATA = make_dir(GENERATED / "data", rmdir=True)
# RESOURCE = make_dir(GENERATED / "assets", rmdir=True)

ingredients = [
    "banner",
    "candle",
    "concrete",
    "concrete_powder",
    "glass_pane",
    "glazed_terracotta",
]

def main():
    for ingredient in ingredients:
        with open(make_dir(DATA / NAMESPACE / f"tags/item/{ingredient}s.json"), 'w') as file:
            json.dump({"replace": False, "values": [f"minecraft:{color}_{ingredient}" for color in COLORS]}, file, indent=4)

        for color in COLORS:
            data = { # type: ignore
                    "type": "minecraft:crafting_shapeless",
                    "pattern": ["AB"],
                    "key": {
                        "A": {"tag": f"minecraft:{ingredient}s"},
                        "B": {"item": f"minecraft:{color}_dye"},
                    },
                    "result": {
                        "item": f"minecraft:{color}_{ingredient}",
                        "count": 1,
                    },
                }

            # for 1.21 below
            with open(make_dir(DATA / NAMESPACE / f"recipes/{color}_{ingredient}.json"), 'w') as file:
                json.dump(data, file, indent=4)
            # for 1.21 and above
            with open(make_dir(DATA / NAMESPACE / f"recipe/{color}_{ingredient}.json"), 'w') as file:
                json.dump(data, file, indent=4)
                