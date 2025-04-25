from Utils import visualize_regions
from worlds.generic.Rules import set_rule, add_rule
from BaseClasses import CollectionState
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import IslesOfSeaAndSkyWorld


def _isles_of_sea_and_sky_is_route(world: "IslesOfSeaAndSkyWorld", route: int):
    if route == 0:
        return world.options.route_required.current_key == "normal_ending"
    if route == 1:
        return world.options.route_required.current_key == "secret_ending"
    if route == 2:
        return world.options.route_required.current_key == "all_gems"
    return False


# Sets rules on entrances and advancements that are always applied
def set_rules(world: "IslesOfSeaAndSkyWorld"):

    player = world.player
    multiworld = world.multiworld

    ### Entrances
    set_rule(multiworld.get_entrance("Ancient West Exit", player),
             lambda state: state.can_reach("Stony West Exit", "Entrance", player))  # Obsidian Sea

    set_rule(multiworld.get_entrance("Ancient East Exit", player),
             lambda state: state.has("Ancient Key", player, 5)
             and state.has("Star Piece", player))  # Obsidian Sea


    ## Required for completion detection
    set_rule(multiworld.get_entrance("Ancient North Exit", player),
             lambda state: state.has("Topaz Quest Complete", player)
                           and state.has("Sapphire Quest Complete", player)
                           and state.has("Ruby Quest Complete", player)
                           and state.has("Diamond Quest Complete", player) ) # Sanctum

    ## Required for completion detection
    set_rule(multiworld.get_entrance("Elemental Rock Path", player),
             lambda state: state.has("Topaz Shard Hit", player)
                           and state.has("Sapphire Shard Hit", player)
                           and state.has("Ruby Shard Hit", player)
                           and state.has("Diamond Shard Hit", player) ) # Sanctum Peak


    set_rule(multiworld.get_entrance("Diamond Sea West Entrance", player),
                 lambda state: state.has("Star Piece", player, 3))  # Diamond Sea

    set_rule(multiworld.get_entrance("Stony West Exit", player),
             lambda state: (state.has("Topaz Rune Stone", player) ) )  # Stony Cliffs Post-Rune
    set_rule(multiworld.get_entrance("Stony Post-Rune East Exit", player),
             lambda state: (state.has("Topaz Rune Stone", player)))  # Stony Cliffs
    set_rule(multiworld.get_entrance("Stony Post-Rune West Exit", player),
             lambda state: (state.has("Topaz Rune Stone", player) or state.has("Phoenix Flute", player))
                           and state.has("Star Piece", player, 5)) # Sapphire Sea



    # NOTE: state.has only works with items classified as progression

    set_rule(multiworld.get_entrance("Ruby Sea West Entrance", player),
             lambda state: state.has("Star Piece", player, 15))  # Ruby Sea
             
    set_rule(multiworld.get_entrance("Diamond Sea Exit", player),
             lambda state: state.has("Star Piece", player, 30))  # North Diamond Sea
    set_rule(multiworld.get_entrance("North Diamond Sea South Exit", player),
             lambda state: state.has("Star Piece", player, 30))  # Diamond Sea
    set_rule(multiworld.get_entrance("North Diamond Sea East Exit", player),
             lambda state: state.can_reach("Lost Sea", "Region", player))  # Northeast Sea

    set_rule(multiworld.get_entrance("Serpent Entrance", player),
             lambda state: state.has("Star Piece", player, 45))  # Serpent Stacks

    set_rule(multiworld.get_entrance("Tidal Exit To Post-Rune", player),
             lambda state: (state.has("Sapphire Rune Stone", player)))  # Tidal Reef Post-Rune

    set_rule(multiworld.get_entrance("Raging Exit To Post-Rune", player),
             lambda state: (state.has("Ruby Rune Stone", player)))  # Raging Volcano Post-Rune

    set_rule(multiworld.get_entrance("Frozen Exit To Post-Rune", player),
             lambda state: (state.has("Diamond Rune Stone", player)))  # Frozen Spire Post-Rune

    set_rule(multiworld.get_entrance("Serpent Exit To Post-Rune", player),
             lambda state: (state.has("Obsidian Rune Stone", player)))  # Serpent Stacks Post-Rune

    set_rule(multiworld.get_entrance("Star West Exit", player),
             lambda state: (state.can_reach("Lost Sea", "Region", player)))  # Lost Sea

    set_rule(multiworld.get_entrance("Star East Exit", player),
             lambda state: (state.has("Ancient Rune Stone", player)))  # Lost Sea

    set_rule(multiworld.get_entrance("Star East Entrance", player),
             lambda state: state.has("Ancient Rune Stone", player)
                            and state.can_reach("Lost Sea", "Region", player) )  # Star Tropic

    set_rule(multiworld.get_entrance("Shoal Entrance", player),
             lambda state: (state.has("Ancient Rune Stone", player)))  # Shoal



    set_rule(multiworld.get_entrance("Beast Bridge Phoenix", player),
             lambda state: state.has("Phoenix Flute", player) )  # Phoenix Hub
    set_rule(multiworld.get_entrance("Stony Phoenix", player),
             lambda state: state.has("Phoenix Flute", player) and state.has("Topaz Rune Stone", player))  # Phoenix Hub
    set_rule(multiworld.get_entrance("Tidal Phoenix", player),
             lambda state: state.has("Phoenix Flute", player) and state.has("Sapphire Rune Stone", player))  # Phoenix Hub
    set_rule(multiworld.get_entrance("Raging Phoenix", player),
             lambda state: state.has("Phoenix Flute", player))  # Phoenix Hub | Doesn't need rune stone
    set_rule(multiworld.get_entrance("Frozen Phoenix", player),
             lambda state: state.has("Phoenix Flute", player) and state.has("Diamond Rune Stone", player))  # Phoenix Hub
    set_rule(multiworld.get_entrance("Lost Phoenix", player),
             lambda state: state.has("Phoenix Flute", player))  # Phoenix Hub

    set_rule(multiworld.get_entrance("Beast Bridge Phoenix Entrance", player),
             lambda state: state.has("Phoenix Flute", player))  # Beast Bridge
    set_rule(multiworld.get_entrance("Stony Phoenix Entrance", player),
             lambda state: state.has("Phoenix Flute", player))  # Stony Cliffs
    set_rule(multiworld.get_entrance("Tidal Phoenix Entrance", player),
             lambda state: state.has("Phoenix Flute", player)
                            and ( state.has("Sapphire Rune Stone", player) or state.has("Frog Flippers", player) ) )  # tidal Reef
    set_rule(multiworld.get_entrance("Raging Phoenix Entrance", player),
             lambda state: state.has("Phoenix Flute", player)
                            and ( state.has("Ruby Quest Complete", player) or state.can_reach("Raging Volcano", "Region", player) ) )  # Raging Volcano
    set_rule(multiworld.get_entrance("Frozen Phoenix Entrance", player),
             lambda state: state.has("Phoenix Flute", player)
                           and state.has("Diamond Rune Stone", player) )  # Frozen Spire
    set_rule(multiworld.get_entrance("Lost Phoenix Entrance", player),
             lambda state: state.has("Phoenix Flute", player)
                           and state.has("Star Piece", player, 30) )  # Lost Landing

    set_rule(multiworld.get_location("Star Lock 3 [Overworld]", player),
             lambda state: state.has("Star Piece", player, 3))
    set_rule(multiworld.get_location("Star Lock 15 [Overworld]", player),
             lambda state: state.has("Star Piece", player, 15))
    set_rule(multiworld.get_location("Star Lock 30 [Overworld]", player),
             lambda state: state.has("Star Piece", player, 30))
    set_rule(multiworld.get_location("Star Lock 45 [Overworld]", player),
             lambda state: state.has("Star Piece", player, 45))


    ### Locations

    # Legendary Item Locations
    set_rule(multiworld.get_location("Gopher Gloves", player),
             lambda state: state.can_reach("Stony Cliffs Post-Rune", "Region", player)
                           and state.has("Topaz Rune Stone", player)
                           and state.has("Topaz Quest Complete", player))

    set_rule(multiworld.get_location("Frog Flippers", player),
             lambda state: state.can_reach("Tidal Reef", "Region", player)
                           and state.has("Sapphire Rune Stone", player)
                           and state.has("Sapphire Quest Complete", player))

    set_rule(multiworld.get_location("Salamander Shirt", player),
             lambda state: state.can_reach("Raging Volcano", "Region", player)
                           and state.has("Ruby Rune Stone", player)
                           and state.has("Ruby Quest Complete", player)
                           and state.has("Fire Key", player, 3))

    set_rule(multiworld.get_location("Kite Cloak", player),
             lambda state: state.can_reach("Frozen Spire", "Region", player)
                           and state.has("Diamond Rune Stone", player)
                           and state.has("Diamond Quest Complete", player)) # since Eggs and Wind key are broken, don't include

    set_rule(multiworld.get_location("Serpent Circlet", player),
             lambda state: state.can_reach("Serpent Stacks", "Region", player)
                           and state.has("Topaz Rune Stone", player)
                           and state.has("Sapphire Rune Stone", player)
                           and state.has("Ruby Rune Stone", player)
                           and state.has("Diamond Rune Stone", player)
                           and state.has("Obsidian Rune Stone", player)
                           and state.has("Obsidian", player, 10))

    set_rule(multiworld.get_location("Phoenix Flute", player),
             lambda state: state.can_reach("Beast Bridge", "Region", player)
                           and state.has("Rolling Bell Rung", player)
                           and state.has("Sunken Bell Rung", player)
                           and state.has("Aggro Bell Rung", player)
                           and state.has("Nunatak Bell Rung", player))

    # Quests
    set_rule(multiworld.get_location("Topaz Quest Complete", player),
             lambda state: state.has("Topaz", player, 6))

    set_rule(multiworld.get_location("Sapphire Quest Complete", player),
             lambda state: state.has("Sapphire", player, 6))

    set_rule(multiworld.get_location("Ruby Quest Complete", player),
             lambda state: state.has("Ruby", player, 6))

    set_rule(multiworld.get_location("Diamond Quest Complete", player),
             lambda state: state.has("Diamond", player, 6))

    # Islands and their Locations
    set_ancient_isle(player, multiworld)
    set_rolling_rocks(player, multiworld)
    set_sunken_island(player, multiworld)
    set_aggro_crag(player, multiworld)
    set_sea_nunatak(player, multiworld)
    set_locked(player, multiworld)
    set_star_tropic(player, multiworld)
    set_shoal(player, multiworld)
    set_lost_landing(player, multiworld)

    set_serpent_stacks(player, multiworld)
    set_stony_cliffs(player, multiworld)
    set_tidal_reef(player, multiworld)
    set_raging_volcano(player, multiworld)
    set_frozen_spire(player, multiworld)



