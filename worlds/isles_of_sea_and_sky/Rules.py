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

    ### Regions



    ### Entrances
    '''set_rule(multiworld.get_entrance("Ancient East Exit", player),
             lambda state: state.has("Star Piece", player)
                           and state.has("Ancient Key", player, 3))  # Topaz Sea
                           '''


    ## Required for completion detection
    set_rule(multiworld.get_entrance("Ancient North Exit", player),
             lambda state: state.has("Topaz Quest Complete", player)
                           and state.has("Sapphire Quest Complete", player)
                           and state.has("Ruby Quest Complete", player)
                           and state.has("Diamond Quest Complete", player) ) # Sanctum

    ## This one too
    set_rule(multiworld.get_entrance("Elemental Rock Path", player),
             lambda state: state.has("Topaz Shard Hit", player)
                           and state.has("Sapphire Shard Hit", player)
                           and state.has("Ruby Shard Hit", player)
                           and state.has("Diamond Shard Hit", player) ) # Sanctum Peak
    '''
    set_rule(multiworld.get_entrance("Stony West Exit", player),
             lambda state: state.has("Topaz Rune Stone", player)
                           and state.has("Star Piece", player, 5)) # Sapphire Sea

    set_rule(multiworld.get_entrance("Ruby Sea West Entrance", player),
             lambda state: state.has("Star Piece", player, 15))  # Ruby Sea

    set_rule(multiworld.get_entrance("Diamond Sea West Entrance", player),
             lambda state: state.has("Star Piece", player, 3))  # Diamond Sea

    set_rule(multiworld.get_entrance("Diamond Sea Exit", player),
             lambda state: state.has("Star Piece", player, 30))  # North Diamond Sea

    set_rule(multiworld.get_entrance("Serpent Entrance", player),
             lambda state: state.has("Star Piece", player, 45))  # Serpent Stacks

    set_rule(multiworld.get_entrance("Beast Bridge Phoenix", player),
             lambda state: state.has("Phoenix Flute", player))  # Serpent Stacks

    ### Locations
    # Ancient Isle
    set_rule(multiworld.get_location("Ancient Key - Ancient C2", player),
             lambda state: state.has("Ancient Key", player, 3)
                           and state.has("Star Piece", player))'''

    '''set_rule(multiworld.get_location("Gopher Gloves", player),
             lambda state: state.can_reach("Stony Cliffs", "Region", player)
                           and state.has("Topaz Rune Tablet", player)
                           and state.has("Topaz Quest Complete", player))'''



# Sets rules on completion condition
def set_completion_rules(world: "IslesOfSeaAndSkyWorld"):
    player = world.player
    multiworld = world.multiworld
    multiworld.completion_condition[player] = lambda state: state.can_reach("Sanctum Peak", "Region", player)

