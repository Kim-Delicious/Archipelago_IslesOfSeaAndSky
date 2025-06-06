from worlds.generic.Rules import set_rule
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import IslesOfSeaAndSkyWorld


def _isles_of_sea_and_sky_is_route(self, route: int):
    if route == 0:
        return self.options.route_required.current_key == "normal_ending"
    if route == 1:
        return self.options.route_required.current_key == "secret_ending"
    if route == 2:
        return self.options.route_required.current_key == "all_gems"
    return False


# Sets rules on entrances and advancements that are always applied
def set_rules(self):

    player = self.player
    multiworld = self.multiworld

    ### WILL IMPACT PERFORMANCE OF GAME GENERATION
    # self.explicit_indirect_conditions = False

    set_rechecks(self)

    ### Entrances
    set_rule(multiworld.get_entrance("Ancient West Exit", player),
             lambda state: state.can_reach("Ruby Sea", "Region", player))  # Obsidian Sea

    set_rule(multiworld.get_entrance("Ancient East Exit", player),
             lambda state: state.has("Ancient Key", player, 6)
             and state.has("Star Piece", player))  # Topaz Sea


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

    set_rule(multiworld.get_entrance("Stony Exit To Post-Rune", player),
             lambda state: state.has("Topaz Rune Stone", player))  # Stony Cliffs Post-Rune
    set_rule(multiworld.get_entrance("Stony West Exit", player),
             lambda state: state.has("Topaz Rune Stone", player ) )  # Stony Cliffs NW
    set_rule(multiworld.get_entrance("Stony NW East Exit", player),
             lambda state: state.has("Topaz Rune Stone", player) )  # Stony Cliffs
    set_rule(multiworld.get_entrance("Stony NW West Exit", player),
             lambda state: state.has("Star Piece", player, 5) ) # Sapphire Sea

    set_rule(multiworld.get_entrance("Stony West Entrance", player),
             lambda state: state.has("Star Piece", player, 5))  # Stony NW



    # NOTE: state.has only works with items classified as progression

    set_rule(multiworld.get_entrance("Ruby Sea West Entrance", player),
             lambda state: state.has("Star Piece", player, 15))  # Ruby Sea

    set_rule(multiworld.get_entrance("Diamond Sea Exit", player),
             lambda state: state.has("Star Piece", player, 30))  # North Diamond Sea

    set_rule(multiworld.get_entrance("North Diamond Sea South Exit", player),
             lambda state: state.has("Star Piece", player, 30))  # Diamond Sea
    set_rule(multiworld.get_entrance("North Diamond Sea East Exit", player),
             lambda state: state.can_reach("Lost Sea", "Region", player))  # Northeast Sea | GEN FAILURES


    set_rule(multiworld.get_entrance("Serpent Entrance", player),
             lambda state: state.has("Star Piece", player, 45))  # Serpent Stacks

    set_rule(multiworld.get_entrance("Tidal Exit To Post-Rune", player),
             lambda state: (state.has("Sapphire Rune Stone", player)))  # Tidal Reef Post-Rune

    set_rule(multiworld.get_entrance("Raging Exit To Post-Rune", player),
             lambda state: (state.has("Ruby Rune Stone", player)))  # Raging Volcano Post-Rune

    set_rule(multiworld.get_entrance("Raging Exit To NE", player),
             lambda state: (state.has("Ruby Rune Stone", player)))  # Raging Volcano NE

    set_rule(multiworld.get_entrance("Frozen Exit To Post-Rune", player),
             lambda state: (state.has("Diamond Rune Stone", player)))  # Frozen Spire Post-Rune

    set_rule(multiworld.get_entrance("Serpent Exit To Post-Rune", player),
             lambda state: (state.has("Obsidian Rune Stone", player)))  # Serpent Stacks Post-Rune


    set_rule(multiworld.get_entrance("Star West Exit", player),
             lambda state: (state.can_reach("Lost Sea", "Region", player)))  # Lost Sea | Gen Failures

    set_rule(multiworld.get_entrance("Star East Exit", player),
             lambda state: (state.has("Ancient Rune Stone", player)))  # Lost Sea

    set_rule(multiworld.get_entrance("Star East Entrance", player),
             lambda state: state.has("Ancient Rune Stone", player)
                            and state.can_reach("Lost Sea", "Region", player) )  # Star Tropic

    set_rule(multiworld.get_entrance("Shoal Entrance", player),
             lambda state: (state.has("Ancient Rune Stone", player)))  # Shoal

    set_rule(multiworld.get_entrance("Locked Entrance", player),
             lambda state: (state.can_reach("Ruby Sea", "Region", player)))  # Attempt to make ancient rune stone reachable

    set_rule(multiworld.get_entrance("Beast Entrance", player),
             lambda state: state.has("Rolling Bell Rung", player)
                           and state.has("Sunken Bell Rung", player)
                           and state.has("Aggro Bell Rung", player)
                           and state.has("Nunatak Bell Rung", player))

    set_rule(multiworld.get_entrance("Abstract Phoenix Exit", player),
             lambda state: state.has("Phoenix Flute", player)
                           and self.options.phoenix_anywhere.value)  # Phoenix Hub
    set_rule(multiworld.get_entrance("Beast Bridge Phoenix", player),
             lambda state: state.has("Phoenix Flute", player) )  # Phoenix Hub
    set_rule(multiworld.get_entrance("Stony Phoenix", player),
             lambda state: state.has("Phoenix Flute", player))  # Phoenix Hub
    set_rule(multiworld.get_entrance("Tidal Phoenix", player),
             lambda state: state.has("Phoenix Flute", player) and state.has("Sapphire Rune Stone", player))  # Phoenix Hub
    set_rule(multiworld.get_entrance("Raging Phoenix", player),
             lambda state: state.has("Phoenix Flute", player))  # Phoenix Hub
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
                            and ( state.has("Sapphire Rune Stone", player) or state.has("Frog Flippers", player) ) )  # Tidal Reef
    set_rule(multiworld.get_entrance("Raging Phoenix Entrance", player),
             lambda state: state.has("Phoenix Flute", player) )  # Raging Volcano NE
    set_rule(multiworld.get_entrance("Frozen Phoenix Entrance", player),
             lambda state: state.has("Phoenix Flute", player)
                           and state.has("Diamond Rune Stone", player) )  # Frozen Spire
    set_rule(multiworld.get_entrance("Lost Phoenix Entrance", player),
             lambda state: state.has("Phoenix Flute", player)
                           and state.has("Star Piece", player, 30) )  # Lost Landing


    if self.options.enable_locksanity.value:
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
             lambda state: (state.can_reach("Stony Cliffs Post-Rune", "Region", player)
                           and state.has("Topaz Rune Stone", player)
                           and state.has("Topaz Quest Complete", player))
                           or (state.can_reach("Stony Cliffs NW", "Region", player)
                           and state.has("Gopher Gloves", player) ) )

    set_rule(multiworld.get_location("Frog Flippers", player),
             lambda state: state.can_reach("Tidal Reef", "Region", player)
                           and state.has("Sapphire Rune Stone", player))

    set_rule(multiworld.get_location("Salamander Shirt", player),
             lambda state: state.can_reach("Raging Volcano NE", "Region", player)
                           and state.has("Fire Key", player, 3))

    set_rule(multiworld.get_location("Kite Cloak", player),
             lambda state: state.can_reach("Frozen Spire", "Region", player)
                           and state.has("Diamond Rune Stone", player)
                           and (state.has("Diamond Quest Complete", player) or state.has("Kite Cloak", player)) ) # since Eggs and Wind key are broken, don't include

    set_rule(multiworld.get_location("Serpent Circlet", player),
             lambda state: state.can_reach("Serpent Stacks", "Region", player)
                           and state.has("Topaz Rune Stone", player)
                           and state.has("Sapphire Rune Stone", player)
                           and state.has("Ruby Rune Stone", player)
                           and state.has("Diamond Rune Stone", player)
                           and state.has("Obsidian Rune Stone", player)
                           and state.has("Obsidian", player, 10))

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
    set_ancient_isle(self)
    set_rolling_rocks(self)
    set_sunken_island(self)
    set_aggro_crag(self)
    set_sea_nunatak(self)
    set_locked(self)
    set_star_tropic(self)
    set_shoal(self)
    set_lost_landing(self)


    set_stony_cliffs(self)
    set_tidal_reef(self)
    set_raging_volcano(self)
    set_frozen_spire(self)
    set_serpent_stacks(self)
    set_beast_bridge(self)
    set_sanctum(self)