def set_ancient_isle(player, multiworld):
    # Collectables
    set_rule(multiworld.get_location("Star Piece [Ancient A1]", player),
             lambda state: state.can_reach("Obsidian Sea", "Region", player))

    set_rule(multiworld.get_location("Star Piece [Ancient B1]", player),
             lambda state: state.can_reach("Obsidian Sea", "Region", player)
             and state.has("Ancient Rune Stone", player))

    set_rule(multiworld.get_location("Ancient Key [Ancient A2 - NW]", player),
             lambda state: state.has("Topaz Quest Complete", player))


    # Locksanity

    set_rule(multiworld.get_location("3x Lock [Ancient A1]", player),
             lambda state: state.can_reach("Obsidian Sea", "Region", player))

    set_rule(multiworld.get_location("Star Lock 1 [Ancient C1]", player),
             lambda state: state.has("Star Piece", player))

    set_rule(multiworld.get_location("Ancient Rune Lock [Ancient B1]", player),
             lambda state: state.has("Ancient Rune Stone", player))

def set_rolling_rocks(player, multiworld):

    set_rule(multiworld.get_location("Topaz [Rolling A0]", player),
             lambda state: state.has("Star Piece", player, 7)
             and state.has("Topaz Quest Complete", player))

    set_rule(multiworld.get_location("Obsidian [Rolling A1]", player),
             lambda state: state.has("Star Piece", player, 7)
                           and state.has("Gopher Gloves", player))

    set_rule(multiworld.get_location("Obsidian [Rolling A1]", player),
             lambda state: state.has("Star Piece", player, 7)
             and (state.has("Topaz Quest complete", player)
                or state.has("Frog Flippers", player) ) )

    set_rule(multiworld.get_location("Rolling Bell Rung", player),
             lambda state: state.has("Ancient Rune Stone", player))

    set_rule(multiworld.get_location("Star Piece [Rolling B1]", player),
             lambda state: state.has("Ancient Rune Stone", player))

    set_rule(multiworld.get_location("Star Piece [Rolling B0]", player),
             lambda state: state.has("Ancient Rune Stone", player)
             and state.has("Gopher Gloves", player))


    # Locksanity

    set_rule(multiworld.get_location("3x Lock [Rolling B1]", player),
             lambda state: state.has("Ancient Rune Stone", player))

    set_rule(multiworld.get_location("Star Lock 7 [Rolling A0]", player),
             lambda state: state.has("Star Piece", player, 7))

    set_rule(multiworld.get_location("Ancient Rune Lock [Rolling A1]", player),
             lambda state: state.has("Ancient Rune Stone", player))

    set_rule(multiworld.get_location("Ancient Rune Lock [Rolling B0]", player),
             lambda state: state.has("Ancient Rune Stone", player))

