from BaseClasses import Location
import typing


class AdvData(typing.NamedTuple):
    id: typing.Optional[int]
    region: str

class IslesOfSeaAndSkyAdvancement(Location):
    game: str = "IslesOfSeaAndSky"

advancement_table = {
    "Ancient Rune Stone":                           AdvData(104285, "Locked"),
    "Topaz Rune Stone":                             AdvData(108054, "Stony Cliffs"),
    "Sapphire Rune Stone":                          AdvData(110024, "Tidal Reef"),
    "Ruby Rune Stone":                              AdvData(116199, "Raging Volcano"),
    "Diamond Rune Stone":                           AdvData(121371, "Frozen Spire"),
    "Obsidian Rune Stone":                          AdvData(125695, "Serpent Stacks"),

    "Topaz Quest Complete":                         AdvData(99901201, "Stony Cliffs"),
    "Sapphire Quest Complete":                      AdvData(99903201, "Tidal Reef"),
    "Ruby Quest Complete":                          AdvData(99904201, "Raging Volcano"),
    "Diamond Quest Complete":                       AdvData(99905221, "Frozen Spire"),

    "Gopher Gloves":                                AdvData(101774, "Stony Cliffs NW"),
    "Frog Flippers":                                AdvData(126060, "Tidal Reef Post-Rune"),
    "Salamander Shirt":                             AdvData(118310, "Raging Volcano NE"),
    "Kite Cloak":                                   AdvData(120221, "Frozen Spire Post-Rune"),
    "Serpent Circlet":                              AdvData(156578, "Serpent Stacks Post-Rune"),

    "Topaz Shard Hit":                              AdvData(99907021, "Sanctum"),
    "Sapphire Shard Hit":                           AdvData(99907221, "Sanctum"),
    "Ruby Shard Hit":                               AdvData(99907201, "Sanctum"),
    "Diamond Shard Hit":                            AdvData(99907001, "Sanctum"),

    "Blue Stone Tablet":                            AdvData(178873, "Stony Cliffs Post-Rune"),
    "Gold Stone Tablet":                            AdvData(183915, "Stony Cliffs Post-Rune"),

    "Fire Key [Fire A4]":                                AdvData(117766, "Raging Volcano Post-Rune"),
    "Fire Key [Fire A0]":                                AdvData(116592, "Raging Volcano Post-Rune"),
    "Fire Key [Fire E4]":                                AdvData(117911, "Raging Volcano Post-Rune"),

    #"Egg [1]":         AdvData(991024, "Frozen Spire"), #Broken due to in-game randomness
    #"Egg [2]":         AdvData(991025, "Frozen Spire"), #Broken due to in-game randomness
    #"Egg [3]":         AdvData(991026, "Frozen Spire"), #Broken due to in-game randomness
   # "Wind Key[]":      AdvData(83505440 || 83505040 || 83505400, "Frozen Spire"), #Broken due to in-game randomness

    "Rolling Bell Rung":                            AdvData(99908101, "Rolling Rocks Post-Rune"),
    "Sunken Bell Rung":                             AdvData(99909111, "Sunken Island"),
    "Aggro Bell Rung":                              AdvData(99910011, "Aggro Crag"),
    "Nunatak Bell Rung":                            AdvData(99911011, "Sea Nunatak"),

    "Phoenix Flute":                                AdvData(123533, "Beast Bridge"),
    "Star Viewing Orb":                             AdvData(104389, "Shoal"),

    # MISC
    "Open Ancient Door [Ancient B2]":               AdvData(101288, "Sanctum"), # Placed in next region for logic
    "Open Topaz Door [Stone Dungeon C2]":           AdvData(101864, "Stony Cliffs Post-Rune"),

    "Blue Puzzle Clue 1":                           AdvData(107717, "Stony Cliffs Post-Rune"),
    "Blue Puzzle Clue 2":                           AdvData(107386, "Stony Cliffs Post-Rune"),
    "Blue Puzzle Clue 3":                           AdvData(107497, "Stony Cliffs NW"),

    "Gold Puzzle Clue 1":                           AdvData(125017, "Stony Cliffs Post-Rune"),
    "Gold Puzzle Clue 2":                           AdvData(102677, "Stony Cliffs Post-Rune"),
    "Gold Puzzle Clue 3":                           AdvData(125406, "Stony Cliffs"),

    "Beast Bell Stone":                             AdvData(123559, "Beast Bridge"),
    "Sanctum Bell Stone":                           AdvData(123976, "Sanctum Peak"),

    #

    "Ancient Key [Ancient B3]":                     AdvData(100220, "Ancient Isle"),
    "Ancient Key [Ancient A1]":                     AdvData(101047, "Ancient Isle"),
    "Ancient Key [Ancient A2 - SE]":                AdvData(100727, "Ancient Isle"),
    "Ancient Key [Ancient A3 - N]":                 AdvData(100547, "Ancient Isle"),
    "Ancient Key [Ancient A3 - S]":                 AdvData(100542, "Ancient Isle"),
    "Ancient Key [Ancient A3 - E]":                 AdvData(100538, "Ancient Isle"),
    "Ancient Key [Ancient C2]":                     AdvData(100422, "Ancient Isle"),
    "Ancient Key [Ancient C3]":                     AdvData(101433, "Ancient Isle"),
    "Ancient Key [Ancient C1]":                     AdvData(100983, "Ancient Isle"),
    "Ancient Key [Ancient A2 - NW]":                AdvData(100730, "Ancient Isle"), # Topaz quest

    "Ancient Key [Rolling A1]":                     AdvData(104494, "Rolling Rocks"),
    "Ancient Key [Rolling A0]":                     AdvData(103798, "Rolling Rocks"),  # 7 stars

    "Ancient Key [Tropic A1]":                      AdvData(104437, "Star Tropic"), # ancient rune

    "Ancient Key [Stone B1]":                       AdvData(107038, "Stony Cliffs NW"), #
    "Ancient Key [Stone C0]":                       AdvData(108052, "Stony Cliffs"), #topaz quest
    "Ancient Key [Stone B2]":                       AdvData(107371, "Stony Cliffs"),
    "Ancient Key [Stone E2]":                       AdvData(107665, "Stony Cliffs Post-Rune"),  # topaz rune
    "Ancient Key [Stone B4]":                       AdvData(106963, "Stony Cliffs Post-Rune"), #topaz quest, topaz rune
    "Ancient Key [Stone Dungeon C1]":               AdvData(101789, "Stony Cliffs NW"), #topaz rune, gopher gloves
    "Ancient Key [Stone Dungeon D0]":               AdvData(124853, "Stony Cliffs NW"), #gopher gloves
    "Ancient Key [Stone Dungeon B1]":               AdvData(124775, "Stony Cliffs NW"), #gopher gloves
    "Ancient Key [Stone B0 - NW1]":                 AdvData(10901103296, "Stony Cliffs NW"), # topaz quest
    "Ancient Key [Stone B0 - NW2]":                 AdvData(10901103280, "Stony Cliffs NW"), # topaz quest
    "Ancient Key [Stone B0 - NW3]":                 AdvData(10901103264, "Stony Cliffs NW"), # topaz quest
    "Ancient Key [Stone Dungeon E2]":               AdvData(102454, "Stony Cliffs Post-Rune"),

    "Ancient Key [Water C2]":                       AdvData(108792, "Tidal Reef"),
    "Ancient Key [Water C3 - W]":                   AdvData(108588, "Tidal Reef Post-Rune"), # s rune
    "Ancient Key [Water A0 - E]":                   AdvData(111567, "Tidal Reef Post-Rune"), # s rune
    "Ancient Key [Water A0 - S]":                   AdvData(111570, "Tidal Reef Post-Rune"), # frog flippers
    "Ancient Key [Water A2]":                       AdvData(112439, "Tidal Reef Post-Rune"), # frog flippers, s quest
    "Ancient Key [Water B3]":                       AdvData(110852, "Tidal Reef"), # frog flippers
    "Ancient Key [Water C3 - NE1]":                 AdvData(109032330448, "Tidal Reef Post-Rune"), # frog flippers
    "Ancient Key [Water C3 - NE2]":                 AdvData(109032328848, "Tidal Reef Post-Rune"), # frog flippers
    "Ancient Key [Water C3 - NE3]":                 AdvData(109032327248, "Tidal Reef Post-Rune"), # frog flippers
    "Ancient Key [Water D1]":                       AdvData(109878, "Tidal Reef"), # frog flippers
    "Ancient Key [Water D0]":                       AdvData(110314, "Tidal Reef Post-Rune"), # frog flippers
    "Ancient Key [Water C0]":                       AdvData(110016, "Tidal Reef"), # s quest
    "Ancient Key [Water D2]":                       AdvData(109104, "Tidal Reef Post-Rune"), # frog flippers

    "Ancient Key [Fire A2 - N]":                    AdvData(115234, "Raging Volcano"),
    "Ancient Key [Fire A2 - S]":                    AdvData(115239, "Raging Volcano"), # salamander shirt
    "Ancient Key [Fire B4]":                        AdvData(118466, "Raging Volcano Post-Rune"), # r quest
    "Ancient Key [Fire A1 - NE]":                   AdvData(116437, "Raging Volcano Post-Rune"), # s shirt
    "Ancient Key [Fire A1 - E]":                    AdvData(116431, "Raging Volcano Post-Rune"), # r rune
    "Ancient Key [Fire B1 - N1]":                   AdvData(109041114448, "Raging Volcano Post-Rune"), # r quest
    "Ancient Key [Fire B1 - N2]":                   AdvData(109041112848, "Raging Volcano Post-Rune"), # r quest
    "Ancient Key [Fire B1 - N3]":                   AdvData(109041111248, "Raging Volcano Post-Rune"), # r quest
    "Ancient Key [Fire C1 - NE]":                   AdvData(115684, "Raging Volcano Post-Rune"), # s shirt
    "Ancient Key [Fire C0]":                        AdvData(116182, "Raging Volcano"), # r quest
    "Ancient Key [Fire C1 - SW]":                   AdvData(115696, "Raging Volcano"), # s shirt
    "Ancient Key [Fire C3]":                        AdvData(116298, "Raging Volcano"), # r quest
    "Ancient Key [Fire A1 - S]":                    AdvData(116433, "Raging Volcano Post-Rune"), # r rune
    "Ancient Key [Fire D4]":                        AdvData(118027, "Raging Volcano Post-Rune"), # s shirt

    # Keys on the Frozen Spire may be broken due to in-game randomness
    "Ancient Key [Wind C4]":                        AdvData(120170, "Frozen Spire"),
    "Ancient Key [Wind D4 - E]":                    AdvData(122397, "Frozen Spire Post-Rune"), # d rune
    "Ancient Key [Wind D4 - NW1]":                  AdvData(10905344864, "Frozen Spire"), # d quest
    "Ancient Key [Wind D4 - NW2]":                  AdvData(10905346464, "Frozen Spire"), # d quest
    "Ancient Key [Wind D4 - NW3]":                  AdvData(10905348064, "Frozen Spire"), # d quest
    "Ancient Key [Wind D3]":                        AdvData(120556, "Frozen Spire Post-Rune"), # k cloak
    "Ancient Key [Wind A3]":                        AdvData(120834, "Frozen Spire Post-Rune"), # k cloak
    "Ancient Key [Wind C2]":                        AdvData(121361, "Frozen Spire"), # d quest
    "Ancient Key [Wind B1]":                        AdvData(120917, "Frozen Spire Post-Rune"), # double check req
    "Ancient Key [Wind E2 - NE]":                   AdvData(121665, "Frozen Spire Post-Rune"), # d quest
    "Ancient Key [Wind E2 - S]":                    AdvData(121664, "Frozen Spire"), # d quest
    "Ancient Key [Wind E4 - E]":                    AdvData(120277, "Frozen Spire Post-Rune"), # d rune
    "Ancient Key [Wind E4 - SW]":                   AdvData(120291, "Frozen Spire Post-Rune"), # k cloak, d quest

    "Ancient Key [Aggro B0 - E]":                   AdvData(122675, "Aggro Crag"),
    "Ancient Key [Aggro B0 - W]":                   AdvData(122674, "Aggro Crag"),

    "Ancient Key [Sunken B0]":                      AdvData(123147, "Sunken Island"),
    "Ancient Key [Sunken A0]":                      AdvData(123004, "Sunken Island"),

    "Ancient Key [Nunatak B1]":                     AdvData(123315, "Sea Nunatak"),
    "Ancient Key [Nunatak A1]":                     AdvData(123362, "Sea Nunatak"), # ancient rune

    "Ancient Key [Stone Dungeon D2]":               AdvData(102289, "Stony Cliffs Post-Rune"), # t quest
    "Ancient Key [Stone A2]":                       AdvData(106850, "Stony Cliffs Post-Rune"), # blue & gold tablet
    #73 keys

    "Topaz [Stone D2]":                             AdvData(107088, "Stony Cliffs"),
    "Topaz [Stone C2 - E]":                         AdvData(107587, "Stony Cliffs"),
    "Topaz [Stone C0]":                             AdvData(108051, "Stony Cliffs Post-Rune"),
    "Topaz [Stone C3 - N]":                         AdvData(106886, "Stony Cliffs"),
    "Topaz [Stone C3 - S]":                         AdvData(106890, "Stony Cliffs"),
    "Topaz [Stone C2 - W]":                         AdvData(107584, "Stony Cliffs Post-Rune"),
    "Topaz [Stone B0]":                             AdvData(108014, "Stony Cliffs NW"),
    "Topaz [Stone B1]":                             AdvData(107043, "Stony Cliffs NW"),
    "Topaz [Stone B2]":                             AdvData(107361, "Stony Cliffs Post-Rune"), #Rq: topaz quest
    "Topaz [Stone Dungeon C1]":                     AdvData(101824, "Stony Cliffs NW"), #Rq: gopher gloves
    "Topaz [Rolling A0]":                           AdvData(103801, "Rolling Rocks"), #Rq: topaz quest, 7 stars
    "Topaz [Tropic A1]":                            AdvData(104450, "Star Tropic"), #Rq: ancient rune stone, all legendaries - serpent circlet,

    "Sapphire [Water C2 - W]":                      AdvData(108790, "Tidal Reef"),
    "Sapphire [Water B2 - S]":                      AdvData(108964, "Tidal Reef"),
    "Sapphire [Water B2 - N]":                      AdvData(108970, "Tidal Reef"),
    "Sapphire [Water D2 - N]":                      AdvData(109090, "Tidal Reef Post-Rune"),
    "Sapphire [Water C0]":                          AdvData(110021, "Tidal Reef Post-Rune"), #sapphire rune stone #
    "Sapphire [Water D2 - W]":                      AdvData(109105, "Tidal Reef Post-Rune"), #s rune stone
    "Sapphire [Water D1]":                          AdvData(109873, "Tidal Reef Post-Rune"), #s rune stone
    "Sapphire [Water D3]":                          AdvData(113108, "Tidal Reef Post-Rune"), #s rune stone
    "Sapphire [Water C2 - N]":                      AdvData(108783, "Tidal Reef"),  # sapphire quest
    "Sapphire [Water A1]":                          AdvData(111264, "Tidal Reef"), #frog flippers
    "Sapphire [Sunken B0]":                         AdvData(123145, "Sunken Island"), #sapphire quest, 21 stars
    "Sapphire [Tropic A1]":                         AdvData(104451, "Star Tropic"), # ancient rune stone, all legendaries except serpent circlet

    "Ruby [Fire B2]":                               AdvData(115353, "Raging Volcano"),
    "Ruby [Fire C2]":                               AdvData(115497, "Raging Volcano"),
    "Ruby [Fire C0]":                               AdvData(116184, "Raging Volcano Post-Rune"), # ruby rune stone
    "Ruby [Fire D2 - E]":                           AdvData(115797, "Raging Volcano"),
    "Ruby [Fire D2 - W]":                           AdvData(115801, "Raging Volcano"),
    "Ruby [Fire D1]":                               AdvData(115980, "Raging Volcano Post-Rune"), # ruby rune stone
    "Ruby [Fire A3 - S]":                           AdvData(116763, "Raging Volcano Post-Rune"), #r rune stone
    "Ruby [Fire A3 - N]":                           AdvData(116762, "Raging Volcano Post-Rune"),
    "Ruby [Fire A3 - NW]":                          AdvData(116772, "Raging Volcano Post-Rune"), # r rune stone
    "Ruby [Fire D0]":                               AdvData(117604, "Raging Volcano NE"), # salamander shirt
    "Ruby [Aggro B1]":                              AdvData(122848, "Aggro Crag"), # ruby quest, 35 stars
    "Ruby [Tropic A1]":                             AdvData(104452, "Star Tropic"), # ancient rune stone, all legendaries - serpent circlet

    "Diamond [Wind C4]":                            AdvData(120171, "Frozen Spire"),
    "Diamond [Wind D4]":                            AdvData(122396, "Frozen Spire Post-Rune"),
    "Diamond [Wind B2]":                            AdvData(120989, "Frozen Spire"),
    "Diamond [Wind D2]":                            AdvData(121523, "Frozen Spire"),
    "Diamond [Wind C2]":                            AdvData(121359, "Frozen Spire Post-Rune"), # diamond rune stone
    "Diamond [Wind C1 - W]":                        AdvData(121254, "Frozen Spire Post-Rune"), # d rune stone
    "Diamond [Wind C1 - E]":                        AdvData(121261, "Frozen Spire Post-Rune"), # d rune stone
    "Diamond [Wind D1 - W]":                        AdvData(121444, "Frozen Spire Post-Rune"), # d rune stone
    "Diamond [Wind D1 - E]":                        AdvData(121440, "Frozen Spire Post-Rune"), # d rune stone
    "Diamond [Wind C3]":                            AdvData(120634, "Frozen Spire Post-Rune"), # diamond quest complete
    "Diamond [Nunatak B0]":                         AdvData(123471, "Sea Nunatak"), # diamond quest complete
    "Diamond [Tropic A1]":                          AdvData(104453, "Star Tropic"), # ancient rune stone, all legendaries - serpent circlet

    "Obsidian [Rolling A1]":                        AdvData(104496, "Rolling Rocks"),  # gopher gloves, 7 stars
    "Obsidian [Stone D1]":                          AdvData(107156, "Stony Cliffs"),
    "Obsidian [Stone A2]":                          AdvData(106851, "Stony Cliffs Post-Rune"),  # DOUBLE CHECK ID # stone tablet blue, tablet golda
    "Obsidian [Water D0]":                          AdvData(110317, "Tidal Reef Post-Rune"),  # frog flippers
    "Obsidian [Fire E0]":                           AdvData(118311, "Raging Volcano Post-Rune"),  # salamander shirt
    "Obsidian [Fire D4]":                           AdvData(118028, "Raging Volcano Post-Rune"),  # DOUBLE CHECK ID #
    "Obsidian [Wind B0]":                           AdvData(120363, "Frozen Spire"),
    "Obsidian [Aggro B0]":                          AdvData(122671, "Aggro Crag"),  # salamander shirt
    "Obsidian [Sunken A0]":                         AdvData(123005, "Sunken Island"),  # frog flippers
    "Obsidian [Nunatak B1]":                        AdvData(123316, "Sea Nunatak"),  # diamond quest
    "Obsidian [Serpent A1]":                        AdvData(125702, "Serpent Stacks Post-Rune"),  # rune stones: t,s,r,d,o, serpent circlet(?)
    "Obsidian [Lost A1]":                           AdvData(127285, "Lost Landing"),  # phoenix flute (or secret find?)

    # 4 of these are trapped in bells, and should be removed from total.
    # 3x4=12 trapped in music puzzle
    # 1 trapped in volcano idol puzzle
    # 1 trapped in stone tablet puzzle
    # Total of 17 stars that aren't locations.
    "Star Piece [Ancient C0]":                     AdvData(100145, "Ancient Isle"),
    "Star Piece [Ancient A1]":                     AdvData(101048, "Ancient Isle"),
    "Star Piece [Ancient B1]":                     AdvData(100250, "Ancient Isle"),

    "Star Piece [Stone C1]":                       AdvData(107477, "Stony Cliffs"), # t quest
    "Star Piece [Stone E1]":                       AdvData(107757, "Stony Cliffs"),
    "Star Piece [Stone B2]":                       AdvData(107364, "Stony Cliffs Post-Rune"), # t quest
    "Star Piece [Stone B3]":                       AdvData(108106, "Stony Cliffs Post-Rune"), # t quest
    "Star Piece [Stone B4]":                       AdvData(106970, "Stony Cliffs Post-Rune"), # g globes t quest
    "Star Piece [Stone C4]":                       AdvData(107253, "Stony Cliffs Post-Rune"), # g gloves t quest
    "Star Piece [Stone E4]":                       AdvData(107811, "Stony Cliffs Post-Rune"),
    "Star Piece [Stone C0]":                       AdvData(108057, "Stony Cliffs"), # t quest
    "Star Piece [Stone Dungeon E1]":               AdvData(125464, "Stony Cliffs Post-Rune"), # t quest
    "Star Piece [Stone Dungeon E2]":               AdvData(102456, "Stony Cliffs Post-Rune"), # g gloves, f flippers
    "Star Piece [Stone Dungeon C3]":               AdvData(101720, "Stony Cliffs Post-Rune"), # t quest
    "Star Piece [Stone Dungeon C1]":               AdvData(101817, "Stony Cliffs NW"), # g gloves
    "Star Piece [Stone Dungeon B1]":               AdvData(124770, "Stony Cliffs NW"), # g gloves
    "Star Piece [Stone A1]":                       AdvData(107547, "Stony Cliffs NW"), # 5 stars

    "Star Piece [Water C1 - E]":                   AdvData(109452, "Tidal Reef"),
    "Star Piece [Water C0]":                       AdvData(110017, "Tidal Reef"), # s quest
    "Star Piece [Water C1 - W]":                   AdvData(109440, "Tidal Reef"),
    "Star Piece [Water C2]":                       AdvData(108791, "Tidal Reef"), # s quest
    "Star Piece [Water D2]":                       AdvData(109108, "Tidal Reef Post-Rune"), # f flippers, k cloak
    "Star Piece [Water D3]":                       AdvData(113112, "Tidal Reef Post-Rune"), # f flippers | Double check
    "Star Piece [Water E2]":                       AdvData(113306, "Tidal Reef Post-Rune"), # f flippers
    "Star Piece [Water E0 - W]":                   AdvData(110696, "Tidal Reef Post-Rune"), # f flippers
    "Star Piece [Water E0 - E]":                   AdvData(110700, "Tidal Reef Post-Rune"), # s quest | double check
    "Star Piece [Water B1]":                       AdvData(109688, "Tidal Reef"), # f flippers
    "Star Piece [Water A0]":                       AdvData(111569, "Tidal Reef Post-Rune"), # s rune
    "Star Piece [Water A2 - N]":                   AdvData(112442, "Tidal Reef Post-Rune"), # f flippers s quest || k cloak
    "Star Piece [Water A2 - S]":                   AdvData(112438, "Tidal Reef Post-Rune"), # f flippers
    "Star Piece [Water A4]":                       AdvData(126061, "Tidal Reef S"), # f flippers
    "Star Piece [Water B4]":                       AdvData(126136, "Tidal Reef S"),

    "Star Piece [Fire B4]":                        AdvData(118454, "Raging Volcano Post-Rune"), # r quest
    "Star Piece [Fire B3]":                        AdvData(118779, "Raging Volcano Post-Rune"),
    "Star Piece [Fire C3]":                        AdvData(116299, "Raging Volcano Post-Rune"),
    "Star Piece [Fire C1]":                        AdvData(115680, "Raging Volcano"),
    "Star Piece [Fire C0]":                        AdvData(116181, "Raging Volcano"),
    "Star Piece [Fire D1 - S]":                    AdvData(115983, "Raging Volcano"), # r quest
    "Star Piece [Fire D1 - N]":                    AdvData(115987, "Raging Volcano Post-Rune"), # r rune
    "Star Piece [Fire D3 - S]":                    AdvData(119006, "Raging Volcano Post-Rune"), # r quest | double check
    "Star Piece [Fire D3 - W]":                    AdvData(119008, "Raging Volcano Post-Rune"), # r quest | double
    "Star Piece [Fire D4]":                        AdvData(118016, "Raging Volcano Post-Rune"), # f flippers # s shirt?
    "Star Piece [Fire E3]":                        AdvData(119106, "Raging Volcano Post-Rune"),
    "Star Piece [Fire E1 - E]":                    AdvData(118578, "Raging Volcano Post-Rune"), # r quest shirt
    "Star Piece [Fire E1 - W]":                    AdvData(118588, "Raging Volcano Post-Rune"), # s shirt
    "Star Piece [Fire E0]":                        AdvData(118314, "Raging Volcano NE"), # s shirt

    #locations might be broken due to in-game randomness
    "Star Piece [Wind D4]":                        AdvData(122399, "Frozen Spire"),
    "Star Piece [Wind C3 - W]":                    AdvData(120638, "Frozen Spire"), # d rune
    "Star Piece [Wind C3 - NE]":                   AdvData(120631, "Frozen Spire"), # d rune
    "Star Piece [Wind B3]":                        AdvData(121097, "Frozen Spire Post-Rune"), # k cloak
    "Star Piece [Wind A3]":                        AdvData(120833, "Frozen Spire Post-Rune"), # k cloak
    "Star Piece [Wind B2 - N]":                    AdvData(120998, "Frozen Spire Post-Rune"), # k cloak?
    "Star Piece [Wind C2]":                        AdvData(121360, "Frozen Spire"), # d quest
    "Star Piece [Wind D2]":                        AdvData(121525, "Frozen Spire Post-Rune"), # k cloak
    "Star Piece [Wind E2]":                        AdvData(121656, "Frozen Spire"), # d quest
    "Star Piece [Wind E4]":                        AdvData(120280, "Frozen Spire Post-Rune"), # k cloak
    "Star Piece [Wind E1]":                        AdvData(121560, "Frozen Spire Post-Rune"), # k cloak, g gloves
    "Star Piece [Wind B1]":                        AdvData(120916, "Frozen Spire"),
    "Star Piece [Wind B0]":                        AdvData(120361, "Frozen Spire Post-Rune"),
    "Star Piece [Wind A0]":                        AdvData(120219, "Frozen Spire Post-Rune"), # k cloak
    "Star Piece [Wind B2 - S]":                    AdvData(120995, "Frozen Spire Post-Rune"),

    "Star Piece [Rolling A0]":                     AdvData(103803, "Rolling Rocks"), # 7 stars, t quest
    "Star Piece [Rolling B1]":                     AdvData(104766, "Rolling Rocks Post-Rune"), #
    "Star Piece [Rolling B0]":                     AdvData(104884, "Rolling Rocks Post-Rune"), # g gloves

    "Star Piece [Sunken B0]":                      AdvData(123146, "Sunken Island"), # 21 stars, s quest
    "Star Piece [Sunken A1]":                      AdvData(123082, "Sunken Island"), # ancient rune

    "Star Piece [Aggro B1]":                       AdvData(122849, "Aggro Crag"), # 35 star, r quest
    "Star Piece [Aggro A1]":                       AdvData(122918, "Aggro Crag"), # ancient rune

    "Star Piece [Nunatak B0]":                     AdvData(123470, "Sea Nunatak"), # 49 stars, d quest
    "Star Piece [Nunatak A0]":                     AdvData(123384, "Sea Nunatak"), # ancient rune

    "Star Piece [Lost B1]":                        AdvData(128962, "Lost Landing"),

    "Star Piece [Shoal A0]":                       AdvData(104392, "Shoal"), # f flippers

    "Star Piece [Tropic A0]":                      AdvData(103229, "Star Tropic"), #
    "Star Piece [Tropic B0 - S]":                  AdvData(104244, "Star Tropic"), # a rune
    "Star Piece [Tropic B0 - N]":                  AdvData(104248, "Star Tropic"), # o rune, s shirt
    "Star Piece [Tropic A1 - 1]":                  AdvData(728130112848, "Star Tropic"), # g gloves
    "Star Piece [Tropic A1 - 2]":                  AdvData(728130114480, "Star Tropic"), # g gloves, s shirt,
    "Star Piece [Tropic A1 - 3]":                  AdvData(728130116048, "Star Tropic"), # g gloves, s shirt, f flippers
    "Star Piece [Tropic A1 - 4]":                  AdvData(728130117680, "Star Tropic"), # g gloves, s shirt, f flippers, k cloak

    "Star Piece [Serpent A3]":                     AdvData(103356, "Serpent Stacks"), # k cloak
    "Star Piece [Serpent A2]":                     AdvData(104825, "Serpent Stacks"), # k cloak, s circlet
    "Star Piece [Serpent A1 - W]":                 AdvData(125692, "Serpent Stacks Post-Rune"), # k cloak, s circlet
    "Star Piece [Serpent A1 - N]":                 AdvData(125709, "Serpent Stacks Post-Rune"), # k cloak, s circlet
    "Star Piece [Serpent A4]":                     AdvData(125783, "Serpent Stacks Post-Rune"), # s circlet, t quest
    "Star Piece [Serpent A6 - W]":                 AdvData(126797, "Serpent Stacks Post-Rune"), # s quest, s circlet
    "Star Piece [Serpent A6 - E]":                 AdvData(126808, "Serpent Stacks Post-Rune"), # s quest, s circlet
    "Star Piece [Serpent A7 - W]":                 AdvData(126986, "Serpent Stacks Post-Rune"), # s circlet, r quest
    "Star Piece [Serpent A7 - E]":                 AdvData(126966, "Serpent Stacks Post-Rune"), # s circlet, r quest
    "Star Piece [Serpent A8 - N]":                 AdvData(127075, "Serpent Stacks Post-Rune"), # s circlet, d quest
    "Star Piece [Serpent A8 - S]":                 AdvData(127070, "Serpent Stacks Post-Rune"), # s circlet, d quest

    "Star Piece [Locked A1]":                      AdvData(104281, "Locked"),
    #91 stars


    #"Jellyfish 1]": AdvData(991027, "Topaz Sea"),

    "Music Note [Stone C1]":                       AdvData(107494, "Stony Cliffs"), #
    "Music Note [Stone D4]":                       AdvData(106797, "Stony Cliffs Post-Rune"), # topaz rune
    "Music Note [Stone B3]":                       AdvData(108112, "Stony Cliffs Post-Rune"), # topaz rune
    "Music Note [Stone B0]":                       AdvData(108015, "Stony Cliffs NW"), # topaz rune
    "Music Note [Stone B2]":                       AdvData(107378, "Stony Cliffs Post-Rune"), # topaz quest
    "Music Note [Stone D1]":                       AdvData(107170, "Stony Cliffs"), # topaz quest

    "Music Note [Water C1]":                       AdvData(109459, "Tidal Reef"),
    "Music Note [Water E0]":                       AdvData(110707, "Tidal Reef Post-Rune"), # s rune
    "Music Note [Water D1]":                       AdvData(109898, "Tidal Reef Post-Rune"), # s rune
    "Music Note [Water E2]":                       AdvData(113309, "Tidal Reef Post-Rune"), # s rune
    "Music Note [Water B0]":                       AdvData(113769, "Tidal Reef Post-Rune"), # s rune
    "Music Note [Water A2]":                       AdvData(112459, "Tidal Reef Post-Rune"), # s rune

    "Music Note [Fire A2]":                        AdvData(115241, "Raging Volcano"),
    "Music Note [Fire C3]":                        AdvData(116308, "Raging Volcano Post-Rune"), # r rune
    "Music Note [Fire B0]":                        AdvData(119349, "Raging Volcano Post-Rune"), # r rune
    "Music Note [Fire B2]":                        AdvData(115377, "Raging Volcano Post-Rune"), # r rune
    "Music Note [Fire E1]":                        AdvData(118593, "Raging Volcano Post-Rune"), # r rune
    "Music Note [Fire D3]":                        AdvData(119009, "Raging Volcano Post-Rune"), # salamander shirt

    "Music Note [Wind B1]":                        AdvData(120922, "Frozen Spire"),
    "Music Note [Wind A0]":                        AdvData(120222, "Frozen Spire"),
    "Music Note [Wind E3]":                        AdvData(121759, "Frozen Spire Post-Rune"),  # d rune
    "Music Note [Wind C3]":                        AdvData(120640, "Frozen Spire Post-Rune"),  # d rune,
    "Music Note [Wind A2]":                        AdvData(120737, "Frozen Spire Post-Rune"), # d quest,
    "Music Note [Wind D3]":                        AdvData(120557, "Frozen Spire Post-Rune"), # d quest



    # In the future, could include milestones as locations. e.g. each of the steam achievements, plus extras.
}

