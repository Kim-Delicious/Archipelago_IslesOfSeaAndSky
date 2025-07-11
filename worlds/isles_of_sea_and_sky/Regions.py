from BaseClasses import MultiWorld


def link_isles_of_sea_and_sky_areas(world: MultiWorld, player: int):
    for (region_exit, region) in mandatory_connections:
        world.get_entrance(region_exit, player).connect(world.get_region(region, player))


# (Region name, list of exits)
## NOTE: Does not take into account for Phoenix Flute
isles_of_sea_and_sky_regions = [
    ("Menu",                        ["New Game"]),

    ("Ancient Isle",                ["Ancient East Exit", "Ancient West Exit", "Ancient North Exit", "Abstract Phoenix Exit"]),

    ("Stony Cliffs",                ["Stony Exit To Post-Rune", "Stony West Exit", "Stony East Exit"]),
    ("Stony Cliffs Post-Rune",      ["Stony Post-Rune Exit"]),
    ("Stony Cliffs NW",             ["Stony NW East Exit", "Stony NW West Exit", "Stony Phoenix"]),

    ("Tidal Reef",                  ["Tidal Exit", "Tidal Exit To Post-Rune", "Tidal Exit To S",]),
    ("Tidal Reef S",                ["Tidal S Exit", "Tidal S Exit To Post-Rune", "Tidal Phoenix"]),
    ("Tidal Reef Post-Rune",        ["Tidal Exit From Post-Rune", "Tidal S Entrance From Post-Rune"]),

    ("Raging Volcano",              ["Raging Exit", "Raging Exit To Post-Rune", "Raging Exit To NE"]),
    ("Raging Volcano NE",           ["Raging NE Exit", "Raging Phoenix"]),
    ("Raging Volcano Post-Rune",    ["Raging Exit From Post-Rune"]),

    ("Frozen Spire",                ["Frozen Exit", "Frozen Exit To Post-Rune"]),
    ("Frozen Spire Post-Rune",      ["Frozen Exit From Post-Rune", "Frozen Phoenix"]),
    ("Serpent Stacks",              ["Serpent Exit", "Serpent Exit To Post-Rune"]),
    ("Serpent Stacks Post-Rune",    ["Serpent Exit From Post-Rune"]),
    ("Sanctum",                     ["Sanctum Exit", "Elemental Rock Path"]),
    ("Sanctum Peak",                []),

    ("Rolling Rocks",               ["Rolling Exit", "Rolling Exit To Post-Rune"]),
    ("Rolling Rocks Post-Rune",     ["Rolling Post-Rune Exit"]),

    ("Aggro Crag",                  ["Aggro Exit"]),
    ("Locked",                      ["Locked Exit"]),
    ("Lost Landing",                ["Lost Exit", "Lost Phoenix"]),
    ("Star Tropic",                 ["Star East Exit", "Star West Exit"]),
    ("Sunken Island",               ["Sunken Exit"]),
    ("Sea Nunatak",                 ["Nunatak Exit"]),
    ("Shoal",                       ["Shoal Exit"]),
    ("Beast Bridge",                ["Beast Exit", "Beast Bridge Phoenix"]),
    ("Phoenix Hub",                 ["Lost Phoenix Entrance", "Stony Phoenix Entrance", "Tidal Phoenix Entrance",
                                     "Raging Phoenix Entrance", "Frozen Phoenix Entrance", "Beast Bridge Phoenix Entrance"]),

    ("Topaz Sea",                   ["Ancient East Entrance", "Stony East Entrance", "Diamond Sea West Entrance",
                                     "Ruby Sea West Entrance", "Rolling West Entrance", "Rolling East Entrance"]),
    ("Sapphire Sea",                ["Stony West Entrance", "Tidal Entrance", "Sapphire Sea Exit", "Aggro Entrance"]),
    ("Obsidian Sea",                ["Ancient West Entrance", "Serpent Entrance", "Locked Entrance", "Serpent Whirlpool"]),
    ("Ruby Sea",                    ["Ruby Whirlpool", "Star East Entrance", "Sunken Entrance", "Raging Entrance"]),
    ("Diamond Sea",                 ["Nunatak Entrance", "Shoal Entrance", "Diamond Whirlpool", "Diamond Sea Exit"]),
    ("North Diamond Sea",           ["Frozen Entrance", "North Diamond Sea South Exit", "North Diamond Sea East Exit"]),
    ("Northeast Sea",               ["Northeast Sea Exit"]),
    ("Beast Sea",                   ["Beast Entrance", "Beast Sea Exit"]),
    ("Lost Sea",                    ["Lost Sea Exit", "Lost Entrance", "Star West Entrance", "Lost Whirlpool"]),
]

