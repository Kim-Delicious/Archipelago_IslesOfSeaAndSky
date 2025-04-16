from BaseClasses import Location
import typing


class AdvData(typing.NamedTuple):
    id: typing.Optional[int]
    region: str

#object ref id, region id, location id, location total
#ancient13 key = 109, 00, 13, 0
#10900130

class IslesOfSeaAndSkyAdvancement(Location):
    game: str = "IslesOfSeaAndSky"

advancement_table = {
    "Ancient Rune Stone":                           AdvData(61612011,        "Locked"),
    "Topaz Rune Stone":                             AdvData(62201201,        "Stony Cliffs"),
    "Sapphire Rune Stone":                          AdvData(62103201,        "Tidal Reef"),
    "Ruby Rune Stone":                              AdvData(62004201,        "Raging Volcano"),
    "Diamond Rune Stone":                           AdvData(61705221,        "Frozen Spire"),
    "Obsidian Rune Stone":                          AdvData(61806011,        "Serpent Stacks"),

    "Topaz Quest Complete":                         AdvData(99901201,       "Stony Cliffs"),
    "Sapphire Quest Complete":                      AdvData(99903201,       "Tidal Reef"),
    "Ruby Quest Complete":                          AdvData(99904201,       "Raging Volcano"),
    "Diamond Quest Complete":                       AdvData(99905221,       "Frozen Spire"),

    "Gopher Gloves":                                AdvData(35802211,       "Stony Cliffs"),
    "Frog Flippers":                                AdvData(34603041,       "Tidal Reef"),
    "Salamander Shirt":                             AdvData(62304401,       "Raging Volcano"),
    "Kite Cloak":                                   AdvData(39905001,       "Frozen Spire"),
    "Serpent Circlet":                              AdvData(65406011,       "Serpent Stacks"),

    "Topaz Shard Hit":                              AdvData(99907021,       "Sanctum"),
    "Sapphire Shard Hit":                           AdvData(99907221,       "Sanctum"),
    "Ruby Shard Hit":                               AdvData(99907201,       "Sanctum"),
    "Diamond Shard Hit":                            AdvData(99907001,       "Sanctum"),

    "Blue Stone Tablet":                            AdvData(59602011,       "Stony Cliffs"),
    "Gold Stone Tablet":                            AdvData(59701431,       "Stony Cliffs"),

    "Fire Key [A4]":                                AdvData(33204041,       "Raging Volcano"),
    "Fire Key [A0]":                                AdvData(33204001,       "Raging Volcano"),
    "Fire Key [E4]":                                AdvData(33204441,       "Raging Volcano"),

    #"Egg 1]":         AdvData(991024,       "Frozen Spire"), #Broken due to in-game randomness
    #"Egg 2]":         AdvData(991025,       "Frozen Spire"), #Broken due to in-game randomness
    #"Egg 3]":         AdvData(991026,       "Frozen Spire"), #Broken due to in-game randomness
   # "Wind Key]":      AdvData(83505440 || 83505040 || 83505400,       "Frozen Spire"), #Broken due to in-game randomness

    "Rolling Bell Rung":                            AdvData(99908101,       "Rolling Rocks"),
    "Sunken Bell Rung":                             AdvData(99909111,       "Sunken Island"),
    "Aggro Bell Rung":                              AdvData(99910011,       "Aggro Crag"),
    "Nunatak Bell Rung":                            AdvData(99911011,       "Sea Nunatak"),

    "Phoenix Flute":                                AdvData(51116111,       "Beast Bridge"),
    "Star Viewing Orb":                             AdvData(73314001,       "Shoal"),

    "Ancient Key [Ancient B3]":                     AdvData(10900131,       "Ancient Isle"),
    "Ancient Key [Ancient A1]":                     AdvData(10900011,       "Ancient Isle"),
    "Ancient Key [Ancient A2 - SE]":                AdvData(10900022,       "Ancient Isle"),
    "Ancient Key [Ancient A3 - N]":                 AdvData(10900033,       "Ancient Isle"),
    "Ancient Key [Ancient A3 - S]":                 AdvData(10900032,       "Ancient Isle"),
    "Ancient Key [Ancient A3 - E]":                 AdvData(10900031,       "Ancient Isle"),
    "Ancient Key [Ancient C2]":                     AdvData(10900221,       "Ancient Isle"),
    "Ancient Key [Ancient C3]":                     AdvData(10900231,       "Ancient Isle"),
    "Ancient Key [Ancient C1]":                     AdvData(10900211,       "Ancient Isle"),
    "Ancient Key [Ancient A2 - NW]":                AdvData(10900021,       "Ancient Isle"), # Topaz quest

    "Ancient Key [Rolling A1]":                     AdvData(10908011,       "Rolling Rocks"),
    "Ancient Key [Rolling A0]":                     AdvData(10908001,       "Rolling Rocks"),  # 7 stars

    "Ancient Key [Tropic A1]":                      AdvData(10913011,       "Star Tropic"), # ancient rune

    "Ancient Key [Stone B1]":                       AdvData(10901111,       "Stony Cliffs"), #
    "Ancient Key [Stone C0]":                       AdvData(10901201,       "Stony Cliffs"), #topaz quest
    "Ancient Key [Stone B2 ]":                      AdvData(10901121,       "Stony Cliffs"),
    "Ancient Key [Stone E2]":                       AdvData(10901421,       "Stony Cliffs"),  # topaz rune
    "Ancient Key [Stone B4]":                       AdvData(10901141,       "Stony Cliffs"), #topaz quest, topaz rune
    "Ancient Key [StoneDungeon C1]":                AdvData(10902211,       "Stony Cliffs"), #topaz rune, gopher gloves
    "Ancient Key [StoneDungeon D0]":                AdvData(10902301,       "Stony Cliffs"), #gopher gloves
    "Ancient Key [StoneDungeon B1]":                AdvData(10902111,       "Stony Cliffs"), #gopher gloves
    "Ancient Key [Stone B0 - NW1]":                 AdvData(10901103,       "Stony Cliffs"), # topaz quest
    "Ancient Key [Stone B0 - NW2]":                 AdvData(10901102,       "Stony Cliffs"), # topaz quest
    "Ancient Key [Stone B0 - NW3]":                 AdvData(10901101,       "Stony Cliffs"), # topaz quest
    "Ancient Key [StoneDungeon E2]":                AdvData(10902421,       "Stony Cliffs"),

    "Ancient Key [Water C2]":                       AdvData(10903221,       "Tidal Reef"),
    "Ancient Key [Water C3 - W]":                   AdvData(10903234,       "Tidal Reef"), # s rune
    "Ancient Key [Water A0 - E]":                   AdvData(10903002,       "Tidal Reef"), # s rune
    "Ancient Key [Water A0 - S]":                   AdvData(10903001,       "Tidal Reef"), # frog flippers
    "Ancient Key [Water A2]":                       AdvData(10903021,       "Tidal Reef"), # frog flippers, s quest
    "Ancient Key [Water B3]":                       AdvData(10903131,       "Tidal Reef"), # frog flippers
    "Ancient Key [Water C3 - NE1]":                 AdvData(10903233,       "Tidal Reef"), # frog flippers
    "Ancient Key [Water C3 - NE2]":                 AdvData(10903232,       "Tidal Reef"), # frog flippers
    "Ancient Key [Water C3 - NE3]":                 AdvData(10903231,       "Tidal Reef"), # frog flippers
    "Ancient Key [Water D1]":                       AdvData(10903311,       "Tidal Reef"), # frog flippers
    "Ancient Key [Water D0]":                       AdvData(10903301,       "Tidal Reef"), # frog flippers
    "Ancient Key [Water C0]":                       AdvData(10903201,       "Tidal Reef"), # s quest
    "Ancient Key [Water D2]":                       AdvData(10903321,       "Tidal Reef"), # frog flippers

    "Ancient Key [Fire A2 - N]":                    AdvData(10904022,       "Raging Volcano"),
    "Ancient Key [Fire A2 - S]":                    AdvData(10904021,       "Raging Volcano"), # salamander shirt
    "Ancient Key [Fire B4]":                        AdvData(10904141,       "Raging Volcano"), # r quest
    "Ancient Key [Fire A1 - NE]":                   AdvData(10904013,       "Raging Volcano"), # s shirt
    "Ancient Key [Fire A1 - E]":                    AdvData(10904012,       "Raging Volcano"), # r rune
    "Ancient Key [Fire B1 - N1]":                   AdvData(10904113,       "Raging Volcano"), # r quest
    "Ancient Key [Fire B1 - N2]":                   AdvData(10904112,       "Raging Volcano"), # r quest
    "Ancient Key [Fire B1 - N3]":                   AdvData(10904111,       "Raging Volcano"), # r quest
    "Ancient Key [Fire C1 - NE]":                   AdvData(10904212,       "Raging Volcano"), # s shirt
    "Ancient Key [Fire C0]":                        AdvData(10904201,       "Raging Volcano"), # r quest
    "Ancient Key [Fire C1 - SW]":                   AdvData(10904211,       "Raging Volcano"), # s shirt
    "Ancient Key [Fire C3]":                        AdvData(10904231,       "Raging Volcano"), # r quest
    "Ancient Key [Fire A1 - S]":                    AdvData(10904011,       "Raging Volcano"), # r rune
    "Ancient Key [Fire D4]":                        AdvData(10904341,       "Raging Volcano"), # s shirt

    # Keys on the Frozen Spire may be broken due to in-game randomness
    "Ancient Key [Wind C4]":                        AdvData(10905241,       "Frozen Spire"),
    "Ancient Key [Wind D4 - E]":                    AdvData(10905344,       "Frozen Spire"), # d rune
    "Ancient Key [Wind D4 - NW1]":                  AdvData(10905343,       "Frozen Spire"), # d quest
    "Ancient Key [Wind D4 - NW2]":                  AdvData(10905342,       "Frozen Spire"), # d quest
    "Ancient Key [Wind D4 - NW3]":                  AdvData(10905341,       "Frozen Spire"), # d quest
    "Ancient Key [Wind D3]":                        AdvData(10905331,       "Frozen Spire"), # k cloak
    "Ancient Key [Wind A3 ]":                       AdvData(10905031,       "Frozen Spire"), # k cloak
    "Ancient Key [Wind C2]":                        AdvData(10905221,       "Frozen Spire"), # d quest
    "Ancient Key [Wind B1]":                        AdvData(10905111,       "Frozen Spire"), # double check req
    "Ancient Key [Wind E2 - NE]":                   AdvData(10905422,       "Frozen Spire"), # d quest
    "Ancient Key [Wind E2 - S]":                    AdvData(10905421,       "Frozen Spire"), # d quest
    "Ancient Key [Wind E4 - E]":                    AdvData(10905442,       "Frozen Spire"), # d rune
    "Ancient Key [Wind E4 - SW]":                   AdvData(10905441,       "Frozen Spire"), # k cloak, d quest

    "Ancient Key [Aggro B0 - E]":                   AdvData(10910102,       "Aggro Crag"),
    "Ancient Key [Aggro B0 - W]":                   AdvData(10910101,       "Aggro Crag"),

    "Ancient Key [Sunken B0]":                      AdvData(10909101,       "Sunken Island"),
    "Ancient Key [Sunken A0]":                      AdvData(10909001,       "Sunken Island"),

    "Ancient Key [Nunatak B1]":                     AdvData(10911111,       "Sea Nunatak"),
    "Ancient Key [Nunatak A1]":                     AdvData(10911011,       "Sea Nunatak"), # ancient rune

    "Ancient Key [Stone D2]":                       AdvData(10902321,       "Stony Cliffs"), #
    "Ancient Key [Stone A2]":                       AdvData(10901021,       "Stony Cliffs"), # blue & gold tablet
    #73 keys

    "Topaz [Stone D2]":                             AdvData(78401321,       "Stony Cliffs"),
    "Topaz [Stone C2 - E]":                         AdvData(78401222,       "Stony Cliffs"),
    "Topaz [Stone C0]":                             AdvData(78401201,       "Stony Cliffs"),
    "Topaz [Stone C3 - N ]":                        AdvData(78401232,       "Stony Cliffs"),
    "Topaz [Stone C3 - S]":                         AdvData(78401231,       "Stony Cliffs"),
    "Topaz [Stone C2 - W]":                         AdvData(78401221,       "Stony Cliffs"),
    "Topaz [Stone B0]":                             AdvData(78401101,       "Stony Cliffs"),
    "Topaz [Stone B1]":                             AdvData(78401111,       "Stony Cliffs"),
    "Topaz [Stone C2]":                             AdvData(78401121,       "Stony Cliffs"), #Rq: topaz quest
    "Topaz [StoneDungeon C1]":                      AdvData(78402211,       "Stony Cliffs"), #Rq: gopher gloves
    "Topaz [Rolling A0]":                           AdvData(78408001,       "Rolling Rocks"), #Rq: topaz quest, gopher gloves, 7 stars
    "Topaz [Tropic A1]":                            AdvData(78413011,       "Star Tropic"), #Rq: ancient rune stone, all legenedaries - serpent circlet,

    "Sapphire [Water C2 - E]":                      AdvData(63503222,       "Tidal Reef"),
    "Sapphire [Water B2 - S]":                      AdvData(63503122,       "Tidal Reef"),
    "Sapphire [Water B2 - N]":                      AdvData(63503121,       "Tidal Reef"),
    "Sapphire [Water D2 - E]":                      AdvData(63503322,       "Tidal Reef"),
    "Sapphire [Water C0]":                          AdvData(63503201,       "Tidal Reef"), #sapphire rune stone #
    "Sapphire [Water D2 - N]":                      AdvData(63503321,       "Tidal Reef"), #s rune stone
    "Sapphire [Water D1]":                          AdvData(63503311,       "Tidal Reef"), #s rune stone
    "Sapphire [Water D3]":                          AdvData(63503332,       "Tidal Reef"), #s rune stone
    "Sapphire [Water C2 - N]":                      AdvData(63503221,       "Tidal Reef"),  # sapphire quest
    "Sapphire [Water A1]":                          AdvData(63503011,       "Tidal Reef"), #frog flippers
    "Sapphire [Sunken B0]":                         AdvData(63509101,       "Sunken Island"), #sapphire quest, 21 stars
    "Sapphire [Tropic A1 ]":                        AdvData(63513011,       "Star Tropic"), # ancient rune stone, all legenedaries exept serpent circlet

    "Ruby [Fire B2]":                               AdvData(60604121,       "Raging Volcano"),
    "Ruby [Fire C2]":                               AdvData(60604221,       "Raging Volcano"),
    "Ruby [Fire C0]":                               AdvData(60604201,       "Raging Volcano"), # ruby rune stone
    "Ruby [Fire D2 - E]":                           AdvData(60604322,       "Raging Volcano"),
    "Ruby [Fire D2 - W]":                           AdvData(60604321,       "Raging Volcano"),
    "Ruby [Fire D1]":                               AdvData(60604311,       "Raging Volcano"), # ruby rune stone
    "Ruby [Fire A3 - S]":                           AdvData(60604033,       "Raging Volcano"), #r rune stone
    "Ruby [Fire A3 - N]":                           AdvData(60604032,       "Raging Volcano"),
    "Ruby [Fire A3 - NW]":                          AdvData(60604031,       "Raging Volcano"), # r rune stone
    "Ruby [Fire D0]":                               AdvData(60604301,       "Raging Volcano"), # salamander shirt
    "Ruby [Aggro B1]":                              AdvData(60610111,       "Aggro Crag"), # ruby quest, 35 stars
    "Ruby [Tropic A1]":                             AdvData(60613011,       "Star Tropic"), # ancient rune stone, all legendaries - serpent circlet

    "Diamond [Wind C4]":                            AdvData(28205241,       "Frozen Spire"),
    "Diamond [Wind D4]":                            AdvData(28205341,       "Frozen Spire"),
    "Diamond [Wind B2]":                            AdvData(28205121,       "Frozen Spire"),
    "Diamond [Wind D2]":                            AdvData(28205321,       "Frozen Spire"),
    "Diamond [Wind C2]":                            AdvData(28205221,       "Frozen Spire"), # diamond rune stone
    "Diamond [Wind C1 - W]":                        AdvData(28205212,       "Frozen Spire"), # d rune stone
    "Diamond [Wind C1 - E]":                        AdvData(28205211,       "Frozen Spire"), # d rune stone
    "Diamond [Wind D1 - W]":                        AdvData(28205312,       "Frozen Spire"), # d rune stone
    "Diamond [Wind D1 - E]":                        AdvData(28205311,       "Frozen Spire"), # d rune stone
    "Diamond [Wind C3]":                            AdvData(28205231,       "Frozen Spire"), # diamond quest complete
    "Diamond [Nunatak B0]":                         AdvData(28211101,       "Sea Nunatak"), # diamond quest complete
    "Diamond [Tropic A1]":                          AdvData(28213011,       "Star Tropic"), # ancient rune stone, all legendaries - serpent circlet

    "Obsidian [Rolling A1]":                        AdvData(46708011,       "Rolling Rocks"),  # gopher gloves, 7 stars
    "Obsidian [Stone D1]":                          AdvData(46701311,       "Stony Cliffs"),
    "Obsidian [Stone A2]":                          AdvData(46701021,       "Stony Cliffs"),  # DOUBLE CHECK ID # stone tablet blue, tablet golda
    "Obsidian [Water D0]":                          AdvData(46703301,       "Tidal Reef"),  # frog flippers
    "Obsidian [Fire E0]":                           AdvData(46704401,       "Raging Volcano"),  # salamander shirt
    "Obsidian [Fire D4]":                           AdvData(46704341,       "Raging Volcano"),  # DOUBLE CHECK ID #
    "Obsidian [Wind B0]":                           AdvData(46705101,       "Frozen Spire"),
    "Obsidian [Aggro B0]":                          AdvData(46710101,       "Aggro Crag"),  # salamander shirt
    "Obsidian [Sunken A0]":                         AdvData(46709001,       "Sunken Island"),  # frog flippers
    "Obsidian [Nunatak B1]":                        AdvData(46711111,       "Sea Nunatak"),  # diamond quest
    "Obsidian [Serpent A1]":                        AdvData(46706011,       "Serpent Stacks"),  # rune stones: t,s,r,d,o, serpent circlet(?)
    "Obsidian [Lost A1]":                           AdvData(46715011,       "Lost Landing"),  # phoenix flute (or secret find?)

    # 4 of these are trapped in bells, and should be removed from total.
    # 3x4=12 trapped in music puzzle
    # 1 trapped in volcano idol puzzle
    # 1 trapped in stone tablet puzzle
    # Total of 17 stars that aren't locations.
    "Star Piece [Ancient C0]":                     AdvData(72800201,       "Ancient Isle"),
    "Star Piece [Ancient A1]":                     AdvData(72800011,       "Ancient Isle"),
    "Star Piece [Ancient B1]":                     AdvData(72800111,       "Ancient Isle"),

    "Star Piece [Stone C1]":                       AdvData(72801211,       "Stony Cliffs"), # t quest
    "Star Piece [Stone E1]":                       AdvData(72801411,       "Stony Cliffs"),
    "Star Piece [Stone B2]":                       AdvData(72801121,       "Stony Cliffs"), # t quest
    "Star Piece [Stone B3]":                       AdvData(72801131,       "Stony Cliffs"), # g gloves
    "Star Piece [Stone B4]":                       AdvData(72801141,       "Stony Cliffs"), # g globes
    "Star Piece [Stone C4]":                       AdvData(72801241,       "Stony Cliffs"), # g gloves
    "Star Piece [Stone E4]":                       AdvData(72801441,       "Stony Cliffs"), # g gloves
    "Star Piece [Stone C0]":                       AdvData(72801201,       "Stony Cliffs"), # t quest
    "Star Piece [StoneDungeon E1]":                AdvData(72802411,       "Stony Cliffs"), # t quest
    "Star Piece [StoneDungeon E2]":                AdvData(72802421,       "Stony Cliffs"), # g gloves, f flippers
    "Star Piece [StoneDungeon C3]":                AdvData(72802231,       "Stony Cliffs"), # t quest
    "Star Piece [StoneDungeon C1]":                AdvData(72802211,       "Stony Cliffs"), # g gloves
    "Star Piece [StoneDungeon B1]":                AdvData(72802111,       "Stony Cliffs"), # g gloves
    "Star Piece [Stone A1]":                       AdvData(72801011,       "Stony Cliffs"), # 5 stars

    "Star Piece [Water C1 - E]":                   AdvData(72803212,       "Tidal Reef"),
    "Star Piece [Water C0]":                       AdvData(72803201,       "Tidal Reef"), # s quest
    "Star Piece [Water C1 - W]":                   AdvData(72803211,       "Tidal Reef"),
    "Star Piece [Water C2]":                       AdvData(72803221,       "Tidal Reef"), # s quest
    "Star Piece [Water D2]":                       AdvData(72803321,       "Tidal Reef"), # f flippers, k cloak
    "Star Piece [Water D3]":                       AdvData(72803331,       "Tidal Reef"),
    "Star Piece [Water E2]":                       AdvData(72803421,       "Tidal Reef"), # f flippers
    "Star Piece [Water E0 - W]":                   AdvData(72803402,       "Tidal Reef"), # f flippers
    "Star Piece [Water E0 - E]":                   AdvData(72803401,       "Tidal Reef"), # s quest | double check
    "Star Piece [Water B1]":                       AdvData(72803111,       "Tidal Reef"), # f flippers
    "Star Piece [Water A0]":                       AdvData(72803001,       "Tidal Reef"), # s rune
    "Star Piece [Water A2 - N]":                   AdvData(72803022,       "Tidal Reef"), # f flippers, k cloak
    "Star Piece [Water A2 - S]":                   AdvData(72803021,       "Tidal Reef"), # f flippers
    "Star Piece [Water A4]":                       AdvData(72803041,       "Tidal Reef"), # f flippers
    "Star Piece [Water B4]":                       AdvData(72803141,       "Tidal Reef"), # f flippers

    "Star Piece [Fire B4]":                        AdvData(72804141,       "Raging Volcano"), # r quest
    "Star Piece [Fire B3]":                        AdvData(72804131,       "Raging Volcano"),
    "Star Piece [Fire C3]":                        AdvData(72804231,       "Raging Volcano"),
    "Star Piece [Fire C1]":                        AdvData(72804211,       "Raging Volcano"),
    "Star Piece [Fire C0]":                        AdvData(72804201,       "Raging Volcano"),
    "Star Piece [Fire D1 - S]":                    AdvData(72804312,       "Raging Volcano"), # r quest
    "Star Piece [Fire D1 - N]":                    AdvData(72804311,       "Raging Volcano"), # r rune
    "Star Piece [Fire D3 - S]":                    AdvData(72804332,       "Raging Volcano"), # r quest | double check
    "Star Piece [Fire D3 - W]":                    AdvData(72804331,       "Raging Volcano"), # r quest | double
    "Star Piece [Fire D4]":                        AdvData(72804341,       "Raging Volcano"), # f flippers # s shirt?
    "Star Piece [Fire E3]":                        AdvData(72804431,       "Raging Volcano"),
    "Star Piece [Fire E1 - E]":                    AdvData(72804412,       "Raging Volcano"), # r quest shirt
    "Star Piece [Fire E1 - W]":                    AdvData(72804411,       "Raging Volcano"), # s shirt
    "Star Piece [Fire E0]":                        AdvData(72804401,       "Raging Volcano"), # s shirt

    #locations might be broken due to in-game randomness
    "Star Piece [Wind D4]":                        AdvData(72805341,       "Frozen Spire"),
    "Star Piece [Wind C3 - W]":                    AdvData(72805232,       "Frozen Spire"), # d rune
    "Star Piece [Wind C3 - NE]":                   AdvData(72805231,       "Frozen Spire"), # d rune
    "Star Piece [Wind B3]":                        AdvData(72805131,       "Frozen Spire"), # k cloak
    "Star Piece [Wind A3]":                        AdvData(72805031,       "Frozen Spire"), # k cloak
    "Star Piece [Wind B2 - N]":                    AdvData(72805122,       "Frozen Spire"), # k cloak?
    "Star Piece [Wind B2 - S]":                    AdvData(72805221,       "Frozen Spire"), # d quest
    "Star Piece [Wind D2]":                        AdvData(72805321,       "Frozen Spire"), # k cloak
    "Star Piece [Wind E2]":                        AdvData(72805421,       "Frozen Spire"), # d quest
    "Star Piece [Wind E4]":                        AdvData(72805441,       "Frozen Spire"), # k cloak
    "Star Piece [Wind E1]":                        AdvData(72805411,       "Frozen Spire"), # k cloak, g gloves
    "Star Piece [Wind B1]":                        AdvData(72805111,       "Frozen Spire"),
    "Star Piece [Wind B0]":                        AdvData(72805101,       "Frozen Spire"),
    "Star Piece [Wind A0]":                        AdvData(72805001,       "Frozen Spire"), # k cloak
    "Star Piece [Wind B2]":                        AdvData(72805121,       "Frozen Spire"), # d quest

    "Star Piece [Rolling A0]":                     AdvData(72808001,       "Rolling Rocks"), # 7 stars, t quest
    "Star Piece [Rolling B1]":                     AdvData(72808111,       "Rolling Rocks"), #
    "Star Piece [Rolling B0]":                     AdvData(72808101,       "Rolling Rocks"), # g gloves

    "Star Piece [Sunken B0]":                      AdvData(72809101,       "Sunken Island"), # 21 stars, s quest
    "Star Piece [Sunken A1]":                      AdvData(72809011,       "Sunken Island"), # ancient rune

    "Star Piece [Aggro B1]":                       AdvData(72810111,       "Aggro Crag"), # 35 star, r quest
    "Star Piece [Aggro A1]":                       AdvData(72810011,       "Aggro Crag"), # ancient rune

    "Star Piece [Nunatak B0]":                     AdvData(72811101,       "Sea Nunatak"), # 49 stars, d quest
    "Star Piece [Nunatak A0]":                     AdvData(72811001,       "Sea Nunatak"), # ancient rune

    "Star Piece [Lost B1]":                        AdvData(72815111,       "Lost Landing"),

    "Star Piece [Shoal A0]":                       AdvData(72814001,       "Shoal"), # f flippers

    "Star Piece [Tropic A0]":                      AdvData(72813001,       "Star Tropic"), #
    "Star Piece [Tropic B0 - E]":                  AdvData(72813102,       "Star Tropic"), # a rune
    "Star Piece [Tropic B0 - N]":                  AdvData(72813101,       "Star Tropic"), # o rune, s shirt
    "Star Piece [Topic A1 - 1]":                   AdvData(72813014,       "Star Tropic"), # g gloves
    "Star Piece [Topic A1 - 2]":                   AdvData(72813013,       "Star Tropic"), # g gloves, s shirt,
    "Star Piece [Topic A1 - 3]":                   AdvData(72813012,       "Star Tropic"), # g gloves, s shirt, f flippers
    "Star Piece [Topic A1 - 4]":                   AdvData(72813011,       "Star Tropic"), # g gloves, s shirt, f flippers, k cloak

    "Star Piece [Serpent A3]":                     AdvData(72806031,       "Serpent Stacks"), # k cloak
    "Star Piece [Serpent A2]":                     AdvData(72806021,       "Serpent Stacks"), # k cloak, s circlet
    "Star Piece [Serpent A1 - W]":                 AdvData(72806012,       "Serpent Stacks"), # k cloak, s circlet
    "Star Piece [Serpent A1 - N]":                 AdvData(72806011,       "Serpent Stacks"), # k cloak, s circlet
    "Star Piece [Serpent A4]":                     AdvData(72806041,       "Serpent Stacks"), # s circlet, t quest
    "Star Piece [Serpent A6 - W]":                 AdvData(72806062,       "Serpent Stacks"), # s quest, s circlet
    "Star Piece [Serpent A6 - E]":                 AdvData(72806061,       "Serpent Stacks"), # s quest, s circlet
    "Star Piece [Serpent A7 - W]":                 AdvData(72806072,       "Serpent Stacks"), # s circlet, r quest
    "Star Piece [Serpent A7 - E]":                 AdvData(72806071,       "Serpent Stacks"), # s circlet, r quest
    "Star Piece [Serpent A8 - N]":                 AdvData(72806082,       "Serpent Stacks"), # s circlet, d quest
    "Star Piece [Serpent A8 - S]":                 AdvData(72806081,       "Serpent Stacks"), # s circlet, d quest

    "Star Piece [Locked A1]":                      AdvData(72812011,       "Locked"),
    #91 stars


    #"Jellyfish 1]": AdvData(991027, "Topaz Sea"),

    "Stone Music Note [C1]":                       AdvData(45701211,       "Stony Cliffs"), # failed?
    "Stone Music Note [D4]":                       AdvData(45701341,       "Stony Cliffs"), # topaz rune
    "Stone Music Note [B3]":                       AdvData(45701131,       "Stony Cliffs"), # topaz rune
    "Stone Music Note [B0]":                       AdvData(45701101,       "Stony Cliffs"), # topaz rune
    "Stone Music Note [B2]":                       AdvData(45701121,       "Stony Cliffs"), # topaz quest
    "Stone Music Note [D1]":                       AdvData(45701311,       "Stony Cliffs"), # topaz quest

    "Water Music Note [C1]":                       AdvData(45703211,       "Tidal Reef"),
    "Water Music Note [E0]":                       AdvData(45703401,       "Tidal Reef"), # s rune
    "Water Music Note [D1]":                       AdvData(45703311,       "Tidal Reef"), # s rune
    "Water Music Note [E2]":                       AdvData(45703421,       "Tidal Reef"), # s rune
    "Water Music Note [B0]":                       AdvData(45703101,       "Tidal Reef"), # s rune
    "Water Music Note [A2]":                       AdvData(45703021,       "Tidal Reef"), # s rune

    "Fire Music Note [A2]":                        AdvData(45704021,       "Raging Volcano"),
    "Fire Music Note [C3]":                        AdvData(45704231,       "Raging Volcano"), # r rune
    "Fire Music Note [B0]":                        AdvData(45704101,       "Raging Volcano"), # r rune
    "Fire Music Note [B2]":                        AdvData(45704121,       "Raging Volcano"), # r rune
    "Fire Music Note [E1]":                        AdvData(45704411,       "Raging Volcano"), # r rune
    "Fire Music Note [D3]":                        AdvData(45704331,       "Raging Volcano"), # salamander shirt

    "Wind Music Note [B1]":                        AdvData(45705111,       "Frozen Spire"),
    "Wind Music Note [A0]":                        AdvData(45705001,       "Frozen Spire"),
    "Wind Music Note [E3]":                        AdvData(45705431,       "Frozen Spire"),  # d rune
    "Wind Music Note [C3]":                        AdvData(45705231,       "Frozen Spire"),  # d rune,
    "Wind Music Note [A2]":                        AdvData(45705021,       "Frozen Spire"), # d quest,
    "Wind Music Note [D3]":                        AdvData(45705331,       "Frozen Spire"), # d quest

    #"Shell [Water B2]":                            AdvData(63603121,      "Tidal Reef"),
    #"Shell [Water C0]":                            AdvData(63603201,      "Tidal Reef"),
    #"Shell [Water B0]":                            AdvData(63603101,      "Tidal Reef"),
    #"Shell [Water B1]":                            AdvData(63603111,      "Tidal Reef"),
    #"Shell [Water C1]":                            AdvData(63603211,      "Tidal Reef"),
    #"Shell [Water C2]":                            AdvData(63603221,      "Tidal Reef"),
    #"Shell [Water D2]":                            AdvData(63603321,      "Tidal Reef"), # s rune
    #"Shell [Water A1]":                            AdvData(63603011,      "Tidal Reef"), # s rune
    #"Shell [Water A0]":                            AdvData(63603001,      "Tidal Reef"), # s rune
    #"Shell [Water A3]":                            AdvData(63603031,      "Tidal Reef"), # s rune
    #"Shell [Water B3]":                            AdvData(63603131,      "Tidal Reef"), # s rune
    #"Shell [Water B4]":                            AdvData(63603141,      "Tidal Reef"), # s rune
    #"Shell [Water C4]":                            AdvData(63603241,      "Tidal Reef"), # s rune
    #"Shell [Water C3]":                            AdvData(63603231,      "Tidal Reef"), # s rune
    #"Shell [Water D4]":                            AdvData(63603341,      "Tidal Reef"), # s rune
    #"Shell [Water E4]":                            AdvData(63603441,      "Tidal Reef"), # s rune
    #"Shell [Water E2]":                            AdvData(63603421,      "Tidal Reef"), # s rune
    #"Shell [Water E1]":                            AdvData(63603411,      "Tidal Reef"), # s rune
    #"Shell [Water E0]":                            AdvData(63603401,      "Tidal Reef"), # s rune
    #"Shell [Water D3]":                            AdvData(63603331,      "Tidal Reef"), # s rune
    #"Shell [Water A4]":                            AdvData(63603041,      "Tidal Reef"),  # f flippers
    #"Shell [Water D1]":                            AdvData(63603311,      "Tidal Reef"),  # f flippers
    #"Shell [Water D0]":                            AdvData(63603301,      "Tidal Reef"),  # f flippers
    #"Shell [Water A2]":                            AdvData(63603021,      "Tidal Reef"),  # f flippers

    #"Jellyfish 1":                            AdvData(39520119,      "Topaz Sea"),
    #"Jellyfish 2":                            AdvData(39520118,      "Sapphire Sea"),
    #"Jellyfish 3":                            AdvData(39520117,      "Obsidian Sea"),
    #"Jellyfish 4":                            AdvData(39520116,      "Diamond Sea"),
    #"Jellyfish 5":                            AdvData(39520115,      "Ruby Sea"),
    #"Jellyfish 6":                            AdvData(39520114,      "Ruby Sea"),
    #"Jellyfish 7":                            AdvData(39520113,      "Beast Sea"),
    #"Jellyfish 8":                            AdvData(39520112,      "Beast Sea"),
    #"Jellyfish 9":                            AdvData(39520111,      "Lost Sea"),
    #"Jellyfish 10":                           AdvData(39520110,      "Northwest Sea"),

    # In the future, could include milestones as locations. e.g. each of the steam achievments, plus extras.
}

exclusion_table = {



}

events_table = {
}