def set_ancient_isle(self):

    player = self.player
    multiworld = self.multiworld

    # Collectables
    set_rule(multiworld.get_location("Star Piece [Ancient A1]", player),
             lambda state: state.can_reach("Obsidian Sea", "Region", player)
             and state.has("Ancient Key", player, 17) ) # Makes this 'unreachable'

    set_rule(multiworld.get_location("Star Piece [Ancient B1]", player),
             lambda state: state.can_reach("Obsidian Sea", "Region", player)
                           and state.has("Ancient Rune Stone", player)
             and state.has("Ancient Key", player, 17) ) # Makes this 'unreachable'

    set_rule(multiworld.get_location("Ancient Key [Ancient A2 - NW]", player),
             lambda state: state.has("Topaz Quest Complete", player)
             )#and state.can_reach("Topaz Sea", "Region", player))

    set_rule(multiworld.get_location("Ancient Key [Ancient A1]", player),
             lambda state: state.has("Ancient Key", player))

    set_rule(multiworld.get_location("Ancient Key [Ancient A2 - SE]", player),
             lambda state: state.has("Ancient Key", player))

    set_rule(multiworld.get_location("Ancient Key [Ancient A3 - N]", player),
             lambda state: state.has("Ancient Key", player, 2))
    set_rule(multiworld.get_location("Ancient Key [Ancient A3 - S]", player),
             lambda state: state.has("Ancient Key", player))
    set_rule(multiworld.get_location("Ancient Key [Ancient A3 - E]", player),
             lambda state: state.has("Ancient Key", player, 2))

    set_rule(multiworld.get_location("Ancient Key [Ancient C2]", player),
             lambda state: state.has("Ancient Key", player, 3))
    set_rule(multiworld.get_location("Ancient Key [Ancient C3]", player),
             lambda state: state.has("Ancient Key", player, 3))
    set_rule(multiworld.get_location("Ancient Key [Ancient C1]", player),
             lambda state: state.has("Star Piece", player)
                               and state.has("Ancient Key", player, 6))

    set_rule(multiworld.get_location("Star Piece [Ancient C0]", player),
             lambda state: state.has("Ancient Key", player, 6))

    # Locksanity
    if self.options.enable_locksanity.value:

        set_rule(multiworld.get_location("3x Lock [Ancient A1]", player),
             lambda state: state.can_reach("Obsidian Sea", "Region", player)
                           and state.has("Ancient Key", player, 17))

        set_rule(multiworld.get_location("Lock [Ancient B3]", player),
                 lambda state: state.has("Ancient Key", player, 1))

        set_rule(multiworld.get_location("Lock [Ancient A3]", player),
                 lambda state: state.has("Ancient Key", player, 2))

        set_rule(multiworld.get_location("Lock [Ancient B2]", player),
                 lambda state: state.has("Ancient Key", player, 3))

        set_rule(multiworld.get_location("3x Lock [Ancient C2]", player),
                 lambda state: state.has("Ancient Key", player, 6))

        set_rule(multiworld.get_location("Star Lock 1 [Ancient C1]", player),
                 lambda state: state.has("Star Piece", player)
                               and state.has("Ancient Key", player, 6))

        set_rule(multiworld.get_location("Ancient Rune Lock [Ancient B1]", player),
             lambda state: state.has("Ancient Rune Stone", player))

    if self.options.enable_snakesanity.value:
        set_rule(multiworld.get_location("Snakeblock [Ancient B3]", player),
                 lambda state: state.has("Ancient Key", player))

        set_rule(multiworld.get_location("Snakeblock [Ancient B2 - W]", player),
                 lambda state: state.has("Ancient Key", player))

        set_rule(multiworld.get_location("Snakeblock [Ancient A3]", player),
                 lambda state: state.has("Ancient Key", player, 2))

        set_rule(multiworld.get_location("Snakeblock [Ancient B2 - E]", player),
                 lambda state: state.has("Ancient Key", player, 3))
        set_rule(multiworld.get_location("Snakeblock [Ancient C2 - E]", player),
                 lambda state: state.has("Ancient Key", player, 3))
        set_rule(multiworld.get_location("Snakeblock [Ancient C2 - S]", player),
                 lambda state: state.has("Ancient Key", player, 3))
        set_rule(multiworld.get_location("Snakeblock [Ancient C2 - W]", player),
                 lambda state: state.has("Ancient Key", player, 3))
        set_rule(multiworld.get_location("Snakeblock [Ancient C3]", player),
                 lambda state: state.has("Ancient Key", player, 3))

        set_rule(multiworld.get_location("Snakeblock [Ancient A1]", player),
                lambda state: state.can_reach("Obsidian Sea", "Region", player))

    # Secretsanity
    if self.options.secretsanity.value:
        set_rule(multiworld.get_location("Discover Ancient Secret 1", player),
                 lambda state: state.can_reach("Obsidian Sea", "Region", player)
                               and state.has("Ancient Key", player, 17))  # Makes this 'unreachable'


def set_rolling_rocks(self):
    player = self.player
    multiworld = self.multiworld

    set_rule(multiworld.get_location("Topaz [Rolling A0]", player),
             lambda state: state.has("Star Piece", player, 7)
                           and state.has("Topaz Quest Complete", player) )

    set_rule(multiworld.get_location("Obsidian [Rolling A1]", player),
             lambda state: state.has("Star Piece", player, 7)
                           and state.has("Gopher Gloves", player))

    set_rule(multiworld.get_location("Star Piece [Rolling A0]", player),
             lambda state: state.has("Star Piece", player, 7)
                           and (state.has("Topaz Quest complete", player) or state.has("Frog Flippers", player) ) )

    set_rule(multiworld.get_location("Rolling Bell Rung", player),
             lambda state: state.has("Ancient Rune Stone", player))

    set_rule(multiworld.get_location("Star Piece [Rolling B1]", player),
             lambda state: state.has("Ancient Rune Stone", player)
                           and state.has("Ancient Key", player, 14))

    set_rule(multiworld.get_location("Star Piece [Rolling B0]", player),
             lambda state: state.has("Ancient Rune Stone", player)
             and state.has("Gopher Gloves", player))



    # Locksanity
    if self.options.enable_locksanity.value:

        set_rule(multiworld.get_location("3x Lock [Rolling B1]", player),
                 lambda state: state.has("Ancient Rune Stone", player)
                                and state.has("Ancient Key", player, 14))

        set_rule(multiworld.get_location("Star Lock 7 [Rolling A0]", player),
                 lambda state: state.has("Star Piece", player, 7))

        set_rule(multiworld.get_location("Ancient Rune Lock [Rolling A1]", player),
                 lambda state: state.has("Ancient Rune Stone", player))

        set_rule(multiworld.get_location("Ancient Rune Lock [Rolling B0]", player),
                 lambda state: state.has("Ancient Rune Stone", player))

    if self.options.enable_snakesanity.value:
        set_rule(multiworld.get_location("Snakeblock [Rolling B0]", player),
                 lambda state: state.has("Ancient Rune Stone", player))

    # Secretsanity
    if self.options.secretsanity.value:
        set_rule(multiworld.get_location("Discover Rolling Secret 1", player),
                 lambda state: state.has("Star Piece", player, 7)
                               and state.has("Gopher Gloves", player))

def set_sunken_island(self):
    player = self.player
    multiworld = self.multiworld

    set_rule(multiworld.get_location("Sunken Bell Rung", player),
             lambda state: state.has("Ancient Rune Stone", player))

    set_rule(multiworld.get_location("Sapphire [Sunken B0]", player),
             lambda state: state.has("Star Piece", player, 21)
             and state.has("Sapphire Quest Complete", player))

    set_rule(multiworld.get_location("Star Piece [Sunken B0]", player),
             lambda state: state.has("Star Piece", player, 21)
                           and state.has("Sapphire Quest Complete", player))

    set_rule(multiworld.get_location("Star Piece [Sunken A1]", player),
             lambda state: state.has("Ancient Key", player, 34)
                               and state.has("Ancient Rune Stone", player) )

    set_rule(multiworld.get_location("Obsidian [Sunken A0]", player),
             lambda state: state.has("Frog Flippers", player))

    # Locksanity
    if self.options.enable_locksanity.value:
        set_rule(multiworld.get_location("3x Lock [Sunken A1]", player),
                 lambda state: state.has("Ancient Key", player, 34)
                               and state.has("Ancient Rune Stone", player))

        set_rule(multiworld.get_location("Star Lock 21 [Sunken B0]", player),
                 lambda state: state.has("Star Piece", player, 21))

        set_rule(multiworld.get_location("Ancient Rune Lock [Sunken A0]", player),
                 lambda state: state.has("Ancient Rune Stone", player))

        set_rule(multiworld.get_location("Ancient Rune Lock [Sunken B1]", player),
                 lambda state: state.has("Ancient Rune Stone", player))

