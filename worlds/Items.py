from BaseClasses import Item, ItemClassification
import typing


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    classification: any


class IslesOfSeaAndSkyItem(Item):
    game: str = "IslesOfSeaAndSky"


item_table = {
    "Ancient Key":              ItemData(999000,     ItemClassification.progression),
    "Topaz":                    ItemData(999001,     ItemClassification.progression),
    "Sapphire":                 ItemData(999002,     ItemClassification.progression),
    "Ruby":                     ItemData(999003,     ItemClassification.progression),
    "Diamond":                  ItemData(999004,     ItemClassification.progression),
    "Obsidian":                 ItemData(999005,     ItemClassification.useful),
    "Star Piece":               ItemData(999006,     ItemClassification.progression),
    "Ancient Rune Tablet":      ItemData(999007,     ItemClassification.progression),
    "Topaz Rune Tablet":        ItemData(999008,     ItemClassification.progression),
    "Sapphire Rune Tablet":     ItemData(999009,     ItemClassification.progression),
    "Ruby Rune Tablet":         ItemData(999010,     ItemClassification.progression),
    "Diamond Rune Tablet":      ItemData(999011,     ItemClassification.progression),
    "Obsidian Rune Tablet":     ItemData(999012,     ItemClassification.useful),
    "Gopher Gloves":            ItemData(999013,     ItemClassification.progression),
    "Frog Flippers":            ItemData(999014,     ItemClassification.progression),
    "Salamander Shirt":         ItemData(999015,     ItemClassification.progression),
    "Kite Cape":                ItemData(999016,     ItemClassification.progression),
    "Serpent Circlet":          ItemData(999017,     ItemClassification.useful),
    "Blue Stone Tablet":        ItemData(999018,     ItemClassification.useful),
    "Gold Stone Tablet":        ItemData(999019,     ItemClassification.useful),
    "Shell":                    ItemData(999020,     ItemClassification.filler),
    "Fire Key":                 ItemData(999021,     ItemClassification.progression),
    "Egg":                      ItemData(999022,     ItemClassification.progression),
    "Wind Key":                 ItemData(999023,     ItemClassification.progression),
    "Music Note":               ItemData(999024,     ItemClassification.useful),
    "Phoenix Flute":            ItemData(999025,     ItemClassification.useful),
    "Star Viewing Orb":         ItemData(999026,     ItemClassification.useful),
    "Earth Quest Complete":     ItemData(999027,     ItemClassification.progression),
    "Water Quest Complete":     ItemData(999028,     ItemClassification.progression),
    "Fire Quest Complete":      ItemData(999029,     ItemClassification.progression),
    "Air Quest Complete":       ItemData(999030,     ItemClassification.progression),
    "Rolling Bell Rung":        ItemData(999031,     ItemClassification.useful),
    "Sunken Bell Rung":         ItemData(999032,     ItemClassification.useful),
    "Aggro Bell Rung":          ItemData(999033,     ItemClassification.useful),
    "Nanatak Bell Rung":        ItemData(999034,     ItemClassification.useful),
    "Earth Shard Hit":          ItemData(999035,     ItemClassification.progression),
    "Water Shard Hit":          ItemData(999036,     ItemClassification.progression),
    "Fire Shard Hit":           ItemData(999037,     ItemClassification.progression),
    "Air Shard Hit":            ItemData(999038,     ItemClassification.progression),

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

'''plot_items = {
    "Earth Quest Complete": 1,
    "Water Quest Complete": 1,
    "Fire Quest Complete": 1,
    "Air Quest Complete": 1,
    "Earth Shard Hit": 1,
    "Water Shard Hit": 1,
    "Fire Shard Hit": 1,
    "Air Shard Hit": 1,

}'''

key_items = {
    "Ancient Key":              73,
    "Topaz":                    12,
    "Sapphire":                 12,
    "Ruby":                     12,
    "Diamond":                  12,
    "Star Piece":               90,
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
    "Egg":                      3,
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
    "Shell":                    0,
    #"Jellyfish":               0,
}

