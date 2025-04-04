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

    ### Regions & Entrances
    '''set_rule(multiworld.get_entrance("Serpent Entrance", player), lambda state: state.has("45 Stars", player))

    set_rule(multiworld.get_entrance("Ancient North Exit", player),
             lambda state: state.has("Topaz Quest Complete", player)
                           and state.has("Sapphire Quest Complete", player)
                           and state.has("Ruby Quest Complete", player)
                           and state.has("Diamond Quest Complete", player) ) # Sanctum

    set_rule(multiworld.get_entrance("Elemental Rock Path", player),
             lambda state: state.has("Topaz Shard Hit", player)
                           and state.has("Sapphire Shard Hit", player)
                           and state.has("Ruby Shard Hit", player)
                           and state.has("Diamond Shard Hit", player) ) # Sanctum Peak

    set_rule(multiworld.get_entrance("Ancient East Exit", player), lambda state: state.has("3 Keys", player)
                                                                         and state.has("1 Stars", player) ) # Topaz Sea

    set_rule(multiworld.get_entrance("Stoney West Exit", player), lambda state: state.has("5 Stars", player) ) # Sapphire Sea

    set_rule(multiworld.get_entrance("Diamond Sea West Entrance", player),
             lambda state: state.has("3 Stars", player))  # Diamond Sea

    set_rule(multiworld.get_entrance("Ruby Sea West Entrance", player),
             lambda state: state.has("15 Stars", player))  # Ruby Sea

    set_rule(multiworld.get_entrance("Diamond Sea Exit", player),
             lambda state: state.has("30 Stars", player))  # North Diamond Sea




    ### Locations
    set_rule(multiworld.get_location("Gopher Gloves", player),
             lambda state: state.can_reach("Stoney Cliffs", "Region", player)
                           and state.has("Topaz Rune Tablet", player)
                           and state.has("Topaz Quest Complete", player))'''

    '''set_rule(multiworld.get_location("Mettaton Plot", player),
             lambda state: state.can_reach("Core Exit", "Entrance", player))
    set_rule(multiworld.get_location("Bunny 1", player),
             lambda state: state.can_reach("Snowdin Town", "Region", player))
    set_rule(multiworld.get_location("Bunny 2", player),
             lambda state: state.can_reach("Snowdin Town", "Region", player))
    set_rule(multiworld.get_location("Bunny 3", player),
             lambda state: state.can_reach("Snowdin Town", "Region", player))
    set_rule(multiworld.get_location("Bunny 4", player),
             lambda state: state.can_reach("Snowdin Town", "Region", player))
    set_rule(multiworld.get_location("Astro 1", player),
             lambda state: state.can_reach("Waterfall", "Region", player))
    set_rule(multiworld.get_location("Astro 2", player),
             lambda state: state.can_reach("Waterfall", "Region", player))
    set_rule(multiworld.get_location("Gerson 1", player),
             lambda state: state.can_reach("Waterfall", "Region", player))
    set_rule(multiworld.get_location("Gerson 2", player),
             lambda state: state.can_reach("Waterfall", "Region", player))
    set_rule(multiworld.get_location("Gerson 3", player),
             lambda state: state.can_reach("Waterfall", "Region", player))
    set_rule(multiworld.get_location("Gerson 4", player),
             lambda state: state.can_reach("Waterfall", "Region", player))
    set_rule(multiworld.get_location("Present Knife", player),
             lambda state: state.can_reach("New Home", "Region", player))
    set_rule(multiworld.get_location("Present Locket", player),
             lambda state: state.can_reach("New Home", "Region", player))
    set_rule(multiworld.get_location("Left New Home Key", player),
             lambda state: state.can_reach("New Home", "Region", player))
    set_rule(multiworld.get_location("Right New Home Key", player),
             lambda state: state.can_reach("New Home", "Region", player))
    set_rule(multiworld.get_location("Trash Burger", player),
             lambda state: state.can_reach("Core", "Region", player))
    set_rule(multiworld.get_location("Quiche Bench", player),
             lambda state: state.can_reach("Waterfall", "Region", player))
    set_rule(multiworld.get_location("Tutu Hidden", player),
             lambda state: state.can_reach("Waterfall", "Region", player))
    set_rule(multiworld.get_location("Grass Shoes", player),
             lambda state: state.can_reach("Waterfall", "Region", player))
    set_rule(multiworld.get_location("TemmieShop 1", player),
             lambda state: state.can_reach("Waterfall", "Region", player))
    set_rule(multiworld.get_location("TemmieShop 2", player),
             lambda state: state.can_reach("Waterfall", "Region", player))
    set_rule(multiworld.get_location("TemmieShop 3", player),
             lambda state: state.can_reach("Waterfall", "Region", player))
    set_rule(multiworld.get_location("TemmieShop 4", player),
             lambda state: state.can_reach("Waterfall", "Region", player) and state.has("1000G", player, 2))
    set_rule(multiworld.get_location("Noodles Fridge", player),
             lambda state: state.can_reach("Hotland", "Region", player))
    set_rule(multiworld.get_location("Pan Hidden", player),
             lambda state: state.can_reach("Hotland", "Region", player))
    set_rule(multiworld.get_location("Bratty Catty 1", player),
             lambda state: state.can_reach("News Show", "Region", player))
    set_rule(multiworld.get_location("Bratty Catty 2", player),
             lambda state: state.can_reach("News Show", "Region", player))
    set_rule(multiworld.get_location("Bratty Catty 3", player),
             lambda state: state.can_reach("News Show", "Region", player))
    set_rule(multiworld.get_location("Bratty Catty 4", player),
             lambda state: state.can_reach("News Show", "Region", player))
    set_rule(multiworld.get_location("Burgerpants 1", player),
             lambda state: state.can_reach("News Show", "Region", player))
    set_rule(multiworld.get_location("Burgerpants 2", player),
             lambda state: state.can_reach("News Show", "Region", player))
    set_rule(multiworld.get_location("Burgerpants 3", player),
             lambda state: state.can_reach("News Show", "Region", player))
    set_rule(multiworld.get_location("Burgerpants 4", player),
             lambda state: state.can_reach("News Show", "Region", player))'''


# Sets rules on completion condition
def set_completion_rules(world: "IslesOfSeaAndSkyWorld"):
    player = world.player
    multiworld = world.multiworld
    multiworld.completion_condition[player] = lambda state: state.can_reach("Sanctum Peak", "Region", player)
    '''if _isles_of_sea_and_sky_is_route(world, 1):
        multiworld.completion_condition[player] = lambda state: state.can_reach("True Lab", "Region", player)'''
