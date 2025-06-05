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


class EnableSnakesanity(Toggle):
    """Turn all snake blocks  in the game into game checks.
     (Snake block = Green directional block with an arrowhead on top)"""
    display_name = "Enable Snakesanity"
    default = 0

class EnableSecretsanity(Toggle):
    """Turns a number of in-game secrets in to location checks.
    These include secret paths, and blocks that are disguised"""

    display_name = "Enable Secretsanity"
    default = 0


class IncludeSeashells(Toggle):
    """Enable seashells on the Tidal Reef island for extra checks"""
    display_name = "Include Seashells"
    default = 0


class IncludeJellyfish(Toggle):
    """Enable jellyfish in the Overworld for extra checks"""
    display_name = "Include Jellyfish"
    default = 0

class PhoenixAnywhere(Toggle):
    """The player can summon the Phoenix in any non-overworld location by pressing: 'E',
    as long as they have picked the Phoenix Flute up."""
    display_name = "Summon Phoenix Anywhere"
    default = 1

class FillerComposition(Choice):
    """Determines what items are sent as Filler, allowing the player to make faster progress
    depending on the option selected.
     Default: only allows Seashells as filler.
     Extra Goodies: adds Ancient Keys, Star Pieces, and Gems to the filler pool.
     Only Goodies: replaces the entire filler pool with Ancient Keys, Star Pieces and Gems."""
    display_name = "Filler Composition"
    option_default = 0
    option_extra_goodies = 1
    option_only_goodies = 2
    default = 0



@dataclass
class IslesOfSeaAndSkyOptions(PerGameCommonOptions):
    route_required:                             RouteRequired
    enable_locksanity:                          EnableLocksanity
    enable_snakesanity:                         EnableSnakesanity
    include_seashells:                          IncludeSeashells
    include_jellyfish:                          IncludeJellyfish
    phoenix_anywhere:                           PhoenixAnywhere
    filler_composition:                         FillerComposition
    secretsanity:                               EnableSecretsanity