# (Entrance, region pointed to)
mandatory_connections = [
    ("New Game",                        "Ancient Isle"),
    ("Elemental Rock Path",             "Sanctum Peak"),

    ("Ancient East Exit",               "Topaz Sea"),
    ("Ancient West Exit",               "Obsidian Sea"),
    ("Ancient North Exit",              "Sanctum"),
    ("Abstract Phoenix Exit",           "Phoenix Hub"), # Logic linchpin for accessing things early

    ("Stony East Exit",                 "Topaz Sea"),
    ("Stony West Exit",                 "Stony Cliffs NW"),
    ("Stony Exit To Post-Rune",         "Stony Cliffs Post-Rune"),
    ("Stony Post-Rune Exit",            "Stony Cliffs"),
    ("Stony NW West Exit",              "Sapphire Sea"),
    ("Stony NW East Exit",              "Stony Cliffs"),
    ("Stony Phoenix",                   "Phoenix Hub"),

    ("Tidal Exit",                      "Sapphire Sea"),
    ("Tidal Exit To Post-Rune",         "Tidal Reef Post-Rune"),
    ("Tidal S Exit To Post-Rune",       "Tidal Reef Post-Rune"),
    ("Tidal Exit From Post-Rune",       "Tidal Reef"),
    ("Tidal S Exit",                    "Tidal Reef"),
    ("Tidal S Entrance From Post-Rune", "Tidal Reef S"),
    ("Tidal Exit To S",                 "Tidal Reef S"),
    ("Tidal Phoenix",                   "Phoenix Hub"),

    ("Raging Exit",                     "Ruby Sea"),
    ("Raging Exit To Post-Rune",        "Raging Volcano Post-Rune"),
    ("Raging Exit From Post-Rune",      "Raging Volcano"),
    ("Raging NE Exit",                  "Raging Volcano"),
    ("Raging Exit To NE",               "Raging Volcano NE"),
    ("Raging Phoenix",                  "Phoenix Hub"),

    ("Frozen Exit",                     "North Diamond Sea"),
    ("Frozen Exit To Post-Rune",        "Frozen Spire Post-Rune"),
    ("Frozen Exit From Post-Rune",      "Frozen Spire"),
    ("Frozen Phoenix",                  "Phoenix Hub"),
    ("Serpent Exit",                    "Obsidian Sea"),
    ("Serpent Exit To Post-Rune",       "Serpent Stacks Post-Rune"),
    ("Serpent Exit From Post-Rune",     "Serpent Stacks"),
    ("Sanctum Exit",                    "Ancient Isle"),

    ("Ancient East Entrance",           "Ancient Isle"),
    ("Ancient West Entrance",           "Ancient Isle"),
    ("Stony East Entrance",             "Stony Cliffs"),
    ("Stony West Entrance",             "Stony Cliffs NW"),
    ("Tidal Entrance",                  "Tidal Reef"),
    ("Raging Entrance",                 "Raging Volcano"),
    ("Frozen Entrance",                 "Frozen Spire"),
    ("North Diamond Sea South Exit",    "Diamond Sea"),
    ("North Diamond Sea East Exit",     "Northeast Sea"),
    ("Serpent Entrance",                "Serpent Stacks"),

    ("Rolling East Entrance",           "Rolling Rocks"),
    ("Rolling West Entrance",           "Rolling Rocks"),

    ("Aggro Entrance",                  "Aggro Crag"),
    ("Locked Entrance",                 "Locked"),
    ("Lost Entrance",                   "Lost Landing"),
    ("Star East Entrance",              "Star Tropic"),
    ("Star West Entrance",              "Star Tropic"),
    ("Sunken Entrance",                 "Sunken Island"),
    ("Nunatak Entrance",                "Sea Nunatak"),
    ("Shoal Entrance",                  "Shoal"),
    ("Beast Entrance",                  "Beast Bridge"),
    ("Beast Bridge Phoenix",            "Phoenix Hub"),

    ("Lost Phoenix Entrance",           "Lost Landing"),
    ("Stony Phoenix Entrance",          "Stony Cliffs NW"),
    ("Tidal Phoenix Entrance",          "Tidal Reef S"),
    ("Raging Phoenix Entrance",         "Raging Volcano NE"),
    ("Frozen Phoenix Entrance",         "Frozen Spire Post-Rune"),
    ("Beast Bridge Phoenix Entrance",   "Beast Bridge"),

    ("Diamond Sea West Entrance",       "Diamond Sea"),
    ("Diamond Whirlpool",               "Obsidian Sea"),
    ("Ruby Sea West Entrance",          "Ruby Sea"),
    ("Sapphire Sea Exit",               "Obsidian Sea"),
    ("Serpent Whirlpool",               "Diamond Sea"),
    ("Ruby Whirlpool",                  "Beast Sea"),
    ("Diamond Sea Exit",                "North Diamond Sea"),
    ("Northeast Sea Exit",              "North Diamond Sea"),
    ("Beast Sea Exit",                  "Diamond Sea"),
    ("Lost Sea Exit",                   "Obsidian Sea"),
    ("Lost Phoenix",                    "Phoenix Hub"),
    ("Lost Whirlpool",                  "Northeast Sea"),

    ("Rolling Exit",                    "Topaz Sea"),
    ("Rolling Exit To Post-Rune",       "Rolling Rocks Post-Rune"),
    ("Rolling Post-Rune Exit",          "Rolling Rocks"),

    ("Aggro Exit",                      "Sapphire Sea"),
    ("Locked Exit",                     "Obsidian Sea"),
    ("Nunatak Exit",                    "Diamond Sea"),
    ("Star East Exit",                  "Ruby Sea"),
    ("Star West Exit",                  "Lost Sea"),
    ("Shoal Exit",                      "Diamond Sea"),
    ("Sunken Exit",                     "Ruby Sea"),
    ("Beast Exit",                      "Beast Sea"),
    ("Lost Exit",                       "Lost Sea"),
]

