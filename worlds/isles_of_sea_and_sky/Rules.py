from worlds.generic.Rules import set_rule, add_rule
from BaseClasses import CollectionState
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import IslesOfSeaAndSkyWorld


def _isles_of_sea_and_sky_is_route(world: "IslesOfSeaAndSkyWorld", route: int):
    if route == 3:
        return world.options.route_required.current_key == "all_routes"
    if world.options.route_required.current_key == "all_routes":
        return True
    if route == 0:
        return world.options.route_required.current_key == "neutral"
    if route == 1:
        return world.options.route_required.current_key == "pacifist"
    if route == 2:
        return world.options.route_required.current_key == "genocide"
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
             lambda state: (state.has("Topaz Rune Stone", player) or state.has("Phoenix Flute", player))
                           and state.has("Star Piece", player, 5)) # Sapphire Sea

    # NOTE: state.has only works with items classified as progression

    set_rule(multiworld.get_entrance("Ruby Sea West Entrance", player),
             lambda state: state.has("Star Piece", player, 15))  # Ruby Sea
             
    set_rule(multiworld.get_entrance("Diamond Sea Exit", player),
             lambda state: state.has("Star Piece", player, 30))  # North Diamond Sea

    set_rule(multiworld.get_entrance("Serpent Entrance", player),
             lambda state: state.has("Star Piece", player, 45))  # Serpent Stacks

    set_rule(multiworld.get_entrance("Beast Bridge Phoenix", player),
             lambda state: state.has("Phoenix Flute", player))  # Phoenix Hub
    set_rule(multiworld.get_entrance("Stony Phoenix", player),
             lambda state: state.has("Phoenix Flute", player))  # Phoenix Hub
    set_rule(multiworld.get_entrance("Tidal Phoenix", player),
             lambda state: state.has("Phoenix Flute", player))  # Phoenix Hub
    set_rule(multiworld.get_entrance("Raging Phoenix", player),
             lambda state: state.has("Phoenix Flute", player))  # Phoenix Hub
    set_rule(multiworld.get_entrance("Frozen Phoenix", player),
             lambda state: state.has("Phoenix Flute", player))  # Phoenix Hub
    set_rule(multiworld.get_entrance("Lost Phoenix", player),
             lambda state: state.has("Phoenix Flute", player))  # Phoenix Hub

    ### Locations

    # Legendary Item Locations
    set_rule(multiworld.get_location("Gopher Gloves", player),
             lambda state: state.can_reach("Stony Cliffs", "Region", player)
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



# Sets rules on completion condition
def set_completion_rules(world: "IslesOfSeaAndSkyWorld"):
    player = world.player
    multiworld = world.multiworld
    multiworld.completion_condition[player] = lambda state: state.can_reach("Sanctum Peak", "Region", player)
    # NOTE: This will need to have its own location check. As it stands, a player can get all quests, and shard hits, and that counts as a win.

