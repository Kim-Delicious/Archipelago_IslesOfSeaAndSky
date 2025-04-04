from __future__ import annotations
import os
import sys
import asyncio
import typing
import bsdiff4
import shutil

import Utils

from NetUtils import NetworkItem, ClientStatus
from worlds import isles_of_sea_and_sky
from MultiServer import mark_raw
from CommonClient import CommonContext, server_loop, \
    gui_enabled, ClientCommandProcessor, logger, get_base_parser
from Utils import async_start


"""

Code taken from the UndertaleClient.

"""

class IslesOfSeaAndSkyCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx):
        super().__init__(ctx)

    def _cmd_resync(self):
        """Manually trigger a resync."""
        if isinstance(self.ctx, IslesOfSeaAndSkyContext):
            self.output(f"Syncing items.")
            self.ctx.syncing = True

    def _cmd_patch(self):
        """Patch the game. Only use this command if /auto_patch fails."""
        if isinstance(self.ctx, IslesOfSeaAndSkyContext):
            os.makedirs(name=Utils.user_path("IslesOfSeaAndSky"), exist_ok=True)
            self.ctx.patch_game()
            self.output("Patched.")

    def _cmd_savepath(self, directory: str):
        """Redirect to proper save data folder. This is necessary for Linux users to use before connecting."""
        if isinstance(self.ctx, IslesOfSeaAndSkyContext):
            self.ctx.save_game_folder = directory
            self.output("Changed to the following directory: " + self.ctx.save_game_folder)

    @mark_raw
    def _cmd_auto_patch(self, steaminstall: typing.Optional[str] = None):
        """Patch the game automatically."""
        if isinstance(self.ctx, IslesOfSeaAndSkyContext):
            os.makedirs(name=Utils.user_path("IslesOfSeaAndSky"), exist_ok=True)
            tempInstall = steaminstall
            if not os.path.isfile(os.path.join(tempInstall, "data.win")):
                tempInstall = None
            if tempInstall is None:
                tempInstall = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\IslesOfSeaAndSky"
                if not os.path.exists(tempInstall):
                    tempInstall = "C:\\Program Files\\Steam\\steamapps\\common\\IslesOfSeaAndSky"
            elif not os.path.exists(tempInstall):
                tempInstall = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\IslesOfSeaAndSky"
                if not os.path.exists(tempInstall):
                    tempInstall = "C:\\Program Files\\Steam\\steamapps\\common\\IslesOfSeaAndSky"
            if not os.path.exists(tempInstall) or not os.path.exists(tempInstall) or not os.path.isfile(os.path.join(tempInstall, "data.win")):
                self.output("ERROR: Cannot find IslesOfSeaAndSky. Please rerun the command with the correct folder."
                            " command. \"/auto_patch (Steam directory)\".")
            else:
                for file_name in os.listdir(tempInstall):
                    if file_name != "steam_api.dll":
                        shutil.copy(os.path.join(tempInstall, file_name),
                               Utils.user_path("IslesOfSeaAndSky", file_name))
                self.ctx.patch_game()
                self.output("Patching successful!")

    def _cmd_online(self):
        """Toggles seeing other IslesOfSeaAndSky players."""
        if isinstance(self.ctx, IslesOfSeaAndSkyContext):
            self.ctx.update_online_mode(not ("Online" in self.ctx.tags))
            if "Online" in self.ctx.tags:
                self.output(f"Now online.")
            else:
                self.output(f"Now offline.")

    def _cmd_deathlink(self):
        """Toggles deathlink"""
        if isinstance(self.ctx, IslesOfSeaAndSkyContext):
            self.ctx.deathlink_status = not self.ctx.deathlink_status
            if self.ctx.deathlink_status:
                self.output(f"Deathlink enabled.")
            else:
                self.output(f"Deathlink disabled.")


