from BaseClasses import MultiWorld


def link_isles_of_sea_and_sky_areas(world: MultiWorld, player: int):
    for (exit, region) in mandatory_connections:
        world.get_entrance(exit, player).connect(world.get_region(region, player))


# (Region name, list of exits)
## NOTE: Does not take into account for Phoenix Flute
isles_of_sea_and_sky_regions = [
    ("Menu", ["New Game"]),

    ("Ancient Isle", ["Ancient East Exit", "Ancient West Exit", "Ancient North Exit"]),
    ("Stony Cliffs", ["Stony East Exit", "Stony West Exit"]),
    ("Tidal Reef", ["Tidal Exit"]),
    ("Raging Volcano", ["Raging Exit"]),
    ("Frozen Spire", ["Frozen Exit"]),
    ("Serpent Stacks", ["Serpent Exit"]),
    ("Sanctum", ["Sanctum Exit", "Elemental Rock Path"]),
    ("Sanctum Peak", []),

    ("Rolling Rocks", ["Rolling East Exit", "Rolling West Exit"]),
    ("Aggro Crag", ["Aggro Exit"]),
    ("Locked", ["Locked Exit"]),
    ("Lost Landing", ["Lost Exit"]),
    ("Star Tropic", ["Star East Exit", "Star West Exit"]),
    ("Sunken Island", ["Sunken Exit"]),
    ("Sea Nunatak", ["Nunatak Exit"]),
    ("Shoal", ["Shoal Exit"]),
    ("Beast Bridge", ["Beast Exit"]),

    ("Topaz Sea", ["Ancient East Entrance", "Stony East Entrance", "Diamond Sea West Entrance", "Ruby Sea West Entrance", "Rolling West Entrance", "Rolling East Entrance"]),
    ("Sapphire Sea", ["Stony West Entrance", "Tidal Entrance", "Sapphire Sea Exit", "Aggro Entrance"]),
    ("Obsidian Sea", ["Ancient West Entrance", "Serpent Entrance", "Locked Entrance", "Serpent Whirlpool"]),
    ("Ruby Sea", ["Ruby Whirlpool", "Star East Entrance", "Sunken Entrance", "Raging Entrance"]),
    ("Diamond Sea", ["Nunatak Entrance", "Shoal Entrance", "Diamond Sea Exit"]),
    ("North Diamond Sea", ["Frozen Entrance"]),
    ("Northwest Sea", ["Northwest Sea Exit"]),
    ("Beast Sea", ["Beast Entrance", "Beast Sea Exit"]),
    ("Lost Sea", ["Lost Sea Exit", "Lost Entrance", "Star West Entrance", "Lost Whirlpool"]),
]

# (Entrance, region pointed to)
mandatory_connections = [
    ("New Game", "Ancient Isle"),
    ("Elemental Rock Path", "Sanctum Peak"),

    ("Ancient East Exit", "Topaz Sea"),
    ("Ancient West Exit", "Obsidian Sea"),
    ("Ancient North Exit", "Sanctum"),
    ("Stony East Exit", "Topaz Sea"),
    ("Stony West Exit", "Sapphire Sea"),
    ("Tidal Exit", "Sapphire Sea"),
    ("Raging Exit", "Ruby Sea"),
    ("Frozen Exit", "North Diamond Sea"),
    ("Serpent Exit", "Obsidian Sea"),
    ("Sanctum Exit", "Ancient Isle"),

    ("Ancient East Entrance", "Ancient Isle"),
    ("Ancient West Entrance", "Ancient Isle"),
    ("Stony East Entrance", "Stony Cliffs"),
    ("Stony West Entrance", "Stony Cliffs"),
    ("Tidal Entrance", "Tidal Reef"),
    ("Raging Entrance", "Raging Volcano"),
    ("Frozen Entrance", "Frozen Spire"),
    ("Serpent Entrance", "Serpent Stacks"),

    ("Rolling East Entrance", "Rolling Rocks"),
    ("Rolling West Entrance", "Rolling Rocks"),
    ("Aggro Entrance", "Aggro Crag"),
    ("Locked Entrance", "Locked"),
    ("Lost Entrance", "Lost Landing"),
    ("Star East Entrance", "Star Tropic"),
    ("Star West Entrance", "Star Tropic"),
    ("Sunken Entrance", "Sunken Island"),
    ("Nunatak Entrance", "Sea Nunatak"),
    ("Shoal Entrance", "Shoal"),
    ("Beast Entrance", "Beast Bridge"),

    ("Diamond Sea West Entrance", "Diamond Sea"),
    ("Ruby Sea West Entrance", "Ruby Sea"),
    ("Sapphire Sea Exit", "Obsidian Sea"),
    ("Serpent Whirlpool", "Diamond Sea"),
    ("Ruby Whirlpool", "Beast Sea"),
    ("Diamond Sea Exit", "North Diamond Sea"),
    ("Northwest Sea Exit", "North Diamond Sea"),
    ("Beast Sea Exit", "Diamond Sea"),
    ("Lost Sea Exit", "Obsidian Sea"),
    ("Lost Whirlpool", "Northwest Sea"),

    ("Rolling East Exit", "Topaz Sea"),
    ("Rolling West Exit", "Topaz Sea"),
    ("Aggro Exit", "Sapphire Sea"),
    ("Locked Exit", "Obsidian Sea"),
    ("Nunatak Exit", "Diamond Sea"),
    ("Star East Exit", "Ruby Sea"),
    ("Star West Exit", "Lost Sea"),
    ("Shoal Exit", "Diamond Sea"),
    ("Sunken Exit", "Ruby Sea"),
    ("Beast Exit", "Beast Sea"),
    ("Lost Exit", "Lost Sea"),

]