def set_sunken_island(player, multiworld):

    set_rule(multiworld.get_location("Sunken Bell Rung", player),
             lambda state: state.has("Ancient Rune Stone", player))

    set_rule(multiworld.get_location("Sapphire [Sunken B0]", player),
             lambda state: state.has("Star Piece", player, 21)
             and state.has("Sapphire Quest Complete", player))

    set_rule(multiworld.get_location("Star Piece [Sunken B0]", player),
             lambda state: state.has("Star Piece", player, 21)
                           and state.has("Sapphire Quest Complete", player))

    set_rule(multiworld.get_location("Star Piece [Sunken A1]", player),
             lambda state: state.has("Ancient Rune Stone", player) )

    set_rule(multiworld.get_location("Obsidian [Sunken A0]", player),
             lambda state: state.has("Ancient Rune Stone", player)
                           and state.has("Frog Flippers", player))

    # Locksanity

    set_rule(multiworld.get_location("Star Lock 21 [Sunken B0]", player),
             lambda state: state.has("Star Piece", player, 21))

    set_rule(multiworld.get_location("Ancient Rune Lock [Rolling A1]", player),
             lambda state: state.has("Ancient Rune Stone", player))

    set_rule(multiworld.get_location("Ancient Rune Lock [Rolling B0]", player),
             lambda state: state.has("Ancient Rune Stone", player))

def set_aggro_crag(player, multiworld):

    set_rule(multiworld.get_location("Aggro Bell Rung", player),
             lambda state: state.has("Ancient Rune Stone", player))

    set_rule(multiworld.get_location("Ruby [Aggro B1]", player),
             lambda state: state.has("Star Piece", player, 35)
             and state.has("Ruby Quest Complete", player) )

    set_rule(multiworld.get_location("Star Piece [Aggro B1]", player),
             lambda state: state.has("Star Piece", player, 35)
                           and state.has("Ruby Quest Complete", player))

    set_rule(multiworld.get_location("Obsidian [Aggro B0]", player),
             lambda state: state.has("Ancient Rune Stone", player)
                            and state.has("Star Piece", player, 35)
                            and state.has("Ruby Quest Complete", player)
                            and state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Star Piece [Aggro A1]", player),
             lambda state: state.has("Star Piece", player, 35)
                           and state.has("Ruby Quest Complete", player)
                           and state.has("Ancient Rune Stone", player))

    # Locksanity

    set_rule(multiworld.get_location("3x Lock [Aggro A1]", player),
             lambda state: state.has("Star Piece", player, 35)
                           and state.has("Ruby Quest Complete", player)
                           and state.has("Ancient Rune Stone", player))

    set_rule(multiworld.get_location("Star Lock 35 [Aggro B0]", player),
             lambda state: state.has("Star Piece", player, 35))

    set_rule(multiworld.get_location("Ancient Rune Lock [Aggro B1]", player),
             lambda state: state.has("Star Piece", player, 35)
                           and state.has("Ruby Quest Complete", player)
                           and state.has("Ancient Rune Stone", player))

    set_rule(multiworld.get_location("3x Lock [Aggro A1]", player),
             lambda state: state.has("Ancient Rune Stone", player))