def set_aggro_crag(self):
    player = self.player
    multiworld = self.multiworld

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
    if self.options.enable_locksanity.value:

        set_rule(multiworld.get_location("3x Lock [Aggro A1]", player),
                 lambda state: state.has("Star Piece", player, 35)
                               and state.has("Ruby Quest Complete", player)
                               and state.has("Ancient Rune Stone", player)
                               and state.has("Ancient Key", player, 42))

        set_rule(multiworld.get_location("Star Lock 35 [Aggro B0]", player),
                 lambda state: state.has("Star Piece", player, 35))

        set_rule(multiworld.get_location("Ancient Rune Lock [Aggro B1]", player),
                 lambda state: state.has("Star Piece", player, 35)
                               and state.has("Ruby Quest Complete", player)
                               and state.has("Ancient Rune Stone", player))

        set_rule(multiworld.get_location("Ancient Rune Lock [Aggro A1]", player),
                 lambda state: state.has("Ancient Rune Stone", player))

        set_rule(multiworld.get_location("Obsidian [Aggro B0]", player),
                 lambda state: state.has("Ancient Rune Stone", player)
                               and state.has("Star Piece", player, 35)
                               and state.has("Ruby Quest Complete", player)
                               and state.has("Salamander Shirt", player))

    # Snakesanity
    if self.options.enable_snakesanity.value:
        set_rule(multiworld.get_location("Snakeblock [Aggro B1 - E]", player),
                 lambda state: state.has("Star Piece", player, 35))

        set_rule(multiworld.get_location("Snakeblock [Aggro B1 - W]", player),
                 lambda state: state.has("Star Piece", player, 35)
                               and state.has("Ruby Quest Complete", player)
                               and state.has("Ancient Rune Stone", player))

        set_rule(multiworld.get_location("Snakeblock [Aggro B0 - W]", player),
                 lambda state: state.has("Star Piece", player, 35)
                               and state.has("Ruby Quest Complete", player)
                               and state.has("Ancient Rune Stone", player)
                               and state.has("Salamander Shirt", player))

    # Secretsanity
    if self.options.secretsanity.value:
        set_rule(multiworld.get_location("Discover Aggro Secret 2", player),
                 lambda state: state.has("Ancient Rune Stone", player)
                               and state.has("Star Piece", player, 35)
                               and state.has("Ruby Quest Complete", player)
                               and state.has("Salamander Shirt", player))

        set_rule(multiworld.get_location("Discover Aggro Secret 3", player),
                 lambda state: state.has("Ancient Rune Stone", player)
                               and state.has("Star Piece", player, 35)
                               and state.has("Ruby Quest Complete", player)
                               and state.has("Salamander Shirt", player))

def set_sea_nunatak(self):
    player = self.player
    multiworld = self.multiworld

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
             lambda state: state.has("Ancient Rune Stone", player)
                               and state.has("Ancient Key", player, 26) )

    set_rule(multiworld.get_location("Obsidian [Nunatak B1]", player),
             lambda state: state.has("Diamond Quest Complete", player)
                           and state.has("Star Piece", player, 49)
                           and state.has("Kite Cloak", player) )

    # Locksanity
    if self.options.enable_locksanity.value:

        set_rule(multiworld.get_location("3x Lock [Nunatak A0]", player),
                 lambda state: state.has("Ancient Rune Stone", player)
                               and state.has("Ancient Key", player, 26))

        set_rule(multiworld.get_location("Ancient Rune Lock [Nunatak B0]", player),
                 lambda state: state.has("Ancient Rune Stone", player))

        set_rule(multiworld.get_location("Star Lock 49 [Nunatak B0]", player),
                 lambda state: state.has("Star Piece", player, 49))

    # Snakesanity
    if self.options.enable_snakesanity.value:
        set_rule(multiworld.get_location("Snakeblock [Nunatak A1]", player),
                     lambda state: state.has("Ancient Rune Stone", player)
                     and state.has("Diamond Quest Complete", player)
                     and state.has("Star Piece", player, 49))

    # Secretsanity
    if self.options.secretsanity.value:
        set_rule(multiworld.get_location("Discover Nunatak Secret 1", player),
                 lambda state: state.has("Diamond Quest Complete", player)
                               and state.has("Star Piece", player, 49)
                               and state.has("Kite Cloak", player))

        set_rule(multiworld.get_location("Discover Nunatak Secret 2", player),
                 lambda state: state.has("Diamond Quest Complete", player)
                               and state.has("Star Piece", player, 49)
                               and state.has("Kite Cloak", player))

        set_rule(multiworld.get_location("Discover Nunatak Secret 3", player),
                 lambda state: state.has("Ancient Rune Stone", player)
                               and state.has("Diamond Quest Complete", player)
                               and state.has("Star Piece", player, 49))
        set_rule(multiworld.get_location("Discover Nunatak Secret 4", player),
                 lambda state: state.has("Ancient Rune Stone", player)
                               and state.has("Diamond Quest Complete", player)
                               and state.has("Star Piece", player, 49))

def set_locked(self):
    player = self.player
    multiworld = self.multiworld
    set_rule(multiworld.get_location("Ancient Rune Stone", player),
             lambda state: state.has("Ancient Key", player, 23))  # Makes this 'unreachable'

    set_rule(multiworld.get_location("Star Piece [Locked A1]", player),
             lambda state: state.has("Ancient Rune Stone", player) )

    # Locksanity
    if self.options.enable_locksanity.value:

        set_rule(multiworld.get_location("6x Lock [Locked B1]", player),
                 lambda state: state.has("Ancient Key", player, 23))

        set_rule(multiworld.get_location("Ancient Rune Lock [Locked A1]", player),
                 lambda state: state.has("Ancient Rune Stone", player))

    # Snakesanity
    if self.options.enable_snakesanity.value:
        set_rule(multiworld.get_location("Snakeblock [Locked A1 - E]", player),
                 lambda state: state.has("Ancient Key", player, 23))
        set_rule(multiworld.get_location("Snakeblock [Locked A1 - C]", player),
                 lambda state: state.has("Ancient Key", player, 23))
        set_rule(multiworld.get_location("Snakeblock [Locked A1 - W]", player),
                 lambda state: state.has("Ancient Key", player, 23))

def set_star_tropic(self):
    player = self.player
    multiworld = self.multiworld

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

    set_rule(multiworld.get_location("Star Piece [Tropic A1 - 1]", player),
             lambda state: state.has("Ancient Rune Stone", player)
                           and state.has("Gopher Gloves", player))

    set_rule(multiworld.get_location("Star Piece [Tropic A1 - 2]", player),
             lambda state: state.has("Ancient Rune Stone", player)
                           and state.has("Gopher Gloves", player)
                           and state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Star Piece [Tropic A1 - 3]", player),
             lambda state: state.has("Ancient Rune Stone", player)
                           and state.has("Gopher Gloves", player)
                           and state.has("Frog Flippers", player)
                           and state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Star Piece [Tropic A1 - 4]", player),
             lambda state: state.has("Ancient Rune Stone", player)
                           and state.has("Gopher Gloves", player)
                           and state.has("Frog Flippers", player)
                           and state.has("Salamander Shirt", player)
                           and state.has("Kite Cloak", player))

    set_rule(multiworld.get_location("Star Piece [Tropic B0 - S]", player),
                 lambda state: state.has("Ancient Rune Stone", player)
                               or (state.can_reach("Lost Sea", "Region", player)
                                   and state.has("Kite Cloak", player) ))

    set_rule(multiworld.get_location("Star Piece [Tropic B0 - N]", player),
             lambda state: state.has("Obsidian Rune Stone", player)
                       and state.has("Kite Cloak", player))


    # Locksanity
    if self.options.enable_locksanity.value:

        set_rule(multiworld.get_location("Ancient Rune Lock [Tropic A1]", player),
                 lambda state: state.has("Ancient Rune Stone", player) )

        set_rule(multiworld.get_location("Ancient Rune Lock [Tropic B0]", player),
                 lambda state: state.has("Ancient Rune Stone", player))

        set_rule(multiworld.get_location("Obsidian Rune Lock [Tropic B0]", player),
                 lambda state: state.has("Obsidian Rune Stone", player)
                           and state.has("Kite Cloak", player))

    # Snakesanity
    if self.options.enable_snakesanity.value:
        set_rule(multiworld.get_location("Snakeblock [Tropic A0 - W]", player),
                 lambda state: state.has("Kite Cloak", player))
        set_rule(multiworld.get_location("Snakeblock [Tropic A0 - C]", player),
                 lambda state: state.has("Kite Cloak", player))
        set_rule(multiworld.get_location("Snakeblock [Tropic A0 - E]", player),
                 lambda state: state.has("Kite Cloak", player))
        set_rule(multiworld.get_location("Snakeblock [Tropic B0 - N]", player),
                 lambda state: state.has("Kite Cloak", player))
        set_rule(multiworld.get_location("Snakeblock [Tropic B0 - S]", player),
                 lambda state: state.has("Kite Cloak", player))

    # Secretsanity
    if self.options.secretsanity.value:
        set_rule(multiworld.get_location("Discover Tropic Secret 1", player),
                 lambda state: state.has("Kite Cloak", player))