seashell_table = {

    # 24 checks
    "Shell [Water B2]":                            AdvData(109001, "Tidal Reef"),
    "Shell [Water C0]":                            AdvData(110034, "Tidal Reef"),
    "Shell [Water B0]":                            AdvData(113779, "Tidal Reef"),
    "Shell [Water B1]":                            AdvData(109727, "Tidal Reef"),
    "Shell [Water C1]":                            AdvData(109466, "Tidal Reef"),
    "Shell [Water C2]":                            AdvData(108836, "Tidal Reef"),
    "Shell [Water D2]":                            AdvData(109127, "Tidal Reef Post-Rune"), # s rune
    "Shell [Water A1]":                            AdvData(111286, "Tidal Reef"), # s rune
    "Shell [Water A0]":                            AdvData(111579, "Tidal Reef Post-Rune"), # s rune
    "Shell [Water A3]":                            AdvData(114803, "Tidal Reef"), # s rune
    "Shell [Water B3]":                            AdvData(110854, "Tidal Reef S"), # s rune
    "Shell [Water B4]":                            AdvData(126146, "Tidal Reef S"), # s rune
    "Shell [Water C4]":                            AdvData(126171, "Tidal Reef S"),
    "Shell [Water C3]":                            AdvData(108596, "Tidal Reef Post-Rune"), # s rune
    "Shell [Water D4]":                            AdvData(129544, "Tidal Reef Post-Rune"), # s rune
    "Shell [Water E4]":                            AdvData(125935, "Tidal Reef Post-Rune"), # s rune
    "Shell [Water E2]":                            AdvData(113315, "Tidal Reef Post-Rune"), # s rune
    "Shell [Water E1]":                            AdvData(113547, "Tidal Reef Post-Rune"), # s rune
    "Shell [Water E0]":                            AdvData(110713, "Tidal Reef Post-Rune"), # s rune
    "Shell [Water D3]":                            AdvData(113163, "Tidal Reef Post-Rune"), # s rune
    "Shell [Water A4]":                            AdvData(126066, "Tidal Reef S"),  # f flippers
    "Shell [Water D1]":                            AdvData(109899, "Tidal Reef"),  # f flippers
    "Shell [Water D0]":                            AdvData(110330, "Tidal Reef Post-Rune"),  # f flippers
    "Shell [Water A2]":                            AdvData(112462, "Tidal Reef Post-Rune"),  # f flippers





}

