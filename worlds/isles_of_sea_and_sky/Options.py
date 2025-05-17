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

class PhoenixAnywhere(Toggle):
    """The player can summon the Phoenix in any non-overworld location by pressing: 'E',
    as long as they have picked the Phoenix Flute up."""
    display_name = "Summon Phoenix Anywhere"
    default = 0


@dataclass
class IslesOfSeaAndSkyOptions(PerGameCommonOptions):
    route_required:                             RouteRequired # not implemented
    enable_locksanity:                          EnableLocksanity
    enable_snakesanity:                         EnableSnakesanity # not implemented
    include_seashells:                          IncludeSeashells
    include_jellyfish:                          IncludeJellyfish
    phoenix_anywhere:                           PhoenixAnywhere