def set_sea_nunatak(player, multiworld):

    set_rule(multiworld.get_location("Nunatak Bell Rung", player),
             lambda state: state.has("Ancient Rune Stone", player))

    set_rule(multiworld.get_location("Ancient Key [Nunatak A1]", player),
             lambda state: state.has("Ancient Rune Stone", player)
             and state.has("Diamond Quest Complete", player)
             and state.has("Star Piece", player, 49))

    set_rule(multiworld.get_location("Diamond [Nunatak B0]", player),
             lambda state: state.has("Diamond Quest Complete", player)
                           and state.has("Star Piece", player, 49))

    set_rule(multiworld.get_location("Star Piece [Nunatak B0]", player),
             lambda state: state.has("Diamond Quest Complete", player)
                           and state.has("Star Piece", player, 49))

    set_rule(multiworld.get_location("Star Piece [Nunatak B0]", player),
             lambda state: state.has("Diamond Quest Complete", player)
                           and state.has("Star Piece", player, 49))

    set_rule(multiworld.get_location("Star Piece [Nunatak A0]", player),
             lambda state: state.has("Ancient Rune Stone", player) )

    set_rule(multiworld.get_location("Obsidian [Nunatak B1]", player),
             lambda state: state.has("Diamond Quest Complete", player)
                           and state.has("Star Piece", player, 49)
                           and state.has("Kite Cloak", player) )

    # Locksanity

    set_rule(multiworld.get_location("3x Lock [Nunatak B1]", player),
             lambda state: state.has("Ancient Rune Stone", player))

    set_rule(multiworld.get_location("Ancient Rune Lock [Nunatak B0]", player),
             lambda state: state.has("Ancient Rune Stone", player))

    set_rule(multiworld.get_location("Star Lock 49 [Nunatak B0]", player),
             lambda state: state.has("Star Piece", player, 49))

def set_locked(player, multiworld):

    set_rule(multiworld.get_location("Ancient Rune Stone", player),
             lambda state: state.has("Ancient Key", player, 18))  # double check key amount

    set_rule(multiworld.get_location("Star Piece [Locked A1]", player),
             lambda state: state.has("Ancient Rune Stone", player)
             and state.has("Ancient Key", player, 18) ) # double check

    # Locksanity

    set_rule(multiworld.get_location("Ancient Rune Lock [Locked A1]", player),
             lambda state: state.has("Ancient Rune Stone", player)
             and state.has("Ancient Key", player, 18) ) # double check


def set_star_tropic(player, multiworld):

    set_rule(multiworld.get_location("Ancient Key [Tropic A1]", player),
             lambda state: state.has("Ancient Rune Stone", player))

    set_rule(multiworld.get_location("Topaz [Tropic A1]", player),
             lambda state: state.has("Ancient Rune Stone", player)
                           and state.has("Gopher Gloves", player)
                         and state.has("Frog Flippers", player)
                         and state.has("Salamander Shirt", player)
                         and state.has("Kite Cloak", player))

    set_rule(multiworld.get_location("Sapphire [Tropic A1]", player),
             lambda state: state.has("Ancient Rune Stone", player)
                           and state.has("Gopher Gloves", player)
                           and state.has("Frog Flippers", player)
                           and state.has("Salamander Shirt", player)
                           and state.has("Kite Cloak", player))

    set_rule(multiworld.get_location("Ruby [Tropic A1]", player),
             lambda state: state.has("Ancient Rune Stone", player)
                           and state.has("Gopher Gloves", player)
                           and state.has("Frog Flippers", player)
                           and state.has("Salamander Shirt", player)
                           and state.has("Kite Cloak", player))

    set_rule(multiworld.get_location("Diamond [Tropic A1]", player),
             lambda state: state.has("Ancient Rune Stone", player)
                           and state.has("Gopher Gloves", player)
                           and state.has("Frog Flippers", player)
                           and state.has("Salamander Shirt", player)
                           and state.has("Kite Cloak", player))

    set_rule(multiworld.get_location("Star Piece [Topic A1 - 1]", player),
             lambda state: state.has("Ancient Rune Stone", player)
                           and state.has("Gopher Gloves", player))

    set_rule(multiworld.get_location("Star Piece [Topic A1 - 2]", player),
             lambda state: state.has("Ancient Rune Stone", player)
                           and state.has("Gopher Gloves", player)
                           and state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Star Piece [Topic A1 - 3]", player),
             lambda state: state.has("Ancient Rune Stone", player)
                           and state.has("Gopher Gloves", player)
                           and state.has("Frog Flippers", player)
                           and state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Star Piece [Topic A1 - 4]", player),
             lambda state: state.has("Ancient Rune Stone", player)
                           and state.has("Gopher Gloves", player)
                           and state.has("Frog Flippers", player)
                           and state.has("Salamander Shirt", player)
                           and state.has("Kite Cloak", player))

    set_rule(multiworld.get_location("Star Piece [Tropic B0 - E]", player),
                 lambda state: state.has("Ancient Rune Stone", player)
                               or state.can_reach("Lost Sea", "Region", player) )

    set_rule(multiworld.get_location("Star Piece [Tropic B0 - N]", player),
             lambda state: state.has("Obsidian Rune Stone", player)
                       and state.has("Kite Cloak", player))


    # Locksanity

    set_rule(multiworld.get_location("Ancient Rune Lock [Tropic A1]", player),
             lambda state: state.has("Ancient Rune Stone", player) )

    set_rule(multiworld.get_location("Ancient Rune Lock [Tropic B0]", player),
             lambda state: state.has("Ancient Rune Stone", player))

    set_rule(multiworld.get_location("Obsidian Rune Lock [Tropic B0]", player),
             lambda state: state.has("Obsidian Rune Stone", player)
                       and state.has("Kite Cloak", player))



    # Sets rules on completion condition