jellyfish_table = {

# 10 checks
    "Jellyfish 1":                                 AdvData(3952011560480, "Topaz Sea"),
    "Jellyfish 2":                                 AdvData(3952011768336, "Diamond Sea"),
    "Jellyfish 3":                                 AdvData(3952011272432, "Obsidian Sea"),
    "Jellyfish 4":                                 AdvData(395201154448, "Sapphire Sea"),
    "Jellyfish 5":                                 AdvData(3952011672512, "Ruby Sea"),
    "Jellyfish 6":                                 AdvData(3952011880480, "Ruby Sea"),
    "Jellyfish 7":                                 AdvData(3952011848176, "Beast Sea"),
    "Jellyfish 8":                                 AdvData(39520111040192, "Beast Sea"),
    "Jellyfish 9":                                 AdvData(3952011528496, "Lost Sea"),
    "Jellyfish 10":                                AdvData(3952011976112, "Northeast Sea"),

}

# 24 checks
secrets_table = {

    "Discover Ancient Secret 1": AdvData(101044, "Ancient Isle"),

    "Discover Stone Secret 1": AdvData(107724, "Stony Cliffs"),
    "Discover Stone Secret 2": AdvData(106792, "Stony Cliffs Post-Rune"),

    "Discover Rolling Secret 1": AdvData(103790, "Rolling Rocks"),

    "Discover Nunatak Secret 1": AdvData(123457, "Sea Nunatak"),
    "Discover Nunatak Secret 2": AdvData(123426, "Sea Nunatak"),
    "Discover Nunatak Secret 3": AdvData(123461, "Sea Nunatak"),
    "Discover Nunatak Secret 4": AdvData(123447, "Sea Nunatak"),

    "Discover Shoal Secret 1": AdvData(104364, "Shoal"),
    "Discover Shoal Secret 2": AdvData(104321, "Shoal"),
    "Discover Shoal Secret 3": AdvData(104322, "Shoal"),

    "Discover Aggro Secret 1": AdvData(122712, "Aggro Crag"),
    "Discover Aggro Secret 2": AdvData(122517, "Aggro Crag"),
    "Discover Aggro Secret 3": AdvData(122488, "Aggro Crag"),

    "Discover Sunken Secret 1": AdvData(122982, "Sunken Island"),

    "Discover Tropic Secret 1": AdvData(103122, "Star Tropic"),

    "Discover Lost Secret 1": AdvData(128953, "Lost Landing"),
    "Discover Lost Secret 2": AdvData(128951, "Lost Landing"),

    "Discover Fire Secret 1": AdvData(118109, "Raging Volcano Post-Rune"),
    "Discover Fire Secret 2": AdvData(115494, "Raging Volcano"),
    "Discover Fire Secret 3": AdvData(118553, "Raging Volcano Post-Rune"),

    "Discover Wind Secret 1": AdvData(120206, "Frozen Spire"),
    "Discover Wind Secret 2": AdvData(120347, "Frozen Spire"),
    "Discover Wind Secret 3": AdvData(121434, "Frozen Spire Post-Rune"),

}

