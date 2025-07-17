# Isles Of Sea And Sky Randomizer Setup Guide

### Required Software

- Isles Of Sea And Sky from the [Steam page](https://store.steampowered.com/app/1233070/Isles_of_Sea_and_Sky/)
- Isles Of Sea And Sky [APWorld](https://github.com/Kim-Delicious/Archipelago_IslesOfSeaAndSky/releases)
- Archipelago from the [Archipelago Releases Page](https://github.com/ArchipelagoMW/Archipelago/releases)

### First time setup

#### Patch the Game

First, the game needs to be patched in order to be compatible with Archipelago.

To do this, you need to have Archipelago installed as well as the `isles_of_sea_and_sky.apworld`. 
Once both of these steps are done, run Archipelago, then find and open the Isles Of Sea And Sky Client. Once that pops
up, type in the console: `/auto_patch`. This will freeze the program for a few moments while it's working,
but when that's done you will receive a message:`"Game patched successfully!"`.

If things have worked correctly, the game should launch automatically.

You should now be able to find a `IslesOfSeaAndSky` folder in
the main Archipelago Directory. This is where you will find the copied, and modified version of the game,
and where you will find the correct executable to launch the modded game in the future.


### Connect to the MultiServer

Make sure both Isles Of Sea And Sky and its Client are running. 

In the top text box of the client, type the `IP Address` (or `Hostname`) and `Port` separated with a `:` symbol. 
(Ex. `archipelago.gg:38281`)

The client will then ask for the slot name, input your slot name chosen during YAML creation in the text box at the 
bottom of the client.



### Play the game

When the console tells you that you have joined the room, you're all set. Congratulations on successfully joining a
multi-world game!

### Setup Custom AP Sprites

*(This can only be setup after `/auto_patch` has been run at least once)*

It's possible to display some of the items that will be sent to other players. To make this work you will need. KaitoKids' [Archipelago Utilities](https://github.com/agilbert1412/ArchipelagoUtilities)

In the modded directory for Isles Of Sea And Sky, there should be a folder called `Custom Sprites`. If there is not, create one.

Once you've downloaded the zip folder of Archipelago Utilities, extract it, and copy the folder called `Custom Assets` Into the `Custom Sprites` folder.

And you should be done! Items should now display if you've connected to the multiserver.

### Where do I get a YAML file?

A Template file can be found inside `isles_of_sea_and_sky.apworld` in `/data`, or should be found on the release page.
