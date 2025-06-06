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
    "Ancient Rune Stone":                           AdvData(616120133664, "Locked"),
    "Topaz Rune Stone":                             AdvData(622012028896, "Stony Cliffs"),
    "Sapphire Rune Stone":                          AdvData(6210320272192, "Tidal Reef"),
    "Ruby Rune Stone":                              AdvData(620042016112, "Raging Volcano"),
    "Diamond Rune Stone":                           AdvData(617052222480, "Frozen Spire"),
    "Obsidian Rune Stone":                          AdvData(618060164160, "Serpent Stacks"),

    "Topaz Quest Complete":                         AdvData(99901201, "Stony Cliffs"),
    "Sapphire Quest Complete":                      AdvData(99903201, "Tidal Reef"),
    "Ruby Quest Complete":                          AdvData(99904201, "Raging Volcano"),
    "Diamond Quest Complete":                       AdvData(99905221, "Frozen Spire"),

    "Gopher Gloves":                                AdvData(358022196144, "Stony Cliffs NW"),
    "Frog Flippers":                                AdvData(346030425696, "Tidal Reef Post-Rune"),
    "Salamander Shirt":                             AdvData(623044012864, "Raging Volcano NE"),
    "Kite Cloak":                                   AdvData(399050028880, "Frozen Spire Post-Rune"),
    "Serpent Circlet":                              AdvData(654060118464, "Serpent Stacks Post-Rune"),

    "Topaz Shard Hit":                              AdvData(99907021, "Sanctum"),
    "Sapphire Shard Hit":                           AdvData(99907221, "Sanctum"),
    "Ruby Shard Hit":                               AdvData(99907201, "Sanctum"),
    "Diamond Shard Hit":                            AdvData(99907001, "Sanctum"),

    "Blue Stone Tablet":                            AdvData(5960201208144, "Stony Cliffs Post-Rune"),
    "Gold Stone Tablet":                            AdvData(5970143176160, "Stony Cliffs Post-Rune"),

    "Fire Key [Fire A4]":                                AdvData(332040480160, "Raging Volcano Post-Rune"),
    "Fire Key [Fire A0]":                                AdvData(332040024064, "Raging Volcano Post-Rune"),
    "Fire Key [Fire E4]":                                AdvData(332044424048, "Raging Volcano Post-Rune"),

    #"Egg [1]":         AdvData(991024, "Frozen Spire"), #Broken due to in-game randomness
    #"Egg [2]":         AdvData(991025, "Frozen Spire"), #Broken due to in-game randomness
    #"Egg [3]":         AdvData(991026, "Frozen Spire"), #Broken due to in-game randomness
   # "Wind Key[]":      AdvData(83505440 || 83505040 || 83505400, "Frozen Spire"), #Broken due to in-game randomness

    "Rolling Bell Rung":                            AdvData(99908101, "Rolling Rocks"),
    "Sunken Bell Rung":                             AdvData(99909111, "Sunken Island"),
    "Aggro Bell Rung":                              AdvData(99910011, "Aggro Crag"),
    "Nunatak Bell Rung":                            AdvData(99911011, "Sea Nunatak"),

    "Phoenix Flute":                                AdvData(5111611192112, "Beast Bridge"),
    "Star Viewing Orb":                             AdvData(7331400192144, "Shoal"),

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

    "Ancient Key [Ancient B3]":                     AdvData(109001327296, "Ancient Isle"),
    "Ancient Key [Ancient A1]":                     AdvData(1090001272176, "Ancient Isle"),
    "Ancient Key [Ancient A2 - SE]":                AdvData(10900029696, "Ancient Isle"),
    "Ancient Key [Ancient A3 - N]":                 AdvData(109000322448, "Ancient Isle"),
    "Ancient Key [Ancient A3 - S]":                 AdvData(1090003176160, "Ancient Isle"),
    "Ancient Key [Ancient A3 - E]":                 AdvData(109000332096, "Ancient Isle"),
    "Ancient Key [Ancient C2]":                     AdvData(1090022192176, "Ancient Isle"),
    "Ancient Key [Ancient C3]":                     AdvData(109002328896, "Ancient Isle"),
    "Ancient Key [Ancient C1]":                     AdvData(1090021240112, "Ancient Isle"),
    "Ancient Key [Ancient A2 - NW]":                AdvData(10900024848, "Ancient Isle"), # Topaz quest

    "Ancient Key [Rolling A1]":                     AdvData(1090801240128, "Rolling Rocks"),
    "Ancient Key [Rolling A0]":                     AdvData(109080016176, "Rolling Rocks"),  # 7 stars

    "Ancient Key [Tropic A1]":                      AdvData(109130196128, "Star Tropic"), # ancient rune

    "Ancient Key [Stone B1]":                       AdvData(10901116464, "Stony Cliffs NW"), #
    "Ancient Key [Stone C0]":                       AdvData(1090120352192, "Stony Cliffs"), #topaz quest
    "Ancient Key [Stone B2]":                       AdvData(109011233648, "Stony Cliffs"),
    "Ancient Key [Stone E2]":                       AdvData(10901421648, "Stony Cliffs Post-Rune"),  # topaz rune
    "Ancient Key [Stone B4]":                       AdvData(1090114272112, "Stony Cliffs Post-Rune"), #topaz quest, topaz rune
    "Ancient Key [Stone Dungeon C1]":               AdvData(109022164176, "Stony Cliffs NW"), #topaz rune, gopher gloves
    "Ancient Key [Stone Dungeon D0]":               AdvData(1090230176144, "Stony Cliffs NW"), #gopher gloves
    "Ancient Key [Stone Dungeon B1]":               AdvData(1090211272128, "Stony Cliffs NW"), #gopher gloves
    "Ancient Key [Stone B0 - NW1]":                 AdvData(10901103296, "Stony Cliffs NW"), # topaz quest
    "Ancient Key [Stone B0 - NW2]":                 AdvData(10901103280, "Stony Cliffs NW"), # topaz quest
    "Ancient Key [Stone B0 - NW3]":                 AdvData(10901103264, "Stony Cliffs NW"), # topaz quest
    "Ancient Key [Stone Dungeon E2]":               AdvData(109024212848, "Stony Cliffs Post-Rune"),

    "Ancient Key [Water C2]":                       AdvData(1090322336144, "Tidal Reef"),
    "Ancient Key [Water C3 - W]":                   AdvData(10903234896, "Tidal Reef Post-Rune"), # s rune
    "Ancient Key [Water A0 - E]":                   AdvData(1090300336160, "Tidal Reef Post-Rune"), # s rune
    "Ancient Key [Water A0 - S]":                   AdvData(1090300272192, "Tidal Reef Post-Rune"), # frog flippers
    "Ancient Key [Water A2]":                       AdvData(1090302160112, "Tidal Reef Post-Rune"), # frog flippers, s quest
    "Ancient Key [Water B3]":                       AdvData(1090313352128, "Tidal Reef"), # frog flippers
    "Ancient Key [Water C3 - NE1]":                 AdvData(109032330448, "Tidal Reef Post-Rune"), # frog flippers
    "Ancient Key [Water C3 - NE2]":                 AdvData(109032328848, "Tidal Reef Post-Rune"), # frog flippers
    "Ancient Key [Water C3 - NE3]":                 AdvData(109032327248, "Tidal Reef Post-Rune"), # frog flippers
    "Ancient Key [Water D1]":                       AdvData(109033119248, "Tidal Reef"), # frog flippers
    "Ancient Key [Water D0]":                       AdvData(1090330208112, "Tidal Reef Post-Rune"), # frog flippers
    "Ancient Key [Water C0]":                       AdvData(109032064128, "Tidal Reef"), # s quest
    "Ancient Key [Water D2]":                       AdvData(109033219264, "Tidal Reef Post-Rune"), # frog flippers

    "Ancient Key [Fire A2 - N]":                    AdvData(109040235280, "Raging Volcano"),
    "Ancient Key [Fire A2 - S]":                    AdvData(1090402336192, "Raging Volcano Post-Rune"), # salamander shirt
    "Ancient Key [Fire B4]":                        AdvData(109041496112, "Raging Volcano Post-Rune"), # r quest
    "Ancient Key [Fire A1 - NE]":                   AdvData(109040132048, "Raging Volcano Post-Rune"), # s shirt
    "Ancient Key [Fire A1 - E]":                    AdvData(1090401256176, "Raging Volcano Post-Rune"), # r rune
    "Ancient Key [Fire B1 - N1]":                   AdvData(109041114448, "Raging Volcano Post-Rune"), # r quest
    "Ancient Key [Fire B1 - N2]":                   AdvData(109041112848, "Raging Volcano Post-Rune"), # r quest
    "Ancient Key [Fire B1 - N3]":                   AdvData(109041111248, "Raging Volcano Post-Rune"), # r quest
    "Ancient Key [Fire C1 - NE]":                   AdvData(109042133680, "Raging Volcano Post-Rune"), # s shirt
    "Ancient Key [Fire C0]":                        AdvData(109042028896, "Raging Volcano"), # r quest
    "Ancient Key [Fire C1 - SW]":                   AdvData(109042132192, "Raging Volcano Post-Rune"), # s shirt
    "Ancient Key [Fire C3]":                        AdvData(109042316048, "Raging Volcano"), # r quest
    "Ancient Key [Fire A1 - S]":                    AdvData(1090401160192, "Raging Volcano Post-Rune"), # r rune
    "Ancient Key [Fire D4]":                        AdvData(109043412896, "Raging Volcano Post-Rune"), # s shirt

    # Keys on the Frozen Spire may be broken due to in-game randomness
    "Ancient Key [Wind C4]":                        AdvData(1090524336144, "Frozen Spire"),
    "Ancient Key [Wind D4 - E]":                    AdvData(109053422480, "Frozen Spire Post-Rune"), # d rune
    "Ancient Key [Wind D4 - NW1]":                  AdvData(10905344864, "Frozen Spire"), # d quest
    "Ancient Key [Wind D4 - NW2]":                  AdvData(10905346464, "Frozen Spire"), # d quest
    "Ancient Key [Wind D4 - NW3]":                  AdvData(10905348064, "Frozen Spire"), # d quest
    "Ancient Key [Wind D3]":                        AdvData(1090533240112, "Frozen Spire Post-Rune"), # k cloak
    "Ancient Key [Wind A3]":                        AdvData(1090503208112, "Frozen Spire Post-Rune"), # k cloak
    "Ancient Key [Wind C2]":                        AdvData(109052211280, "Frozen Spire"), # d quest
    "Ancient Key [Wind B1]":                        AdvData(109051125648, "Frozen Spire Post-Rune"), # double check req
    "Ancient Key [Wind E2 - NE]":                   AdvData(109054235248, "Frozen Spire Post-Rune"), # d quest
    "Ancient Key [Wind E2 - S]":                    AdvData(1090542256144, "Frozen Spire"), # d quest
    "Ancient Key [Wind E4 - E]":                    AdvData(109054412896, "Frozen Spire Post-Rune"), # d rune
    "Ancient Key [Wind E4 - SW]":                   AdvData(109054448160, "Frozen Spire Post-Rune"), # k cloak, d quest

    "Ancient Key [Aggro B0 - E]":                   AdvData(109101019280, "Aggro Crag"),
    "Ancient Key [Aggro B0 - W]":                   AdvData(1091010112176, "Aggro Crag"),

    "Ancient Key [Sunken B0]":                      AdvData(10909104880, "Sunken Island"),
    "Ancient Key [Sunken A0]":                      AdvData(1090900256192, "Sunken Island"),

    "Ancient Key [Nunatak B1]":                     AdvData(109111112896, "Sea Nunatak"),
    "Ancient Key [Nunatak A1]":                     AdvData(109110130480, "Sea Nunatak"), # ancient rune

    "Ancient Key [Stone Dungeon D2]":               AdvData(109023232176, "Stony Cliffs Post-Rune"), # t quest
    "Ancient Key [Stone A2]":                       AdvData(1090102144144, "Stony Cliffs Post-Rune"), # blue & gold tablet
    #73 keys

    "Topaz [Stone D2]":                             AdvData(784013224096, "Stony Cliffs"),
    "Topaz [Stone C2 - E]":                         AdvData(784012224064, "Stony Cliffs"),
    "Topaz [Stone C0]":                             AdvData(78401208096, "Stony Cliffs Post-Rune"),
    "Topaz [Stone C3 - N]":                         AdvData(7840123336112, "Stony Cliffs"),
    "Topaz [Stone C3 - S]":                         AdvData(7840123336160, "Stony Cliffs"),
    "Topaz [Stone C2 - W]":                         AdvData(784012214464, "Stony Cliffs Post-Rune"),
    "Topaz [Stone B0]":                             AdvData(7840110240160, "Stony Cliffs NW"),
    "Topaz [Stone B1]":                             AdvData(784011116192, "Stony Cliffs NW"),
    "Topaz [Stone B2]":                             AdvData(7840112192192, "Stony Cliffs Post-Rune"), #Rq: topaz quest
    "Topaz [Stone Dungeon C1]":                     AdvData(7840221240192, "Stony Cliffs NW"), #Rq: gopher gloves
    "Topaz [Rolling A0]":                           AdvData(784080035280, "Rolling Rocks"), #Rq: topaz quest, 7 stars
    "Topaz [Tropic A1]":                            AdvData(784130119280, "Star Tropic"), #Rq: ancient rune stone, all legendaries - serpent circlet,

    "Sapphire [Water C2 - W]":                      AdvData(63503224896, "Tidal Reef"),
    "Sapphire [Water B2 - S]":                      AdvData(6350312144176, "Tidal Reef"),
    "Sapphire [Water B2 - N]":                      AdvData(635031227264, "Tidal Reef"),
    "Sapphire [Water D2 - N]":                      AdvData(63503328048, "Tidal Reef Post-Rune"),
    "Sapphire [Water C0]":                          AdvData(6350320320192, "Tidal Reef Post-Rune"), #sapphire rune stone #
    "Sapphire [Water D2 - W]":                      AdvData(63503323296, "Tidal Reef Post-Rune"), #s rune stone
    "Sapphire [Water D1]":                          AdvData(6350331288176, "Tidal Reef Post-Rune"), #s rune stone
    "Sapphire [Water D3]":                          AdvData(635033328848, "Tidal Reef Post-Rune"), #s rune stone
    "Sapphire [Water C2 - N]":                      AdvData(635032212848, "Tidal Reef"),  # sapphire quest
    "Sapphire [Water A1]":                          AdvData(6350301304144, "Tidal Reef"), #frog flippers
    "Sapphire [Sunken B0]":                         AdvData(635091027296, "Sunken Island"), #sapphire quest, 21 stars
    "Sapphire [Tropic A1]":                         AdvData(635130120880, "Star Tropic"), # ancient rune stone, all legendaries except serpent circlet

    "Ruby [Fire B2]":                               AdvData(6060412336144, "Raging Volcano"),
    "Ruby [Fire C2]":                               AdvData(60604228064, "Raging Volcano"),
    "Ruby [Fire C0]":                               AdvData(606042016192, "Raging Volcano Post-Rune"), # ruby rune stone
    "Ruby [Fire D2 - E]":                           AdvData(606043228864, "Raging Volcano"),
    "Ruby [Fire D2 - W]":                           AdvData(606043216064, "Raging Volcano"),
    "Ruby [Fire D1]":                               AdvData(6060431192160, "Raging Volcano Post-Rune"), # ruby rune stone
    "Ruby [Fire A3 - S]":                           AdvData(6060403192176, "Raging Volcano Post-Rune"), #r rune stone
    "Ruby [Fire A3 - N]":                           AdvData(606040316080, "Raging Volcano Post-Rune"),
    "Ruby [Fire A3 - NW]":                          AdvData(606040311248, "Raging Volcano Post-Rune"), # r rune stone
    "Ruby [Fire D0]":                               AdvData(60604309648, "Raging Volcano NE"), # salamander shirt
    "Ruby [Aggro B1]":                              AdvData(606101180176, "Aggro Crag"), # ruby quest, 35 stars
    "Ruby [Tropic A1]":                             AdvData(606130120864, "Star Tropic"), # ancient rune stone, all legendaries - serpent circlet

    "Diamond [Wind C4]":                            AdvData(282052416064, "Frozen Spire"),
    "Diamond [Wind D4]":                            AdvData(282053412848, "Frozen Spire Post-Rune"),
    "Diamond [Wind B2]":                            AdvData(28205124848, "Frozen Spire"),
    "Diamond [Wind D2]":                            AdvData(282053220848, "Frozen Spire"),
    "Diamond [Wind C2]":                            AdvData(282052214496, "Frozen Spire Post-Rune"), # diamond rune stone
    "Diamond [Wind C1 - W]":                        AdvData(2820521144160, "Frozen Spire Post-Rune"), # d rune stone
    "Diamond [Wind C1 - E]":                        AdvData(2820521176160, "Frozen Spire Post-Rune"), # d rune stone
    "Diamond [Wind D1 - W]":                        AdvData(282053132160, "Frozen Spire Post-Rune"), # d rune stone
    "Diamond [Wind D1 - E]":                        AdvData(2820531256192, "Frozen Spire Post-Rune"), # d rune stone
    "Diamond [Wind C3]":                            AdvData(28205239648, "Frozen Spire Post-Rune"), # diamond quest complete
    "Diamond [Nunatak B0]":                         AdvData(282111016048, "Sea Nunatak"), # diamond quest complete
    "Diamond [Tropic A1]":                          AdvData(282130119264, "Star Tropic"), # ancient rune stone, all legendaries - serpent circlet

    "Obsidian [Rolling A1]":                        AdvData(467080128848, "Rolling Rocks"),  # gopher gloves, 7 stars
    "Obsidian [Stone D1]":                          AdvData(467013135264, "Stony Cliffs"),
    "Obsidian [Stone A2]":                          AdvData(4670102224144, "Stony Cliffs Post-Rune"),  # DOUBLE CHECK ID # stone tablet blue, tablet golda
    "Obsidian [Water D0]":                          AdvData(467033016064, "Tidal Reef Post-Rune"),  # frog flippers
    "Obsidian [Fire E0]":                           AdvData(4670440240176, "Raging Volcano NE"),  # salamander shirt
    "Obsidian [Fire D4]":                           AdvData(467043425696, "Raging Volcano Post-Rune"),  # DOUBLE CHECK ID #
    "Obsidian [Wind B0]":                           AdvData(46705103280, "Frozen Spire"),
    "Obsidian [Aggro B0]":                          AdvData(46710103280, "Aggro Crag"),  # salamander shirt
    "Obsidian [Sunken A0]":                         AdvData(4670900320160, "Sunken Island"),  # frog flippers
    "Obsidian [Nunatak B1]":                        AdvData(467111127280, "Sea Nunatak"),  # diamond quest
    "Obsidian [Serpent A1]":                        AdvData(467060164192, "Serpent Stacks Post-Rune"),  # rune stones: t,s,r,d,o, serpent circlet(?)
    "Obsidian [Lost A1]":                           AdvData(467150117696, "Lost Landing"),  # phoenix flute (or secret find?)

    # 4 of these are trapped in bells, and should be removed from total.
    # 3x4=12 trapped in music puzzle
    # 1 trapped in volcano idol puzzle
    # 1 trapped in stone tablet puzzle
    # Total of 17 stars that aren't locations.
    "Star Piece [Ancient C0]":                     AdvData(7280020208128, "Ancient Isle"),
    "Star Piece [Ancient A1]":                     AdvData(7280001272128, "Ancient Isle"),
    "Star Piece [Ancient B1]":                     AdvData(7280011128192, "Ancient Isle"),

    "Star Piece [Stone C1]":                       AdvData(7280121320176, "Stony Cliffs"), # t quest
    "Star Piece [Stone E1]":                       AdvData(728014164192, "Stony Cliffs"),
    "Star Piece [Stone B2]":                       AdvData(728011222480, "Stony Cliffs Post-Rune"), # t quest
    "Star Piece [Stone B3]":                       AdvData(728011332192, "Stony Cliffs Post-Rune"), # t quest
    "Star Piece [Stone B4]":                       AdvData(72801144848, "Stony Cliffs Post-Rune"), # g globes t quest
    "Star Piece [Stone C4]":                       AdvData(728012432128, "Stony Cliffs Post-Rune"), # g gloves t quest
    "Star Piece [Stone E4]":                       AdvData(72801443248, "Stony Cliffs Post-Rune"),
    "Star Piece [Stone C0]":                       AdvData(728012016192, "Stony Cliffs"), # t quest
    "Star Piece [Stone Dungeon E1]":               AdvData(728024114480, "Stony Cliffs Post-Rune"), # t quest
    "Star Piece [Stone Dungeon E2]":               AdvData(7280242192144, "Stony Cliffs Post-Rune"), # g gloves, f flippers
    "Star Piece [Stone Dungeon C3]":               AdvData(728022312848, "Stony Cliffs Post-Rune"), # t quest
    "Star Piece [Stone Dungeon C1]":               AdvData(72802218096, "Stony Cliffs NW"), # g gloves
    "Star Piece [Stone Dungeon B1]":               AdvData(728021164192, "Stony Cliffs NW"), # g gloves
    "Star Piece [Stone A1]":                       AdvData(728010180192, "Stony Cliffs NW"), # 5 stars

    "Star Piece [Water C1 - E]":                   AdvData(7280321192112, "Tidal Reef"),
    "Star Piece [Water C0]":                       AdvData(7280320272112, "Tidal Reef"), # s quest
    "Star Piece [Water C1 - W]":                   AdvData(72803213264, "Tidal Reef"),
    "Star Piece [Water C2]":                       AdvData(7280322352112, "Tidal Reef"), # s quest
    "Star Piece [Water D2]":                       AdvData(7280332320192, "Tidal Reef Post-Rune"), # f flippers, k cloak
    "Star Piece [Water D3]":                       AdvData(7280333304160, "Tidal Reef Post-Rune"), # f flippers | Double check
    "Star Piece [Water E2]":                       AdvData(7280342320128, "Tidal Reef Post-Rune"), # f flippers
    "Star Piece [Water E0 - W]":                   AdvData(728034016144, "Tidal Reef Post-Rune"), # f flippers
    "Star Piece [Water E0 - E]":                   AdvData(728034032080, "Tidal Reef Post-Rune"), # s quest | double check
    "Star Piece [Water B1]":                       AdvData(728031164192, "Tidal Reef"), # f flippers
    "Star Piece [Water A0]":                       AdvData(728030032048, "Tidal Reef Post-Rune"), # s rune
    "Star Piece [Water A2 - N]":                   AdvData(728030212848, "Tidal Reef Post-Rune"), # f flippers s quest || k cloak
    "Star Piece [Water A2 - S]":                   AdvData(7280302208192, "Tidal Reef Post-Rune"), # f flippers
    "Star Piece [Water A4]":                       AdvData(7280304336128, "Tidal Reef"), # f flippers
    "Star Piece [Water B4]":                       AdvData(7280314352128, "Tidal Reef"),

    "Star Piece [Fire B4]":                        AdvData(728041432080, "Raging Volcano Post-Rune"), # r quest
    "Star Piece [Fire B3]":                        AdvData(7280413352176, "Raging Volcano Post-Rune"),
    "Star Piece [Fire C3]":                        AdvData(7280423240112, "Raging Volcano Post-Rune"),
    "Star Piece [Fire C1]":                        AdvData(728042148160, "Raging Volcano"),
    "Star Piece [Fire C0]":                        AdvData(7280420336112, "Raging Volcano"),
    "Star Piece [Fire D1 - S]":                    AdvData(728043116144, "Raging Volcano"), # r quest
    "Star Piece [Fire D1 - N]":                    AdvData(72804311680, "Raging Volcano Post-Rune"), # r rune
    "Star Piece [Fire D3 - S]":                    AdvData(7280433208192, "Raging Volcano Post-Rune"), # r quest | double check
    "Star Piece [Fire D3 - W]":                    AdvData(728043380112, "Raging Volcano Post-Rune"), # r quest | double
    "Star Piece [Fire D4]":                        AdvData(72804346464, "Raging Volcano Post-Rune"), # f flippers # s shirt?
    "Star Piece [Fire E3]":                        AdvData(7280443240112, "Raging Volcano Post-Rune"),
    "Star Piece [Fire E1 - E]":                    AdvData(7280441176128, "Raging Volcano NE"), # r quest shirt
    "Star Piece [Fire E1 - W]":                    AdvData(72804411696, "Raging Volcano Post-Rune"), # s shirt
    "Star Piece [Fire E0]":                        AdvData(728044027264, "Raging Volcano NE"), # s shirt

    #locations might be broken due to in-game randomness
    "Star Piece [Wind D4]":                        AdvData(728053430464, "Frozen Spire"),
    "Star Piece [Wind C3 - W]":                    AdvData(728052332176, "Frozen Spire"), # d rune
    "Star Piece [Wind C3 - NE]":                   AdvData(728052327248, "Frozen Spire"), # d rune
    "Star Piece [Wind B3]":                        AdvData(7280513304112, "Frozen Spire Post-Rune"), # k cloak
    "Star Piece [Wind A3]":                        AdvData(7280503160192, "Frozen Spire Post-Rune"), # k cloak
    "Star Piece [Wind B2 - N]":                    AdvData(728051227248, "Frozen Spire Post-Rune"), # k cloak?
    "Star Piece [Wind C2]":                        AdvData(72805223264, "Frozen Spire"), # d quest
    "Star Piece [Wind D2]":                        AdvData(728053232128, "Frozen Spire Post-Rune"), # k cloak
    "Star Piece [Wind E2]":                        AdvData(728054216064, "Frozen Spire"), # d quest
    "Star Piece [Wind E4]":                        AdvData(728054480160, "Frozen Spire Post-Rune"), # k cloak
    "Star Piece [Wind E1]":                        AdvData(728054132144, "Frozen Spire Post-Rune"), # k cloak, g gloves
    "Star Piece [Wind B1]":                        AdvData(7280511208144, "Frozen Spire"),
    "Star Piece [Wind B0]":                        AdvData(728051025696, "Frozen Spire Post-Rune"),
    "Star Piece [Wind A0]":                        AdvData(728050017696, "Frozen Spire Post-Rune"), # k cloak
    "Star Piece [Wind B2 - S]":                    AdvData(728051232192, "Frozen Spire Post-Rune"),

    "Star Piece [Rolling A0]":                     AdvData(72808009680, "Rolling Rocks"), # 7 stars, t quest
    "Star Piece [Rolling B1]":                     AdvData(7280811176112, "Rolling Rocks"), #
    "Star Piece [Rolling B0]":                     AdvData(7280810176112, "Rolling Rocks"), # g gloves

    "Star Piece [Sunken B0]":                      AdvData(728091027264, "Sunken Island"), # 21 stars, s quest
    "Star Piece [Sunken A1]":                      AdvData(728090120896, "Sunken Island"), # ancient rune

    "Star Piece [Aggro B1]":                       AdvData(7281011240176, "Aggro Crag"), # 35 star, r quest
    "Star Piece [Aggro A1]":                       AdvData(728100164144, "Aggro Crag"), # ancient rune

    "Star Piece [Nunatak B0]":                     AdvData(728111030448, "Sea Nunatak"), # 49 stars, d quest
    "Star Piece [Nunatak A0]":                     AdvData(7281100208160, "Sea Nunatak"), # ancient rune

    "Star Piece [Lost B1]":                        AdvData(7281511192144, "Lost Landing"),

    "Star Piece [Shoal A0]":                       AdvData(7281400272176, "Shoal"), # f flippers

    "Star Piece [Tropic A0]":                      AdvData(7281300304176, "Star Tropic"), #
    "Star Piece [Tropic B0 - S]":                  AdvData(728131080128, "Star Tropic"), # a rune
    "Star Piece [Tropic B0 - N]":                  AdvData(728131014464, "Star Tropic"), # o rune, s shirt
    "Star Piece [Tropic A1 - 1]":                  AdvData(728130112848, "Star Tropic"), # g gloves
    "Star Piece [Tropic A1 - 2]":                  AdvData(728130114480, "Star Tropic"), # g gloves, s shirt,
    "Star Piece [Tropic A1 - 3]":                  AdvData(728130116048, "Star Tropic"), # g gloves, s shirt, f flippers
    "Star Piece [Tropic A1 - 4]":                  AdvData(728130117680, "Star Tropic"), # g gloves, s shirt, f flippers, k cloak

    "Star Piece [Serpent A3]":                     AdvData(728060327280, "Serpent Stacks"), # k cloak
    "Star Piece [Serpent A2]":                     AdvData(728060230464, "Serpent Stacks"), # k cloak, s circlet
    "Star Piece [Serpent A1 - W]":                 AdvData(728060148176, "Serpent Stacks Post-Rune"), # k cloak, s circlet
    "Star Piece [Serpent A1 - N]":                 AdvData(728060122448, "Serpent Stacks Post-Rune"), # k cloak, s circlet
    "Star Piece [Serpent A4]":                     AdvData(72806044864, "Serpent Stacks Post-Rune"), # s circlet, t quest
    "Star Piece [Serpent A6 - W]":                 AdvData(72806063264, "Serpent Stacks Post-Rune"), # s quest, s circlet
    "Star Piece [Serpent A6 - E]":                 AdvData(7280606336176, "Serpent Stacks Post-Rune"), # s quest, s circlet
    "Star Piece [Serpent A7 - W]":                 AdvData(728060732192, "Serpent Stacks Post-Rune"), # s circlet, r quest
    "Star Piece [Serpent A7 - E]":                 AdvData(7280607352192, "Serpent Stacks Post-Rune"), # s circlet, r quest
    "Star Piece [Serpent A8 - N]":                 AdvData(7280608320144, "Serpent Stacks Post-Rune"), # s circlet, d quest
    "Star Piece [Serpent A8 - S]":                 AdvData(7280608320176, "Serpent Stacks Post-Rune"), # s circlet, d quest

    "Star Piece [Locked A1]":                      AdvData(7281201320192, "Locked"),
    #91 stars


    #"Jellyfish 1]": AdvData(991027, "Topaz Sea"),

    "Music Note [Stone C1]":                       AdvData(457012127264, "Stony Cliffs"), #
    "Music Note [Stone D4]":                       AdvData(4570134304112, "Stony Cliffs Post-Rune"), # topaz rune
    "Music Note [Stone B3]":                       AdvData(4570113160176, "Stony Cliffs Post-Rune"), # topaz rune
    "Music Note [Stone B0]":                       AdvData(4570110320192, "Stony Cliffs NW"), # topaz rune
    "Music Note [Stone B2]":                       AdvData(4570112192144, "Stony Cliffs Post-Rune"), # topaz quest
    "Music Note [Stone D1]":                       AdvData(457013180160, "Stony Cliffs"), # topaz quest

    "Music Note [Water C1]":                       AdvData(457032196176, "Tidal Reef"),
    "Music Note [Water E0]":                       AdvData(4570340288160, "Tidal Reef Post-Rune"), # s rune
    "Music Note [Water D1]":                       AdvData(457033135248, "Tidal Reef Post-Rune"), # s rune
    "Music Note [Water E2]":                       AdvData(4570342288176, "Tidal Reef Post-Rune"), # s rune
    "Music Note [Water B0]":                       AdvData(457031032128, "Tidal Reef Post-Rune"), # s rune
    "Music Note [Water A2]":                       AdvData(4570302288112, "Tidal Reef Post-Rune"), # s rune

    "Music Note [Fire A2]":                        AdvData(4570402176160, "Raging Volcano"),
    "Music Note [Fire C3]":                        AdvData(4570423240176, "Raging Volcano Post-Rune"), # r rune
    "Music Note [Fire B0]":                        AdvData(4570410192160, "Raging Volcano Post-Rune"), # r rune
    "Music Note [Fire B2]":                        AdvData(4570412240192, "Raging Volcano Post-Rune"), # r rune
    "Music Note [Fire E1]":                        AdvData(4570441320144, "Raging Volcano Post-Rune"), # r rune
    "Music Note [Fire D3]":                        AdvData(4570433352144, "Raging Volcano Post-Rune"), # salamander shirt

    "Music Note [Wind B1]":                        AdvData(4570511144160, "Frozen Spire"),
    "Music Note [Wind A0]":                        AdvData(4570500320160, "Frozen Spire"),
    "Music Note [Wind E3]":                        AdvData(457054348112, "Frozen Spire Post-Rune"),  # d rune
    "Music Note [Wind C3]":                        AdvData(457052332128, "Frozen Spire Post-Rune"),  # d rune,
    "Music Note [Wind A2]":                        AdvData(4570502304128, "Frozen Spire Post-Rune"), # d quest,
    "Music Note [Wind D3]":                        AdvData(457053380192, "Frozen Spire Post-Rune"), # d quest



    # In the future, could include milestones as locations. e.g. each of the steam achievements, plus extras.
}