# Est. 101 extra checks here.
locksanity_table = {
    "Lock [Ancient B3]":                            AdvData(100221, "Ancient Isle"),
    "Lock [Ancient B2]":                            AdvData(101289, "Ancient Isle"),
    "Lock [Ancient A3]":                            AdvData(100548, "Ancient Isle"),
    "3x Lock [Ancient C2]":                         AdvData(100436, "Ancient Isle"),
    "3x Lock [Ancient A1]":                         AdvData(101049, "Ancient Isle"), # access o sea

    "Lock [Stone C2]":                              AdvData(107588, "Stony Cliffs"),
    "3x Lock [Stone E1]":                           AdvData(107761, "Stony Cliffs"),
    "Lock [Stone B1]":                              AdvData(107044, "Stony Cliffs NW"), # t rune

    "Lock [Water B2]":                              AdvData(108972, "Tidal Reef"),
    "3x Lock [Water C1]":                           AdvData(109439, "Tidal Reef"),
    "Lock [Water D3]":                              AdvData(113120, "Tidal Reef Post-Rune"), # s rune

    "3x Lock (Fire) [Fire E0]":                     AdvData(118309, "Raging Volcano NE"),
    "Lock [Fire A3]":                               AdvData(116779, "Raging Volcano Post-Rune"),
    "Lock [Fire D2]":                               AdvData(115819, "Raging Volcano"),
    "3x Lock [Fire D2]":                            AdvData(115799, "Raging Volcano"),

    "Lock [Wind C3]":                               AdvData(120637, "Frozen Spire Post-Rune"),
    "3x Lock [Wind D3]":                            AdvData(120553, "Frozen Spire"),
    "Lock [Wind D1]":                               AdvData(121455, "Frozen Spire Post-Rune"),
    "Lock (Wind) [Wind A0]":                        AdvData(120220, "Frozen Spire"),

    "3x Lock [Sanctum B2 - W]":                     AdvData(123943, "Sanctum"),
    "3x Lock [Sanctum B2 - E]":                     AdvData(123942, "Sanctum"),
    "3x Lock [Sanctum A1]":                         AdvData(124157, "Sanctum"),
    "3x Lock [Sanctum C1]":                         AdvData(124282, "Sanctum"),

    "3x Lock [Rolling B1]":                         AdvData(104767, "Rolling Rocks Post-Rune"),

    "3x Lock [Sunken A1]":                          AdvData(123081, "Sunken Island"),

    "3x Lock [Aggro A1]":                           AdvData(122917, "Aggro Crag"),

    "3x Lock [Nunatak A0]":                         AdvData(123383, "Sea Nunatak"),

    "6x Lock [Locked A0]":                          AdvData(104286, "Locked"),

    "Lock [Lost A1]":                               AdvData(127286, "Lost Landing"),

    "Star Lock 1 [Ancient C1]":                     AdvData(100984, "Ancient Isle"),

    "Star Lock 3 [Overworld]":                      AdvData(108488, "Topaz Sea"),
    "Star Lock 15 [Overworld]":                     AdvData(108494, "Topaz Sea"),
    "Star Lock 30 [Overworld]":                     AdvData(108499, "Diamond Sea"),
    "Star Lock 45 [Overworld]":                     AdvData(108516, "Obsidian Sea"),

    "Star Lock 5 [Stone A1]":                       AdvData(107545, "Stony Cliffs NW"),
    "Star Lock 15 [Stone C4]":                      AdvData(107259, "Stony Cliffs Post-Rune"),
    "Star Lock 20 [Stone E3]":                      AdvData(106823, "Stony Cliffs Post-Rune"),
    "Star Lock 20 [Stone Dungeon A1]":              AdvData(101941, "Stony Cliffs Post-Rune"),

    "Star Lock 30 [Water A2]":                      AdvData(112443, "Tidal Reef Post-Rune"),

    "Star Lock 7 [Rolling A0]":                     AdvData(103800, "Rolling Rocks"),
    "Star Lock 21 [Sunken B0]":                     AdvData(123144, "Sunken Island"),
    "Star Lock 30 [Lost B0]":                       AdvData(100181, "Lost Landing"),
    "Star Lock 35 [Aggro B0]":                      AdvData(122670, "Aggro Crag"),
    "Star Lock 49 [Nunatak B0]":                    AdvData(123481, "Sea Nunatak"),

    "Ancient Rune Lock [Ancient B1]":               AdvData(100251, "Ancient Isle"),

    "Topaz Rune Lock [Stone C0]":                   AdvData(108053, "Stony Cliffs Post-Rune"), #post-rune is inclusive of rune lock checks
    "Topaz Rune Lock [Stone C1]":                   AdvData(107476, "Stony Cliffs Post-Rune"),
    "Topaz Rune Lock [Stone E1]":                   AdvData(107758, "Stony Cliffs Post-Rune"),
    "Topaz Rune Lock [Stone E2]":                   AdvData(107666, "Stony Cliffs Post-Rune"),
    "Topaz Rune Lock [Stone E3]":                   AdvData(106822, "Stony Cliffs Post-Rune"),
    "Topaz Rune Lock [Stone C4]":                   AdvData(107252, "Stony Cliffs Post-Rune"),

    "Sapphire Rune Lock [Water C0]":                AdvData(110023, "Tidal Reef Post-Rune"),
    "Sapphire Rune Lock [Water B2]":                AdvData(108971, "Tidal Reef Post-Rune"),
    "Sapphire Rune Lock [Water A0]":                AdvData(111572, "Tidal Reef Post-Rune"),
    "Sapphire Rune Lock [Water A3]":                AdvData(114802, "Tidal Reef Post-Rune"),
    "Sapphire Rune Lock [Water D2 - N]":            AdvData(109109, "Tidal Reef Post-Rune"),
    "Sapphire Rune Lock [Water D2 - S]":            AdvData(109106, "Tidal Reef Post-Rune"),
    "Sapphire Rune Lock [Water D0]":                AdvData(110316, "Tidal Reef Post-Rune"),
    "Sapphire Rune Lock [Water C3 - E]":            AdvData(108592, "Tidal Reef Post-Rune"),
    "Sapphire Rune Lock [Water C3 - W]":            AdvData(108593, "Tidal Reef Post-Rune"),
    "Sapphire Rune Lock [Water B3]":                AdvData(110851, "Tidal Reef Post-Rune"),

    "Ruby Rune Lock [Fire A1 - S]":                 AdvData(116434, "Raging Volcano Post-Rune"),
    "Ruby Rune Lock [Fire A1 - E]":                 AdvData(116436, "Raging Volcano Post-Rune"),
    "Ruby Rune Lock [Fire A2]":                     AdvData(115237, "Raging Volcano Post-Rune"),
    "Ruby Rune Lock [Fire A3]":                     AdvData(116778, "Raging Volcano Post-Rune"),
    "Ruby Rune Lock [Fire B2 - N]":                 AdvData(115374, "Raging Volcano Post-Rune"),
    "Ruby Rune Lock [Fire B2 - S]":                 AdvData(115375, "Raging Volcano Post-Rune"),
    "Ruby Rune Lock [Fire C0]":                     AdvData(116200, "Raging Volcano Post-Rune"),
    "Ruby Rune Lock [Fire C1]":                     AdvData(115702, "Raging Volcano Post-Rune"),
    "Ruby Rune Lock [Fire C3 - S]":                 AdvData(116304, "Raging Volcano Post-Rune"),
    "Ruby Rune Lock [Fire C3 - W]":                 AdvData(116302, "Raging Volcano Post-Rune"),
    "Ruby Rune Lock [Fire D1]":                     AdvData(116005, "Raging Volcano Post-Rune"),
    "Ruby Rune Lock [Fire E0]":                     AdvData(118316, "Raging Volcano Post-Rune"),

    "Diamond Rune Lock [Wind C3]":                  AdvData(120636, "Frozen Spire Post-Rune"),
    "Diamond Rune Lock [Wind D4]":                  AdvData(122402, "Frozen Spire Post-Rune"),
    "Diamond Rune Lock [Wind E3]":                  AdvData(121758, "Frozen Spire Post-Rune"),
    "Diamond Rune Lock [Wind E2 - W]":              AdvData(121659, "Frozen Spire Post-Rune"),
    "Diamond Rune Lock [Wind E2 - E]":              AdvData(121666, "Frozen Spire Post-Rune"),
    "Diamond Rune Lock [Wind E0]":                  AdvData(120494, "Frozen Spire Post-Rune"),
    "Diamond Rune Lock [Wind D1]":                  AdvData(121454, "Frozen Spire Post-Rune"),
    "Diamond Rune Lock [Wind C2]":                  AdvData(121372, "Frozen Spire Post-Rune"),
    "Diamond Rune Lock [Wind C1]":                  AdvData(121260, "Frozen Spire Post-Rune"),
    "Diamond Rune Lock [Wind B1]":                  AdvData(120915, "Frozen Spire Post-Rune"),
    "Diamond Rune Lock [Wind B3]":                  AdvData(121098, "Frozen Spire Post-Rune"),
    "Diamond Rune Lock [Wind A2]":                  AdvData(120736, "Frozen Spire Post-Rune"),

    "Elemental Rune Lock [Serpent A2]":             AdvData(104819, "Serpent Stacks"),
    "Obsidian Rune Lock [Serpent A1 - N]":          AdvData(125703, "Serpent Stacks Post-Rune"),
    "Obsidian Rune Lock [Serpent A1 - W]":          AdvData(125701, "Serpent Stacks Post-Rune"),
    "Obsidian Rune Lock [Serpent A1 - E]":          AdvData(125689, "Serpent Stacks Post-Rune"),
    "Obsidian Rune Lock [Serpent A3]":              AdvData(103366, "Serpent Stacks Post-Rune"),

    "Ancient Rune Lock [Rolling A1]":               AdvData(104495, "Rolling Rocks Post-Rune"), # double check later
    "Ancient Rune Lock [Rolling B0]":               AdvData(104912, "Rolling Rocks Post-Rune"),

    "Ancient Rune Lock [Sunken A0]":                AdvData(123006, "Sunken Island"),
    "Ancient Rune Lock [Sunken B1]":                AdvData(123252, "Sunken Island"),

    "Ancient Rune Lock [Aggro B1]":                 AdvData(122860, "Aggro Crag"),
    "Ancient Rune Lock [Aggro A1]":                 AdvData(122919, "Aggro Crag"),

    "Ancient Rune Lock [Nunatak B0]":               AdvData(123480, "Sea Nunatak"),

    "Ancient Rune Lock [Locked A1]":                AdvData(104284, "Locked"),

    "Ancient Rune Lock [Tropic A1]":                AdvData(104457, "Star Tropic"),
    "Ancient Rune Lock [Tropic B0]":                AdvData(104247, "Star Tropic"),
    "Obsidian Rune Lock [Tropic B0]":               AdvData(104246, "Star Tropic"),

    "Ancient Rune Lock [Shoal A0]":                 AdvData(104388, "Shoal"),

}