class IslesOfSeaAndSkyContext(CommonContext):
    tags = {"AP", "Online"}
    game = "IslesOfSeaAndSky"
    command_processor = IslesOfSeaAndSkyCommandProcessor
    items_handling = 0b111
    route = None
    pieces_needed = None
    completed_routes = None
    completed_count = 0
    save_game_folder = os.path.expandvars(r"%localappdata%/IslesOfSeaAndSky")

    def __init__(self, server_address, password):
        super().__init__(server_address, password)
        self.finished_game = False
        self.game = "IslesOfSeaAndSky"
        self.got_deathlink = False
        self.syncing = False
        self.deathlink_status = False
        # self.save_game_folder: files go in this path to pass data between us and the actual game
        self.save_game_folder = os.path.expandvars(r"%localappdata%/IslesOfSeaAndSky")

    def patch_game(self):
        with open(Utils.user_path("IslesOfSeaAndSky", "data.win"), "rb") as f:
            patchedFile = bsdiff4.patch(f.read(), isles_of_sea_and_sky.data_path("patch.bsdiff"))
        with open(Utils.user_path("IslesOfSeaAndSky", "data.win"), "wb") as f:
            f.write(patchedFile)
        os.makedirs(name=Utils.user_path("IslesOfSeaAndSky", "Custom Sprites"), exist_ok=True)
        with open(os.path.expandvars(Utils.user_path("IslesOfSeaAndSky", "Custom Sprites",
                                     "Which Character.txt")), "w") as f:
            f.writelines(["// Put the folder name of the sprites you want to play as, make sure it is the only "
                          "line other than this one.\n", "frisk"])
            f.close()

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super().server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    def clear_isles_of_sea_and_sky_files(self):
        path = self.save_game_folder
        self.finished_game = False
        for root, dirs, files in os.walk(path):
            for file in files:
                if "check.spot" == file or "scout" == file:
                    os.remove(os.path.join(root, file))
                elif file.endswith((".item", ".victory", ".route", ".playerspot", ".mad", 
                                            ".youDied", ".LV", ".mine", ".flag", ".hint")):
                    os.remove(os.path.join(root, file))

    async def connect(self, address: typing.Optional[str] = None):
        self.clear_isles_of_sea_and_sky_files()
        await super().connect(address)

    async def disconnect(self, allow_autoreconnect: bool = False):
        self.clear_isles_of_sea_and_sky_files()
        await super().disconnect(allow_autoreconnect)

    async def connection_closed(self):
        self.clear_isles_of_sea_and_sky_files()
        await super().connection_closed()

    async def shutdown(self):
        self.clear_isles_of_sea_and_sky_files()
        await super().shutdown()

    def update_online_mode(self, online):
        old_tags = self.tags.copy()
        if online:
            self.tags.add("Online")
        else:
            self.tags -= {"Online"}
        if old_tags != self.tags and self.server and not self.server.socket.closed:
            async_start(self.send_msgs([{"cmd": "ConnectUpdate", "tags": self.tags}]))

    def on_package(self, cmd: str, args: dict):
        if cmd == "Connected":
            self.game = self.slot_info[self.slot].game
        async_start(process_isles_of_sea_and_sky_cmd(self, cmd, args))

    def run_gui(self):
        from kvui import GameManager

        class IOSASManager(GameManager):
            logging_pairs = [
                ("Client", "Archipelago")
            ]
            base_title = "Archipelago IslesOfSeaAndSky Client"

        self.ui = IOSASManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")

    def on_deathlink(self, data: typing.Dict[str, typing.Any]):
        self.got_deathlink = True
        super().on_deathlink(data)


def to_room_name(place_name: str):
    if place_name == "Old Home Exit":
        return "room_ruinsexit"
    elif place_name == "Snowdin Forest":
        return "room_tundra1"
    elif place_name == "Snowdin Town Exit":
        return "room_fogroom"
    elif place_name == "Waterfall":
        return "room_water1"
    elif place_name == "Waterfall Exit":
        return "room_fire2"
    elif place_name == "Hotland":
        return "room_fire_prelab"
    elif place_name == "Hotland Exit":
        return "room_fire_precore"
    elif place_name == "Core":
        return "room_fire_core1"


async def process_isles_of_sea_and_sky_cmd(ctx: IslesOfSeaAndSkyContext, cmd: str, args: dict):
    if cmd == "Connected":
        if not os.path.exists(ctx.save_game_folder):
            os.mkdir(ctx.save_game_folder)
        #ctx.route = args["slot_data"]["route"]




        '''filename = f"{ctx.route}.route"
        with open(os.path.join(ctx.save_game_folder, filename), "w") as f:
            f.close()
            '''
        print(args["checked_locations"])
        for ss in set(args["checked_locations"]):
            filename = str(ss) + ".ini"
            with open(os.path.join(ctx.save_game_folder + "/AP/IN", filename), "a") as f:

                f.write(str(ss))
            f.close()
    elif cmd == "LocationInfo":
        for l in args["locations"]:
            locationid = l.location
            filename = f"{str(locationid)}.hint"
            with open(os.path.join(ctx.save_game_folder, filename), "w") as f:
                toDraw = ""
                for i in range(20):
                    if i < len(str(ctx.item_names.lookup_in_game(l.item))):
                        toDraw += str(ctx.item_names.lookup_in_game(l.item))[i]
                    else:
                        break
                f.write(toDraw)
                f.close()

    elif cmd == "ReceivedItems":
        start_index = args["index"]

        if start_index == 0:
            ctx.items_received = []
        elif start_index != len(ctx.items_received):
            sync_msg = [{"cmd": "Sync"}]
            if ctx.locations_checked:
                sync_msg.append({"cmd": "LocationChecks",
                                 "locations": list(ctx.locations_checked)})
            await ctx.send_msgs(sync_msg)
        if start_index == len(ctx.items_received):
            counter = -1
            for item in args["items"]:
                id = NetworkItem(*item).location
                while NetworkItem(*item).location < 0 and \
                        counter <= id:
                    id -= 1
                if NetworkItem(*item).location < 0:
                    counter -= 1
                #print(NetworkItem(*item))
                ctx.items_received.append(NetworkItem(*item))

        ctx.watcher_event.set()

    elif cmd == "RoomUpdate":
        if "checked_locations" in args:
            filename = f"check.spot"
            with open(os.path.join(ctx.save_game_folder, filename), "a") as f:
                for ss in set(args["checked_locations"]):
                    f.write(str(ss-12000)+"\n")
                f.close()

    ### This is for checking other player's position in-game.
    elif cmd == "Bounced":
        tags = args.get("tags", [])
        if "Online" in tags:
            data = args.get("data", {})


            if data["player"] != ctx.slot and data["player"] is not None:
                filename = str(data["room"]) + "_" + str(data["name"]) + "_" + str(data["total"]) + ".ini"
                path_to_file = os.path.join(ctx.save_game_folder + "\AP\IN", filename)
                if os.path.exists(path_to_file):
                    return

                with open(path_to_file, "w") as f:
                    f.write(str(data["room"]) + "\n" +
                            str(data["name"]) + "\n" +
                            str(data["type"]) + "\n" +
                            str(data["obj_index"]) + "\n" +
                            str(data["total"]) )

                    f.close()