def set_shoal(player, multiworld):

    set_rule(multiworld.get_location("Star Viewing Orb", player),
             lambda state: state.has("Ancient Rune Stone", player))

    set_rule(multiworld.get_location("Star Piece [Shoal A0]", player),
             lambda state: state.has("Ancient Rune Stone", player)
                         and state.has("Frog Flippers", player)
                         and state.has("Kite Cloak", player))

    # Locksanity

    set_rule(multiworld.get_location("Ancient Rune Lock [Shoal A0]", player),
             lambda state: state.has("Ancient Rune Stone", player))


def set_lost_landing(player, multiworld):

    set_rule(multiworld.get_location("Obsidian [Lost A1]", player),
             lambda state: state.has("Star Piece", player, 30)
                           and state.has("Frog Flippers", player))

    set_rule(multiworld.get_location("Star Piece [Lost B1]", player),
             lambda state: state.has("Star Piece", player, 30) )

    # Locksanity
    set_rule(multiworld.get_location("Lock [Lost B1]", player),
             lambda state: state.has("Star Piece", player, 30)
                           and state.has("Frog Flippers", player))

    set_rule(multiworld.get_location("Star Lock 30 [Lost A0]", player),
             lambda state: state.has("Star Piece", player, 30))

def set_serpent_stacks(player, multiworld):

    set_rule(multiworld.get_location("Obsidian Rune Stone", player),
             lambda state: state.has("Topaz Rune Stone", player)
                         and state.has("Sapphire Rune Stone", player)
                         and state.has("Ruby Rune Stone", player)
                         and state.has("Diamond Rune Stone", player))

    set_rule(multiworld.get_location("Obsidian [Serpent A1]", player),
             lambda state: state.has("Topaz Rune Stone", player)
                           and state.has("Sapphire Rune Stone", player)
                           and state.has("Ruby Rune Stone", player)
                           and state.has("Diamond Rune Stone", player))

    set_rule(multiworld.get_location("Star Piece [Serpent A1 - W]", player),
             lambda state: state.has("Serpent Circlet", player)
                           and state.has("Topaz Rune Stone", player)
                           and state.has("Sapphire Rune Stone", player)
                           and state.has("Ruby Rune Stone", player)
                           and state.has("Diamond Rune Stone", player))

    set_rule(multiworld.get_location("Star Piece [Serpent A1 - N]", player),
             lambda state: state.has("Serpent Circlet", player)
                           and state.has("Topaz Rune Stone", player)
                           and state.has("Sapphire Rune Stone", player)
                           and state.has("Ruby Rune Stone", player)
                           and state.has("Diamond Rune Stone", player))

    set_rule(multiworld.get_location("Star Piece [Serpent A2]", player),
             lambda state: state.has("Serpent Circlet", player) )

    set_rule(multiworld.get_location("Star Piece [Serpent A3]", player),
             lambda state: state.has("Kite Cloak", player))

    set_rule(multiworld.get_location("Star Piece [Serpent A4]", player),
             lambda state: state.has("Serpent Circlet", player)
                           and state.has("Topaz Quest Complete", player))

    set_rule(multiworld.get_location("Star Piece [Serpent A6 - W]", player),
             lambda state: state.has("Serpent Circlet", player)
                           and state.has("Topaz Quest Complete", player)
                           and state.has("Sapphire Quest Complete", player))

    set_rule(multiworld.get_location("Star Piece [Serpent A6 - E]", player),
             lambda state: state.has("Serpent Circlet", player)
                           and state.has("Topaz Quest Complete", player)
                           and state.has("Sapphire Quest Complete", player))

    set_rule(multiworld.get_location("Star Piece [Serpent A7 - W]", player),
             lambda state: state.has("Serpent Circlet", player)
                           and state.has("Topaz Quest Complete", player)
                           and state.has("Sapphire Quest Complete", player)
                           and state.has("Ruby Quest Complete", player))

    set_rule(multiworld.get_location("Star Piece [Serpent A7 - E]", player),
             lambda state: state.has("Serpent Circlet", player)
                           and state.has("Topaz Quest Complete", player)
                           and state.has("Sapphire Quest Complete", player)
                           and state.has("Ruby Quest Complete", player))

    set_rule(multiworld.get_location("Star Piece [Serpent A8 - N]", player),
             lambda state: state.has("Serpent Circlet", player)
                           and state.has("Topaz Quest Complete", player)
                           and state.has("Sapphire Quest Complete", player)
                           and state.has("Ruby Quest Complete", player)
                           and state.has("Diamond Quest Complete", player))

    set_rule(multiworld.get_location("Star Piece [Serpent A8 - S]", player),
             lambda state: state.has("Serpent Circlet", player)
                           and state.has("Topaz Quest Complete", player)
                           and state.has("Sapphire Quest Complete", player)
                           and state.has("Ruby Quest Complete", player)
                           and state.has("Diamond Quest Complete", player))

    # Locksanity

    set_rule(multiworld.get_location("Elemental Rune Lock [Serpent A2]", player),
             lambda state: state.has("Topaz Rune Stone", player)
                           and state.has("Sapphire Rune Stone", player)
                           and state.has("Ruby Rune Stone", player)
                           and state.has("Diamond Rune Stone", player))

    set_rule(multiworld.get_location("Obsidian Rune Lock [Serpent A1 - N]", player),
             lambda state: state.has("Topaz Rune Stone", player)
                           and state.has("Sapphire Rune Stone", player)
                           and state.has("Ruby Rune Stone", player)
                           and state.has("Diamond Rune Stone", player))

    set_rule(multiworld.get_location("Obsidian Rune Lock [Serpent A1 - W]", player),
             lambda state: state.has("Topaz Rune Stone", player)
                           and state.has("Sapphire Rune Stone", player)
                           and state.has("Ruby Rune Stone", player)
                           and state.has("Diamond Rune Stone", player))

    set_rule(multiworld.get_location("Obsidian Rune Lock [Serpent A1 - E]", player),
             lambda state: state.has("Topaz Rune Stone", player)
                           and state.has("Sapphire Rune Stone", player)
                           and state.has("Ruby Rune Stone", player)
                           and state.has("Diamond Rune Stone", player)
                           and state.has("Serpent Circlet", player))