def set_shoal(self):
    player = self.player
    multiworld = self.multiworld

    set_rule(multiworld.get_location("Star Viewing Orb", player),
             lambda state: state.has("Ancient Rune Stone", player))

    set_rule(multiworld.get_location("Star Piece [Shoal A0]", player),
             lambda state: state.has("Ancient Rune Stone", player)
                           and state.has("Frog Flippers", player)
                           and state.has("Kite Cloak", player))

    # Locksanity
    if self.options.enable_locksanity.value:

        set_rule(multiworld.get_location("Ancient Rune Lock [Shoal A0]", player),
                 lambda state: state.has("Ancient Rune Stone", player))

    # Snakesanity
    if self.options.enable_snakesanity.value:

        set_rule(multiworld.get_location("Snakeblock [Shoal A0]", player),
                 lambda state: state.has("Ancient Rune Stone", player)
                               and state.has("Kite Cloak", player))

    if self.options.secretsanity.value:
        set_rule(multiworld.get_location("Discover Shoal Secret 2", player),
                 lambda state: state.has("Ancient Rune Stone", player))

        set_rule(multiworld.get_location("Discover Shoal Secret 3", player),
                 lambda state: state.has("Ancient Rune Stone", player)
                               and state.has("Frog Flippers", player)
                               and state.has("Kite Cloak", player))

def set_lost_landing(self):
    player = self.player
    multiworld = self.multiworld

    set_rule(multiworld.get_location("Obsidian [Lost A1]", player),
             lambda state: state.has("Star Piece", player, 30)
                           and state.has("Frog Flippers", player))

    set_rule(multiworld.get_location("Star Piece [Lost B1]", player),
             lambda state: state.has("Star Piece", player, 30) )

    # Locksanity
    if self.options.enable_locksanity.value:

        set_rule(multiworld.get_location("Lock [Lost B1]", player),
                 lambda state: state.can_reach("Lost Sea", "Region", player)
                               and state.has("Frog Flippers", player)
                                and state.has("Ancient Key", player, 48))

        set_rule(multiworld.get_location("Star Lock 30 [Lost A0]", player),
                 lambda state: state.has("Star Piece", player, 30))

    # Snakesanity
    if self.options.enable_snakesanity.value:
        set_rule(multiworld.get_location("Snakeblock [Lost B1]", player),
                 lambda state: state.has("Star Piece", player, 30))

    # Secretsanity
    if self.options.secretsanity.value:
        set_rule(multiworld.get_location("Discover Lost Secret 1", player),
                 lambda state: state.can_reach("Lost Sea", "Region", player)
                               and state.has("Frog Flippers", player))

        set_rule(multiworld.get_location("Discover Lost Secret 2", player),
                 lambda state: state.can_reach("Lost Sea", "Region", player)
                               and state.has("Frog Flippers", player))


def set_serpent_stacks(self):
    player = self.player
    multiworld = self.multiworld

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
    if self.options.enable_locksanity.value:

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

    # Snakesanity
    if self.options.enable_snakesanity.value:
        set_rule(multiworld.get_location("Snakeblock [Serpent A1 - C]", player),
                 lambda state: state.has("Serpent Circlet", player) and state.has("Topaz Rune Stone", player)
                           and state.has("Sapphire Rune Stone", player)
                           and state.has("Ruby Rune Stone", player)
                           and state.has("Diamond Rune Stone", player))
        set_rule(multiworld.get_location("Snakeblock [Serpent A1 - CE]", player),
                 lambda state: state.has("Serpent Circlet", player)
                               and state.has("Topaz Rune Stone", player)
                           and state.has("Sapphire Rune Stone", player)
                           and state.has("Ruby Rune Stone", player)
                           and state.has("Diamond Rune Stone", player))
        set_rule(multiworld.get_location("Snakeblock [Serpent A1 - E]", player),
                 lambda state: state.has("Serpent Circlet", player)
                               and state.has("Topaz Rune Stone", player)
                           and state.has("Sapphire Rune Stone", player)
                           and state.has("Ruby Rune Stone", player)
                           and state.has("Diamond Rune Stone", player))
        set_rule(multiworld.get_location("Snakeblock [Serpent A6 - SW]", player),
                 lambda state: state.has("Serpent Circlet", player)
                               and state.has("Topaz Quest Complete", player)
                               and state.has("Sapphire Quest Complete", player))
        set_rule(multiworld.get_location("Snakeblock [Serpent A6 - NW]", player),
                 lambda state: state.has("Serpent Circlet", player)
                               and state.has("Topaz Quest Complete", player)
                               and state.has("Sapphire Quest Complete", player))
        set_rule(multiworld.get_location("Snakeblock [Serpent A6 - C]", player),
                 lambda state: state.has("Serpent Circlet", player)
                               and state.has("Topaz Quest Complete", player)
                               and state.has("Sapphire Quest Complete", player))
        set_rule(multiworld.get_location("Snakeblock [Serpent A6 - E]", player),
                 lambda state: state.has("Serpent Circlet", player)
                               and state.has("Topaz Quest Complete", player)
                               and state.has("Sapphire Quest Complete", player))
        set_rule(multiworld.get_location("Snakeblock [Serpent A8]", player),
                 lambda state: state.has("Serpent Circlet", player)
                               and state.has("Topaz Quest Complete", player)
                               and state.has("Sapphire Quest Complete", player)
                               and state.has("Ruby Quest Complete", player)
                               and state.has("Diamond Quest Complete", player))

