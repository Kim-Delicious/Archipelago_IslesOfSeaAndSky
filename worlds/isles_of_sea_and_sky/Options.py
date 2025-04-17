from Options import Choice, Toggle, Range, PerGameCommonOptions
from dataclasses import dataclass

# NOT IMPLEMENTED YET
class RouteRequired(Choice):
    """Main route of the game required to win."""
    display_name = "Required Route"
    option_normal_ending = 0
    option_secret_ending = 1
    option_all_gems = 2
    default = 0

# Possibility for the future???
class StartingArea(Choice):
    """Which area to start with access to."""
    display_name = "Starting Area"
    option_ruins = 0
    option_snowdin = 1
    option_waterfall = 2
    option_hotland = 3
    option_core = 4
    default = 0

class LocalAncientIsle(Toggle):
    """Make most of the Ancient Isle items to be typical as to prevent the player
    from getting stuck early."""
    display_name = "Local Starting Isle"
    default = 1


class EnableLocksanity(Toggle):
    """Turn all locks in the game into game checks.
    This includes big 3x locks, all Rune Stone locks, and other specialty locks"""
    display_name = "Enable Locksanity"
    default = 0


# NOT IMPLEMENTED YET
class EnableSnakesanity(Toggle):
    """Turn all snake blocks  in the game into game checks.
     (Snake block = Green directional block with an arrowhead on top)"""
    display_name = "Enable Snakesanity"
    default = 0


class IncludeSeashells(Toggle):
    """Enable seashells on the Tidal Reef island for extra checks"""
    display_name = "Include Seashells"
    default = 1


class IncludeJellyfish(Toggle):
    """Enable jellyfish in the Overworld for extra checks"""
    display_name = "Include Jellyfish"
    default = 0


@dataclass
class IslesOfSeaAndSkyOptions(PerGameCommonOptions):
    route_required:                             RouteRequired # not implemented
    starting_area:                              StartingArea # not implemented
    local_ancient_isle:                         LocalAncientIsle
    enable_locksanity:                          EnableLocksanity
    enable_snakesanity:                         EnableSnakesanity # not implemented
    include_seashells:                          IncludeSeashells
    include_jellyfish:                          IncludeJellyfish

