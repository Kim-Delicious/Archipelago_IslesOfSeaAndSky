import os.path
import random
import warnings

from .Items import IslesOfSeaAndSkyItem, item_table, non_key_items, key_items, \
    junk_weights, progression_items, trap_weights
from .Locations import IslesOfSeaAndSkyAdvancement, advancement_table, exclusion_table, \
    jellyfish_table, seashell_table, locksanity_table, snakesanity_table, secrets_table
from .Regions import isles_of_sea_and_sky_regions, link_isles_of_sea_and_sky_areas
from .Rules import set_rules, set_completion_rules
#from worlds.generic.Rules import exclusion_rules
from BaseClasses import Region, Entrance, Tutorial, Item
from .Options import IslesOfSeaAndSkyOptions, EnableSecretsanity, EnableSnakesanity, EnableLocksanity, isles_of_sea_and_sky_option_groups
from worlds.AutoWorld import World, WebWorld
import worlds.LauncherComponents as LauncherComponents

from settings import (
    Group,
    FilePath,
)





def launch_client() -> None:
    from .Client import main
    LauncherComponents.launch_subprocess(main, name="IslesOfSeaAndSkyClient")


LauncherComponents.components.append(
    LauncherComponents.Component(
        "Isles Of Sea And Sky Client",
        func=launch_client,
        component_type=LauncherComponents.Type.CLIENT,
        icon="isles_of_sea_and_sky"
    )
)


isles_component = LauncherComponents.components[len(LauncherComponents.components) - 1]
# Checks first component for a Class property that should be shared by all components
# for backwards compatibility
if hasattr(isles_component, "description"):
    isles_component.description = "That Sokoban Adventure Game by Cicada Games!"

LauncherComponents.icon_paths["isles_of_sea_and_sky"] = f"ap:{__name__}/data/sprites/isles_of_sea_and_sky.png"

def data_path(file_name: str):
    import pkgutil
    return pkgutil.get_data(__name__, "data/" + file_name)

def read_data(file_path: str):
    import pkgutil
    return pkgutil.get_data(__name__, file_path)


class IslesOfSeaAndSkySettings(Group):
    class GMDataFile(FilePath):
        """Path to IslesOfSeaAndSky Vanilla data file"""
        description = "Isles Of Sea And Sky Vanilla File"
        md5s = [
            "F24EFE2F28A3DB2B5E4EAA5294DCE25D",  # steam
            #"",  # epic
            # "",  # itch.io, does not work
            ]
        # the hashes for vanilla to be verified by the /patch command
        required = True
    steam_install = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\IslesOfSeaAndSky"
    data_file: GMDataFile = GMDataFile(os.path.join(steam_install, "data.win"))

class IslesOfSeaAndSkyWeb(WebWorld):
    theme = "ocean"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Archipelago Isles Of Sea And Sky software on your computer. This guide covers "
        "single-player, multiworld, and related software.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Kim-Delicious"]
    )]

    option_groups = isles_of_sea_and_sky_option_groups