def set_stony_cliffs(self):
    player = self.player
    multiworld = self.multiworld

    set_rule(multiworld.get_location("Gold Stone Tablet", player),
             lambda state: state.has("Topaz Rune Stone", player)
                         and state.has("Star Piece", player, 20)
                         and state.has("Topaz Quest Complete", player))

    set_rule(multiworld.get_location("Blue Stone Tablet", player),
             lambda state: state.has("Topaz Rune Stone", player)
                           and state.has("Star Piece", player, 20))

    set_rule(multiworld.get_location("Ancient Key [Stone C0]", player),
             lambda state: state.has("Topaz Quest Complete", player))

    set_rule(multiworld.get_location("Ancient Key [Stone B4]", player),
             lambda state: state.has("Topaz Quest Complete", player)
                           and state.has("Gopher Gloves", player)
                           and state.has("Star Piece", player, 15))

    set_rule(multiworld.get_location("Ancient Key [Stone Dungeon C1]", player),
             lambda state: state.has("Gopher Gloves", player)
                           and (state.can_reach("Stony Cliffs NW", "Region", player)
                           or (state.can_reach("Stony Cliffs Post-Rune", "Region", player)
                           and state.has("Topaz Rune Stone", player) ) ) )

    set_rule(multiworld.get_location("Ancient Key [Stone Dungeon D0]", player),
             lambda state: state.has("Gopher Gloves", player))

    set_rule(multiworld.get_location("Ancient Key [Stone Dungeon B1]", player),
             lambda state: state.has("Gopher Gloves", player))

    set_rule(multiworld.get_location("Ancient Key [Stone B0 - NW1]", player),
             lambda state: state.has("Topaz Quest Complete", player))
    set_rule(multiworld.get_location("Ancient Key [Stone B0 - NW2]", player),
             lambda state: state.has("Topaz Quest Complete", player))
    set_rule(multiworld.get_location("Ancient Key [Stone B0 - NW3]", player),
             lambda state: state.has("Topaz Quest Complete", player))

    set_rule(multiworld.get_location("Ancient Key [Stone A2]", player),
             lambda state: state.has("Blue Stone Tablet", player)
                           and state.has("Gold Stone Tablet", player))

    set_rule(multiworld.get_location("Ancient Key [Stone Dungeon D2]", player),
             lambda state: state.has("Topaz Quest Complete", player))


    set_rule(multiworld.get_location("Topaz [Stone Dungeon C1]", player),
             lambda state: state.has("Gopher Gloves", player)
                           and (state.can_reach("Stony Cliffs NW", "Region", player)
                           or (state.can_reach("Stony Cliffs Post-Rune", "Region", player)
                           and state.has("Topaz Rune Stone", player) ) ) )

    set_rule(multiworld.get_location("Topaz [Stone C2 - E]", player),
             lambda state: state.has("Ancient Key", player, 7))

    set_rule(multiworld.get_location("Obsidian [Stone A2]", player),
             lambda state: state.has("Blue Stone Tablet", player)
                           and state.has("Gold Stone Tablet", player))

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

    set_rule(multiworld.get_location("Star Piece [Stone Dungeon E1]", player),
             lambda state: state.has("Topaz Quest Complete", player))

    set_rule(multiworld.get_location("Star Piece [Stone Dungeon E2]", player),
             lambda state: state.has("Topaz Quest Complete", player)
                           and state.has("Gopher Gloves", player)
                           and state.has("Frog Flippers", player))

    set_rule(multiworld.get_location("Ancient Key [Stone Dungeon E2]", player),
             lambda state: state.has("Topaz Quest Complete", player))

    set_rule(multiworld.get_location("Star Piece [Stone Dungeon C3]", player),
                 lambda state: state.has("Topaz Quest Complete", player))

    set_rule(multiworld.get_location("Star Piece [Stone Dungeon C1]", player),
             lambda state: state.has("Gopher Gloves", player)
                           and (state.can_reach("Stony Cliffs NW", "Region", player)
                           or (state.can_reach("Stony Cliffs Post-Rune", "Region", player)
                           and state.has("Topaz Rune Stone", player) ) ) )

    set_rule(multiworld.get_location("Star Piece [Stone Dungeon B1]", player),
             lambda state: state.has("Gopher Gloves", player))

    set_rule(multiworld.get_location("Star Piece [Stone A1]", player),
             lambda state: state.has("Star Piece", player, 5))

    set_rule(multiworld.get_location("Star Piece [Stone E1]", player),
             lambda state: state.has("Ancient Key", player, 10))

    set_rule(multiworld.get_location("Music Note [Stone B2]", player),
             lambda state: state.has("Topaz Quest Complete", player))

    set_rule(multiworld.get_location("Music Note [Stone D1]", player),
             lambda state: state.has("Topaz Quest Complete", player))

    set_rule(multiworld.get_location("Open Topaz Door [Stone Dungeon C2]", player),
             lambda state: state.has("Topaz Quest Complete", player))



    # Locksanity
    if self.options.enable_locksanity.value:

        set_rule(multiworld.get_location("Lock [Stone C2]", player),
                 lambda state: state.has("Ancient Key", player, 7))

        set_rule(multiworld.get_location("3x Lock [Stone E1]", player),
                 lambda state: state.has("Ancient Key", player, 10))

        set_rule(multiworld.get_location("Lock [Stone B1]", player),
                 lambda state: state.has("Ancient Key", player, 11))

        set_rule(multiworld.get_location("Star Lock 5 [Stone A1]", player),
                 lambda state: state.has("Star Piece", player, 5))

        set_rule(multiworld.get_location("Star Lock 15 [Stone C4]", player),
                 lambda state: state.has("Star Piece", player, 15)
                               and state.has("Topaz Quest Complete", player) )

        set_rule(multiworld.get_location("Star Lock 20 [Stone E3]", player),
                 lambda state: state.has("Star Piece", player, 20))

        set_rule(multiworld.get_location("Star Lock 20 [Stone Dungeon A1]", player),
                 lambda state: state.has("Star Piece", player, 20)
                               and state.has("Gopher Gloves", player))

    # Snakesanity
    if self.options.enable_snakesanity.value:
        set_rule(multiworld.get_location("Snakeblock [Stone C1]", player),
                 lambda state: state.has("Topaz Quest Complete", player))
        set_rule(multiworld.get_location("Snakeblock [Stone D1]", player),
                 lambda state: state.has("Topaz Quest Complete", player))
        set_rule(multiworld.get_location("Snakeblock [Stone E1 - E]", player),
                 lambda state: state.has("Topaz Quest Complete", player))
        set_rule(multiworld.get_location("Snakeblock [Stone C4]", player),
                 lambda state: state.has("Topaz Quest Complete", player))
        set_rule(multiworld.get_location("Snakeblock [Stone Dungeon C4]", player),
                 lambda state: state.has("Topaz Quest Complete", player))
        set_rule(multiworld.get_location("Snakeblock [Stone Dungeon C3]", player),
                 lambda state: state.has("Topaz Quest Complete", player))
        set_rule(multiworld.get_location("Snakeblock [Stone Dungeon B2 - E]", player),
                 lambda state: state.has("Topaz Quest Complete", player))
        set_rule(multiworld.get_location("Snakeblock [Stone Dungeon D2 - E]", player),
                 lambda state: state.has("Topaz Quest Complete", player))
        set_rule(multiworld.get_location("Snakeblock [Stone Dungeon D2 - CE]", player),
                 lambda state: state.has("Topaz Quest Complete", player))
        set_rule(multiworld.get_location("Snakeblock [Stone Dungeon D2 - W]", player),
                 lambda state: state.has("Topaz Quest Complete", player))
        set_rule(multiworld.get_location("Snakeblock [Stone Dungeon D2 - CW]", player),
                 lambda state: state.has("Topaz Quest Complete", player))
        set_rule(multiworld.get_location("Snakeblock [Stone Dungeon D1 - W]", player),
                 lambda state: state.has("Topaz Quest Complete", player))
        set_rule(multiworld.get_location("Snakeblock [Stone Dungeon D1 - CS]", player),
                 lambda state: state.has("Topaz Quest Complete", player))
        set_rule(multiworld.get_location("Snakeblock [Stone Dungeon D1 - E]", player),
                 lambda state: state.has("Topaz Quest Complete", player))
        set_rule(multiworld.get_location("Snakeblock [Stone Dungeon E1]", player),
                 lambda state: state.has("Topaz Quest Complete", player))
        set_rule(multiworld.get_location("Snakeblock [Stone Dungeon E2]", player),
                 lambda state: state.has("Topaz Quest Complete", player))


        set_rule(multiworld.get_location("Snakeblock [Stone Dungeon C1]", player),
                 lambda state: state.has("Gopher Gloves", player)
                           and (state.can_reach("Stony Cliffs NW", "Region", player)
                           or (state.can_reach("Stony Cliffs Post-Rune", "Region", player)
                           and state.has("Topaz Rune Stone", player) ) ) )

        set_rule(multiworld.get_location("Snakeblock [Stone B4]", player),
                 lambda state: state.has("Star Piece", player, 15)
                               and state.has("Gopher Gloves", player))
        set_rule(multiworld.get_location("Snakeblock [Stone A4 - E]", player),
                 lambda state: state.has("Star Piece", player, 15)
                               and state.has("Gopher Gloves", player)
                               and state.has("Topaz Quest Complete", player))

    # Secretsanity
    if self.options.secretsanity.value:
        set_rule(multiworld.get_location("Discover Stone Secret 1", player),
                 lambda state: (state.has("Topaz Quest Complete", player)
                                and state.has("Topaz Rune Stone", player))
                               or state.has("Kite cloak", player))

