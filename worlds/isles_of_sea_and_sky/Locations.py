from BaseClasses import Location
import typing


class AdvData(typing.NamedTuple):
    id: typing.Optional[int]
    region: str

#object ref id, region id, location id, location total
#ancient13 key = 109, 00, 13, 0
#10900130

'''
ancient = 00
stone = 01
stonedungeon = 02
water = 03
fire = 04
wind = 05
serpent = 06
sanctum = 07
rolling = 08
sunken = 09
aggro = 10
nunatak = 11
locked = 12
tropic = 13
shoal = 14
lost = 15
beast = 16




'''



class IslesOfSeaAndSkyAdvancement(Location):
    game: str = "IslesOfSeaAndSky"

advancement_table = {
    "Ancient Rune Tablet":          AdvData(61612011,     "Locked"),
    "Topaz Rune Tablet":            AdvData(62201201,     "Stoney Cliffs"),
    "Sapphire Rune Tablet":         AdvData(62103201,     "Tidal Reef"),
    "Ruby Rune Tablet":             AdvData(62004201,     "Raging Volcano"),
    "Diamond Rune Tablet":          AdvData(61705221,     "Frozen Spire"),
    "Obsidian Rune Tablet":         AdvData(61806011,     "Serpent Stacks"),

    "Topaz Quest Complete":         AdvData(99901201,     "Stoney Cliffs"),
    "Sapphire Quest Complete":      AdvData(99903201,     "Tidal Reef"),
    "Ruby Quest Complete":          AdvData(99904201,     "Raging Volcano"),
    "Diamond Quest Complete":       AdvData(99905221,     "Frozen Spire"),

    "Gopher Gloves":                AdvData(35802211,     "Stoney Cliffs"),
    "Frog Flippers":                AdvData(34603041,     "Tidal Reef"),
    "Salamander Shirt":             AdvData(62304401,     "Raging Volcano"),
    "Kite Cape":                    AdvData(39905001,     "Frozen Spire"),
    "Serpent Circlet":              AdvData(65406011,     "Serpent Stacks"),

    "Topaz Shard Hit":              AdvData(99907021,     "Sanctum"),
    "Sapphire Shard Hit":           AdvData(99907221,     "Sanctum"),
    "Ruby Shard Hit":               AdvData(99907201,     "Sanctum"),
    "Diamond Shard Hit":            AdvData(99907001,     "Sanctum"),

    "Blue Stone Tablet":            AdvData(59602011,     "Stoney Cliffs"),
    "Gold Stone Tablet":            AdvData(59701431,     "Stoney Cliffs"),

    "Fire Key 1":                   AdvData(33204041,     "Raging Volcano"),
    "Fire Key 2":                   AdvData(33204001,     "Raging Volcano"),
    "Fire Key 3":                   AdvData(33204441,     "Raging Volcano"),

    "Egg 1":         AdvData(991024,     "Frozen Spire"), #Broken due to in-game randomness
    "Egg 2":         AdvData(991025,     "Frozen Spire"), #Broken due to in-game randomness
    "Egg 3":         AdvData(991026,     "Frozen Spire"), #Broken due to in-game randomness
    "Wind Key":      AdvData(991027,     "Frozen Spire"), #Broken due to in-game randomness

    # Order is based on object reference search in UndertaleModTools
    "Ancient Key 1" :               AdvData(10900131,     "Ancient Isle"),
    "Ancient Key 2" :               AdvData(10900011,     "Ancient Isle"),
    "Ancient Key 3" :               AdvData(10900022,     "Ancient Isle"),
    "Ancient Key 4" :               AdvData(10900033,     "Ancient Isle"),
    "Ancient Key 5" :               AdvData(10900032,     "Ancient Isle"),
    "Ancient Key 6" :               AdvData(10900031,     "Ancient Isle"),
    "Ancient Key 7" :               AdvData(10900221,     "Ancient Isle"),
    "Ancient Key 8" :               AdvData(10900231,     "Ancient Isle"),
    "Ancient Key 9" :               AdvData(10900211,     "Ancient Isle"),
    "Ancient Key 10" :              AdvData(10900021,     "Ancient Isle"),
    "Ancient Key 11" :AdvData(991038,     "Stoney Cliffs"),
    "Ancient Key 12" :AdvData(991039,     "Stoney Cliffs"),
    "Ancient Key 13" :AdvData(991040,     "Stoney Cliffs"),
    "Ancient Key 14" :AdvData(991041,     "Rolling Rocks"),
    "Ancient Key 15" :AdvData(991042,     "Tropic Star"),
    "Ancient Key 16" :AdvData(991043,     "Rolling Rocks"),
    "Ancient Key 17" :AdvData(991044,     "Stoney Cliffs"),
    "Ancient Key 18" :AdvData(991045,     "Stoney Cliffs"),
    "Ancient Key 19" :AdvData(991046,     "Stoney Cliffs"),
    "Ancient Key 20" :AdvData(991047,     "Stoney Cliffs"),
    "Ancient Key 21" :AdvData(991048,     "Stoney Cliffs"),
    "Ancient Key 22" :AdvData(991049,     "Stoney Cliffs"),
    "Ancient Key 23" :AdvData(991050,     "Stoney Cliffs"),
    "Ancient Key 24" :AdvData(991051,     "Stoney Cliffs"),
    "Ancient Key 25" :AdvData(991052,     "Stoney Cliffs"),
    "Ancient Key 26" :AdvData(991053,     "Tidal Reef"),
    "Ancient Key 27" :AdvData(991054,     "Tidal Reef"),
    "Ancient Key 28" :AdvData(991055,     "Tidal Reef"),
    "Ancient Key 29" :AdvData(991056,     "Tidal Reef"),
    "Ancient Key 30" :AdvData(991057,     "Tidal Reef"),
    "Ancient Key 31" :AdvData(991058,     "Tidal Reef"),
    "Ancient Key 32" :AdvData(991059,     "Tidal Reef"),
    "Ancient Key 33" :AdvData(991060,     "Tidal Reef"),
    "Ancient Key 34" :AdvData(991061,     "Tidal Reef"),
    "Ancient Key 35" :AdvData(991062,     "Tidal Reef"),
    "Ancient Key 36" :AdvData(991063,     "Tidal Reef"),
    "Ancient Key 37" :AdvData(991064,     "Tidal Reef"),
    "Ancient Key 38" :AdvData(991065,     "Tidal Reef"),
    "Ancient Key 39" :AdvData(991066,     "Raging Volcano"),
    "Ancient Key 40" :AdvData(991067,     "Raging Volcano"),
    "Ancient Key 41" :AdvData(991068,     "Raging Volcano"),
    "Ancient Key 42" :AdvData(991069,     "Raging Volcano"),
    "Ancient Key 43" :AdvData(991070,     "Raging Volcano"),
    "Ancient Key 44" :AdvData(991071,     "Raging Volcano"),
    "Ancient Key 45" :AdvData(991072,     "Raging Volcano"),
    "Ancient Key 46" :AdvData(991073,     "Raging Volcano"),
    "Ancient Key 47" :AdvData(991074,     "Raging Volcano"),
    "Ancient Key 48" :AdvData(991075,     "Raging Volcano"),
    "Ancient Key 49" :AdvData(991076,     "Raging Volcano"),
    "Ancient Key 50" :AdvData(991077,     "Raging Volcano"),
    "Ancient Key 51" :AdvData(991078,     "Raging Volcano"),
    "Ancient Key 52" :AdvData(991079,     "Raging Volcano"),
    "Ancient Key 53" :AdvData(991080,     "Frozen Spire"),
    "Ancient Key 54" :AdvData(991081,     "Frozen Spire"),
    "Ancient Key 55" :AdvData(991082,     "Frozen Spire"),
    "Ancient Key 56" :AdvData(991083,     "Frozen Spire"),
    "Ancient Key 57" :AdvData(991084,     "Frozen Spire"),
    "Ancient Key 58" :AdvData(991085,     "Frozen Spire"),
    "Ancient Key 59" :AdvData(991086,     "Frozen Spire"),
    "Ancient Key 60" :AdvData(991087,     "Frozen Spire"),
    "Ancient Key 61" :AdvData(991088,     "Frozen Spire"),
    "Ancient Key 62" :AdvData(991089,     "Frozen Spire"),
    "Ancient Key 63" :AdvData(991090,     "Frozen Spire"),
    "Ancient Key 64" :AdvData(991091,     "Frozen Spire"),
    "Ancient Key 65" :AdvData(991092,     "Frozen Spire"),
    "Ancient Key 66" :AdvData(991093,     "Aggro Crag"),
    "Ancient Key 67" :AdvData(991094,     "Aggro Crag"),
    "Ancient Key 68" :AdvData(991095,     "Sunken Island"),
    "Ancient Key 69" :AdvData(991096,     "Sunken Island"),
    "Ancient Key 70" :AdvData(991097,     "Sea Nunatuk"),
    "Ancient Key 71" :AdvData(991294,     "Sea Nunatuk"), # Off number due to initial miscount
    "Ancient Key 72" :AdvData(991295,     "Stoney Cliffs"), # Off number due to initial miscount
    "Ancient Key 73" :AdvData(991296,     "Stoney Cliffs"), # Off number due to initial miscount

    "Topaz 1" :      AdvData(991098,     "Stoney Cliffs"),
    "Topaz 2" :      AdvData(991099,     "Stoney Cliffs"),
    "Topaz 3" :      AdvData(991100,     "Stoney Cliffs"),
    "Topaz 4" :      AdvData(991101,     "Stoney Cliffs"),
    "Topaz 5" :      AdvData(991102,     "Stoney Cliffs"),
    "Topaz 6" :      AdvData(991103,     "Stoney Cliffs"),
    "Topaz 7" :      AdvData(991104,     "Stoney Cliffs"),
    "Topaz 8" :      AdvData(991105,     "Stoney Cliffs"),
    "Topaz 9" :      AdvData(991106,     "Stoney Cliffs"),
    "Topaz 10" :     AdvData(991107,     "Stoney Cliffs"),
    "Topaz 11" :     AdvData(991108,     "Rolling Rocks"),
    "Topaz 12" :     AdvData(991109,     "Star Tropic"),

    "Sapphire 1" :   AdvData(991110,     "Tidal Reef"),
    "Sapphire 2" :   AdvData(991111,     "Tidal Reef"),
    "Sapphire 3" :   AdvData(991112,     "Tidal Reef"),
    "Sapphire 4" :   AdvData(991113,     "Tidal Reef"),
    "Sapphire 5" :   AdvData(991114,     "Tidal Reef"),
    "Sapphire 6" :   AdvData(991115,     "Tidal Reef"),
    "Sapphire 7" :   AdvData(991116,     "Tidal Reef"),
    "Sapphire 8" :   AdvData(991117,     "Tidal Reef"),
    "Sapphire 9" :   AdvData(991118,     "Tidal Reef"),
    "Sapphire 10" :  AdvData(991119,     "Tidal Reef"),
    "Sapphire 11" :  AdvData(991120,     "Sunken Island"),
    "Sapphire 12" :  AdvData(991121,     "Star Tropic"),

    "Ruby 1" :       AdvData(991122,     "Raging Volcano"),
    "Ruby 2" :       AdvData(991123,     "Raging Volcano"),
    "Ruby 3" :       AdvData(991124,     "Raging Volcano"),
    "Ruby 4" :       AdvData(991125,     "Raging Volcano"),
    "Ruby 5" :       AdvData(991126,     "Raging Volcano"),
    "Ruby 6" :       AdvData(991127,     "Raging Volcano"),
    "Ruby 7" :       AdvData(991128,     "Raging Volcano"),
    "Ruby 8" :       AdvData(991129,     "Raging Volcano"),
    "Ruby 9" :       AdvData(991130,     "Raging Volcano"),
    "Ruby 10" :      AdvData(991131,     "Raging Volcano"),
    "Ruby 11" :      AdvData(991132,     "Aggro Crag"),
    "Ruby 12" :      AdvData(991133,     "Star Tropic"),

    "Diamond 1" :    AdvData(991134,     "Frozen Spire"),
    "Diamond 2" :    AdvData(991135,     "Frozen Spire"),
    "Diamond 3" :    AdvData(991136,     "Frozen Spire"),
    "Diamond 4" :    AdvData(991137,     "Frozen Spire"),
    "Diamond 5" :    AdvData(991138,     "Frozen Spire"),
    "Diamond 6" :    AdvData(991139,     "Frozen Spire"),
    "Diamond 7" :    AdvData(991140,     "Frozen Spire"),
    "Diamond 8" :    AdvData(991141,     "Frozen Spire"),
    "Diamond 9" :    AdvData(991142,     "Frozen Spire"),
    "Diamond 10" :   AdvData(991143,     "Frozen Spire"),
    "Diamond 11" :   AdvData(991144,     "Sea Nanatak"),
    "Diamond 12" :   AdvData(991145,     "Star Tropic"),

    # 4 of these are trapped in bells, and should be removed.
    # 3x4=12 trapped in music puzzle
    # 3 trapped in volcano idol puzzle
    # Total of 19 stars that aren't locations.
    "Star Piece 1" :            AdvData(72800201,     "Ancient Isle"),
    "Star Piece 2" :            AdvData(72800011,     "Ancient Isle"),
    "Star Piece 3" :            AdvData(72800111,     "Ancient Isle"),
    "Star Piece 4" : AdvData(991149,     "Stoney Cliffs"),
    "Star Piece 5" : AdvData(991150,     "Stoney Cliffs"),
    "Star Piece 6" : AdvData(991151,     "Stoney Cliffs"),
    "Star Piece 7" : AdvData(991152,     "Stoney Cliffs"),
    "Star Piece 8" : AdvData(991153,     "Stoney Cliffs"),
    "Star Piece 9" : AdvData(991154,     "Stoney Cliffs"),
    "Star Piece 10" :AdvData(991155,     "Stoney Cliffs"),
    "Star Piece 11" :AdvData(991156,     "Stoney Cliffs"),
    "Star Piece 12" :AdvData(991157,     "Stoney Cliffs"),
    "Star Piece 13" :AdvData(991158,     "Stoney Cliffs"),
    "Star Piece 14" :AdvData(991159,     "Stoney Cliffs"),
    "Star Piece 15" :AdvData(991160,     "Stoney Cliffs"),
    "Star Piece 16" :AdvData(991161,     "Stoney Cliffs"),
    "Star Piece 17" :AdvData(991162,     "Stoney Cliffs"),
    "Star Piece 18" :AdvData(991163,     "Tidal Reef"),
    "Star Piece 19" :AdvData(991164,     "Tidal Reef"),
    "Star Piece 20" :AdvData(991165,     "Tidal Reef"),
    "Star Piece 21" :AdvData(991166,     "Tidal Reef"),
    "Star Piece 22" :AdvData(991167,     "Tidal Reef"),
    "Star Piece 23" :AdvData(991168,     "Tidal Reef"),
    "Star Piece 24" :AdvData(991169,     "Tidal Reef"),
    "Star Piece 25" :AdvData(991170,     "Tidal Reef"),
    "Star Piece 26" :AdvData(991171,     "Tidal Reef"),
    "Star Piece 27" :AdvData(991172,     "Tidal Reef"),
    "Star Piece 28" :AdvData(991173,     "Tidal Reef"),
    "Star Piece 29" :AdvData(991174,     "Tidal Reef"),
    "Star Piece 30" :AdvData(991175,     "Tidal Reef"),
    "Star Piece 31" :AdvData(991176,     "Tidal Reef"),
    "Star Piece 32" :AdvData(991177,     "Tidal Reef"),
    "Star Piece 33" :AdvData(991178,     "Raging Volcano"),
    "Star Piece 34" :AdvData(991179,     "Raging Volcano"),
    "Star Piece 35" :AdvData(991180,     "Raging Volcano"),
    "Star Piece 36" :AdvData(991181,     "Raging Volcano"),
    "Star Piece 37" :AdvData(991182,     "Raging Volcano"),
    "Star Piece 38" :AdvData(991183,     "Raging Volcano"),
    "Star Piece 39" :AdvData(991184,     "Raging Volcano"),
    "Star Piece 40" :AdvData(991185,     "Raging Volcano"),
    "Star Piece 41" :AdvData(991186,     "Raging Volcano"),
    "Star Piece 42" :AdvData(991187,     "Raging Volcano"),
    "Star Piece 43" :AdvData(991188,     "Raging Volcano"),
    "Star Piece 44" :AdvData(991189,     "Raging Volcano"),
    "Star Piece 45" :AdvData(991190,     "Raging Volcano"),
    "Star Piece 46" :AdvData(991191,     "Raging Volcano"),
    "Star Piece 47" :AdvData(991192,     "Frozen Spire"),
    "Star Piece 48" :AdvData(991193,     "Frozen Spire"),
    "Star Piece 49" :AdvData(991194,     "Frozen Spire"),
    "Star Piece 50" :AdvData(991195,     "Frozen Spire"),
    "Star Piece 51" :AdvData(991196,     "Frozen Spire"),
    "Star Piece 52" :AdvData(991197,     "Frozen Spire"),
    "Star Piece 53" :AdvData(991198,     "Frozen Spire"),
    "Star Piece 54" :AdvData(991199,     "Frozen Spire"),
    "Star Piece 55" :AdvData(991200,     "Frozen Spire"),
    "Star Piece 56" :AdvData(991201,     "Frozen Spire"),
    "Star Piece 57" :AdvData(991202,     "Frozen Spire"),
    "Star Piece 58" :AdvData(991203,     "Frozen Spire"),
    "Star Piece 59" :AdvData(991204,     "Frozen Spire"),
    "Star Piece 60" :AdvData(991205,     "Frozen Spire"),
    "Star Piece 61" :AdvData(991206,     "Frozen Spire"),
    "Star Piece 62" :AdvData(991207,     "Rolling Rocks"),
    "Star Piece 63" :AdvData(991208,     "Rolling Rocks"),
    "Star Piece 64" :AdvData(991209,     "Rolling Rocks"),
    "Star Piece 65" :AdvData(991210,     "Sunken Island"),
    "Star Piece 66" :AdvData(991211,     "Sunken Island"),
    "Star Piece 67" :AdvData(991212,     "Aggro Crag"),
    "Star Piece 68" :AdvData(991213,     "Aggro Crag"),
    "Star Piece 69" :AdvData(991214,     "Sea Nanatak"),
    "Star Piece 70" :AdvData(991215,     "Sea Nanatak"),
    "Star Piece 71" :AdvData(991216,     "Lost Landing"),
    "Star Piece 72" :AdvData(991217,     "Shoal"),
    "Star Piece 73" :AdvData(991218,     "Star Tropic"),
    "Star Piece 74" :AdvData(991219,     "Star Tropic"),
    "Star Piece 75" :AdvData(991220,     "Star Tropic"),
    "Star Piece 76" :AdvData(991221,     "Star Tropic"),
    "Star Piece 77" :AdvData(991222,     "Star Tropic"),
    "Star Piece 78" :AdvData(991223,     "Star Tropic"),
    "Star Piece 79" :AdvData(991224,     "Star Tropic"),
    "Star Piece 80" :AdvData(991225,     "Serpent Stacks"),
    "Star Piece 81" :AdvData(991226,     "Serpent Stacks"),
    "Star Piece 82" :AdvData(991227,     "Serpent Stacks"),
    "Star Piece 83" :AdvData(991228,     "Serpent Stacks"),
    "Star Piece 84" :AdvData(991229,     "Serpent Stacks"),
    "Star Piece 85" :AdvData(991230,     "Serpent Stacks"),
    "Star Piece 86" :AdvData(991231,     "Serpent Stacks"),
    "Star Piece 87" :AdvData(991232,     "Serpent Stacks"),
    "Star Piece 88" :AdvData(991233,     "Serpent Stacks"),
    "Star Piece 89" :AdvData(991234,     "Serpent Stacks"),
    "Star Piece 90" :AdvData(991235,     "Serpent Stacks"),

    "Rolling Bell Rung" :           AdvData(99908101,     "Rolling Rocks"),
    "Sunken Bell Rung":             AdvData(99909111, "Sunken Island"),
    "Aggro Bell Rung" :             AdvData(99910011,     "Aggro Crag"),
    "Nunatak Bell Rung" :           AdvData(99911011,     "Sea Nanatak"),

    "Phoenix Flute" :               AdvData(51116111,     "Beast Bridge"),
    "Star Viewing Orb" :            AdvData(73314001,     "Shoal"),
    #"Shell 1" : AdvData(991027, "Tidal Reef"),
    #"Jellyfish 1" : AdvData(991027, "Topaz Sea"),

    "Music Note 1" : AdvData(991270,     "Stoney Cliffs"),
    "Music Note 2" : AdvData(991271,     "Stoney Cliffs"),
    "Music Note 3" : AdvData(991272,     "Stoney Cliffs"),
    "Music Note 4" : AdvData(991273,     "Stoney Cliffs"),
    "Music Note 5" : AdvData(991274,     "Stoney Cliffs"),
    "Music Note 6" : AdvData(991275,     "Stoney Cliffs"),

    "Music Note 7" : AdvData(991276,     "Tidal Reef"),
    "Music Note 8" : AdvData(991277,     "Tidal Reef"),
    "Music Note 9" : AdvData(991278,     "Tidal Reef"),
    "Music Note 10" :AdvData(991279,     "Tidal Reef"),
    "Music Note 11" :AdvData(991280,     "Tidal Reef"),
    "Music Note 12" :AdvData(991281,     "Tidal Reef"),

    "Music Note 13" :AdvData(991282,     "Raging Volcano"),
    "Music Note 14" :AdvData(991283,     "Raging Volcano"),
    "Music Note 15" :AdvData(991284,     "Raging Volcano"),
    "Music Note 16" :AdvData(991285,     "Raging Volcano"),
    "Music Note 17" :AdvData(991286,     "Raging Volcano"),
    "Music Note 18" :AdvData(991287,     "Raging Volcano"),

    "Music Note 19" :AdvData(991288,     "Frozen Spire"),
    "Music Note 20" :AdvData(991289,     "Frozen Spire"),
    "Music Note 21" :AdvData(991290,     "Frozen Spire"),
    "Music Note 22" :AdvData(991291,     "Frozen Spire"),
    "Music Note 23" :AdvData(991292,     "Frozen Spire"),
    "Music Note 24" :AdvData(991293,     "Frozen Spire"),

    "Obsidian 1" :    AdvData(991297,    "Rolling Rocks"), # Other items above have what would be next num -> Ancient Key
    "Obsidian 2" :    AdvData(991298,    "Stoney Cliffs"),
    "Obsidian 3" :    AdvData(991299,    "Stoney Cilffs"),
    "Obsidian 4" :    AdvData(991300,    "Tidal Reef"),
    "Obsidian 5" :    AdvData(991301,    "Raging Volcano"),
    "Obsidian 6" :    AdvData(991302,    "Raging Volcano"),
    "Obsidian 7" :    AdvData(991303,    "Frozen Spire"),
    "Obsidian 8" :    AdvData(991304,    "Aggro Crag"),
    "Obsidian 9" :    AdvData(991305,    "Sunken Island"),
    "Obsidian 10" :   AdvData(991306,    "Sea Nanatak"),
    "Obsidian 11" :   AdvData(991307,    "Serpent Stacks"),
    "Obsidian 12" :   AdvData(991308,    "Lost Landing"),

    # In the future, could include milestones as locations. e.g. each of the steam achievments, plus extras.
}

exclusion_table = {
# Exclude the very first items of the game, such as the starting key.

}

events_table = {
}