def set_stony_cliffs(player, multiworld):

    set_rule(multiworld.get_location("Gold Stone Tablet", player),
             lambda state: state.has("Topaz Rune Stone", player)
                         and state.has("Star Piece", player, 20))

    set_rule(multiworld.get_location("Blue Stone Tablet", player),
             lambda state: state.has("Topaz Rune Stone", player)
                           and state.has("Star Piece", player, 20))

    set_rule(multiworld.get_location("Ancient Key [Stone C0]", player),
             lambda state: state.has("Topaz Quest Complete", player))

    set_rule(multiworld.get_location("Ancient Key [Stone B4]", player),
             lambda state: state.has("Topaz Quest Complete", player)
                           and state.has("Gopher Gloves", player)
                           and state.has("Star Piece", player, 15))

    set_rule(multiworld.get_location("Ancient Key [StoneDungeon C1]", player),
             lambda state: state.has("Gopher Gloves", player))

    set_rule(multiworld.get_location("Ancient Key [StoneDungeon D0]", player),
             lambda state: state.has("Gopher Gloves", player))

    set_rule(multiworld.get_location("Ancient Key [StoneDungeon B1]", player),
             lambda state: state.has("Gopher Gloves", player))

    set_rule(multiworld.get_location("Ancient Key [Stone B0 - NW1]", player),
             lambda state: state.has("Topaz Quest Complete", player))
    set_rule(multiworld.get_location("Ancient Key [Stone B0 - NW2]", player),
             lambda state: state.has("Topaz Quest Complete", player))
    set_rule(multiworld.get_location("Ancient Key [Stone B0 - NW3]", player),
             lambda state: state.has("Topaz Quest Complete", player))

    set_rule(multiworld.get_location("Ancient Key [Stone A2]", player),
             lambda state: state.has("Blue Stone Tablet", player) and state.has("Gold Stone Tablet", player))

    set_rule(multiworld.get_location("Ancient Key [StoneDungeon D2]", player),
             lambda state: state.has("Topaz Quest Complete", player))

    set_rule(multiworld.get_location("Topaz [Stone B2]", player),
             lambda state: state.has("Topaz Quest Complete", player))

    set_rule(multiworld.get_location("Topaz [Stone B2]", player),
             lambda state: state.has("Topaz Quest Complete", player))

    set_rule(multiworld.get_location("Topaz [StoneDungeon C1]", player),
             lambda state: state.has("Gopher Gloves", player))

    set_rule(multiworld.get_location("Obsidian [Stone A2]", player),
             lambda state: state.has("Blue Stone Tablet", player) and state.has("Gold Stone Tablet", player))

    set_rule(multiworld.get_location("Star Piece [Stone C1]", player),
             lambda state: state.has("Topaz Quest Complete", player))

    set_rule(multiworld.get_location("Star Piece [Stone B2]", player),
             lambda state: state.has("Topaz Quest Complete", player))

    set_rule(multiworld.get_location("Star Piece [Stone B4]", player),
             lambda state: state.has("Topaz Quest Complete", player)
                           and state.has("Gopher Gloves", player)
                           and state.has("Star Piece", player, 15))

    set_rule(multiworld.get_location("Star Piece [Stone C4]", player),
             lambda state: state.has("Topaz Quest Complete", player)
                           and state.has("Gopher Gloves", player)
                           and state.has("Star Piece", player, 15))

    set_rule(multiworld.get_location("Star Piece [Stone C0]", player),
             lambda state: state.has("Topaz Quest Complete", player))

    set_rule(multiworld.get_location("Star Piece [StoneDungeon E1]", player),
             lambda state: state.has("Topaz Quest Complete", player))

    set_rule(multiworld.get_location("Star Piece [StoneDungeon E2]", player),
             lambda state: state.has("Topaz Quest Complete", player)
                           and state.has("Gopher Gloves", player)
                           and state.has("Frog Flippers", player))

    set_rule(multiworld.get_location("Star Piece [StoneDungeon C3]", player),
                 lambda state: state.has("Topaz Quest Complete", player))

    set_rule(multiworld.get_location("Star Piece [StoneDungeon C1]", player),
             lambda state: state.has("Gopher Gloves", player)
                           and (state.has("Topaz Quest Complete", player) or state.has("Phoenix Flute", player) ) )

    set_rule(multiworld.get_location("Star Piece [StoneDungeon B1]", player),
             lambda state: state.has("Gopher Gloves", player))

    set_rule(multiworld.get_location("Star Piece [Stone A1]", player),
             lambda state: state.has("Star Piece", player, 5))

    set_rule(multiworld.get_location("Stone Music Note [B2]", player),
             lambda state: state.has("Topaz Quest Complete", player))

    set_rule(multiworld.get_location("Stone Music Note [D1]", player),
             lambda state: state.has("Topaz Quest Complete", player))

    set_rule(multiworld.get_location("Star Lock 5 [Stone A1]", player),
             lambda state: state.has("Star Piece", player, 5))

    set_rule(multiworld.get_location("Star Lock 15 [Stone C4]", player),
             lambda state: state.has("Star Piece", player, 15)
                           and state.has("Topaz Quest Complete", player) )

    set_rule(multiworld.get_location("Star Lock 20 [Stone E3]", player),
             lambda state: state.has("Star Piece", player, 20))

    set_rule(multiworld.get_location("Star Lock 20 [StoneDungeon A2]", player),
             lambda state: state.has("Star Piece", player, 20)
                           and state.has("Gopher Gloves", player))