def set_tidal_reef(self):
    player = self.player
    multiworld = self.multiworld

    set_rule(multiworld.get_location("Ancient Key [Water A0 - S]", player),
             lambda state: state.has("Frog Flippers", player))

    set_rule(multiworld.get_location("Ancient Key [Water A2]", player),
             lambda state: state.has("Frog Flippers", player)
                           and state.has("Sapphire Quest Complete", player))

    set_rule(multiworld.get_location("Ancient Key [Water B3]", player),
             lambda state: state.has("Frog Flippers", player))

    set_rule(multiworld.get_location("Ancient Key [Water C3 - NE1]", player),
             lambda state: state.has("Frog Flippers", player)
                           and state.has("Sapphire Quest Complete", player))
    set_rule(multiworld.get_location("Ancient Key [Water C3 - NE2]", player),
             lambda state: state.has("Frog Flippers", player)
                           and state.has("Sapphire Quest Complete", player))
    set_rule(multiworld.get_location("Ancient Key [Water C3 - NE3]", player),
             lambda state: state.has("Frog Flippers", player)
                           and state.has("Sapphire Quest Complete", player))

    set_rule(multiworld.get_location("Ancient Key [Water D1]", player),
             lambda state: state.has("Frog Flippers", player))

    set_rule(multiworld.get_location("Ancient Key [Water D0]", player),
             lambda state: state.has("Frog Flippers", player))

    set_rule(multiworld.get_location("Ancient Key [Water C0]", player),
             lambda state: state.has("Sapphire Quest Complete", player))

    set_rule(multiworld.get_location("Ancient Key [Water D2]", player),
             lambda state: state.has("Frog Flippers", player)
                           and state.has("Sapphire Quest Complete", player))

    set_rule(multiworld.get_location("Sapphire [Water C2 - N]", player),
             lambda state: state.has("Sapphire Quest Complete", player))

    set_rule(multiworld.get_location("Sapphire [Water A1]", player),
             lambda state: state.has("Frog Flippers", player))

    set_rule(multiworld.get_location("Obsidian [Water D0]", player),
             lambda state: state.has("Frog Flippers", player))

    set_rule(multiworld.get_location("Star Piece [Water C0]", player),
             lambda state: state.has("Sapphire Quest Complete", player))

    set_rule(multiworld.get_location("Star Piece [Water C2]", player),
             lambda state: state.has("Frog Flippers", player) and state.has("Sapphire Quest Complete", player)  )

    set_rule(multiworld.get_location("Star Piece [Water D2]", player),
             lambda state: state.has("Frog Flippers", player)
                           and state.has("Kite Cloak", player) )

    set_rule(multiworld.get_location("Star Piece [Water D3]", player),
             lambda state: state.has("Frog Flippers", player)
                           and state.has("Sapphire Quest Complete", player))

    set_rule(multiworld.get_location("Star Piece [Water E0 - W]", player),
             lambda state: state.has("Sapphire Quest Complete", player)
                           or state.has("Kite Cloak", player) )

    set_rule(multiworld.get_location("Star Piece [Water E0 - E]", player),
             lambda state: state.has("Frog Flippers", player))

    set_rule(multiworld.get_location("Star Piece [Water E2]", player),
             lambda state: state.has("Frog Flippers", player))

    set_rule(multiworld.get_location("Star Piece [Water B1]", player),
             lambda state: state.has("Sapphire Quest Complete", player)
             and state.has("Frog Flippers", player) )

    set_rule(multiworld.get_location("Star Piece [Water A2 - N]", player),
             lambda state: state.has("Sapphire Quest Complete", player)
                           and state.has("Frog Flippers", player)
                           and state.has("Star Piece", player, 30))

    set_rule(multiworld.get_location("Star Piece [Water B4]", player),
             lambda state: state.has("Frog Flippers", player)
                           or state.has("Phoenix Flute", player)
                           or state.has("Sapphire Rune Stone", player))

    set_rule(multiworld.get_location("Star Piece [Water A2 - S]", player),
             lambda state: state.has("Sapphire Quest Complete", player)
                           and state.has("Frog Flippers", player)
                           and state.has("Star Piece", player, 30))

    set_rule(multiworld.get_location("Star Piece [Water A4]", player),
             lambda state: state.has("Frog Flippers", player) )

    set_rule(multiworld.get_location("Star Piece [Water C1 - W]", player),
             lambda state: state.has("Ancient Key", player, 32))

    # IncludeShells
    if self.options.include_seashells.value:

        set_rule(multiworld.get_location("Shell [Water B2]", player),
                 lambda state: state.has("Frog Flippers", player))

        set_rule(multiworld.get_location("Shell [Water B3]", player),
                 lambda state: state.has("Frog Flippers", player)
                               or state.has("Phoenix Flute", player)
                               or state.has("Sapphire Rune Stone", player) )

        set_rule(multiworld.get_location("Shell [Water B4]", player),
                 lambda state: state.has("Frog Flippers", player)
                               or state.has("Phoenix Flute", player)
                               or state.has("Sapphire Rune Stone", player))

        set_rule(multiworld.get_location("Shell [Water C4]", player),
                 lambda state: state.has("Frog Flippers", player)
                               or state.has("Phoenix Flute", player)
                               or state.has("Sapphire Rune Stone", player))

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

        set_rule(multiworld.get_location("Shell [Water A3]", player),
                 lambda state: state.has("Frog Flippers", player)
                               or state.has("Sapphire Rune Stone", player))

    # Locksanity
    if self.options.enable_locksanity.value:
        set_rule(multiworld.get_location("Lock [Water B2]", player),
                 lambda state: state.has("Ancient Key", player, 29))

        set_rule(multiworld.get_location("3x Lock [Water C1]", player),
                 lambda state: state.has("Ancient Key", player, 32))

        set_rule(multiworld.get_location("Lock [Water D3]", player),
                 lambda state: state.has("Ancient Key", player, 33))

        set_rule(multiworld.get_location("Star Lock 30 [Water A2]", player),
                 lambda state: state.has("Frog Flippers", player)
                               and state.has("Sapphire Quest Complete", player))

    # Snakesanity
    if self.options.enable_snakesanity.value:
        set_rule(multiworld.get_location("Snakeblock [Water B0 - E]", player),
                 lambda state: state.has("Sapphire Quest Complete", player))
        set_rule(multiworld.get_location("Snakeblock [Water B0 - C]", player),
                 lambda state: state.has("Sapphire Quest Complete", player))
        set_rule(multiworld.get_location("Snakeblock [Water B1 - E]", player),
                 lambda state: state.has("Sapphire Quest Complete", player))
        set_rule(multiworld.get_location("Snakeblock [Water B1 - C]", player),
                 lambda state: state.has("Sapphire Quest Complete", player))

        set_rule(multiworld.get_location("Snakeblock [Water B4]", player),
                 lambda state: state.has("Frog Flippers", player)
                               or state.has("Phoenix Flute", player)
                               or state.has("Sapphire Rune Stone", player))

        set_rule(multiworld.get_location("Snakeblock [Water D2 - C]", player),
                 lambda state: state.has("Frog Flippers", player))
        set_rule(multiworld.get_location("Snakeblock [Water D2 - E]", player),
                 lambda state: state.has("Frog Flippers", player))
        set_rule(multiworld.get_location("Snakeblock [Water E1 - W]", player),
                 lambda state: state.has("Frog Flippers", player))
        set_rule(multiworld.get_location("Snakeblock [Water E1 - E]", player),
                 lambda state: state.has("Frog Flippers", player))
        set_rule(multiworld.get_location("Snakeblock [Water E2 - E]", player),
                 lambda state: state.has("Frog Flippers", player))
        set_rule(multiworld.get_location("Snakeblock [Water A0 - S]", player),
                 lambda state: state.has("Frog Flippers", player))

        set_rule(multiworld.get_location("Snakeblock [Water A2]", player),
                 lambda state: state.has("Frog Flippers", player)
                               and state.has("Sapphire Quest Complete", player)
                               and state.has("Star Piece", player, 30))

        set_rule(multiworld.get_location("Snakeblock [Water A3]", player),
                 lambda state: state.has("Frog Flippers", player)
                               and state.has("Sapphire Quest Complete", player)
                               and state.has("Star Piece", player, 30))

