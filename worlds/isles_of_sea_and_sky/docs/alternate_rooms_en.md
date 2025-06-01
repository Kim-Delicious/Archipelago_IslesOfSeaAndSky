# Isles Of Sea And Sky - Contributing Alternate Rooms Guide

### Required Software

- Isles Of Sea And Sky from the [Steam page](https://store.steampowered.com/app/1233070/Isles_of_Sea_and_Sky/)
- Delta Patcher from the [Delta Patcher Page](https://www.romhacking.net/utilities/704/) //TO BE REPLACED WITH BSDIFF
- UndertaleModTool from the [Github Releases Page](https://github.com/UnderminersTeam/UndertaleModTool/releases)


## What is this?

The basic Randomizer employed by Archipelago changes a few things, but largely the experience of the Player is much the same as base game.
Because Isles of Sea And Sky is a puzzle-exploration game and not an action game, once the player has figured out a puzzle, subsequent
playthroughs won't have the same feeling nor the same challenge. Alternate Rooms (or Alternate Puzzles) is a proposed solution to this.

The aim here is not an entire overhaul of the game. Instead, the idea is that any person could add a single room to a larger collection
that would be sampled from randomly---effectively giving IOSAS an easily expandable, and highly purmutable way to have entirely new games!


## How does this work?

FULL EXPLANATION TBD ON WORKING IMPLEMENTATION!!!

Basically small patch files contained ONLY to room changes added to a simple file system to be chosen at random to be patched to the
select Data.Win file.

## What Are The Hard Requirements?

In order to keep the final experience of the player smooth even with hundreds of changed rooms, there are a number of rules to adhere to.

### Requirement 1 - Certain Objects cannot be moved.

- The AP World runes on Location IDs, and these are govered by the item type, room, and both x and y position. Because of this
Checks will be broken if an object is put in another place.
- This Includes Collectable Items, Locks, and the initial Snakeblock of a snakeblock chain.

### Requirement 2 - Entrances and Exits cannot be altered.

- The game keeps track of the Players position when they cross between rooms, so if and Entrance and an Exit don't match up
it is likely that the player will be subject to unwanted behavior, glitches, and even softlocks. Given how many possible different
rooms there could be, there is a large possibility of this occuring unless precautions are taken.

### Requirement 3 - All Location Checks Must Adhere to the APWORLD's Logic

- In order to ensure a valid playthrough of the game, rules are put in place to limit what checks correspond to what items.
Without these players will get stuck, and may not be able to finish a game. To keep this from happening, any person creating an
Alternate Room needs to keep in mind the rules of the checks therein. 
- E.g. If the check for a Star Piece has a rule that requires the Frog Flippers, the Alternate Room's version must also require Frog Flippers. Likewise the altered version should also be free from logic-impacting restrictions. For instance, requiring extra Ancient Keys would be forbidden, but utilizing extra pits and wooden boxes would not!


Here is an example of a valid Alternate Room: []() <--- SHOW ALT ROOM!!!

NOTE: Logic is bound to change between release of the APWORLD so keep an eye on that to keep abreast of any tweaks.

## How Do I Create My Own Alternate Room?

### Get all the required programs

### Set up a backup Data.Win

### Use Undertale Mode Tool

    open, select correct data.win

    Find the room you wish to change, and go to town!

    Save changes, and open game to verify them.

    NOTE: Experience with GameMaker will be helpful!

## I Made An Alternate Room, How Do I Share/Use It?

### Use DeltaPatcher to create an .xDelta patch

### Send it to your friends, or install it!

### Share it with the community, and add it to the growing library

