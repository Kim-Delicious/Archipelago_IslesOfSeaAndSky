from BaseClasses import Item, ItemClassification
import typing


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    classification: any


class IslesOfSeaAndSkyItem(Item):
    game: str = "IslesOfSeaAndSky"

# Item Id is set to in-game Object Index
item_table = {
    "Ancient Key":              ItemData(109,     ItemClassification.useful),
    "Topaz":                    ItemData(784,     ItemClassification.progression),
    "Sapphire":                 ItemData(635,     ItemClassification.progression),
    "Ruby":                     ItemData(606,     ItemClassification.progression),
    "Diamond":                  ItemData(282,     ItemClassification.progression),
    "Obsidian":                 ItemData(467,     ItemClassification.useful),
    "Star Piece":               ItemData(728,     ItemClassification.useful),
    "Ancient Rune Tablet":      ItemData(616,     ItemClassification.progression),
    "Topaz Rune Tablet":        ItemData(622,     ItemClassification.progression),
    "Sapphire Rune Tablet":     ItemData(621,     ItemClassification.progression),
    "Ruby Rune Tablet":         ItemData(620,     ItemClassification.progression),
    "Diamond Rune Tablet":      ItemData(617,     ItemClassification.progression),
    "Obsidian Rune Tablet":     ItemData(618,     ItemClassification.useful),
    "Gopher Gloves":            ItemData(358,     ItemClassification.progression),
    "Frog Flippers":            ItemData(346,     ItemClassification.progression),
    "Salamander Shirt":         ItemData(623,     ItemClassification.progression),
    "Kite Cape":                ItemData(399,     ItemClassification.progression),
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
    "Earth Quest Complete":     ItemData(905,     ItemClassification.progression),
    "Water Quest Complete":     ItemData(906,     ItemClassification.progression),
    "Fire Quest Complete":      ItemData(907,     ItemClassification.progression),
    "Air Quest Complete":       ItemData(908,     ItemClassification.progression),
    "Rolling Bell Rung":        ItemData(901,     ItemClassification.useful),
    "Sunken Bell Rung":         ItemData(902,     ItemClassification.useful),
    "Aggro Bell Rung":          ItemData(903,     ItemClassification.useful),
    "Nunatak Bell Rung":        ItemData(904,     ItemClassification.useful),
    "Earth Shard Hit":          ItemData(909,     ItemClassification.progression),
    "Water Shard Hit":          ItemData(910,     ItemClassification.progression),
    "Fire Shard Hit":           ItemData(911,     ItemClassification.progression),
    "Air Shard Hit":            ItemData(912,     ItemClassification.progression),

}

non_key_items = {
    "Obsidian":                 12,
    "Obsidian Rune Tablet":     1,
    "Serpent Circlet":          1,
    "Blue Stone Tablet":        1,
    "Gold Stone Tablet":        1,
    "Music Note":               24,
    "Phoenix Flute":            1,
    "Star Viewing Orb":         1,
    "Rolling Bell Rung":        1,
    "Sunken Bell Rung":         1,
    "Aggro Bell Rung":          1,
    "Nunatak Bell Rung":        1,
}


key_items = {
    "Ancient Key":              73,
    "Topaz":                    12,
    "Sapphire":                 12,
    "Ruby":                     12,
    "Diamond":                  12,
    "Star Piece":               91,
    "Ancient Rune Tablet":      1,
    "Topaz Rune Tablet":        1,
    "Sapphire Rune Tablet":     1,
    "Ruby Rune Tablet":         1,
    "Diamond Rune Tablet":      1,
    "Gopher Gloves":            1,
    "Frog Flippers":            1,
    "Salamander Shirt":         1,
    "Kite Cape":                1,
    "Fire Key":                 3,
    "Egg":                      0, # broken
    "Wind Key":                 1,
    "Earth Quest Complete":     1,
    "Water Quest Complete":     1,
    "Fire Quest Complete":      1,
    "Air Quest Complete":       1,
    "Earth Shard Hit":          1,
    "Water Shard Hit":          1,
    "Fire Shard Hit":           1,
    "Air Shard Hit":            1,

}

junk_weights = {
    "Shell":                    0, #Currently no in-game checks
    "Jellyfish":                0, #Currently no in-game checks
}