class IslesOfSeaAndSkyWorld(World):
    """
    Isles Of Sea And Sky is a sokoban-style puzzle game with metroidvania elements.
    As the player collects items, and equipment they can explore islands to collect as many goodies as they can,
    until they reach the Sanctum, and learn just what all these Stars are for.
    """
    game = "Isles Of Sea And Sky"
    options_dataclass = IslesOfSeaAndSkyOptions
    settings: IslesOfSeaAndSkySettings
    options: IslesOfSeaAndSkyOptions
    web = IslesOfSeaAndSkyWeb()

    #explicit_indirect_conditions = False

    item_name_to_id = {name: data.code for name, data in item_table.items()}

    location_name_to_id = (
            {name: data.id for name, data in advancement_table.items()} |
            {name: data.id for name, data in jellyfish_table.items()} |
            {name: data.id for name, data in seashell_table.items()} |
            {name: data.id for name, data in locksanity_table.items()} |
            {name: data.id for name, data in snakesanity_table.items()}|
            {name: data.id for name, data in secrets_table.items()}
    )


    def _get_isles_of_sea_and_sky_data(self):
        return {
            "world_seed":           self.random.getrandbits(32),
            "seed_name":            self.multiworld.seed_name,
            "player_name":          self.multiworld.get_player_name(self.player),
            "player_id":            self.player,
            "client_version":       self.required_client_version,
            "race":                 self.multiworld.is_race,
            "route_required":       self.options.route_required.current_key,
            "enable_locksanity":    bool(self.options.enable_locksanity.value),
            "enable_snakesanity":   bool(self.options.enable_snakesanity.value),
            "include_seashells":    bool(self.options.include_seashells.value),
            "include_jellyfish":    bool(self.options.include_jellyfish.value),
            "phoenix_anywhere":     bool(self.options.phoenix_anywhere.value),
            "traps":                self.options.traps.current_key,
            "trap_link":            bool(self.options.trap_link.value),
            "filler_composition":   self.options.filler_composition.current_key,
            "secretsanity":         bool(self.options.secretsanity.value),
            "death_link":           bool(self.options.death_link.value),
            "death_amnesty_total":  int(self.options.death_amnesty_total.value),
            "alt_rooms":            bool(self.options.alt_rooms.value),

        }

    def get_filler_item_name(self):

        junk_pool = junk_weights
        return self.random.choices(list(junk_pool.keys()), weights=list(junk_pool.values()))[0]

    def pre_fill(self) -> None:

        ### A more fine-tuned way to put important items in important places
        ### Prone to Fill errors
        '''priority_locs = self.options.priority_locations.value
        prog_items = list(progression_items.keys())

        for loc_name in priority_locs:
            loc = self.get_location(loc_name)
            item = self.create_item(choice(prog_items) )

            prog_items.remove(item.name)

            loc.place_locked_item(item)
            self.multiworld.itempool.remove(item)'''

        pass

    def create_items(self):

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

        # Create copies of pools so that data isn't changed when multiple worlds are used
        progression_pool = progression_items.copy()
        key_pool = key_items.copy()
        non_key_pool = non_key_items.copy()
        junk_pool = junk_weights.copy()
        trap_pool = trap_weights.copy()


        # Remove the pre-placed items from generation
        key_pool['Ancient Key'] -= 6
        key_pool['Star Piece'] -= 1

        # Bias generation to reduce fill errors
        self.multiworld.early_items[self.player]["Topaz Rune Stone"] = 1

        # Generate item pool
        itempool = []
        # Add all required progression items
        for name, num in progression_pool.items():
            itempool += [name] * num
        for name, num in key_pool.items():
            itempool += [name] * num
        for name, num in non_key_pool.items():
            itempool += [name] * num

        missing_items = len(self.multiworld.get_unfilled_locations(self.player) ) - len(itempool)
        print("Creating " + str(missing_items) + " Filler Items for " + str(self.game) )

        # Create a limited number of traps based on a weighted list of items.
        trap_number = 0
        match self.options.traps.current_key:
            case "some_traps":
                trap_number = self.random.randrange(4, 9)
            case "plenty_traps":
                trap_number = self.random.randrange(10, 20)
            case _:  # default
                pass

        if trap_number > missing_items:
            trap_number = missing_items

        if trap_number > 0:
            print("Converting " + str(trap_number) + " Filler Items into Traps")
            trap_item_weights = []

            for name, num in trap_pool.items():
                trap_item_weights += [name] * num

            while trap_number > 0:
                rand_item = self.random.choice(trap_item_weights)
                itempool += [rand_item]
                trap_number -= 1
                missing_items -= 1

        weight_list = []
        # Add filler weights to potential filler pool
        for name, num in junk_pool.items():
            match self.options.filler_composition.current_key:
                case "extra_goodies":
                    pass
                case "only_goodies":
                    if name == "Seashell":
                        continue
                case _: # default
                    weight_list += ["Seashell"] * num
                    break
            weight_list += [name] * num

        # For each free filler spot, choose an item from weight_list at random, then add it to the item pool
        while missing_items > 0:
            rand_item = self.random.choice(weight_list)
            itempool += [rand_item]
            missing_items = len(self.multiworld.get_unfilled_locations(self.player)) - len(itempool)

        # Convert itempool into real items
        itempool = [item for item in map(lambda item_name: self.create_item(item_name), itempool)]

        self.multiworld.itempool += itempool

    def pick_priorities(self):
        """ Randomly assign locations to priority_locations to
         encourage fill to better utilize gems, and legendary equipment"""
        rand_ints = [1, 2, 3 ,4 ,5]


        if self.random.choice(rand_ints) == 1:  # 20%
            self.options.priority_locations.value.add("Topaz Quest Complete")
        if self.random.choice(rand_ints) == 1:  # 20%
            self.options.priority_locations.value.add("Sapphire Quest Complete")
        if self.random.choice(rand_ints) == 1:  # 20%
            self.options.priority_locations.value.add("Ruby Quest Complete")
        if self.random.choice(rand_ints) == 1:  # 20%
            self.options.priority_locations.value.add("Diamond Quest Complete")
        if self.random.choice(rand_ints) == 1:  # 20%
            self.options.priority_locations.value.add("Serpent Circlet")
        if self.random.choice(rand_ints) == 1:  # 20%
            self.options.priority_locations.value.add("Serpent Circlet")

        rand_ints.pop(len(rand_ints)-1)
        if self.random.choice(rand_ints) == 1:  # 25%
            self.options.priority_locations.value.add("Gopher Gloves")
        if self.random.choice(rand_ints) == 1:  # 25%
            self.options.priority_locations.value.add("Frog Flippers")
        if self.random.choice(rand_ints) == 1:  # 25%
            self.options.priority_locations.value.add("Salamander Shirt")
        if self.random.choice(rand_ints) == 1:  # 25%
            self.options.priority_locations.value.add("Kite Cloak")

        rand_ints.pop(len(rand_ints)-1)
        if self.random.choice(rand_ints) == 1:  # 33%
            self.options.priority_locations.value.add("Phoenix Flute")

        print("Prioritizing Locations...")


    def set_rules(self):
        set_rules(self)
        set_completion_rules(self)

        #self.pick_priorities()

        '''# for creating visuals, should be disabled for unittests
        from Utils import visualize_regions
        state = self.multiworld.get_all_state(False)
        state.update_reachable_regions(self.player)
        state.allow_partial_entrances = True
        visualize_regions(self.get_region("Menu"), "my_world.puml", show_entrance_names=True,
                          regions_to_highlight=state.reachable_regions[self.player])'''

    def create_regions(self):
        def IslesOfSeaAndSkyRegion(region_name: str, exits=None):
            if exits is None:
                exits = []
            ret = Region(region_name, self.player, self.multiworld)

            # Normal locations
            ret.locations += [IslesOfSeaAndSkyAdvancement(self.player, loc_name, loc_data.id, ret)
                              for loc_name, loc_data in advancement_table.items()
                              if loc_data.region == region_name]

            # Locksanity Locations
            if self.options.enable_locksanity:
                ret.locations += [IslesOfSeaAndSkyAdvancement(self.player, loc_name, loc_data.id, ret)
                                  for loc_name, loc_data in locksanity_table.items()
                                  if loc_data.region == region_name]
            # Snakesanity Locations
            if self.options.enable_snakesanity:
                ret.locations += [IslesOfSeaAndSkyAdvancement(self.player, loc_name, loc_data.id, ret)
                                  for loc_name, loc_data in snakesanity_table.items()
                                  if loc_data.region == region_name]
            # Seashell Locations
            if self.options.include_seashells:
                ret.locations += [IslesOfSeaAndSkyAdvancement(self.player, loc_name, loc_data.id, ret)
                                  for loc_name, loc_data in seashell_table.items()
                                  if loc_data.region == region_name]

            # Jellyfish Locations
            if self.options.include_jellyfish:
                ret.locations += [IslesOfSeaAndSkyAdvancement(self.player, loc_name, loc_data.id, ret)
                                  for loc_name, loc_data in jellyfish_table.items()
                                  if loc_data.region == region_name]

            # Secretsanity Locations
            if self.options.secretsanity:
                ret.locations += [IslesOfSeaAndSkyAdvancement(self.player, loc_name, loc_data.id, ret)
                                  for loc_name, loc_data in secrets_table.items()
                                  if loc_data.region == region_name]


            for region_exit in exits:
                ret.exits.append(Entrance(self.player, region_exit, ret))

            return ret

        self.multiworld.regions += [IslesOfSeaAndSkyRegion(*r) for r in isles_of_sea_and_sky_regions]
        link_isles_of_sea_and_sky_areas(self.multiworld, self.player)

    def fill_slot_data(self):
        return self._get_isles_of_sea_and_sky_data()

    def create_item(self, name: str) -> Item:
        if name is None:
            warnings.warn("Attempted to create an item with a None name")
            name = "Seashell"

        item_data = item_table[name]
        item = IslesOfSeaAndSkyItem(name, item_data.classification, item_data.code, self.player)
        return item
