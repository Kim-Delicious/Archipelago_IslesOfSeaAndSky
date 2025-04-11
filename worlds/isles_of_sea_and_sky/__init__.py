from .items import IslesOfSeaAndSkyItem, item_table, non_key_items, key_items, \
    junk_weights, progression_items
from .locations import IslesOfSeaAndSkyAdvancement, advancement_table, exclusion_table
from .regions import isles_of_sea_and_sky_regions, link_isles_of_sea_and_sky_areas
from .rules import set_rules, set_completion_rules
from worlds.generic.Rules import exclusion_rules
from BaseClasses import Region, Entrance, Tutorial, Item
#from .Options import IslesOfSeaAndSkyOptions
from worlds.AutoWorld import World, WebWorld
from worlds.LauncherComponents import Component, components
from multiprocessing import Process
import worlds.LauncherComponents as LauncherComponents





def launch_client() -> None:
    from .client import main
    LauncherComponents.launch_subprocess(main, name="IslesOfSeaAndSkyClient")


LauncherComponents.components.append(
    LauncherComponents.Component(
        "Isles Of Sea And Sky Client",
        func=launch_client,
        component_type=LauncherComponents.Type.CLIENT,
        icon="isles_of_sea_and_sky"
    )
)

LauncherComponents.icon_paths["isles_of_sea_and_sky"] = f"ap:{__name__}/data/isles_of_sea_and_sky.png"

def data_path(file_name: str):
    import pkgutil
    return pkgutil.get_data(__name__, "data/" + file_name)


class IslesOfSeaAndSkyWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Archipelago Isles Of Sea And Sky software on your computer. This guide covers "
        "single-player, multiworld, and related software.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Mewlif"]
    )]


class IslesOfSeaAndSkyWorld(World):
    """
    Isles Of Sea And Sky needs a full description
    """
    game = "Isles Of Sea And Sky"
    #options_dataclass = IslesOfSeaAndSkyOptions
    #options: IslesOfSeaAndSkyOptions
    web = IslesOfSeaAndSkyWeb()

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.id for name, data in advancement_table.items()}

    def _get_isles_of_sea_and_sky_data(self):
        return {
            "world_seed": self.random.getrandbits(32),
            "seed_name": self.multiworld.seed_name,
            "player_name": self.multiworld.get_player_name(self.player),
            "player_id": self.player,
            "client_version": self.required_client_version,
            #"race": self.multiworld.is_race,
            #"route": self.options.route_required.current_key,
            #"starting_area": self.options.starting_area.current_key,

        }

    def get_filler_item_name(self):

        junk_pool = junk_weights


    def create_items(self):
        # Plando Most of Ancient Isle to prevent soft lock
        self.multiworld.get_location("Ancient Key [Ancient B3]", self.player).place_locked_item(
            self.create_item("Ancient Key"))
        self.multiworld.get_location("Ancient Key [Ancient A1]", self.player).place_locked_item(
            self.create_item("Ancient Key"))
        self.multiworld.get_location("Ancient Key [Ancient A2 - SE]", self.player).place_locked_item(
            self.create_item("Ancient Key"))
        self.multiworld.get_location("Ancient Key [Ancient A3 - N]", self.player).place_locked_item(
            self.create_item("Ancient Key"))
        self.multiworld.get_location("Ancient Key [Ancient A3 - S]", self.player).place_locked_item(
            self.create_item("Ancient Key"))
        self.multiworld.get_location("Ancient Key [Ancient C2]", self.player).place_locked_item(
            self.create_item("Ancient Key"))


        self.multiworld.get_location("Star Piece [Ancient C0]", self.player).place_locked_item(
            self.create_item("Star Piece"))

        # Generate item pool
        itempool = []
        junk_pool = junk_weights.copy()
        # Add all required progression items
        for name, num in progression_items.items():
            itempool += [name] * num
        for name, num in key_items.items():
            itempool += [name] * num
        for name, num in non_key_items.items():
            itempool += [name] * num


        #starting_key = self.options.starting_area.current_key.title() + " Key"
        #itempool.remove(starting_key)
        #self.multiworld.push_precollected(self.create_item(starting_key))

        # Choose locations to automatically exclude based on settings
        #exclusion_pool = set()
        #exclusion_pool.update(exclusion_table)

        # Choose locations to automatically exclude based on settings
        #exclusion_checks = set()
        #exclusion_checks.update(["Normal Ending Reached"])
        #exclusion_rules(self.multiworld, self.player, exclusion_checks)

        # Convert itempool into real items
        itempool = [item for item in map(lambda name: self.create_item(name), itempool)]
        # Fill remaining items with randomly generated junk or Temmie Flakes
        while len(itempool) < len(self.multiworld.get_unfilled_locations(self.player)):
            #itempool.append(self.create_filler())
            for name, num in junk_weights.items():
                itempool += [name] * num

        self.multiworld.itempool += itempool

    def set_rules(self):
        set_rules(self)
        set_completion_rules(self)

    def create_regions(self):
        def IslesOfSeaAndSkyRegion(region_name: str, exits=[]):
            ret = Region(region_name, self.player, self.multiworld)
            ret.locations += [IslesOfSeaAndSkyAdvancement(self.player, loc_name, loc_data.id, ret)
                              for loc_name, loc_data in advancement_table.items()
                              if loc_data.region == region_name]

            for exit in exits:
                ret.exits.append(Entrance(self.player, exit, ret))
            return ret

        self.multiworld.regions += [IslesOfSeaAndSkyRegion(*r) for r in isles_of_sea_and_sky_regions]
        link_isles_of_sea_and_sky_areas(self.multiworld, self.player)

    def fill_slot_data(self):
        return self._get_isles_of_sea_and_sky_data()

    def create_item(self, name: str) -> Item:
        item_data = item_table[name]
        item = IslesOfSeaAndSkyItem(name, item_data.classification, item_data.code, self.player)
        return item
