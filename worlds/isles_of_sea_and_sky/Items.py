from BaseClasses import Item, ItemClassification
import typing


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    classification: any


class IslesOfSeaAndSkyItem(Item):
    game: str = "IslesOfSeaAndSky"

# Item Id is set to in-game Object Index
item_table = {
    "Ancient Key":              ItemData(109,     ItemClassification.progression_skip_balancing),
    "Topaz":                    ItemData(784,     ItemClassification.progression_skip_balancing),
    "Sapphire":                 ItemData(635,     ItemClassification.progression_skip_balancing),
    "Ruby":                     ItemData(606,     ItemClassification.progression_skip_balancing),
    "Diamond":                  ItemData(282,     ItemClassification.progression_skip_balancing),
    "Obsidian":                 ItemData(467,     ItemClassification.progression_skip_balancing),
    "Star Piece":               ItemData(728,     ItemClassification.progression_skip_balancing),
    "Ancient Rune Stone":       ItemData(616,     ItemClassification.progression),
    "Topaz Rune Stone":         ItemData(622,     ItemClassification.progression),
    "Sapphire Rune Stone":      ItemData(621,     ItemClassification.progression),
    "Ruby Rune Stone":          ItemData(620,     ItemClassification.progression),
    "Diamond Rune Stone":       ItemData(617,     ItemClassification.progression),
    "Obsidian Rune Stone":      ItemData(618,     ItemClassification.progression),
    "Gopher Gloves":            ItemData(358,     ItemClassification.progression),
    "Frog Flippers":            ItemData(346,     ItemClassification.progression),
    "Salamander Shirt":         ItemData(623,     ItemClassification.progression),
    "Kite Cloak":               ItemData(399,     ItemClassification.progression),
    "Serpent Circlet":          ItemData(654,     ItemClassification.useful),
    "Blue Stone Tablet":        ItemData(596,     ItemClassification.useful),
    "Gold Stone Tablet":        ItemData(597,     ItemClassification.useful),
    "Shell":                    ItemData(636,     ItemClassification.filler),
    "Jellyfish":                ItemData(395,     ItemClassification.filler),
    "Fire Key":                 ItemData(332,     ItemClassification.progression),
    "Egg":                      ItemData(294,     ItemClassification.progression),
    "Wind Key":                 ItemData(835,     ItemClassification.progression),
    "Music Note":               ItemData(457,     ItemClassification.useful),
    "Phoenix Flute":            ItemData(511,     ItemClassification.useful),
    "Star Viewing Orb":         ItemData(733,     ItemClassification.useful),
    "Topaz Quest Complete":     ItemData(905,     ItemClassification.progression),
    "Sapphire Quest Complete":  ItemData(906,     ItemClassification.progression),
    "Ruby Quest Complete":      ItemData(907,     ItemClassification.progression),
    "Diamond Quest Complete":   ItemData(908,     ItemClassification.progression),
    "Rolling Bell Rung":        ItemData(901,     ItemClassification.useful),
    "Sunken Bell Rung":         ItemData(902,     ItemClassification.useful),
    "Aggro Bell Rung":          ItemData(903,     ItemClassification.useful),
    "Nunatak Bell Rung":        ItemData(904,     ItemClassification.useful),
    "Topaz Shard Hit":          ItemData(909,     ItemClassification.progression),
    "Sapphire Shard Hit":       ItemData(910,     ItemClassification.progression),
    "Ruby Shard Hit":           ItemData(911,     ItemClassification.progression),
    "Diamond Shard Hit":        ItemData(912,     ItemClassification.progression),
    #"GOAL":                     ItemData(999,     ItemClassification.progression),

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
    #"Egg":                      0, # broken
    #"Wind Key":                 0, # broken
    "Topaz Quest Complete":     1,
    "Sapphire Quest Complete":  1,
    "Ruby Quest Complete":      1,
    "Diamond Quest Complete":   1,
    "Topaz Shard Hit":          1,
    "Sapphire Shard Hit":       1,
    "Ruby Shard Hit":           1,
    "Diamond Shard Hit":        1,
    "Phoenix Flute":            1,
}

key_items = {
    "Ancient Key":              70, # Should be 73?
    "Topaz":                    12,
    "Sapphire":                 12,
    "Ruby":                     12,
    "Diamond":                  12,
    "Star Piece":               91,


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
    "Nunatak Bell Rung":        1,

}

junk_weights = {
    "Shell":                    0, #Currently no in-game checks
    "Jellyfish":                0, #Currently no in-game checks
}

