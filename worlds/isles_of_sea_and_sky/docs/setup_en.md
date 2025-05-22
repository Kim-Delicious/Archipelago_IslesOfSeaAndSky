# Isles Of Sea And Sky Randomizer Setup Guide

### Required Software

- Isles Of Sea And Sky from the [Steam page](https://store.steampowered.com/app/1233070/Isles_of_Sea_and_Sky/)
- Archipelago from the [Archipelago Releases Page](https://github.com/ArchipelagoMW/Archipelago/releases)
- Delta Patcher from the [Delta Patcher Page](https://www.romhacking.net/utilities/704/)

### First time setup

#### Patch the Game

First, the game needs to be patched in order to be compatibale with Archipelago.

Open up Delta Patcher, and there will be two folder icons. One with 'Original File', and the other with 'XDelta Patch'. Click on 'Original File' Icon, and use the prompt window to find the game directory. This is usually located `C:\Program Files\Steam\steamapps\IslesOfSeaAndSky`
Inside the game directory select the **data.win** file.

Now, click on the second icon, 'XDelta Patch', and navigate to your download of the Isles Of Sea And Sky APWorld, and find the data folder.
It will likely be here: `C:\..\Archipelago\worlds\isles_of_sea_and_sky\data` Inside you will find the **patch.xDelta** file. 
Select it, then click **Apply Patch**



### Connect to the MultiServer

Make sure both Isles Of Sea And Sky and its Client are running. 

In the top text box of the client, type the `IP Address` (or `Hostname`) and `Port` separated with a `:` symbol. 
(Ex. `archipelago.gg:38281`)

The client will then ask for the slot name, input your slot name chosen during YAML creation in the text box at the 
bottom of the client.



### Play the game

When the console tells you that you have joined the room, you're all set. Congratulations on successfully joining a
multi-world game!


### Where do I get a YAML file?

A Template file can be found in `..\Archipelago\worlds\isles_of_sea_and_sky\data`, or should be found on the release page.