def set_raging_volcano(self):
    player = self.player
    multiworld = self.multiworld

    set_rule(multiworld.get_location("Ancient Key [Fire A2 - S]", player),
             lambda state: state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Ancient Key [Fire B4]", player),
             lambda state: state.has("Ruby Quest Complete", player))

    set_rule(multiworld.get_location("Ancient Key [Fire A1 - NE]", player),
             lambda state: state.has("Salamander Shirt", player))
    set_rule(multiworld.get_location("Ancient Key [Fire A1 - E]", player),
             lambda state: state.has("Salamander Shirt", player))
    set_rule(multiworld.get_location("Ancient Key [Fire A1 - S]", player),
             lambda state: state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Ancient Key [Fire B1 - N1]", player),
             lambda state: state.has("Ruby Quest Complete", player) and state.has("Salamander Shirt", player))
    set_rule(multiworld.get_location("Ancient Key [Fire B1 - N2]", player),
             lambda state: state.has("Ruby Quest Complete", player) and state.has("Salamander Shirt", player))
    set_rule(multiworld.get_location("Ancient Key [Fire B1 - N3]", player),
             lambda state: state.has("Ruby Quest Complete", player) and state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Ancient Key [Fire C1 - NE]", player),
             lambda state: state.has("Salamander Shirt", player)
                           and state.has("Ruby Quest Complete", player))

    set_rule(multiworld.get_location("Star Piece [Fire C1]", player),
             lambda state: state.has("Ruby Quest Complete", player))

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

    set_rule(multiworld.get_location("Star Piece [Fire C0]", player),
             lambda state: state.has("Ruby Quest Complete", player))

    set_rule(multiworld.get_location("Star Piece [Fire D1 - N]", player),
             lambda state: state.has("Ruby Quest Complete", player))
    set_rule(multiworld.get_location("Star Piece [Fire D1 - S]", player),
             lambda state: state.has("Ancient Key", player, 38))

    set_rule(multiworld.get_location("Star Piece [Fire D3 - S]", player),
             lambda state: state.has("Ruby Quest Complete", player) and state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Star Piece [Fire D3 - W]", player),
             lambda state: state.has("Ruby Quest Complete", player) and state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Star Piece [Fire E3]", player),
             lambda state: state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Star Piece [Fire D4]", player),
             lambda state: state.has("Frog Flippers", player)
                           and state.has("Salamander Shirt", player)
                           and state.has("Ruby Quest Complete", player))

    set_rule(multiworld.get_location("Star Piece [Fire E1 - E]", player),
             lambda state: state.has("Ruby Quest Complete", player) and state.has("Salamander Shirt", player) )

    set_rule(multiworld.get_location("Star Piece [Fire E1 - W]", player),
             lambda state: state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Star Piece [Fire E0]", player),
             lambda state: state.has("Salamander Shirt", player) )

    set_rule(multiworld.get_location("Music Note [Fire B0]", player),
             lambda state: state.has("Salamander Shirt", player))

    set_rule(multiworld.get_location("Music Note [Fire D3]", player),
             lambda state: state.has("Salamander Shirt", player))


    # Locksanity
    if self.options.enable_locksanity.value:
        set_rule(multiworld.get_location("Lock [Fire D2]", player),
                 lambda state: state.has("Ancient Key", player, 35))

        set_rule(multiworld.get_location("3x Lock [Fire D2]", player),
                 lambda state: state.has("Ancient Key", player, 38))

        set_rule(multiworld.get_location("Lock [Fire A3]", player),
                 lambda state: state.has("Ancient Key", player, 39))

        set_rule(multiworld.get_location("3x Lock (Fire) [Fire E0]", player),
                 lambda state: state.has("Fire Key", player, 3))

        set_rule(multiworld.get_location("Ruby Rune Lock [Fire A1 - E]", player),
                 lambda state: state.has("Salamander Shirt", player))

        set_rule(multiworld.get_location("Ruby Rune Lock [Fire B2 - N]", player),
                 lambda state: state.has("Salamander Shirt", player))

    # Snakesanity
    if self.options.enable_snakesanity.value:
        set_rule(multiworld.get_location("Snakeblock [Fire B4 - W]", player),
                 lambda state: state.has("Ruby Quest Complete", player))
        set_rule(multiworld.get_location("Snakeblock [Fire B4 - E]", player),
                 lambda state: state.has("Ruby Quest Complete", player))
        set_rule(multiworld.get_location("Snakeblock [Fire B3 - CW]", player),
                 lambda state: state.has("Ruby Quest Complete", player))
        set_rule(multiworld.get_location("Snakeblock [Fire B3 - W]", player),
                 lambda state: state.has("Ruby Quest Complete", player))
        set_rule(multiworld.get_location("Snakeblock [Fire B3 - CE]", player),
                 lambda state: state.has("Ruby Quest Complete", player))
        set_rule(multiworld.get_location("Snakeblock [Fire C3 - E]", player),
                 lambda state: state.has("Ruby Quest Complete", player))


        set_rule(multiworld.get_location("Snakeblock [Fire D1 - SE]", player),
                 lambda state: state.has("Salamander Shirt", player)
                               and state.has("Ancient Key", player, 38))
        set_rule(multiworld.get_location("Snakeblock [Fire B1]", player),
                 lambda state: state.has("Salamander Shirt", player))
        set_rule(multiworld.get_location("Snakeblock [Fire D4 - E]", player),
                 lambda state: state.has("Salamander Shirt", player))
        set_rule(multiworld.get_location("Snakeblock [Fire E4 - CE]", player),
                 lambda state: state.has("Salamander Shirt", player))
        set_rule(multiworld.get_location("Snakeblock [Fire E4 - W]", player),
                 lambda state: state.has("Salamander Shirt", player))
        set_rule(multiworld.get_location("Snakeblock [Fire D3 - W]", player),
                 lambda state: state.has("Salamander Shirt", player))
        set_rule(multiworld.get_location("Snakeblock [Fire D2 - SE]", player),
                 lambda state: state.has("Salamander Shirt", player))
        set_rule(multiworld.get_location("Snakeblock [Fire A1 - E]", player),
                 lambda state: state.has("Salamander Shirt", player))

        set_rule(multiworld.get_location("Snakeblock [Fire D3 - E]", player),
                 lambda state: state.has("Salamander Shirt", player)
                               and state.has("Ruby Quest Complete", player))
        set_rule(multiworld.get_location("Snakeblock [Fire D3 - SW]", player),
                 lambda state: state.has("Salamander Shirt", player)
                               and state.has("Ruby Quest Complete", player))

    # Secretsanity
    if self.options.secretsanity.value:
        set_rule(multiworld.get_location("Discover Fire Secret 2", player),
                 lambda state: state.has("Salamander Shirt", player))
        set_rule(multiworld.get_location("Discover Fire Secret 3", player),
                 lambda state: state.has("Salamander Shirt", player))

def set_frozen_spire(self):
    player = self.player
    multiworld = self.multiworld

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

    set_rule(multiworld.get_location("Ancient Key [Wind E4 - E]", player),
             lambda state: state.has("Diamond Quest Complete", player)
                           and state.has("Kite Cloak", player))

    set_rule(multiworld.get_location("Ancient Key [Wind E4 - SW]", player),
             lambda state: state.has("Diamond Quest Complete", player)
                           and state.has("Kite Cloak", player))

    set_rule(multiworld.get_location("Diamond [Wind C3]", player),
             lambda state: state.has("Diamond Quest Complete", player))
    set_rule(multiworld.get_location("Diamond [Wind D1 - E]", player),
             lambda state: state.has("Kite Cloak", player)
                           or state.has("Diamond Quest Complete", player))

    set_rule(multiworld.get_location("Star Piece [Wind B3]", player),
             lambda state: state.has("Kite Cloak", player)
                               and state.has("Diamond Quest Complete", player))

    set_rule(multiworld.get_location("Star Piece [Wind A3]", player),
             lambda state: state.has("Diamond Quest Complete", player))

    set_rule(multiworld.get_location("Star Piece [Wind B2 - N]", player),
             lambda state: state.has("Diamond Quest Complete", player)
                           or state.has("Kite Cloak", player))

    set_rule(multiworld.get_location("Star Piece [Wind C2]", player),
             lambda state: state.has("Diamond Quest Complete", player))

    set_rule(multiworld.get_location("Star Piece [Wind D2]", player),
             lambda state: state.has("Kite Cloak", player))

    set_rule(multiworld.get_location("Star Piece [Wind E2]", player),
             lambda state: state.has("Diamond Quest Complete", player))

    set_rule(multiworld.get_location("Star Piece [Wind E4]", player),
             lambda state: state.has("Diamond Quest Complete", player))

    set_rule(multiworld.get_location("Star Piece [Wind E1]", player),
             lambda state: state.has("Kite Cloak", player)
                           and state.has("Gopher Gloves", player))

    set_rule(multiworld.get_location("Star Piece [Wind A0]", player),
             lambda state: state.has("Kite Cloak", player))

    set_rule(multiworld.get_location("Star Piece [Wind C3 - NE]", player),
             lambda state: state.has("Diamond Quest Complete", player))

    set_rule(multiworld.get_location("Music Note [Wind A2]", player),
             lambda state: state.has("Diamond Quest Complete", player))

    set_rule(multiworld.get_location("Music Note [Wind D3]", player),
             lambda state: state.has("Diamond Quest Complete", player))

    set_rule(multiworld.get_location("Music Note [Wind E3]", player),
             lambda state: state.has("Diamond Quest Complete", player))


    # Locksanity
    if self.options.enable_locksanity.value:
        set_rule(multiworld.get_location("3x Lock [Wind D3]", player),
                 lambda state: state.has("Ancient Key", player, 45))

        set_rule(multiworld.get_location("Lock [Wind C3]", player),
                 lambda state: state.has("Ancient Key", player, 46)
                               and state.has("Diamond Quest Complete", player))

        set_rule(multiworld.get_location("Lock [Wind D1]", player),
                 lambda state: state.has("Ancient Key", player, 47) )

        set_rule(multiworld.get_location("Lock (Wind) [Wind A0]", player),
                 lambda state: state.has("Diamond Rune Stone", player)) # Remove later when wind key item is fixed

    # Snakesanity
    if self.options.enable_snakesanity.value:
        set_rule(multiworld.get_location("Snakeblock [Wind A2 - SE]", player),
                 lambda state: state.has("Diamond Quest Complete", player))
        set_rule(multiworld.get_location("Snakeblock [Wind E4]", player),
                 lambda state: state.has("Diamond Quest Complete", player))
        set_rule(multiworld.get_location("Snakeblock [Wind E3]", player),
                 lambda state: state.has("Diamond Quest Complete", player))
        set_rule(multiworld.get_location("Snakeblock [Wind C2]", player),
                 lambda state: state.has("Diamond Quest Complete", player))

        set_rule(multiworld.get_location("Snakeblock [Wind B3 - CE]", player),
                 lambda state: state.has("Kite Cloak", player))
        set_rule(multiworld.get_location("Snakeblock [Wind B3 - NE]", player),
                 lambda state: state.has("Kite Cloak", player))
        set_rule(multiworld.get_location("Snakeblock [Wind B2 - SW]", player),
                 lambda state: state.has("Diamond Quest Complete", player))
        set_rule(multiworld.get_location("Snakeblock [Wind B4]", player),
                 lambda state: state.has("Kite Cloak", player))

        set_rule(multiworld.get_location("Snakeblock [Wind E1]", player),
                 lambda state: state.has("Gopher Gloves", player)
                               and state.has("Kite Cloak", player))

    # Secretsanity
    if self.options.secretsanity.value:
        set_rule(multiworld.get_location("Discover Wind Secret 3", player),
                 lambda state: state.has("Kite Cloak", player))

