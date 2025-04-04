from Options import Choice, Toggle, Range, PerGameCommonOptions
from dataclasses import dataclass


'''class RouteRequired(Choice):
    """Main route of the game required to win."""
    display_name = "Required Route"
    option_neutral = 0
    option_pacifist = 1
    option_genocide = 2
    option_all_routes = 3
    default = 0'''


class StartingArea(Choice):
    """Which area to start with access to."""
    display_name = "Starting Area"
    option_ruins = 0
    option_snowdin = 1
    option_waterfall = 2
    option_hotland = 3
    option_core = 4
    default = 0



@dataclass
class IslesOfSeaAndSkyOptions(PerGameCommonOptions):
    #route_required:                           RouteRequired
    starting_area:                            StartingArea