seashell_table = {

    # 24 checks
    "Shell [Water B2]":                            AdvData(6360312352192, "Tidal Reef"),
    "Shell [Water C0]":                            AdvData(63603206464, "Tidal Reef"),
    "Shell [Water B0]":                            AdvData(63603106448, "Tidal Reef"),
    "Shell [Water B1]":                            AdvData(636031135280, "Tidal Reef"),
    "Shell [Water C1]":                            AdvData(6360321240176, "Tidal Reef"),
    "Shell [Water C2]":                            AdvData(636032224048, "Tidal Reef"),
    "Shell [Water D2]":                            AdvData(636033216048, "Tidal Reef Post-Rune"), # s rune
    "Shell [Water A1]":                            AdvData(636030164192, "Tidal Reef"), # s rune
    "Shell [Water A0]":                            AdvData(6360300352112, "Tidal Reef Post-Rune"), # s rune
    "Shell [Water A3]":                            AdvData(636030364112, "Tidal Reef"), # s rune
    "Shell [Water B3]":                            AdvData(636031380192, "Tidal Reef"), # s rune
    "Shell [Water B4]":                            AdvData(6360314192192, "Tidal Reef"), # s rune
    "Shell [Water C4]":                            AdvData(636032464160, "Tidal Reef"), # s rune
    "Shell [Water C3]":                            AdvData(6360323352144, "Tidal Reef Post-Rune"), # s rune
    "Shell [Water D4]":                            AdvData(6360334352176, "Tidal Reef Post-Rune"), # s rune
    "Shell [Water E4]":                            AdvData(636034412848, "Tidal Reef Post-Rune"), # s rune
    "Shell [Water E2]":                            AdvData(636034225680, "Tidal Reef Post-Rune"), # s rune
    "Shell [Water E1]":                            AdvData(636034116192, "Tidal Reef Post-Rune"), # s rune
    "Shell [Water E0]":                            AdvData(6360340256112, "Tidal Reef Post-Rune"), # s rune
    "Shell [Water D3]":                            AdvData(6360333128112, "Tidal Reef Post-Rune"), # s rune
    "Shell [Water A4]":                            AdvData(6360304240176, "Tidal Reef"),  # f flippers
    "Shell [Water D1]":                            AdvData(636033111248, "Tidal Reef"),  # f flippers
    "Shell [Water D0]":                            AdvData(6360330304112, "Tidal Reef Post-Rune"),  # f flippers
    "Shell [Water A2]":                            AdvData(636030264176, "Tidal Reef Post-Rune"),  # f flippers





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

secrets_table = {

    "Discover Ancient Secret 1": AdvData(101044, "Ancient Isle"),

    "Discover Stone Secret 1": AdvData(107724, "Stony Cliffs"),
    "Discover Stone Secret 2": AdvData(106794, "Stony Cliffs Post-Rune"),

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
    "Discover Fire Secret 3": AdvData(118553, "Raging Volcano NE"),

    "Discover Wind Secret 1": AdvData(121435, "Frozen Spire"),
    "Discover Wind Secret 2": AdvData(120347, "Frozen Spire"),
    "Discover Wind Secret 3": AdvData(121434, "Frozen Spire Post-Rune"),

}

# Est. 101 extra checks here.
locksanity_table = {
    "Lock [Ancient B3]":                            AdvData(11100131, "Ancient Isle"),
    "Lock [Ancient B2]":                            AdvData(11100121, "Ancient Isle"),
    "Lock [Ancient A3]":                            AdvData(11100031, "Ancient Isle"),
    "3x Lock [Ancient C2]":                         AdvData(43500221, "Ancient Isle"),
    "3x Lock [Ancient A1]":                         AdvData(43500011, "Ancient Isle"), # access o sea

    "Lock [Stone C2]":                              AdvData(11101221, "Stony Cliffs"),
    "3x Lock [Stone E1]":                           AdvData(43501411, "Stony Cliffs"),
    "Lock [Stone B1]":                              AdvData(11101111, "Stony Cliffs NW"), # t rune

    "Lock [Water B2]":                              AdvData(11103121, "Tidal Reef"),
    "3x Lock [Water C1]":                           AdvData(43503211, "Tidal Reef"),
    "Lock [Water D3]":                              AdvData(11103331, "Tidal Reef Post-Rune"), # s rune

    "3x Lock (Fire) [Fire E0]":                     AdvData(78804401, "Raging Volcano NE"),
    "Lock [Fire A3]":                               AdvData(11104031, "Raging Volcano Post-Rune"),
    "Lock [Fire D2]":                               AdvData(11104321, "Raging Volcano"),
    "3x Lock [Fire D2]":                            AdvData(43504321, "Raging Volcano"),

    "Lock [Wind C3]":                               AdvData(11105231, "Frozen Spire Post-Rune"),
    "3x Lock [Wind D3]":                            AdvData(43505331, "Frozen Spire"),
    "Lock [Wind D1]":                               AdvData(11105311, "Frozen Spire Post-Rune"),
    "Lock (Wind) [Wind A0]":                        AdvData(83605001, "Frozen Spire"),

    "3x Lock [Sanctum B2 - W]":                     AdvData(43507122, "Sanctum"),
    "3x Lock [Sanctum B2 - E]":                     AdvData(43507121, "Sanctum"),
    "3x Lock [Sanctum A1]":                         AdvData(43507011, "Sanctum"),
    "3x Lock [Sanctum C1]":                         AdvData(43507211, "Sanctum"),

    "3x Lock [Rolling B1]":                         AdvData(43508111, "Rolling Rocks"),

    "3x Lock [Sunken A1]":                          AdvData(43509011, "Sunken Island"),

    "3x Lock [Aggro A1]":                           AdvData(43510011, "Aggro Crag"),

    "3x Lock [Nunatak A0]":                         AdvData(43511001, "Sea Nunatak"),

    "6x Lock [Locked B1]":                          AdvData(43412011, "Locked"),

    "Lock [Lost B1]":                               AdvData(11115011, "Lost Landing"),

    "Star Lock 1 [Ancient C1]":                     AdvData(73000211, "Ancient Isle"),

    "Star Lock 3 [Overworld]":                      AdvData(73020111, "Topaz Sea"),
    "Star Lock 15 [Overworld]":                     AdvData(73020112, "Topaz Sea"),
    "Star Lock 30 [Overworld]":                     AdvData(73020113, "Diamond Sea"),
    "Star Lock 45 [Overworld]":                     AdvData(73020114, "Obsidian Sea"),

    "Star Lock 5 [Stone A1]":                       AdvData(73001011, "Stony Cliffs NW"),
    "Star Lock 15 [Stone C4]":                      AdvData(73001241, "Stony Cliffs Post-Rune"),
    "Star Lock 20 [Stone E3]":                      AdvData(73001431, "Stony Cliffs Post-Rune"),
    "Star Lock 20 [Stone Dungeon A1]":              AdvData(73002011, "Stony Cliffs Post-Rune"),

    "Star Lock 30 [Water A2]":                      AdvData(73003021, "Tidal Reef Post-Rune"),

    "Star Lock 7 [Rolling A0]":                     AdvData(73008001, "Rolling Rocks"),
    "Star Lock 21 [Sunken B0]":                     AdvData(73009101, "Sunken Island"),
    "Star Lock 30 [Lost A0]":                       AdvData(73015101, "Lost Landing"),
    "Star Lock 35 [Aggro B0]":                      AdvData(73010101, "Aggro Crag"),
    "Star Lock 49 [Nunatak B0]":                    AdvData(73011101, "Sea Nunatak"),

    "Ancient Rune Lock [Ancient B1]":               AdvData(60700111, "Ancient Isle"),

    "Topaz Rune Lock [Stone C0]":                   AdvData(61401201, "Stony Cliffs Post-Rune"), #post-rune is inclusive of rune lock checks
    "Topaz Rune Lock [Stone C1]":                   AdvData(61401211, "Stony Cliffs Post-Rune"),
    "Topaz Rune Lock [Stone E1]":                   AdvData(61401411, "Stony Cliffs Post-Rune"),
    "Topaz Rune Lock [Stone E2]":                   AdvData(61401421, "Stony Cliffs Post-Rune"),
    "Topaz Rune Lock [Stone E3]":                   AdvData(61401431, "Stony Cliffs Post-Rune"),
    "Topaz Rune Lock [Stone C4]":                   AdvData(61401241, "Stony Cliffs Post-Rune"),

    "Sapphire Rune Lock [Water C0]":                AdvData(61303201, "Tidal Reef Post-Rune"),
    "Sapphire Rune Lock [Water B2]":                AdvData(61303121, "Tidal Reef Post-Rune"),
    "Sapphire Rune Lock [Water A0]":                AdvData(61303001, "Tidal Reef Post-Rune"),
    "Sapphire Rune Lock [Water A3]":                AdvData(61303031, "Tidal Reef Post-Rune"),
    "Sapphire Rune Lock [Water D2 - N]":            AdvData(61303322, "Tidal Reef Post-Rune"),
    "Sapphire Rune Lock [Water D2 - S]":            AdvData(61303321, "Tidal Reef Post-Rune"),
    "Sapphire Rune Lock [Water D0]":                AdvData(61303301, "Tidal Reef Post-Rune"),
    "Sapphire Rune Lock [Water C3 - E]":            AdvData(61303232, "Tidal Reef Post-Rune"),
    "Sapphire Rune Lock [Water C3 - W]":            AdvData(61303231, "Tidal Reef Post-Rune"),
    "Sapphire Rune Lock [Water B3]":                AdvData(61303131, "Tidal Reef Post-Rune"),

    "Ruby Rune Lock [Fire A1 - S]":                 AdvData(61204011, "Raging Volcano Post-Rune"),
    "Ruby Rune Lock [Fire A1 - E]":                 AdvData(61204012, "Raging Volcano Post-Rune"),
    "Ruby Rune Lock [Fire A2]":                     AdvData(61204021, "Raging Volcano Post-Rune"),
    "Ruby Rune Lock [Fire A3]":                     AdvData(61204031, "Raging Volcano Post-Rune"),
    "Ruby Rune Lock [Fire B2 - N]":                 AdvData(61204122, "Raging Volcano Post-Rune"),
    "Ruby Rune Lock [Fire B2 - S]":                 AdvData(61204121, "Raging Volcano Post-Rune"),
    "Ruby Rune Lock [Fire C0]":                     AdvData(61204201, "Raging Volcano Post-Rune"),
    "Ruby Rune Lock [Fire C1]":                     AdvData(61204211, "Raging Volcano Post-Rune"),
    "Ruby Rune Lock [Fire C2 - S]":                 AdvData(61204232, "Raging Volcano Post-Rune"),
    "Ruby Rune Lock [Fire C2 - W]":                 AdvData(61204231, "Raging Volcano Post-Rune"),
    "Ruby Rune Lock [Fire D1]":                     AdvData(61204311, "Raging Volcano Post-Rune"),
    "Ruby Rune Lock [Fire E0]":                     AdvData(61204401, "Raging Volcano Post-Rune"),

    "Diamond Rune Lock [Wind C3]":                  AdvData(60805231, "Frozen Spire Post-Rune"),
    "Diamond Rune Lock [Wind D4]":                  AdvData(60805341, "Frozen Spire Post-Rune"),
    "Diamond Rune Lock [Wind E3]":                  AdvData(60805431, "Frozen Spire Post-Rune"),
    "Diamond Rune Lock [Wind E2 - W]":              AdvData(60805422, "Frozen Spire Post-Rune"),
    "Diamond Rune Lock [Wind E2 - E]":              AdvData(60805421, "Frozen Spire Post-Rune"),
    "Diamond Rune Lock [Wind E0]":                  AdvData(60805401, "Frozen Spire Post-Rune"),
    "Diamond Rune Lock [Wind D1]":                  AdvData(60805311, "Frozen Spire Post-Rune"),
    "Diamond Rune Lock [Wind C2]":                  AdvData(60805221, "Frozen Spire Post-Rune"),
    "Diamond Rune Lock [Wind C1]":                  AdvData(60805211, "Frozen Spire Post-Rune"),
    "Diamond Rune Lock [Wind B1]":                  AdvData(60805111, "Frozen Spire Post-Rune"),
    "Diamond Rune Lock [Wind B2]":                  AdvData(60805131, "Frozen Spire Post-Rune"),
    "Diamond Rune Lock [Wind A2]":                  AdvData(60805021, "Frozen Spire Post-Rune"),

    "Elemental Rune Lock [Serpent A2]":             AdvData(60906021, "Serpent Stacks"),
    "Obsidian Rune Lock [Serpent A1 - N]":          AdvData(61006011, "Serpent Stacks Post-Rune"),
    "Obsidian Rune Lock [Serpent A1 - W]":          AdvData(61006012, "Serpent Stacks Post-Rune"),
    "Obsidian Rune Lock [Serpent A1 - E]":          AdvData(61006013, "Serpent Stacks Post-Rune"),
    "Obsidian Rune Lock [Serpent A3]":              AdvData(61006031, "Serpent Stacks Post-Rune"),

    "Ancient Rune Lock [Rolling A1]":               AdvData(60708011, "Rolling Rocks"),
    "Ancient Rune Lock [Rolling B0]":               AdvData(60708101, "Rolling Rocks"),

    "Ancient Rune Lock [Sunken A0]":                AdvData(60709001, "Sunken Island"),
    "Ancient Rune Lock [Sunken B1]":                AdvData(60709111, "Sunken Island"),

    "Ancient Rune Lock [Aggro B1]":                 AdvData(60710111, "Aggro Crag"),
    "Ancient Rune Lock [Aggro A1]":                 AdvData(60710011, "Aggro Crag"),

    "Ancient Rune Lock [Nunatak B0]":               AdvData(60711101, "Sea Nunatak"),

    "Ancient Rune Lock [Locked A1]":                AdvData(60712011, "Locked"),

    "Ancient Rune Lock [Tropic A1]":                AdvData(60713011, "Star Tropic"),
    "Ancient Rune Lock [Tropic B0]":                AdvData(60713101, "Star Tropic"),
    "Obsidian Rune Lock [Tropic B0]":               AdvData(61013101, "Star Tropic"),

    "Ancient Rune Lock [Shoal A0]":                 AdvData(60714001, "Shoal"),

}

# 196 checks
snakesanity_table = {
    "Snakeblock [Ancient B3]": AdvData(681001319280, "Ancient Isle"),
    "Snakeblock [Ancient B2 - W]": AdvData(683001232128, "Ancient Isle"),
    "Snakeblock [Ancient B2 - E]": AdvData(6860012336144, "Ancient Isle"),
    "Snakeblock [Ancient A3]": AdvData(681000316064, "Ancient Isle"),
    "Snakeblock [Ancient A1]": AdvData(6800001192160, "Ancient Isle"),
    "Snakeblock [Ancient C2 - E]": AdvData(6810022288128, "Ancient Isle"),
    "Snakeblock [Ancient C2 - S]": AdvData(6800022224176, "Ancient Isle"),
    "Snakeblock [Ancient C2 - W]": AdvData(6810022160176, "Ancient Isle"),
    "Snakeblock [Ancient C3]": AdvData(68100238064, "Ancient Isle"),

    "Snakeblock [Stone D2]": AdvData(680013264144, "Stony Cliffs"),
    "Snakeblock [Stone E1 - W]": AdvData(6800141144144, "Stony Cliffs"),
    "Snakeblock [Stone C1]": AdvData(6810121176128, "Stony Cliffs"), # topaz Quest
    "Snakeblock [Stone D1]": AdvData(6800131144144, "Stony Cliffs"), # topaz Quest
    "Snakeblock [Stone E1 - E]": AdvData(6830141176112, "Stony Cliffs Post-Rune"), # t quest
    "Snakeblock [Stone E0]": AdvData(681014064112, "Stony Cliffs Post-Rune"),
    "Snakeblock [Stone B1 - W]": AdvData(681011124064, "Stony Cliffs NW"),
    "Snakeblock [Stone B0]": AdvData(6860110256112, "Stony Cliffs NW"),
    "Snakeblock [Stone A2 - N]": AdvData(683010235248, "Stony Cliffs NW"),
    "Snakeblock [Stone A2 - S]": AdvData(686010235264, "Stony Cliffs Post-Rune"),
    "Snakeblock [Stone A3]": AdvData(6830103320192, "Stony Cliffs Post-Rune"),
    "Snakeblock [Stone B3 - S]": AdvData(680011348192, "Stony Cliffs Post-Rune"),
    "Snakeblock [Stone A4 - W]": AdvData(68001048048, "Stony Cliffs Post-Rune"),
    "Snakeblock [Stone A0]": AdvData(6810100256192, "Stony Cliffs NW"),
    "Snakeblock [Stone B1 - E]": AdvData(683011135296, "Stony Cliffs NW"),
    "Snakeblock [Stone B4]": AdvData(6830114176160, "Stony Cliffs Post-Rune"), #g gloves, 15 stars
    "Snakeblock [Stone A4 - E]": AdvData(6810104352144, "Stony Cliffs Post-Rune"), #g gloves, 15 stars
    "Snakeblock [Stone C4]": AdvData(68601248064, "Stony Cliffs Post-Rune"), # t quest
    "Snakeblock [Stone B3 - N]": AdvData(68101136448, "Stony Cliffs Post-Rune"),
    "Snakeblock [Stone B2 - W]": AdvData(6810112160192, "Stony Cliffs Post-Rune"),
    "Snakeblock [Stone B2 - E]": AdvData(6800112224192, "Stony Cliffs Post-Rune"),
    "Snakeblock [Stone C2]": AdvData(6800122128176, "Stony Cliffs Post-Rune"),
    "Snakeblock [Stone E4]": AdvData(680014432160, "Stony Cliffs Post-Rune"),
    "Snakeblock [Stone Dungeon C4]": AdvData(681022420896, "Stony Cliffs Post-Rune"), # t quest
    "Snakeblock [Stone Dungeon C3]": AdvData(683022319296, "Stony Cliffs Post-Rune"), # t quest
    "Snakeblock [Stone Dungeon B2 - E]": AdvData(6860212240144, "Stony Cliffs Post-Rune"),
    "Snakeblock [Stone Dungeon B2 - W]": AdvData(680021248128, "Stony Cliffs Post-Rune"),
    "Snakeblock [Stone Dungeon B2 - N]": AdvData(6830212176112, "Stony Cliffs Post-Rune"),
    "Snakeblock [Stone Dungeon B1]": AdvData(6860211176176, "Stony Cliffs Post-Rune"),
    "Snakeblock [Stone Dungeon D2 - E]": AdvData(6830232320112, "Stony Cliffs Post-Rune"), # t quest
    "Snakeblock [Stone Dungeon D2 - CE]": AdvData(6810232240128, "Stony Cliffs Post-Rune"), # t quest
    "Snakeblock [Stone Dungeon D2 - W]": AdvData(6800232112160, "Stony Cliffs Post-Rune"), # t quest
    "Snakeblock [Stone Dungeon D2 - CW]": AdvData(6810232192128, "Stony Cliffs Post-Rune"), # t quest
    "Snakeblock [Stone Dungeon D1 - W]": AdvData(6830231160176, "Stony Cliffs Post-Rune"), # t quest
    "Snakeblock [Stone Dungeon D1 - CS]": AdvData(6860231256112, "Stony Cliffs Post-Rune"), # t quest
    "Snakeblock [Stone Dungeon D1 - CN]": AdvData(683023125696, "Stony Cliffs"),
    "Snakeblock [Stone Dungeon D1 - E]": AdvData(6860231336128, "Stony Cliffs Post-Rune"), # t quest
    "Snakeblock [Stone Dungeon E1]": AdvData(683024117696, "Stony Cliffs Post-Rune"), # t quest
    "Snakeblock [Stone Dungeon E2]": AdvData(683024296112, "Stony Cliffs Post-Rune"), # t quest
    "Snakeblock [Stone Dungeon C1]": AdvData(6830221208112, "Stony Cliffs NW"), # t quest, #g gloves

    "Snakeblock [Rolling B0]": AdvData(6830810256176, "Rolling Rocks"),

    "Snakeblock [Aggro B1 - E]": AdvData(681101130496, "Aggro Crag"), # 35 stars
    "Snakeblock [Aggro B1 - W]": AdvData(686101116160, "Aggro Crag"), # 35 stars, R quest, A rune
    "Snakeblock [Aggro B0 - E]": AdvData(6861010112160, "Aggro Crag"),
    "Snakeblock [Aggro B0 - W]": AdvData(680101096144, "Aggro Crag"), # 35 stars, R quest, A rune, s shirt

    "Snakeblock [Locked A1 - E]": AdvData(6861201112160, "Locked"),
    "Snakeblock [Locked A1 - C]": AdvData(6861201160160, "Locked"),
    "Snakeblock [Locked A1 - W]": AdvData(6831201208144, "Locked"),

    "Snakeblock [Nunatak A1]": AdvData(6811101288112, "Sea Nunatak"), # a rune, d quest?

    "Snakeblock [Shoal A0]": AdvData(681140020896, "Shoal"), # a rune, k cloak

    "Snakeblock [Lost B1]": AdvData(680151120896, "Lost Landing"), # 30 Stars, p flute

    "Snakeblock [Tropic A0 - W]": AdvData(6811300224160, "Star Tropic"), # k cloak
    "Snakeblock [Tropic A0 - C]": AdvData(6811300272160, "Star Tropic"), # k cloak
    "Snakeblock [Tropic A0 - E]": AdvData(6811300320176, "Star Tropic"), # k cloak
    "Snakeblock [Tropic B0 - N]": AdvData(68313104896, "Star Tropic"), # k cloak
    "Snakeblock [Tropic B0 - S]": AdvData(680131064160, "Star Tropic"), # k cloak

    "Damsnake [Overworld - Sapphire Sea]": AdvData(4782011320256, "Sapphire Sea"),
    "Damsnake [Overworld - Beast Sea]": AdvData(4792011784224, "Beast Sea"),
    "Damsnake [Overworld - Lost Sea]": AdvData(4782011352432, "Lost Sea"),
    "Damsnake [Overworld - Northeast Sea]": AdvData(4792011800112, "Northeast Sea"),

    "Snakeblock [Water C2 - W]": AdvData(683032216128, "Tidal Reef"),
    "Snakeblock [Water C2 - SE]": AdvData(6810322272176, "Tidal Reef"),
    "Snakeblock [Water D2 - W]": AdvData(683033216112, "Tidal Reef"),
    "Snakeblock [Water C1 - E]": AdvData(6860321304144, "Tidal Reef"),
    "Snakeblock [Water C1 - CE]": AdvData(6810321240128, "Tidal Reef"),
    "Snakeblock [Water C2 - NE]": AdvData(6810322224112, "Tidal Reef"),
    "Snakeblock [Water C2 - CE]": AdvData(6830322256128, "Tidal Reef"),
    "Snakeblock [Water B2 - SE]": AdvData(6800312256128, "Tidal Reef"),
    "Snakeblock [Water B2 - NE]": AdvData(683031230480, "Tidal Reef"),
    "Snakeblock [Water C1 - W]": AdvData(683032132160, "Tidal Reef"),
    "Snakeblock [Water C1 - CW]": AdvData(6800321128128, "Tidal Reef"),
    "Snakeblock [Water B0 - E]": AdvData(6800310240128, "Tidal Reef"), # s quest
    "Snakeblock [Water B0 - C]": AdvData(6800310128144, "Tidal Reef"), # s quest, f flippers
    "Snakeblock [Water B1 - E]": AdvData(6800311272192, "Tidal Reef"), # s quest,
    "Snakeblock [Water B1 - C]": AdvData(6830311208144, "Tidal Reef"), # s quest,
    "Snakeblock [Water B3]": AdvData(680031316048, "Tidal Reef"),
    "Snakeblock [Water D0 - W]": AdvData(686033011280, "Tidal Reef"),
    "Snakeblock [Water D0 - E]": AdvData(6830330240112, "Tidal Reef Post-Rune"),
    "Snakeblock [Water D1]": AdvData(681033196192, "Tidal Reef Post-Rune"),
    "Snakeblock [Water D2 - C]": AdvData(6810332208160, "Tidal Reef Post-Rune"), # f flippers
    "Snakeblock [Water D2 - E]": AdvData(680033233664, "Tidal Reef Post-Rune"), # f flippers
    "Snakeblock [Water E1 - W]": AdvData(681034114480, "Tidal Reef Post-Rune"), # f flippers
    "Snakeblock [Water E1 - E]": AdvData(683034132096, "Tidal Reef Post-Rune"), # f flippers
    "Snakeblock [Water E2 - E]": AdvData(6810342304128, "Tidal Reef Post-Rune"), # f flippers
    "Snakeblock [Water E2 - W]": AdvData(686034264144, "Tidal Reef Post-Rune"),
    "Snakeblock [Water E3]": AdvData(683034332160, "Tidal Reef Post-Rune"),
    "Snakeblock [Water D3]": AdvData(6810333224144, "Tidal Reef Post-Rune"),
    "Snakeblock [Water A0 - W]": AdvData(6810300224128, "Tidal Reef Post-Rune"),
    "Snakeblock [Water A0 - S]": AdvData(6860300256144, "Tidal Reef Post-Rune"), # f flippers
    "Snakeblock [Water A2]": AdvData(686030222496, "Tidal Reef Post-Rune"), # f flippers, s quest, 30 stars
    "Snakeblock [Water A3]": AdvData(683030316064, "Tidal Reef Post-Rune"), # f flippers, s quest, 30 stars
    "Snakeblock [Water B4]": AdvData(681031430496, "Tidal Reef"),
    "Snakeblock [Water B0]": AdvData(683031016112, "Tidal Reef Post-Rune"),

    "Snakeblock [Fire B2 - W]": AdvData(681041296128, "Raging Volcano"),
    "Snakeblock [Fire B2 - CW]": AdvData(6860412128144, "Raging Volcano"),
    "Snakeblock [Fire B2 - CE]": AdvData(6830412192128, "Raging Volcano"),
    "Snakeblock [Fire B2 - E]": AdvData(6810412304128, "Raging Volcano"),
    "Snakeblock [Fire B2 - SW]": AdvData(6860412112176, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire C2 - W]": AdvData(686042217680, "Raging Volcano"),
    "Snakeblock [Fire C2 - NE]": AdvData(683042228880, "Raging Volcano"),
    "Snakeblock [Fire C2 - E]": AdvData(6860422336160, "Raging Volcano"),
    "Snakeblock [Fire D2 - W]": AdvData(6830432112112, "Raging Volcano"),
    "Snakeblock [Fire D2 - C]": AdvData(6860432240176, "Raging Volcano"),
    "Snakeblock [Fire D2 - NE]": AdvData(683043232096, "Raging Volcano"),
    "Snakeblock [Fire D2 - SE]": AdvData(6810432320192, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire D1 - SW]": AdvData(6860431112176, "Raging Volcano"),
    "Snakeblock [Fire D1 - W]": AdvData(6810431112128, "Raging Volcano"),
    "Snakeblock [Fire D1 - C]": AdvData(6800431240176, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire D1 - NE]": AdvData(686043130496, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire D1 - SE]": AdvData(6810431336192, "Raging Volcano Post-Rune"), # S shirt
    "Snakeblock [Fire C1]": AdvData(6810421320112, "Raging Volcano"),
    "Snakeblock [Fire B1]": AdvData(6860411304160, "Raging Volcano"), # s shirt
    "Snakeblock [Fire B0]": AdvData(681041032128, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire A1 - E]": AdvData(6810401320112, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire A1 - NE]": AdvData(683040128880, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire A0 - E]": AdvData(6800400272112, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire A0 - W]": AdvData(6810400176144, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire A3 - E]": AdvData(686040335296, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire A3 - SE]": AdvData(6810403336176, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire A3 - S]": AdvData(6860403256176, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire A3 - W]": AdvData(6830403160112, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire A4]": AdvData(686040430464, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire B4 - W]": AdvData(6830414112128, "Raging Volcano Post-Rune"), # r quest
    "Snakeblock [Fire B4 - E]": AdvData(6800414304128, "Raging Volcano Post-Rune"), # r quest
    "Snakeblock [Fire B3 - CW]": AdvData(68304136480, "Raging Volcano Post-Rune"), # r quest
    "Snakeblock [Fire B3 - W]": AdvData(683041316144, "Raging Volcano Post-Rune"), # r quest
    "Snakeblock [Fire B3 - CE]": AdvData(6830413240128, "Raging Volcano Post-Rune"), # r quest
    "Snakeblock [Fire B3 - E]": AdvData(6860413352144, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire C3 - E]": AdvData(681042312848, "Raging Volcano Post-Rune"), # r quest
    "Snakeblock [Fire C3 - W]": AdvData(68004233296, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire C4 - NE]": AdvData(681042427248, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire C4 - SE]": AdvData(6810424224128, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire D4 - W]": AdvData(683043480128, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire D4 - E]": AdvData(6830434320128, "Raging Volcano Post-Rune"),# s shirt
    "Snakeblock [Fire E4 - E]": AdvData(681044419248, "Raging Volcano Post-Rune"),
    "Snakeblock [Fire E4 - CE]": AdvData(680044417648, "Raging Volcano Post-Rune"), # s shirt
    "Snakeblock [Fire E4 - W]": AdvData(683044432128, "Raging Volcano Post-Rune"), # s shirt

    "Snakeblock [Fire D3 - W]": AdvData(680043316112, "Raging Volcano Post-Rune"), # s shirt
    "Snakeblock [Fire D3 - E]": AdvData(686043330464, "Raging Volcano Post-Rune"), # s shirt, r quest
    "Snakeblock [Fire D3 - SW]": AdvData(681043348160, "Raging Volcano Post-Rune"), # s shirt, r quest

    "Snakeblock [Wind C4 - E]": AdvData(6810524304128, "Frozen Spire"),
    "Snakeblock [Wind C4 - C]": AdvData(6830524176128, "Frozen Spire"),
    "Snakeblock [Wind C4 - N]": AdvData(683052412864, "Frozen Spire"),
    "Snakeblock [Wind D4]": AdvData(6830534304144, "Frozen Spire"),
    "Snakeblock [Wind B3 - SW]": AdvData(680051396176, "Frozen Spire"),
    "Snakeblock [Wind B3 - CE]": AdvData(681051325696, "Frozen Spire"), # k cloak
    "Snakeblock [Wind B3 - NE]": AdvData(686051325680, "Frozen Spire"), # k cloak
    "Snakeblock [Wind A3]": AdvData(6810503112176, "Frozen Spire"), # D quest
    "Snakeblock [Wind A2 - SW]": AdvData(6810502208192, "Frozen Spire"),
    "Snakeblock [Wind A2 - SE]": AdvData(6810502256192, "Frozen Spire"), # D quest
    "Snakeblock [Wind B2 - E]": AdvData(6800512256128, "Frozen Spire"),
    "Snakeblock [Wind B2 - SW]": AdvData(680051264192, "Frozen Spire"), # k cloak
    "Snakeblock [Wind B4]": AdvData(680051414480, "Frozen Spire"), # k cloak
    "Snakeblock [Wind B1]": AdvData(6800511304176, "Frozen Spire"),
    "Snakeblock [Wind D2 - SE]": AdvData(6800532320192, "Frozen Spire"),
    "Snakeblock [Wind D2 - SW]": AdvData(686053280144, "Frozen Spire"),
    "Snakeblock [Wind B0 - W]": AdvData(6860510176176, "Frozen Spire"),
    "Snakeblock [Wind B0 - E]": AdvData(6830510256160, "Frozen Spire"),
    "Snakeblock [Wind C0]": AdvData(68005203296, "Frozen Spire"),
    "Snakeblock [Wind E4]": AdvData(680054414464, "Frozen Spire Post-Rune"), # d quest
    "Snakeblock [Wind E3]": AdvData(68105436496, "Frozen Spire Post-Rune"), # d quest
    "Snakeblock [Wind E1]": AdvData(686054132128, "Frozen Spire Post-Rune"), # g gloves
    "Snakeblock [Wind C1]": AdvData(68605219664, "Frozen Spire"),
    "Snakeblock [Wind C2]": AdvData(683052211296, "Frozen Spire"), # d quest

    "Snakeblock [Serpent A1 - W]": AdvData(683060196192, "Serpent Stacks Post-Rune"),
    "Snakeblock [Serpent A1 - C]": AdvData(6800601176128, "Serpent Stacks Post-Rune"), #s circlet
    "Snakeblock [Serpent A1 - CE]": AdvData(6810601224160, "Serpent Stacks Post-Rune"), #s circlet
    "Snakeblock [Serpent A1 - E]": AdvData(6860601304176, "Serpent Stacks Post-Rune"), #s circlet
    "Snakeblock [Serpent A6 - SW]": AdvData(6800606144112, "Serpent Stacks Post-Rune"), #s circlet, S quest, T quest
    "Snakeblock [Serpent A6 - NW]": AdvData(686060614496, "Serpent Stacks Post-Rune"), #s circlet, S quest, T quest
    "Snakeblock [Serpent A6 - C]": AdvData(6860606176128, "Serpent Stacks Post-Rune"), #s circlet, S quest, T quest
    "Snakeblock [Serpent A6 - E]": AdvData(6860606256144, "Serpent Stacks Post-Rune"), #s circlet, S quest, T quest
    "Snakeblock [Serpent A8]": AdvData(6860608336128, "Serpent Stacks Post-Rune"), #s circlet, all quests

    "Snakeblock [Sanctum A2 - S]": AdvData(6810702176192, "Sanctum"), #all quests
    "Snakeblock [Sanctum A2 - C]": AdvData(6810702128128, "Sanctum"), #all quests
    "Snakeblock [Sanctum A2 - W]": AdvData(681070280112, "Sanctum"), #all quests
    "Snakeblock [Sanctum A0 - E]": AdvData(6810700320192, "Sanctum"), #all quests
    "Snakeblock [Sanctum A0 - CE]": AdvData(6800700176160, "Sanctum"), #all quests
    "Snakeblock [Sanctum A0 - CW]": AdvData(6860700144144, "Sanctum"), #all quests
    "Snakeblock [Sanctum A0 - W]": AdvData(686070016144, "Sanctum"), #all quests
    "Snakeblock [Sanctum C2 - E]": AdvData(6810722256128, "Sanctum"), #all quests
    "Snakeblock [Sanctum C2 - W]": AdvData(683072214496, "Sanctum"), #all quests
    "Snakeblock [Sanctum C0 - W]": AdvData(681072096192, "Sanctum"), #all quests
    "Snakeblock [Sanctum C0 - CSW]": AdvData(6810720144144, "Sanctum"), #all quests
    "Snakeblock [Sanctum C0 - CNW]": AdvData(6800720160112, "Sanctum"), #all quests
    "Snakeblock [Sanctum C0 - CN]": AdvData(681072022496, "Sanctum"), #all quests
    "Snakeblock [Sanctum C0 - E]": AdvData(6860720272176, "Sanctum"), #all quests
}

exclusion_table = {



}

events_table = {
}
