from BaseClasses import Item, ItemClassification as IC
import typing


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    classification: any


class IslesOfSeaAndSkyItem(Item):
    game: str = "IslesOfSeaAndSky"

# Item ID is set to in-game Object Index
item_table = {
    "Ancient Key":              ItemData(109,       IC.progression_skip_balancing),
    "Topaz":                    ItemData(784,       IC.progression_skip_balancing),
    "Sapphire":                 ItemData(635,       IC.progression_skip_balancing),
    "Ruby":                     ItemData(606,       IC.progression_skip_balancing),
    "Diamond":                  ItemData(282,       IC.progression_skip_balancing),
    "Obsidian":                 ItemData(467,       IC.progression_skip_balancing),
    "Star Piece":               ItemData(728,       IC.progression_skip_balancing),
    "Ancient Rune Stone":       ItemData(616,       IC.progression | IC.useful),
    "Topaz Rune Stone":         ItemData(622,       IC.progression | IC.useful),
    "Sapphire Rune Stone":      ItemData(621,       IC.progression | IC.useful),
    "Ruby Rune Stone":          ItemData(620,       IC.progression | IC.useful),
    "Diamond Rune Stone":       ItemData(617,       IC.progression | IC.useful),
    "Obsidian Rune Stone":      ItemData(618,       IC.progression | IC.useful),
    "Gopher Gloves":            ItemData(358,       IC.progression | IC.useful),
    "Frog Flippers":            ItemData(346,       IC.progression | IC.useful),
    "Salamander Shirt":         ItemData(623,       IC.progression | IC.useful),
    "Kite Cloak":               ItemData(399,       IC.progression | IC.useful),
    "Serpent Circlet":          ItemData(654,       IC.progression | IC.useful),
    "Blue Stone Tablet":        ItemData(596,       IC.progression_skip_balancing),
    "Gold Stone Tablet":        ItemData(597,       IC.progression_skip_balancing),
    "Seashell":                 ItemData(636,       IC.filler),
    "Fire Key":                 ItemData(332,       IC.progression_skip_balancing),
    "Music Note":               ItemData(457,       IC.useful),
    "Phoenix Flute":            ItemData(511,       IC.progression | IC.useful),
    "Star Viewing Orb":         ItemData(733,       IC.useful),
    # Cutscenes
    "Topaz Quest Complete":     ItemData(905,       IC.progression | IC.useful),
    "Sapphire Quest Complete":  ItemData(906,       IC.progression | IC.useful),
    "Ruby Quest Complete":      ItemData(907,       IC.progression | IC.useful),
    "Diamond Quest Complete":   ItemData(908,       IC.progression | IC.useful),
    "Rolling Bell Rung":        ItemData(901,       IC.progression),
    "Sunken Bell Rung":         ItemData(902,       IC.progression),
    "Aggro Bell Rung":          ItemData(903,       IC.progression),
    "Nunatak Bell Rung":        ItemData(904,       IC.progression),
    "Topaz Shard Hit":          ItemData(909,       IC.progression),
    "Sapphire Shard Hit":       ItemData(910,       IC.progression),
    "Ruby Shard Hit":           ItemData(911,       IC.progression),
    "Diamond Shard Hit":        ItemData(912,       IC.progression),
    # Traps
    "Slow Trap":                ItemData(7000,      IC.trap),
    "Fast Trap":                ItemData(7001,      IC.trap),
    "Tiny Trap":                ItemData(7002,      IC.trap),
    "Thicc Trap":               ItemData(7003,      IC.trap),
    "Ice Trap":                 ItemData(7004,      IC.trap),
    "Magma Spirit Trap":        ItemData(7005,      IC.trap),
    "Metal Spirit Trap":        ItemData(7006,      IC.trap),
    "Lava Spirit Trap":         ItemData(7007,      IC.trap),
    "Reversed Controls Trap":   ItemData(7008,      IC.trap),
    "Floor Is Lava Trap":       ItemData(7009,      IC.trap)

}



progression_items = {

    "Ancient Rune Stone":       1,
    "Topaz Rune Stone":         1,
    "Sapphire Rune Stone":      1,
    "Ruby Rune Stone":          1,
    "Diamond Rune Stone":       1,
    "Gopher Gloves":            1,
    "Frog Flippers":            1,
    "Salamander Shirt":         1,
    "Kite Cloak":               1,
    "Fire Key":                 3,
    "Topaz Quest Complete":     1,
    "Sapphire Quest Complete":  1,
    "Ruby Quest Complete":      1,
    "Diamond Quest Complete":   1,
    "Topaz Shard Hit":          1,
    "Sapphire Shard Hit":       1,
    "Ruby Shard Hit":           1,
    "Diamond Shard Hit":        1,
    "Phoenix Flute":            1
}

key_items = {
    "Ancient Key":              73,
    "Topaz":                    12,
    "Sapphire":                 12,
    "Ruby":                     12,
    "Diamond":                  12,
    "Star Piece":               91
}

non_key_items = {
    "Obsidian":                 12,
    "Obsidian Rune Stone":      1,
    "Serpent Circlet":          1,
    "Blue Stone Tablet":        1,
    "Gold Stone Tablet":        1,
    "Music Note":               24,
    "Star Viewing Orb":         1,
    "Rolling Bell Rung":        1,
    "Sunken Bell Rung":         1,
    "Aggro Bell Rung":          1,
    "Nunatak Bell Rung":        1

}

# 52 total
junk_weights = {
    "Seashell":                     16,
    "Ancient Key":                  10,
    "Star Piece":                   8,
    "Obsidian":                     2,
    "Topaz":                        4,
    "Sapphire":                     4,
    "Ruby":                         4,
    "Diamond":                      4,
}

# 20 total
trap_weights = {
    "Slow Trap":                    1,
    "Fast Trap":                    1,
    "Tiny Trap":                    1,
    "Thicc Trap":                     1,
    "Ice Trap":                     2,
    "Magma Spirit Trap":            3,
    "Lava Spirit Trap":             3,
    "Metal Spirit Trap":            3,
    "Reversed Controls Trap":       2,
    "Floor Is Lava Trap":           3,
}