def set_beast_bridge(self):
    player = self.player
    multiworld = self.multiworld

    set_rule(multiworld.get_location("Phoenix Flute", player),
             lambda state: state.can_reach("Beast Bridge", "Region", player))

    set_rule(multiworld.get_location("Beast Bell Stone", player),
             lambda state: state.has("Rolling Bell Rung", player)
                           and state.has("Sunken Bell Rung", player)
                           and state.has("Aggro Bell Rung", player)
                           and state.has("Nunatak Bell Rung", player))

def set_sanctum(self):
    player = self.player
    multiworld = self.multiworld

    set_rule(multiworld.get_location("Topaz Shard Hit", player),
             lambda state: state.has("Ancient Key", player, 51))

    set_rule(multiworld.get_location("Sapphire Shard Hit", player),
             lambda state: state.has("Ancient Key", player, 54))

    set_rule(multiworld.get_location("Diamond Shard Hit", player),
             lambda state: state.has("Ancient Key", player, 57))

    set_rule(multiworld.get_location("Ruby Shard Hit", player),
             lambda state: state.has("Ancient Key", player, 60))



    # Locksanity
    if self.options.enable_locksanity.value:
        set_rule(multiworld.get_location("3x Lock [Sanctum B2 - W]", player),
                 lambda state: state.has("Ancient Key", player, 51))

        set_rule(multiworld.get_location("3x Lock [Sanctum B2 - E]", player),
                 lambda state: state.has("Ancient Key", player, 54))

        set_rule(multiworld.get_location("3x Lock [Sanctum A1]", player),
                 lambda state: state.has("Ancient Key", player, 57))

        set_rule(multiworld.get_location("3x Lock [Sanctum C1]", player),
                 lambda state: state.has("Ancient Key", player, 60))

    # Snakesanity
    if self.options.enable_snakesanity.value:
        set_rule(multiworld.get_location("Snakeblock [Sanctum A2 - S]", player),
                 lambda state: state.has("Ancient Key", player, 51))
        set_rule(multiworld.get_location("Snakeblock [Sanctum A2 - C]", player),
                 lambda state: state.has("Ancient Key", player, 51))
        set_rule(multiworld.get_location("Snakeblock [Sanctum A2 - W]", player),
                 lambda state: state.has("Ancient Key", player, 51))

        set_rule(multiworld.get_location("Snakeblock [Sanctum C2 - E]", player),
                 lambda state: state.has("Ancient Key", player, 54))
        set_rule(multiworld.get_location("Snakeblock [Sanctum C2 - W]", player),
                 lambda state: state.has("Ancient Key", player, 54))

        set_rule(multiworld.get_location("Snakeblock [Sanctum A0 - E]", player),
                 lambda state: state.has("Ancient Key", player, 57))
        set_rule(multiworld.get_location("Snakeblock [Sanctum A0 - CW]", player),
                 lambda state: state.has("Ancient Key", player, 57))
        set_rule(multiworld.get_location("Snakeblock [Sanctum A0 - CE]", player),
                 lambda state: state.has("Ancient Key", player, 57))
        set_rule(multiworld.get_location("Snakeblock [Sanctum A0 - W]", player),
                 lambda state: state.has("Ancient Key", player, 57))

        set_rule(multiworld.get_location("Snakeblock [Sanctum C0 - W]", player),
                 lambda state: state.has("Ancient Key", player, 60))
        set_rule(multiworld.get_location("Snakeblock [Sanctum C0 - CSW]", player),
                 lambda state: state.has("Ancient Key", player, 60))
        set_rule(multiworld.get_location("Snakeblock [Sanctum C0 - CNW]", player),
                 lambda state: state.has("Ancient Key", player, 60))
        set_rule(multiworld.get_location("Snakeblock [Sanctum C0 - CN]", player),
                 lambda state: state.has("Ancient Key", player, 60))
        set_rule(multiworld.get_location("Snakeblock [Sanctum C0 - E]", player),
                 lambda state: state.has("Ancient Key", player, 60))

def set_rechecks(self):
    # Rechecks reachability later in the fill sweep, so that some unreachable locations can
    # be registered correctly.

    player = self.player
    multiworld = self.multiworld

    multiworld.register_indirect_condition(multiworld.get_region("Obsidian Sea", player),
                                           multiworld.get_entrance("Ancient West Exit", player))

    multiworld.register_indirect_condition(multiworld.get_region("Ruby Sea", player),
                                           multiworld.get_entrance("Locked Entrance", player))


    multiworld.register_indirect_condition(multiworld.get_region("Raging Volcano", player),
             multiworld.get_entrance("Raging Phoenix Entrance", player))

    multiworld.register_indirect_condition(multiworld.get_region("Lost Sea", player),
                                           multiworld.get_entrance("North Diamond Sea East Exit", player))

    multiworld.register_indirect_condition(multiworld.get_region("Lost Sea", player),
                                           multiworld.get_entrance("Star West Exit", player))

    multiworld.register_indirect_condition(multiworld.get_region("Lost Sea", player),
                                           multiworld.get_entrance("Star East Entrance", player))


    multiworld.register_indirect_condition(multiworld.get_region("Obsidian Sea", player),
                                           multiworld.get_entrance("Locked Entrance", player))
    multiworld.register_indirect_condition(multiworld.get_region("Obsidian Sea", player),
                                           multiworld.get_entrance("Ancient West Entrance", player))

    # Later ancient isle checks, and the Locked region
    multiworld.register_indirect_condition(multiworld.get_region("Frozen Spire", player),
                                           multiworld.get_entrance("Locked Entrance", player))
    multiworld.register_indirect_condition(multiworld.get_region("Frozen Spire", player),
                                           multiworld.get_entrance("Ancient West Entrance", player))

    multiworld.register_indirect_condition(multiworld.get_region("Frozen Spire", player),
                                           multiworld.get_entrance("Nunatak Entrance", player))
    multiworld.register_indirect_condition(multiworld.get_region("Frozen Spire", player),
                                           multiworld.get_entrance("Sunken Entrance", player))

def set_completion_rules(self):
    player = self.player
    multiworld = self.multiworld

    # Normal Ending

    if _isles_of_sea_and_sky_is_route(self, 0):
        multiworld.completion_condition[player] = lambda state: state.can_reach("Sanctum Peak", "Region", player)

    # Secret Ending
    elif _isles_of_sea_and_sky_is_route(self, 1):
        multiworld.completion_condition[player] = lambda state: (state.can_reach("Sanctum Peak", "Region", player)
                                                                 and state.has("Ancient Rune Stone", player)
                                                                 and state.has("Topaz Rune Stone", player)
                                                                 and state.has("Sapphire Rune Stone", player)
                                                                 and state.has("Ruby Rune Stone", player)
                                                                 and state.has("Diamond Rune Stone", player)
                                                                 and state.has("Obsidian Rune Stone", player)
                                                                 and state.has("Gopher Gloves", player)
                                                                 and state.has("Frog Flippers", player)
                                                                 and state.has("Salamander Shirt", player)
                                                                 and state.has("Kite Cloak", player)
                                                                 and state.has("Serpent Circlet", player)
                                                                 and state.has("Phoenix Flute", player))
    # All Gems
    elif _isles_of_sea_and_sky_is_route(self, 2):
        multiworld.completion_condition[player] = lambda state: (state.has("Topaz", player, 12)
                                                                 and state.has("Sapphire", player, 12)
                                                                 and state.has("Ruby", player, 12)
                                                                 and state.has("Diamond", player, 12)
                                                                 and state.has("Obsidian", player, 12))