async def multi_watcher(ctx: IslesOfSeaAndSkyContext):
    ### Send a server packet that no one else receives except the original player.
    while not ctx.exit_event.is_set():
        path = ctx.save_game_folder + "/AP/OUT"
        for root, dirs, files in os.walk(path):
            for file in files:
                if "Online" in ctx.tags:
                    with open(os.path.join(root, file), "r") as mine:
                        this_room = mine.readline().replace("\n", "")
                        this_name = mine.readline().replace("\n", "")
                        this_type = mine.readline().replace("\n", "")
                        this_obj_index = mine.readline().replace("\n", "")
                        this_room_total = mine.readline().replace("\n", "")
                        mine.close()

                    message = [{"cmd": "Bounce", "tags": ["Online"],
                                "data": {"player": ctx.slot, "room": this_room, "name": this_name, "type": this_type,
                                         "obj_index": this_obj_index, "total": this_room_total}}]
                    #await ctx.send_msgs(message)

        await asyncio.sleep(0.1)

# Look in the AP/OUT folder for files, and send checks.
async def game_watcher(ctx: IslesOfSeaAndSkyContext):
    while not ctx.exit_event.is_set():
        #await ctx.update_death_link(ctx.deathlink_status)
        path = ctx.save_game_folder + "/AP/OUT"
        if ctx.syncing:
            for root, dirs, files in os.walk(path):
                for file in files:
                    #if ".item" in file:
                    os.remove(os.path.join(root, file))
            sync_msg = [{"cmd": "Sync"}]
            if ctx.locations_checked:
                sync_msg.append({"cmd": "LocationChecks", "locations": list(ctx.locations_checked)})
            await ctx.send_msgs(sync_msg)
            ctx.syncing = False
        if ctx.got_deathlink:
            ctx.got_deathlink = False
            with open(os.path.join(ctx.save_game_folder, "WelcomeToTheDead.youDied"), "w") as f:
                f.close()
        sending = []
        victory = False
        #found_routes = 0
        for root, dirs, files in os.walk(path):
            for file in files:
                if "DontBeMad.mad" in file:
                    os.remove(os.path.join(root, file))
                    if "DeathLink" in ctx.tags:
                        await ctx.send_death()

                if "scout" == file:
                    sending = []
                    try:
                        with open(os.path.join(root, file), "r") as f:
                            lines = f.readlines()
                        for l in lines:
                            if ctx.server_locations.__contains__(int(l)+12000):
                                sending = sending + [int(l.rstrip('\n'))+12000]
                    finally:
                        await ctx.send_msgs([{"cmd": "LocationScouts", "locations": sending,
                                                          "create_as_hint": int(2)}])
                        os.remove(os.path.join(root, file))

                if "victory" in file and str(ctx.route) in file:
                    victory = True
                if ".playerspot" in file and "Online" not in ctx.tags:
                    os.remove(os.path.join(root, file))
                ''''&&"check.spot" in file'''
                if True:
                    sending = []
                    try:
                        with open(os.path.join(root, file), "r") as f:
                            item_id = f.readline()

                        sending = sending + [int(item_id)]

                    finally:
                        await ctx.send_msgs([{"cmd": "LocationChecks", "locations": sending}])
                        os.remove(os.path.join(root, file))
                #if "victory" in file:

        #victory = True
        ctx.locations_checked = sending
        if (not ctx.finished_game) and victory:
            await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
            ctx.finished_game = True

        await asyncio.sleep(0.1)


def main():
    Utils.init_logging("IslesOfSeaAndSkyClient", exception_logger="Client")

    async def _main():
        ctx = IslesOfSeaAndSkyContext(None, None)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")
        asyncio.create_task(
            game_watcher(ctx), name="IslesOfSeaAndSkyProgressionWatcher")

        asyncio.create_task(
            multi_watcher(ctx), name="IslesOfSeaAndSkyMultiplayerWatcher")

        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        await ctx.exit_event.wait()
        await ctx.shutdown()

    import colorama

    colorama.just_fix_windows_console()

    asyncio.run(_main())
    colorama.deinit()


if __name__ == "__main__":
    parser = get_base_parser(description="IslesOfSeaAndSky Client, for text interfacing.")
    args = parser.parse_args()
    main()