def set_tidal_reef(player, multiworld):

    set_rule(multiworld.get_location("Ancient Key [Water A0 - S]", player),
             lambda state: state.has("Frog Flippers", player))

    set_rule(multiworld.get_location("Ancient Key [Water A2]", player),
             lambda state: state.has("Frog Flippers", player)
                           and state.has("Sapphire Quest Complete", player))

    set_rule(multiworld.get_location("Ancient Key [Water B3]", player),
             lambda state: state.has("Frog Flippers", player))

    set_rule(multiworld.get_location("Ancient Key [Water C3 - NE1]", player),
             lambda state: state.has("Frog Flippers", player))
    set_rule(multiworld.get_location("Ancient Key [Water C3 - NE2]", player),
             lambda state: state.has("Frog Flippers", player))
    set_rule(multiworld.get_location("Ancient Key [Water C3 - NE3]", player),
             lambda state: state.has("Frog Flippers", player))

    set_rule(multiworld.get_location("Ancient Key [Water D1]", player),
             lambda state: state.has("Frog Flippers", player))

    set_rule(multiworld.get_location("Ancient Key [Water D0]", player),
             lambda state: state.has("Frog Flippers", player))

    set_rule(multiworld.get_location("Ancient Key [Water C0]", player),
             lambda state: state.has("Sapphire Quest Complete", player))

    set_rule(multiworld.get_location("Ancient Key [Water D2]", player),
             lambda state: state.has("Frog Flippers", player))

    set_rule(multiworld.get_location("Sapphire [Water C2 - N]", player),
             lambda state: state.has("Sapphire Quest Complete", player))

    set_rule(multiworld.get_location("Sapphire [Water A1]", player),
             lambda state: state.has("Frog Flippers", player))

    set_rule(multiworld.get_location("Obsidian [Water D0]", player),
             lambda state: state.has("Frog Flippers", player))

    set_rule(multiworld.get_location("Star Piece [Water C0]", player),
             lambda state: state.has("Sapphire Quest Complete", player))

    set_rule(multiworld.get_location("Star Piece [Water C2]", player),
             lambda state: state.has("Sapphire Quest Complete", player)
             or (state.has("Frog Flippers", player) and state.has("Sapphire Quest Complete", player) ) )

    set_rule(multiworld.get_location("Star Piece [Water D2]", player),
             lambda state: state.has("Frog Flippers", player)
                           and state.has("Kite Cloak", player) )

    set_rule(multiworld.get_location("Star Piece [Water D3]", player),
             lambda state: state.has("Frog Flippers", player))

    set_rule(multiworld.get_location("Star Piece [Water E0 - W]", player),
             lambda state: state.has("Sapphire Quest Complete", player) )

    set_rule(multiworld.get_location("Star Piece [Water E0 - E]", player),
             lambda state: state.has("Frog Flippers", player))

    set_rule(multiworld.get_location("Star Piece [Water B1]", player),
             lambda state: state.has("Sapphire Quest Complete", player)
             and state.has("Frog Flippers", player) )

    set_rule(multiworld.get_location("Star Piece [Water A2 - N]", player),
             lambda state: state.has("Sapphire Quest Complete", player)
                           and state.has("Frog Flippers", player)
                           and state.has("Star Piece", player, 30))

    set_rule(multiworld.get_location("Star Piece [Water A2 - S]", player),
             lambda state: state.has("Sapphire Quest Complete", player)
                           and state.has("Frog Flippers", player)
                           and state.has("Star Piece", player, 30))

    set_rule(multiworld.get_location("Star Piece [Water A4]", player),
             lambda state: state.has("Frog Flippers", player) )

    # IncludeShells

    set_rule(multiworld.get_location("Shell [Water B2]", player),
             lambda state: state.has("Frog Flippers", player))

    set_rule(multiworld.get_location("Shell [Water B0]", player),
             lambda state: state.has("Sapphire Quest Complete", player))

    set_rule(multiworld.get_location("Shell [Water D1]", player),
             lambda state: state.has("Frog Flippers", player))

    set_rule(multiworld.get_location("Shell [Water A4]", player),
             lambda state: state.has("Frog Flippers", player))

    set_rule(multiworld.get_location("Shell [Water D0]", player),
             lambda state: state.has("Frog Flippers", player))

    set_rule(multiworld.get_location("Shell [Water A2]", player),
             lambda state: state.has("Frog Flippers", player))

    # Locksanity

    set_rule(multiworld.get_location("Star Lock 30 [Water A2]", player),
             lambda state: state.has("Frog Flippers", player) and state.has("Sapphire Quest Complete", player))

