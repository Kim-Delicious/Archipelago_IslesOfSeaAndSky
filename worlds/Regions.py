from BaseClasses import MultiWorld


def link_isles_of_sea_and_sky_areas(world: MultiWorld, player: int):
    for (exit, region) in mandatory_connections:
        world.get_entrance(exit, player).connect(world.get_region(region, player))


# (Region name, list of exits)
## NOTE: Does not take into account for Phoenix Flute
isles_of_sea_and_sky_regions = [
    ("Menu", ["New Game"]),

    ("Ancient Isle", ["Ancient Eastern Exit", "Ancient Western Exit", "Ancient Northern Exit"]),
    ("Stoney Cliffs", ["Stoney Eastern Exit", "Stoney Western Exit"]),
    ("Tidal Reef", ["Tidal Southern Exit"]),
    ("Raging Volcano", ["Raging Exit"]),
    ("Frozen Spire", ["Frozen Exit"]),
    ("Serpent Stacks", ["Serpent Exit"]),
    ("Sanctum", ["Sanctum Exit"]),

    ("Rolling Rocks", ["Rolling Eastern Exit", "Rolling Western Exit"]),
    ("Aggro Crag", ["Aggro Exit"]),
    ("Locked", ["Locked Exit"]),
    ("Lost Landing", ["Lost Exit"]),
    ("Star Tropic", ["Star Eastern Exit", "Star Western Exit"]),
    ("Sunken Island", ["Sunken Exit"]),
    ("Sea Nanatak", ["Nanatak Exit"]),
    ("Shoal", ["Shoal Exit"]),
    ("Beast Bridge", ["Beast Exit"]),

    ("Topaz Sea", ["Ancient Eastern Entrance", "Stoney Eastern Entrance", "Diamond Sea Western Entrance", "Ruby Sea Western Entrance", "Rolling Western Entrance", "Rolling Eastern Entrance"]),
    ("Sapphire Sea", ["Stoney Western Entrance", "Tidal Entrance", "Sapphire Sea Exit", "Aggro Entrance"]),
    ("Obsidian Sea", ["Ancient Western Entrance", "Serpent Entrance", "Locked Entrance", "Serpent Whirlpool"]),
    ("Ruby Sea", ["Ruby Whirlpool", "Star Eastern Entrance", "Sunken Entrance"]),
    ("Diamond Sea", ["Nanatak Entrance", "Shoal Entrance", "Diamond Sea Exit"]),
    ("North Diamond Sea", ["Frozen Entrance"]),
    ("Northwest Sea", ["Northwest Sea Exit"]),
    ("Beast Sea", ["Beast Entrance", "Beast Sea Exit"]),
    ("Lost Sea", ["Lost Sea Exit", "Lost Entrance", "Star Western Entrance", "Lost Whirlpool"]),
]

# (Entrance, region pointed to)
mandatory_connections = [
    ("New Game", "Ancient Isle"),

    ("Ancient Eastern Exit", "Topaz Sea"),
    ("Ancient Western Exit", "Obsidian Sea"),
    ("Ancient Northern Exit", "Sanctum"),
    ("Stoney Eastern Exit", "Topaz Sea"),
    ("Stoney Western Exit", "Sapphire Sea"),
    ("Tidal Exit", "Sapphire Sea"),
    ("Raging Exit", "Ruby Sea"),
    ("Frozen Exit", "Northern Diamond Sea"),
    ("Serpent Exit", "Obsidian Sea"),
    ("Sanctum Exit", "Ancient Isle"),

    ("Ancient Eastern Entrance", "Ancient Isle"),
    ("Ancient Western Entrance", "Ancient Isle"),
    ("Stoney Eastern Entrance", "Stoney Cliffs"),
    ("Stoney Western Entrance", "Stoney Cliffs"),
    ("Tidal Entrance", "Tidal Reef"),
    ("Raging Entrance", "Raging Volcano"),
    ("Frozen Entrance", "Frozen Spire"),
    ("Serpent Entrance", "Serpent Stacks"),

    ("Rolling Eastern Entrance", "Rolling Rocks"),
    ("Rolling Western Entrance", "Rolling Rocks"),
    ("Aggro Entrance", "Aggro Crag"),
    ("Locked Entrance", "Locked"),
    ("Lost Entrance", "Lost Landing"),
    ("Star Eastern Entrance", "Star Tropic"),
    ("Star Western Entrance", "Star Tropic"),
    ("Sunken Entrance", "Sunken Island"),
    ("Nanatak Entrance", "Sea Nanatak"),
    ("Shoal Entrance", "Shoal"),
    ("Beast Entrance", "Beast Bridge"),

    ("Diamond Sea Western Entrance", "Diamond Sea"),
    ("Ruby Sea Western Entrance", "Ruby Sea"),
    ("Sapphire Sea Exit", "Obsidian Sea"),
    ("Serpent Whirlpool", "Diamond Sea"),
    ("Ruby Whirlpool", "Beast Sea"),
    ("Diamond Sea Exit", "North Diamond Sea"),
    ("Northwest Sea Exit", "North Diamond Sea"),
    ("Beast Sea Exit", "Diamond Sea"),
    ("Lost Sea Exit", "Obsidian Sea"),
    ("Lost Whirlpool", "Northwest Sea"),

]
