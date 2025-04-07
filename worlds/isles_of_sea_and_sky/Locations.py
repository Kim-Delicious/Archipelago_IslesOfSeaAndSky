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
    "Ancient Rune Tablet":          AdvData(61612011,     "Locked"),
    "Topaz Rune Tablet":            AdvData(62201201,     "Stony Cliffs"),
    "Sapphire Rune Tablet":         AdvData(62103201,     "Tidal Reef"),
    "Ruby Rune Tablet":             AdvData(62004201,     "Raging Volcano"),
    "Diamond Rune Tablet":          AdvData(61705221,     "Frozen Spire"),
    "Obsidian Rune Tablet":         AdvData(61806011,     "Serpent Stacks"),

    "Topaz Quest Complete":         AdvData(99901201,     "Stony Cliffs"),
    "Sapphire Quest Complete":      AdvData(99903201,     "Tidal Reef"),
    "Ruby Quest Complete":          AdvData(99904201,     "Raging Volcano"),
    "Diamond Quest Complete":       AdvData(99905221,     "Frozen Spire"),

    "Gopher Gloves":                AdvData(35802211,     "Stony Cliffs"),
    "Frog Flippers":                AdvData(34603041,     "Tidal Reef"),
    "Salamander Shirt":             AdvData(62304401,     "Raging Volcano"),
    "Kite Cape":                    AdvData(39905001,     "Frozen Spire"),
    "Serpent Circlet":              AdvData(65406011,     "Serpent Stacks"),

    "Topaz Shard Hit":              AdvData(99907021,     "Sanctum"),
    "Sapphire Shard Hit":           AdvData(99907221,     "Sanctum"),
    "Ruby Shard Hit":               AdvData(99907201,     "Sanctum"),
    "Diamond Shard Hit":            AdvData(99907001,     "Sanctum"),

    "Blue Stone Tablet":            AdvData(59602011,     "Stony Cliffs"),
    "Gold Stone Tablet":            AdvData(59701431,     "Stony Cliffs"),

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

    "Ancient Key 11" :              AdvData(10901121,     "Stony Cliffs"),
    "Ancient Key 12" :              AdvData(10901111,     "Stony Cliffs"), #
    "Ancient Key 13" :              AdvData(10901201,     "Stony Cliffs"), #topaz quest

    "Ancient Key 14" :              AdvData(10908011,     "Rolling Rocks"),

    "Ancient Key 15" :              AdvData(10913011,     "Tropic Star"), # ancient rune

    "Ancient Key 16" :              AdvData(10908001,     "Rolling Rocks"), # 7 stars

    "Ancient Key 17" :              AdvData(10901421,     "Stony Cliffs"), # topaz rune
    "Ancient Key 18" :              AdvData(10901141,     "Stony Cliffs"), #topaz quest, topaz rune
    "Ancient Key 19" :              AdvData(10902211,     "Stony Cliffs"), #topaz rune, gopher gloves
    "Ancient Key 20" :              AdvData(10902300,     "Stony Cliffs"), #gopher gloves
    "Ancient Key 21" :              AdvData(10902111,     "Stony Cliffs"), #gopher gloves
    "Ancient Key 22" :              AdvData(10901103,     "Stony Cliffs"), # topaz quest
    "Ancient Key 23" :              AdvData(10901102,     "Stony Cliffs"), # topaz quest
    "Ancient Key 24" :              AdvData(10901101,     "Stony Cliffs"), # topaz quest
    "Ancient Key 25" :              AdvData(10902421,     "Stony Cliffs"),

    "Ancient Key 26" :              AdvData(10903221,     "Tidal Reef"),
    "Ancient Key 27" :              AdvData(10903234,     "Tidal Reef"), # s rune
    "Ancient Key 28" :              AdvData(10903002,     "Tidal Reef"), # s rune
    "Ancient Key 29" :              AdvData(10903001,     "Tidal Reef"), # frog flippers
    "Ancient Key 30" :              AdvData(10903021,     "Tidal Reef"), # frog flippers, s quest
    "Ancient Key 31" :              AdvData(10903131,     "Tidal Reef"), # frog flippers
    "Ancient Key 32" :              AdvData(10903233,     "Tidal Reef"), # frog flippers
    "Ancient Key 33" :              AdvData(10903232,     "Tidal Reef"), # frog flippers
    "Ancient Key 34" :              AdvData(10903231,     "Tidal Reef"), # frog flippers
    "Ancient Key 35" :              AdvData(10903311,     "Tidal Reef"), # frog flippers
    "Ancient Key 36" :              AdvData(10903301,     "Tidal Reef"), # frog flippers
    "Ancient Key 37" :              AdvData(10903201,     "Tidal Reef"), # s quest
    "Ancient Key 38" :              AdvData(10903321,     "Tidal Reef"), # frog flippers

    "Ancient Key 39" :              AdvData(10904022,     "Raging Volcano"),
    "Ancient Key 40" :              AdvData(10904021,     "Raging Volcano"), # salamander shirt
    "Ancient Key 41" :              AdvData(10904141,     "Raging Volcano"), # r quest
    "Ancient Key 42" :              AdvData(10904013,     "Raging Volcano"), # s shirt
    "Ancient Key 43" :              AdvData(10904012,     "Raging Volcano"), # r rune
    "Ancient Key 44" :              AdvData(10904113,     "Raging Volcano"), # r quest
    "Ancient Key 45" :              AdvData(10904112,     "Raging Volcano"), # r quest
    "Ancient Key 46" :              AdvData(10904111,     "Raging Volcano"), # r quest
    "Ancient Key 47" :              AdvData(10904212,     "Raging Volcano"), # s shirt
    "Ancient Key 48" :              AdvData(10904201,     "Raging Volcano"), # r quest
    "Ancient Key 49" :              AdvData(10904211,     "Raging Volcano"), # s shirt
    "Ancient Key 50" :              AdvData(10904231,     "Raging Volcano"), # r quest
    "Ancient Key 51" :              AdvData(10904011,     "Raging Volcano"), # r rune
    "Ancient Key 52" :              AdvData(10904341,     "Raging Volcano"), # s shirt

    # Keys on the Frozen Spire may be broken due to in-game randomness
    "Ancient Key 53" :              AdvData(10905241,     "Frozen Spire"),
    "Ancient Key 54" :              AdvData(10905344,     "Frozen Spire"), # d rune
    "Ancient Key 55" :              AdvData(10905343,     "Frozen Spire"), # d quest
    "Ancient Key 56" :              AdvData(10905342,     "Frozen Spire"), # d quest
    "Ancient Key 57" :              AdvData(10905341,     "Frozen Spire"), # d quest
    "Ancient Key 58" :              AdvData(10905331,     "Frozen Spire"), # k cloak
    "Ancient Key 59" :              AdvData(10905031,     "Frozen Spire"), # k cloak
    "Ancient Key 60" :              AdvData(10905221,     "Frozen Spire"), # d quest
    "Ancient Key 61" :              AdvData(10905111,     "Frozen Spire"), # double check req
    "Ancient Key 62" :              AdvData(10905422,     "Frozen Spire"), # d quest
    "Ancient Key 63" :              AdvData(10905421,     "Frozen Spire"), # d quest
    "Ancient Key 64" :              AdvData(10905442,     "Frozen Spire"), # d rune
    "Ancient Key 65" :              AdvData(10905441,     "Frozen Spire"), # k cloak, d quest

    "Ancient Key 66" :              AdvData(10910102,     "Aggro Crag"),
    "Ancient Key 67" :              AdvData(10910101,     "Aggro Crag"),

    "Ancient Key 68" :              AdvData(10909101,     "Sunken Island"),
    "Ancient Key 69" :              AdvData(10909001,     "Sunken Island"),

    "Ancient Key 70" :              AdvData(10911111,     "Sea Nunatuk"),
    "Ancient Key 71" :              AdvData(10911011,     "Sea Nunatuk"), # ancient rune

    "Ancient Key 72" :              AdvData(10902321,     "Stony Cliffs"), #
    "Ancient Key 73" :              AdvData(10901021,     "Stony Cliffs"), # blue & gold tablet

    "Topaz 1" :                     AdvData(78401321,     "Stony Cliffs"),
    "Topaz 2" :                     AdvData(78401222,     "Stony Cliffs"),
    "Topaz 3" :                     AdvData(78401200,     "Stony Cliffs"),
    "Topaz 4" :                     AdvData(78401232,     "Stony Cliffs"),
    "Topaz 5" :                     AdvData(78401231,     "Stony Cliffs"),
    "Topaz 6" :                     AdvData(78401221,     "Stony Cliffs"),
    "Topaz 7" :                     AdvData(78401101,     "Stony Cliffs"),
    "Topaz 8" :                     AdvData(78401111,     "Stony Cliffs"),
    "Topaz 9" :                     AdvData(78401121,     "Stony Cliffs"), #Rq: topaz quest
    "Topaz 10" :                    AdvData(78402211,     "Stony Cliffs"), #Rq: gopher gloves
    "Topaz 11" :                    AdvData(78408001,     "Rolling Rocks"), #Rq: topaz quest, gopher gloves, 7 stars
    "Topaz 12" :                    AdvData(78413011,     "Star Tropic"), #Rq: ancient rune stone, all legenedaries - serpent circlet,

    "Sapphire 1" :                  AdvData(63503222,     "Tidal Reef"),
    "Sapphire 2" :                  AdvData(63503122,     "Tidal Reef"),
    "Sapphire 3" :                  AdvData(63503121,     "Tidal Reef"),
    "Sapphire 4" :                  AdvData(63503322,     "Tidal Reef"),
    "Sapphire 5" :                  AdvData(63503201,     "Tidal Reef"), #sapphire rune stone
    "Sapphire 6" :                  AdvData(63503321,     "Tidal Reef"), #s rune stone
    "Sapphire 7" :                  AdvData(63503311,     "Tidal Reef"), #s rune stone
    "Sapphire 8" :                  AdvData(63503331,     "Tidal Reef"), #s rune stone
    "Sapphire 9":                   AdvData(63503221,     "Tidal Reef"),  # sapphire quest
    "Sapphire 10" :                 AdvData(63503011,     "Tidal Reef"), #frog flippers
    "Sapphire 11" :                 AdvData(63509101,     "Sunken Island"), #sapphire quest, 21 stars
    "Sapphire 12" :                 AdvData(63513011,     "Star Tropic"), # ancient rune stone, all legenedaries exept serpent circlet

    "Ruby 1" :                      AdvData(60604121,     "Raging Volcano"),
    "Ruby 2" :                      AdvData(60604221,     "Raging Volcano"),
    "Ruby 3" :                      AdvData(60604201,     "Raging Volcano"), # ruby rune stone
    "Ruby 4" :                      AdvData(60604322,     "Raging Volcano"),
    "Ruby 5" :                      AdvData(60604321,     "Raging Volcano"),
    "Ruby 6" :                      AdvData(60604311,     "Raging Volcano"), # ruby rune stone
    "Ruby 7" :                      AdvData(60604033,     "Raging Volcano"), #r rune stone
    "Ruby 8" :                      AdvData(60604032,     "Raging Volcano"),
    "Ruby 9" :                      AdvData(60604031,     "Raging Volcano"), # r rune stone
    "Ruby 10" :                     AdvData(60604301,     "Raging Volcano"), # salamander shirt
    "Ruby 11" :                     AdvData(60610111,     "Aggro Crag"), # ruby quest, 35 stars
    "Ruby 12" :                     AdvData(60613011,     "Star Tropic"), # ancient rune stone, all legendaries - serpent circlet

    "Diamond 1" :                   AdvData(28205241,     "Frozen Spire"),
    "Diamond 2" :                   AdvData(28205341,     "Frozen Spire"),
    "Diamond 3" :                   AdvData(28205121,     "Frozen Spire"),
    "Diamond 4" :                   AdvData(28205321,     "Frozen Spire"),
    "Diamond 5" :                   AdvData(28205221,     "Frozen Spire"), # diamond rune stone
    "Diamond 6" :                   AdvData(28205212,     "Frozen Spire"), # d rune stone
    "Diamond 7" :                   AdvData(28205211,     "Frozen Spire"), # d rune stone
    "Diamond 8" :                   AdvData(28205312,     "Frozen Spire"), # d rune stone
    "Diamond 9" :                   AdvData(28205311,     "Frozen Spire"), # d rune stone
    "Diamond 10" :                  AdvData(28205231,     "Frozen Spire"), # diamond quest complete
    "Diamond 11" :                  AdvData(28211101,     "Sea Nunatak"), # diamond quest complete
    "Diamond 12" :                  AdvData(28213011,     "Star Tropic"), # ancient rune stone, all legendaries - serpent circlet

    # 4 of these are trapped in bells, and should be removed.
    # 3x4=12 trapped in music puzzle
    # 3 trapped in volcano idol puzzle
    # Total of 19 stars that aren't locations.
    "Star Piece 1" :                AdvData(72800201,     "Ancient Isle"),
    "Star Piece 2" :                AdvData(72800011,     "Ancient Isle"),
    "Star Piece 3" :                AdvData(72800111,     "Ancient Isle"),

    "Star Piece 4" :                AdvData(72801211,     "Stony Cliffs"), # t quest
    "Star Piece 5" :                AdvData(72801411,     "Stony Cliffs"),
    "Star Piece 6" :                AdvData(72801121,     "Stony Cliffs"), # t quest
    "Star Piece 7" :                AdvData(72801131,     "Stony Cliffs"), # g gloves
    "Star Piece 8" :                AdvData(72801141,     "Stony Cliffs"), # g globes
    "Star Piece 9" :                AdvData(72801241,     "Stony Cliffs"), # g gloves
    "Star Piece 10" :               AdvData(72801441,     "Stony Cliffs"), # g gloves
    "Star Piece 11" :               AdvData(72801201,     "Stony Cliffs"), # t quest
    "Star Piece 12" :               AdvData(72802411,     "Stony Cliffs"), # t quest
    "Star Piece 13" :               AdvData(72802420,     "Stony Cliffs"), # g gloves, f flippers
    "Star Piece 14" :               AdvData(72802231,     "Stony Cliffs"), # t quest
    "Star Piece 15" :               AdvData(72802211,     "Stony Cliffs"), # g gloves
    "Star Piece 16" :               AdvData(72802111,     "Stony Cliffs"), # g gloves
    "Star Piece 17" :               AdvData(72801011,     "Stony Cliffs"), # 5 stars

    "Star Piece 18" :               AdvData(72803212,     "Tidal Reef"),
    "Star Piece 19" :               AdvData(72803201,     "Tidal Reef"), # s quest
    "Star Piece 20" :               AdvData(72803211,     "Tidal Reef"),
    "Star Piece 21" :               AdvData(72803221,     "Tidal Reef"), # s quest
    "Star Piece 22" :               AdvData(72803321,     "Tidal Reef"), # f flippers, k cloak
    "Star Piece 23" :               AdvData(72803331,     "Tidal Reef"),
    "Star Piece 24" :               AdvData(72803421,     "Tidal Reef"), # f flippers
    "Star Piece 25" :               AdvData(72803402,     "Tidal Reef"), # f flippers
    "Star Piece 26" :               AdvData(72803401,     "Tidal Reef"), # s quest | double check
    "Star Piece 27" :               AdvData(72803111,     "Tidal Reef"), # f flippers
    "Star Piece 28" :               AdvData(72803000,     "Tidal Reef"), # s rune
    "Star Piece 29" :               AdvData(72803022,     "Tidal Reef"), # f flippers, k cloak
    "Star Piece 30" :               AdvData(72803021,     "Tidal Reef"), # f flippers
    "Star Piece 31" :               AdvData(72803041,     "Tidal Reef"), # f flippers
    "Star Piece 32" :               AdvData(72803141,     "Tidal Reef"), # f flippers

    "Star Piece 33" :               AdvData(72804141,     "Raging Volcano"), # r quest
    "Star Piece 34" :               AdvData(72804131,     "Raging Volcano"),
    "Star Piece 35" :               AdvData(72804231,     "Raging Volcano"),
    "Star Piece 36" :               AdvData(72804211,     "Raging Volcano"),
    "Star Piece 37" :               AdvData(72804201,     "Raging Volcano"),
    "Star Piece 38" :               AdvData(72804312,     "Raging Volcano"), # r quest
    "Star Piece 39" :               AdvData(72804311,     "Raging Volcano"), # r rune
    "Star Piece 40" :               AdvData(72804332,     "Raging Volcano"), # r quest | double check
    "Star Piece 41" :               AdvData(72804331,     "Raging Volcano"), # r quest | double
    "Star Piece 42" :               AdvData(72804341,     "Raging Volcano"), # f flippers # s shirt?
    "Star Piece 43" :               AdvData(72804431,     "Raging Volcano"),
    "Star Piece 44" :               AdvData(72804412,     "Raging Volcano"), # r quest shirt
    "Star Piece 45" :               AdvData(72804411,     "Raging Volcano"), # s shirt
    "Star Piece 46" :               AdvData(72804401,     "Raging Volcano"), # s shirt

    #locations might be broken due to in-game randomness
    "Star Piece 47" :               AdvData(72805341,     "Frozen Spire"),
    "Star Piece 48" :               AdvData(72805232,     "Frozen Spire"), # d rune
    "Star Piece 49" :               AdvData(72805231,     "Frozen Spire"), # d rune
    "Star Piece 50" :               AdvData(72805131,     "Frozen Spire"), # k cloak
    "Star Piece 51" :               AdvData(72805031,     "Frozen Spire"), # k cloak
    "Star Piece 52" :               AdvData(72805122,     "Frozen Spire"), # k cloak?
    "Star Piece 53" :               AdvData(72805221,     "Frozen Spire"), # d quest
    "Star Piece 54" :               AdvData(72805321,     "Frozen Spire"), # k cloak
    "Star Piece 55" :               AdvData(72805421,     "Frozen Spire"), # d quest
    "Star Piece 56" :               AdvData(72805441,     "Frozen Spire"), # k cloak
    "Star Piece 57" :               AdvData(72805411,     "Frozen Spire"), # k cloak, g gloves
    "Star Piece 58" :               AdvData(72805111,     "Frozen Spire"),
    "Star Piece 59" :               AdvData(72805101,     "Frozen Spire"),
    "Star Piece 60" :               AdvData(72805001,     "Frozen Spire"), # k cloak
    "Star Piece 61" :               AdvData(72805121,     "Frozen Spire"), # d quest

    "Star Piece 62" :               AdvData(72808001,     "Rolling Rocks"), # 7 stars, t quest
    "Star Piece 63" :               AdvData(72808111,     "Rolling Rocks"), #
    "Star Piece 64" :               AdvData(72808101,     "Rolling Rocks"), # g gloves

    "Star Piece 65" :               AdvData(72809101,     "Sunken Island"), # 21 stars, s quest
    "Star Piece 66" :               AdvData(72809011,     "Sunken Island"), # ancient rune

    "Star Piece 67" :               AdvData(72810111,     "Aggro Crag"), # 35 star, r quest
    "Star Piece 68" :               AdvData(72810011,     "Aggro Crag"), # ancient rune

    "Star Piece 69" :               AdvData(72811101,     "Sea Nunatak"), # 49 stars, d quest
    "Star Piece 70" :               AdvData(72811001,     "Sea Nunatak"), # ancient rune

    "Star Piece 71" :               AdvData(72815111,     "Lost Landing"),

    "Star Piece 72" :               AdvData(72814000,     "Shoal"), # f flippers

    "Star Piece 73" :               AdvData(72813001,     "Star Tropic"), #
    "Star Piece 74" :               AdvData(72813102,     "Star Tropic"), # a rune
    "Star Piece 75" :               AdvData(72813101,     "Star Tropic"), # o rune, s shirt
    "Star Piece 76" :               AdvData(72813014,     "Star Tropic"), # g gloves
    "Star Piece 77" :               AdvData(72813013,     "Star Tropic"), # g gloves, s shirt,
    "Star Piece 78" :               AdvData(72813012,     "Star Tropic"), # g gloves, s shirt, f flippers
    "Star Piece 79" :               AdvData(72813011,     "Star Tropic"), # g gloves, s shirt, f flippers, k cloak

    "Star Piece 80" :               AdvData(72806031,     "Serpent Stacks"), # k cloak
    "Star Piece 81" :               AdvData(72806021,     "Serpent Stacks"), # k cloak, s circlet
    "Star Piece 82" :               AdvData(72806012,     "Serpent Stacks"), # k cloak, s circlet
    "Star Piece 83" :               AdvData(72806011,     "Serpent Stacks"), # k cloak, s circlet
    "Star Piece 84" :               AdvData(72806041,     "Serpent Stacks"), # s circlet, t quest
    "Star Piece 85" :               AdvData(72806062,     "Serpent Stacks"), # s quest, s circlet
    "Star Piece 86" :               AdvData(72806061,     "Serpent Stacks"), # s quest, s circlet
    "Star Piece 87" :               AdvData(72806072,     "Serpent Stacks"), # s circlet, r quest
    "Star Piece 88" :               AdvData(72806071,     "Serpent Stacks"), # s circlet, r quest
    "Star Piece 89" :               AdvData(72806082,     "Serpent Stacks"), # s circlet, d quest
    "Star Piece 90" :               AdvData(72806081,       "Serpent Stacks"), # s circlet, d quest

    "Star Piece 91":                AdvData(72812011,     "Locked"),

    "Rolling Bell Rung" :           AdvData(99908101,     "Rolling Rocks"),
    "Sunken Bell Rung":             AdvData(99909111,     "Sunken Island"),
    "Aggro Bell Rung" :             AdvData(99910011,     "Aggro Crag"),
    "Nunatak Bell Rung" :           AdvData(99911011,     "Sea Nunatak"),

    "Phoenix Flute" :               AdvData(51116111,     "Beast Bridge"),
    "Star Viewing Orb" :            AdvData(73314001,     "Shoal"),
    #"Shell 1" : AdvData(991027, "Tidal Reef"),
    #"Jellyfish 1" : AdvData(991027, "Topaz Sea"),

    "Stone Music Note 1" :          AdvData(45701210,     "Stony Cliffs"),
    "Stone Music Note 2" :          AdvData(45701340,     "Stony Cliffs"), # topaz rune
    "Stone Music Note 3" :          AdvData(45701130,     "Stony Cliffs"), # topaz rune
    "Stone Music Note 4":           AdvData(45701100,     "Stony Cliffs"), # topaz rune
    "Stone Music Note 5" :          AdvData(45701120,     "Stony Cliffs"), # topaz quest
    "Stone Music Note 6" :          AdvData(45701310,     "Stony Cliffs"), # topaz quest

    "Water Music Note 1" :          AdvData(45703210,     "Tidal Reef"),
    "Water Music Note 2" :          AdvData(45703400,     "Tidal Reef"), # s rune
    "Water Music Note 3" :          AdvData(45703310,     "Tidal Reef"), # s rune
    "Water Music Note 4" :          AdvData(45703420,     "Tidal Reef"), # s rune
    "Water Music Note 5" :          AdvData(45703100,     "Tidal Reef"), # s rune
    "Water Music Note 6" :          AdvData(45703020,     "Tidal Reef"), # s rune

    "Fire Music Note 1" :           AdvData(45704020,     "Raging Volcano"),
    "Fire Music Note 2" :           AdvData(45704230,     "Raging Volcano"), # r rune
    "Fire Music Note 3" :           AdvData(45704100,     "Raging Volcano"), # r rune
    "Fire Music Note 4" :           AdvData(45704120,     "Raging Volcano"), # r rune
    "Fire Music Note 5" :           AdvData(45704410,     "Raging Volcano"), # r rune
    "Fire Music Note 6" :           AdvData(45704330,     "Raging Volcano"), # salamander shirt

    "Wind Music Note 1" :           AdvData(45705110,     "Frozen Spire"),
    "Wind Music Note 2":            AdvData(45705000,     "Frozen Spire"),
    "Wind Music Note 3":            AdvData(45705430,     "Frozen Spire"),  # d rune
    "Wind Music Note 4":            AdvData(45705230,     "Frozen Spire"),  # d rune,
    "Wind Music Note 5" :           AdvData(45705020,     "Frozen Spire"), # d quest,
    "Wind Music Note 6" :           AdvData(45705330,     "Frozen Spire"), # d quest

    "Obsidian 1" :                  AdvData(46708011,    "Rolling Rocks"), # gopher gloves, 7 stars
    "Obsidian 2" :                  AdvData(46701311,    "Stony Cliffs"),
    "Obsidian 3" :                  AdvData(46701021,    "Stony Cliffs"), # DOUBLE CHECK ID # stone tablet blue, tablet golda
    "Obsidian 4" :                  AdvData(46703301,    "Tidal Reef"), # frog flippers
    "Obsidian 5" :                  AdvData(46704401,    "Raging Volcano"), # salamander shirt
    "Obsidian 6" :                  AdvData(46704341,    "Raging Volcano"), # DOUBLE CHECK ID #
    "Obsidian 7" :                  AdvData(46705101,    "Frozen Spire"),
    "Obsidian 8" :                  AdvData(46710101,    "Aggro Crag"), # salamander shirt
    "Obsidian 9" :                  AdvData(46709001,    "Sunken Island"), # frog flippers
    "Obsidian 10" :                 AdvData(46711111,    "Sea Nunatak"), # diamond quest
    "Obsidian 11" :                 AdvData(46706011,    "Serpent Stacks"), # rune stones: t,s,r,d,o, serpent circlet(?)
    "Obsidian 12" :                 AdvData(46715011,    "Lost Landing"), # phoenix flute (or secret find?)

    # In the future, could include milestones as locations. e.g. each of the steam achievments, plus extras.
}

exclusion_table = {
# Exclude the very first items of the game, such as the starting key.

}

events_table = {
}