def set_raging_volcano(player, multiworld):

    set_rule(multiworld.get_location("Ancient Key [Fire A2 - S]", player),
             lambda state: state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Ancient Key [Fire B4]", player),
             lambda state: state.has("Ruby Quest Complete", player))

    set_rule(multiworld.get_location("Ancient Key [Fire A1 - NE]", player),
             lambda state: state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Ancient Key [Fire B1 - N1]", player),
             lambda state: state.has("Ruby Quest Complete", player) and state.has("Salamander Shirt", player))
    set_rule(multiworld.get_location("Ancient Key [Fire B1 - N2]", player),
             lambda state: state.has("Ruby Quest Complete", player) and state.has("Salamander Shirt", player))
    set_rule(multiworld.get_location("Ancient Key [Fire B1 - N3]", player),
             lambda state: state.has("Ruby Quest Complete", player) and state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Ancient Key [Fire C1 - NE]", player),
             lambda state: state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Ancient Key [Fire C0]", player),
             lambda state: state.has("Ruby Quest Complete", player))

    set_rule(multiworld.get_location("Ancient Key [Fire C1 - SW]", player),
             lambda state: state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Ancient Key [Fire C3]", player),
             lambda state: state.has("Ruby Quest Complete", player))

    set_rule(multiworld.get_location("Ancient Key [Fire D4]", player),
             lambda state: state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Ruby [Fire D0]", player),
             lambda state: state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Obsidian [Fire E0]", player),
             lambda state: state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Star Piece [Fire B4]", player),
             lambda state: state.has("Ruby Quest Complete", player))

    set_rule(multiworld.get_location("Star Piece [Fire D1 - N]", player),
             lambda state: state.has("Ruby Quest Complete", player))

    set_rule(multiworld.get_location("Star Piece [Fire D3 - S]", player),
             lambda state: state.has("Ruby Quest Complete", player))

    set_rule(multiworld.get_location("Star Piece [Fire D3 - W]", player),
             lambda state: state.has("Ruby Quest Complete", player))

    set_rule(multiworld.get_location("Star Piece [Fire D4]", player),
             lambda state: state.has("Frog Flippers", player))

    set_rule(multiworld.get_location("Star Piece [Fire E1 - E]", player),
             lambda state: state.has("Ruby Quest Complete", player) and state.has("Salamander Shirt", player) )

    set_rule(multiworld.get_location("Star Piece [Fire E1 - W]", player),
             lambda state: state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Star Piece [Fire E0]", player),
             lambda state: state.has("Salamander Shirt", player) )

    set_rule(multiworld.get_location("Fire Music Note [D3]", player),
             lambda state: state.has("Salamander Shirt", player))


    # Locksanity

    set_rule(multiworld.get_location("Ruby Rune Lock [Fire A1 - E]", player),
             lambda state: state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Ruby Rune Lock [Fire B2 - N]", player),
             lambda state: state.has("Salamander Shirt", player))

def set_frozen_spire(player, multiworld):

    set_rule(multiworld.get_location("Ancient Key [Wind D4 - NW1]", player),
             lambda state: state.has("Diamond Quest Complete", player))
    set_rule(multiworld.get_location("Ancient Key [Wind D4 - NW2]", player),
             lambda state: state.has("Diamond Quest Complete", player))
    set_rule(multiworld.get_location("Ancient Key [Wind D4 - NW3]", player),
             lambda state: state.has("Diamond Quest Complete", player))

    set_rule(multiworld.get_location("Ancient Key [Wind D3]", player),
             lambda state: state.has("Kite Cloak", player))

    set_rule(multiworld.get_location("Ancient Key [Wind A3]", player),
             lambda state: state.has("Kite Cloak", player))

    set_rule(multiworld.get_location("Ancient Key [Wind C2]", player),
             lambda state: state.has("Diamond Quest Complete", player))

    set_rule(multiworld.get_location("Ancient Key [Wind E2 - NE]", player),
             lambda state: state.has("Diamond Quest Complete", player))

    set_rule(multiworld.get_location("Ancient Key [Wind E2 - S]", player),
             lambda state: state.has("Diamond Quest Complete", player))

    set_rule(multiworld.get_location("Ancient Key [Wind E4 - SW]", player),
             lambda state: state.has("Diamond Quest Complete", player) and state.has("Kite Cloak", player))

    set_rule(multiworld.get_location("Diamond [Wind C3]", player),
             lambda state: state.has("Diamond Quest Complete", player))

    set_rule(multiworld.get_location("Star Piece [Wind B3]", player),
             lambda state: state.has("Kite Cloak", player))

    set_rule(multiworld.get_location("Star Piece [Wind A3]", player),
             lambda state: state.has("Kite Cloak", player))

    set_rule(multiworld.get_location("Star Piece [Wind B2 - N]", player),
             lambda state: state.has("Kite Cloak", player))

    set_rule(multiworld.get_location("Star Piece [Wind C2]", player),
             lambda state: state.has("Diamond Quest Complete", player))

    set_rule(multiworld.get_location("Star Piece [Wind D2]", player),
             lambda state: state.has("Kite Cloak", player))

    set_rule(multiworld.get_location("Star Piece [Wind E2]", player),
             lambda state: state.has("Diamond Quest Complete", player))

    set_rule(multiworld.get_location("Star Piece [Wind E4]", player),
             lambda state: state.has("Kite Cloak", player))

    set_rule(multiworld.get_location("Star Piece [Wind E1]", player),
             lambda state: state.has("Kite Cloak", player) and state.has("Gopher Gloves", player))

    set_rule(multiworld.get_location("Star Piece [Wind A0]", player),
             lambda state: state.has("Kite Cloak", player))

    set_rule(multiworld.get_location("Wind Music Note [A2]", player),
             lambda state: state.has("Diamond Quest Complete", player))

    set_rule(multiworld.get_location("Wind Music Note [D3]", player),
             lambda state: state.has("Diamond Quest Complete", player))



def set_completion_rules(world: "IslesOfSeaAndSkyWorld"):
    player = world.player
    multiworld = world.multiworld

    # Normal Ending
    if _isles_of_sea_and_sky_is_route(world, 0):
        multiworld.completion_condition[player] = lambda state: state.can_reach("Sanctum Peak", "Region", player)
    # Secret Ending
    elif _isles_of_sea_and_sky_is_route(world, 1):
        multiworld.completion_condition[player] = lambda state: state.can_reach("Sanctum Peak", "Region", player) and state.has("Star Piece", player, 91)

    # All Gems
    elif _isles_of_sea_and_sky_is_route(world, 2):
        multiworld.completion_condition[player] = lambda state: (state.has("Topaz", player, 12)
                                                                 and state.has("Sapphire", player, 12)
                                                                 and state.has("Ruby", player, 12)
                                                                 and state.has("Diamond", player, 12)
                                                                 and state.has("Obsidian", player, 12))