# 196 checks
snakesanity_table = {
    "Snakeblock [Ancient B3]": AdvData(100223, "Ancient Isle"),
    "Snakeblock [Ancient B2 - W]": AdvData(101292, "Ancient Isle"),
    "Snakeblock [Ancient B2 - E]": AdvData(101294, "Ancient Isle"),
    "Snakeblock [Ancient A3]": AdvData(100550, "Ancient Isle"),
    "Snakeblock [Ancient A1]": AdvData(101050, "Ancient Isle"),
    "Snakeblock [Ancient C2 - E]": AdvData(100429, "Ancient Isle"),
    "Snakeblock [Ancient C2 - S]": AdvData(100424, "Ancient Isle"),
    "Snakeblock [Ancient C2 - W]": AdvData(100423, "Ancient Isle"),
    "Snakeblock [Ancient C3]": AdvData(101434, "Ancient Isle"),

    "Snakeblock [Stone D2]": AdvData(107090, "Stony Cliffs"),
    "Snakeblock [Stone E1 - W]": AdvData(107760, "Stony Cliffs"),
    "Snakeblock [Stone C1]": AdvData(107480, "Stony Cliffs"), # topaz Quest
    "Snakeblock [Stone D1]": AdvData(107164, "Stony Cliffs"), # topaz Quest
    "Snakeblock [Stone E1 - E]": AdvData(107759, "Stony Cliffs Post-Rune"), # t quest
    "Snakeblock [Stone E0]": AdvData(108233, "Stony Cliffs Post-Rune"),
    "Snakeblock [Stone B1 - W]": AdvData(107048, "Stony Cliffs NW"),
    "Snakeblock [Stone B0]": AdvData(108013, "Stony Cliffs NW"),
    "Snakeblock [Stone A2 - N]": AdvData(106853, "Stony Cliffs NW"),
    "Snakeblock [Stone A2 - S]": AdvData(106852, "Stony Cliffs Post-Rune"),
    "Snakeblock [Stone A3]": AdvData(107422, "Stony Cliffs Post-Rune"),
    "Snakeblock [Stone B3 - S]": AdvData(108107, "Stony Cliffs Post-Rune"),
    "Snakeblock [Stone A4 - W]": AdvData(107712, "Stony Cliffs Post-Rune"),
    "Snakeblock [Stone A0]": AdvData(108155, "Stony Cliffs NW"),
    "Snakeblock [Stone B1 - E]": AdvData(107050, "Stony Cliffs NW"),
    "Snakeblock [Stone B4]": AdvData(106956, "Stony Cliffs Post-Rune"), #g gloves, 15 stars
    "Snakeblock [Stone A4 - E]": AdvData(107713, "Stony Cliffs Post-Rune"), #g gloves, 15 stars
    "Snakeblock [Stone C4]": AdvData(107256, "Stony Cliffs Post-Rune"), # t quest
    "Snakeblock [Stone B3 - N]": AdvData(108108, "Stony Cliffs Post-Rune"),
    "Snakeblock [Stone B2 - W]": AdvData(107366, "Stony Cliffs Post-Rune"),
    "Snakeblock [Stone B2 - E]": AdvData(107367, "Stony Cliffs Post-Rune"),
    "Snakeblock [Stone C2]": AdvData(107591, "Stony Cliffs Post-Rune"),
    "Snakeblock [Stone E4]": AdvData(107810, "Stony Cliffs Post-Rune"),
    "Snakeblock [Stone Dungeon C4]": AdvData(102913, "Stony Cliffs Post-Rune"), # t quest
    "Snakeblock [Stone Dungeon C3]": AdvData(101712, "Stony Cliffs Post-Rune"), # t quest
    "Snakeblock [Stone Dungeon B2 - E]": AdvData(102663, "Stony Cliffs Post-Rune"),
    "Snakeblock [Stone Dungeon B2 - W]": AdvData(102664, "Stony Cliffs Post-Rune"),
    "Snakeblock [Stone Dungeon B2 - N]": AdvData(102667, "Stony Cliffs Post-Rune"),
    "Snakeblock [Stone Dungeon B1]": AdvData(124810, "Stony Cliffs Post-Rune"),
    "Snakeblock [Stone Dungeon D2 - E]": AdvData(6830232320112, "Stony Cliffs Post-Rune"), # t quest
    "Snakeblock [Stone Dungeon D2 - CE]": AdvData(6810232240128, "Stony Cliffs Post-Rune"), # t quest
    "Snakeblock [Stone Dungeon D2 - W]": AdvData(6800232112160, "Stony Cliffs Post-Rune"), # t quest
    "Snakeblock [Stone Dungeon D2 - CW]": AdvData(6810232192128, "Stony Cliffs Post-Rune"), # t quest
    "Snakeblock [Stone Dungeon D1 - W]": AdvData(102862, "Stony Cliffs Post-Rune"), # t quest
    "Snakeblock [Stone Dungeon D1 - CS]": AdvData(102860, "Stony Cliffs Post-Rune"), # t quest
    "Snakeblock [Stone Dungeon D1 - CN]": AdvData(102861, "Stony Cliffs"),
    "Snakeblock [Stone Dungeon D1 - E]": AdvData(102863, "Stony Cliffs Post-Rune"), # t quest
    "Snakeblock [Stone Dungeon E1]": AdvData(125459, "Stony Cliffs Post-Rune"), # t quest
    "Snakeblock [Stone Dungeon E2]": AdvData(102455, "Stony Cliffs Post-Rune"), # t quest
    "Snakeblock [Stone Dungeon C1]": AdvData(101827, "Stony Cliffs NW"), # t quest, #g gloves

    "Snakeblock [Rolling B0]": AdvData(104885, "Rolling Rocks Post-Rune"),

    "Snakeblock [Aggro B1 - E]": AdvData(122861, "Aggro Crag"), # 35 stars
    "Snakeblock [Aggro B1 - W]": AdvData(122832, "Aggro Crag"), # 35 stars, R quest, A rune
    "Snakeblock [Aggro B0 - E]": AdvData(122673, "Aggro Crag"),
    "Snakeblock [Aggro B0 - W]": AdvData(122672, "Aggro Crag"), # 35 stars, R quest, A rune, s shirt

    "Snakeblock [Locked A1 - E]": AdvData(104287, "Locked"),
    "Snakeblock [Locked A1 - C]": AdvData(104301, "Locked"),
    "Snakeblock [Locked A1 - W]": AdvData(104292, "Locked"),

    "Snakeblock [Nunatak A1]": AdvData(123363, "Sea Nunatak"), # a rune, d quest?

    "Snakeblock [Shoal A0]": AdvData(104391, "Shoal"), # a rune, k cloak

    "Snakeblock [Lost B1]": AdvData(128960, "Lost Landing"), # 30 Stars, p flute

    "Snakeblock [Tropic A0 - W]": AdvData(103230, "Star Tropic"), # k cloak
    "Snakeblock [Tropic A0 - C]": AdvData(103234, "Star Tropic"), # k cloak
    "Snakeblock [Tropic A0 - E]": AdvData(103236, "Star Tropic"), # k cloak
    "Snakeblock [Tropic B0 - N]": AdvData(104249, "Star Tropic"), # k cloak
    "Snakeblock [Tropic B0 - S]": AdvData(104245, "Star Tropic"), # k cloak

    "Damsnake [Overworld - Sapphire Sea]": AdvData(4782011320256, "Sapphire Sea"),
    "Damsnake [Overworld - Beast Sea]": AdvData(4792011784224, "Beast Sea"),
    "Damsnake [Overworld - Lost Sea]": AdvData(4782011352432, "Lost Sea"),
    "Damsnake [Overworld - Northeast Sea]": AdvData(4792011800112, "Northeast Sea"),

    "Snakeblock [Water C2 - W]": AdvData(108781, "Tidal Reef"),
    "Snakeblock [Water C2 - SE]": AdvData(108786, "Tidal Reef"),
    "Snakeblock [Water D2 - W]": AdvData(109099, "Tidal Reef"),
    "Snakeblock [Water C1 - E]": AdvData(109448, "Tidal Reef"),
    "Snakeblock [Water C1 - CE]": AdvData(109443, "Tidal Reef"),
    "Snakeblock [Water C2 - NE]": AdvData(108780, "Tidal Reef"),
    "Snakeblock [Water C2 - CE]": AdvData(108778, "Tidal Reef"),
    "Snakeblock [Water B2 - SE]": AdvData(109697, "Tidal Reef"),
    "Snakeblock [Water B2 - NE]": AdvData(109695, "Tidal Reef"),
    "Snakeblock [Water C1 - W]": AdvData(109441, "Tidal Reef"),
    "Snakeblock [Water C1 - CW]": AdvData(109442, "Tidal Reef"),
    "Snakeblock [Water B0 - E]": AdvData(113766, "Tidal Reef"), # s quest
    "Snakeblock [Water B0 - C]": AdvData(113757, "Tidal Reef"), # s quest, f flippers
    "Snakeblock [Water B2 - E]": AdvData(108963, "Tidal Reef"), # s quest,
    "Snakeblock [Water B2 - C]": AdvData(108968, "Tidal Reef"), # s quest,
    "Snakeblock [Water B3]": AdvData(110853, "Tidal Reef"),
    "Snakeblock [Water D0 - W]": AdvData(110313, "Tidal Reef"),
    "Snakeblock [Water D0 - E]": AdvData(110315, "Tidal Reef Post-Rune"),
    "Snakeblock [Water D1]": AdvData(109881, "Tidal Reef Post-Rune"),
    "Snakeblock [Water D2 - C]": AdvData(109096, "Tidal Reef Post-Rune"), # f flippers
    "Snakeblock [Water D2 - E]": AdvData(109107, "Tidal Reef Post-Rune"), # f flippers
    "Snakeblock [Water E1 - W]": AdvData(113541, "Tidal Reef Post-Rune"), # f flippers
    "Snakeblock [Water E1 - E]": AdvData(113544, "Tidal Reef Post-Rune"), # f flippers
    "Snakeblock [Water E2 - E]": AdvData(113307, "Tidal Reef Post-Rune"), # f flippers
    "Snakeblock [Water E2 - W]": AdvData(113308, "Tidal Reef Post-Rune"),
    "Snakeblock [Water E3]": AdvData(114089, "Tidal Reef Post-Rune"),
    "Snakeblock [Water D3]": AdvData(113121, "Tidal Reef Post-Rune"),
    "Snakeblock [Water A0 - W]": AdvData(111573, "Tidal Reef Post-Rune"),
    "Snakeblock [Water A0 - S]": AdvData(111571, "Tidal Reef Post-Rune"), # f flippers
    "Snakeblock [Water A2]": AdvData(112437, "Tidal Reef Post-Rune"), # f flippers, s quest, 30 stars
    "Snakeblock [Water A3]": AdvData(114801, "Tidal Reef Post-Rune"), # f flippers, s quest, 30 stars
    "Snakeblock [Water B4]": AdvData(126139, "Tidal Reef S"),
    "Snakeblock [Water B0]": AdvData(113765, "Tidal Reef Post-Rune"),

    "Snakeblock [Fire B2 - W]": AdvData(115367, "Raging Volcano"),
    "Snakeblock [Fire B2 - CW]": AdvData(115362, "Raging Volcano"),
    "Snakeblock [Fire B2 - CE]": AdvData(115366, "Raging Volcano"),
    "Snakeblock [Fire B2 - E]": AdvData(115356, "Raging Volcano"),
    "Snakeblock [Fire B2 - SW]": AdvData(115370, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire C2 - W]": AdvData(115500, "Raging Volcano"),
    "Snakeblock [Fire C2 - NE]": AdvData(115511, "Raging Volcano"),
    "Snakeblock [Fire C2 - E]": AdvData(115501, "Raging Volcano"),
    "Snakeblock [Fire D2 - W]": AdvData(115802, "Raging Volcano"),
    "Snakeblock [Fire D2 - C]": AdvData(115810, "Raging Volcano"),
    "Snakeblock [Fire D2 - NE]": AdvData(115800, "Raging Volcano"),
    "Snakeblock [Fire D2 - SE]": AdvData(115803, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire D1 - SW]": AdvData(115988, "Raging Volcano"),
    "Snakeblock [Fire D1 - W]": AdvData(115991, "Raging Volcano"),
    "Snakeblock [Fire D1 - C]": AdvData(115993, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire D1 - NE]": AdvData(116001, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire D1 - SE]": AdvData(116000, "Raging Volcano Post-Rune"), # S shirt
    "Snakeblock [Fire C1]": AdvData(115683, "Raging Volcano"),
    "Snakeblock [Fire B1]": AdvData(116901, "Raging Volcano"), # s shirt
    "Snakeblock [Fire B0]": AdvData(119347, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire A1 - E]": AdvData(116435, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire A1 - NE]": AdvData(116438, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire A0 - E]": AdvData(116597, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire A0 - W]": AdvData(116603, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire A3 - E]": AdvData(116771, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire A3 - SE]": AdvData(116773, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire A3 - S]": AdvData(116774, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire A3 - W]": AdvData(116776, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire A4]": AdvData(117784, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire B4 - W]": AdvData(118465, "Raging Volcano Post-Rune"), # r quest
    "Snakeblock [Fire B4 - E]": AdvData(118455, "Raging Volcano Post-Rune"), # r quest
    "Snakeblock [Fire B3 - CW]": AdvData(118773, "Raging Volcano Post-Rune"), # r quest
    "Snakeblock [Fire B3 - W]": AdvData(118783, "Raging Volcano Post-Rune"), # r quest
    "Snakeblock [Fire B3 - CE]": AdvData(118784, "Raging Volcano Post-Rune"), # r quest
    "Snakeblock [Fire B3 - E]": AdvData(118780, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire C3 - E]": AdvData(116307, "Raging Volcano Post-Rune"), # r quest
    "Snakeblock [Fire C3 - W]": AdvData(116301, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire C4 - NE]": AdvData(118129, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire C4 - SE]": AdvData(118122, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire D4 - W]": AdvData(118017, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire D4 - E]": AdvData(118018, "Raging Volcano Post-Rune"),# s shirt
    "Snakeblock [Fire E4 - E]": AdvData(117925, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire E4 - CE]": AdvData(117917, "Raging Volcano Post-Rune"), # s shirt
    "Snakeblock [Fire E4 - W]": AdvData(117924, "Raging Volcano Post-Rune"), # s shirt
    "Snakeblock [Fire D3 - W]": AdvData(118990, "Raging Volcano Post-Rune"), # s shirt
    "Snakeblock [Fire D3 - E]": AdvData(119003, "Raging Volcano Post-Rune"), # s shirt, r quest
    "Snakeblock [Fire D3 - SW]": AdvData(119001, "Raging Volcano Post-Rune"), # s shirt, r quest

    "Snakeblock [Wind C4 - E]": AdvData(120164, "Frozen Spire"),
    "Snakeblock [Wind C4 - C]": AdvData(120167, "Frozen Spire"),
    "Snakeblock [Wind C4 - N]": AdvData(120156, "Frozen Spire"),
    "Snakeblock [Wind D4]": AdvData(122398, "Frozen Spire"),
    "Snakeblock [Wind B3 - SW]": AdvData(121094, "Frozen Spire"),
    "Snakeblock [Wind B3 - CE]": AdvData(121105, "Frozen Spire"), # k cloak
    "Snakeblock [Wind B3 - NE]": AdvData(121103, "Frozen Spire"), # k cloak
    "Snakeblock [Wind A3]": AdvData(120826, "Frozen Spire"), # D quest
    "Snakeblock [Wind A2 - SW]": AdvData(120730, "Frozen Spire"),
    "Snakeblock [Wind A2 - SE]": AdvData(120735, "Frozen Spire"), # D quest
    "Snakeblock [Wind B2 - E]": AdvData(120993, "Frozen Spire"),
    "Snakeblock [Wind B2 - SW]": AdvData(121002, "Frozen Spire"), # k cloak
    "Snakeblock [Wind B4]": AdvData(121162, "Frozen Spire"), # k cloak
    "Snakeblock [Wind B1]": AdvData(120911, "Frozen Spire"),
    "Snakeblock [Wind D2 - SE]": AdvData(121524, "Frozen Spire"),
    "Snakeblock [Wind D2 - SW]": AdvData(121527, "Frozen Spire"),
    "Snakeblock [Wind B0 - W]": AdvData(120364, "Frozen Spire"),
    "Snakeblock [Wind B0 - E]": AdvData(120362, "Frozen Spire"),
    "Snakeblock [Wind C0]": AdvData(120406, "Frozen Spire"),
    "Snakeblock [Wind E4]": AdvData(120276, "Frozen Spire Post-Rune"), # d quest
    "Snakeblock [Wind E3]": AdvData(121756, "Frozen Spire Post-Rune"), # d quest
    "Snakeblock [Wind E1]": AdvData(121559, "Frozen Spire Post-Rune"), # g gloves
    "Snakeblock [Wind C1]": AdvData(121259, "Frozen Spire"),
    "Snakeblock [Wind C2]": AdvData(121370, "Frozen Spire"), # d quest

    "Snakeblock [Serpent A1 - W]": AdvData(125712, "Serpent Stacks Post-Rune"),
    "Snakeblock [Serpent A1 - C]": AdvData(125704, "Serpent Stacks Post-Rune"), #s circlet
    "Snakeblock [Serpent A1 - CE]": AdvData(125690, "Serpent Stacks Post-Rune"), #s circlet
    "Snakeblock [Serpent A1 - E]": AdvData(125711, "Serpent Stacks Post-Rune"), #s circlet
    "Snakeblock [Serpent A6 - SW]": AdvData(126815, "Serpent Stacks Post-Rune"), #s circlet, S quest, T quest
    "Snakeblock [Serpent A6 - NW]": AdvData(126807, "Serpent Stacks Post-Rune"), #s circlet, S quest, T quest
    "Snakeblock [Serpent A6 - C]": AdvData(126804, "Serpent Stacks Post-Rune"), #s circlet, S quest, T quest
    "Snakeblock [Serpent A6 - E]": AdvData(126805, "Serpent Stacks Post-Rune"), #s circlet, S quest, T quest
    "Snakeblock [Serpent A8]": AdvData(127076, "Serpent Stacks Post-Rune"), #s circlet, all quests

    "Snakeblock [Sanctum A2 - S]": AdvData(123858, "Sanctum"), #all quests
    "Snakeblock [Sanctum A2 - C]": AdvData(123857, "Sanctum"), #all quests
    "Snakeblock [Sanctum A2 - W]": AdvData(123856, "Sanctum"), #all quests
    "Snakeblock [Sanctum A0 - E]": AdvData(124109, "Sanctum"), #all quests
    "Snakeblock [Sanctum A0 - CE]": AdvData(124108, "Sanctum"), #all quests
    "Snakeblock [Sanctum A0 - CW]": AdvData(124121, "Sanctum"), #all quests
    "Snakeblock [Sanctum A0 - W]": AdvData(124111, "Sanctum"), #all quests
    "Snakeblock [Sanctum C2 - E]": AdvData(124026, "Sanctum"), #all quests
    "Snakeblock [Sanctum C2 - W]": AdvData(124023, "Sanctum"), #all quests
    "Snakeblock [Sanctum C0 - W]": AdvData(124238, "Sanctum"), #all quests
    "Snakeblock [Sanctum C0 - CSW]": AdvData(124231, "Sanctum"), #all quests
    "Snakeblock [Sanctum C0 - CNW]": AdvData(124241, "Sanctum"), #all quests
    "Snakeblock [Sanctum C0 - CN]": AdvData(124251, "Sanctum"), #all quests
    "Snakeblock [Sanctum C0 - E]": AdvData(124250, "Sanctum"), #all quests
}

exclusion_table = {



}

events_table = {
}
