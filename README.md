# Midair (2018) client patches

## Want to play without straight away without patching?
Follow the instructions at [here](HowToRunWithoutPatches.md)

---

## What are the patches and why?
A collection of client side patches for Midair
Currently just a set of assembly patches to
1. Disable Midair's player prediction (set via Predict command)
2. Disable Midair's fake projectile logic (also set via Predict command)

Patches (1, 2) are to prevent the Midair client from performing client side prediction of other players, so lag compensation can be implemented server side. If these patches are not performed on the client while joined to a server with lag compensation enabled, then the player will not be able to utilise the benefits of server side lag compensation due to inaccurate client predictions and inaccurate "fake" projectiles.

### Requirements
1. Midair client (normally obtainable via Steam)
2. Python 3 (preferably the latest or closest to latest version)
3. Pymem package installed via PIP
4. This repository (for the python file/s)

## Setting up for the first time

### Getting Midair
Simply visit the store page for Midair on Steam (https://store.steampowered.com/app/439370/Midair/)

### Getting Python and Pymem
1. Download your relevant Python installer from https://www.python.org/downloads/
2. Run the Python installer, ensuring to check/tick/enable the checkbox which reads "Add python.exe to PATH"
3. Once the installation is complete, run command prompt and enter the following: `pip install pymem`

### Getting this repository
If you're unfamiliar with Git/GitHub, simply download using this following link: https://github.com/karan283861/Midair-2018-client-patches/archive/refs/heads/main.zip

## Setting up Midair
Once you have successfully installed Midair,
1. Find your local installation of the Midair games files (should be similar to `C:\Program Files (x86)\Steam\steamapps\common\Midair\`
2. Find the main executable inside the installation of the Midair game files (should be similar to `C:\Program Files (x86)\Steam\steamapps\common\Midair\Midair\Binaries\Win64\Midair-Win64-Test.exe`)
3. Create a shortcut of this executeable and add the "-nosteam" parameter to the launch target (ie. `"C:\Program Files (x86)\Steam\steamapps\common\Midair\Midair\Binaries\Win64\Midair-Win64-Test.exe" -nosteam`)

## Running Midair after setting up
1. Ensure Steam is closed and not running
2. Run Midair via the shortcut you have created
3. Run the python script provided
4. If your last `predict` command value is non zero, then enter `predict 0` once you have joined a server

## Connecting to a server
Currently server support is limited, however you can attempt to connect to a server by entering `open midair2018-1.ddns.net` in console
