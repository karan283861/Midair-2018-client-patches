# Midair (2018) client patches
A collection of client side patches for Midair
Currently just a set of assembly patches to
* Disable Midair's prediction (set via Predict command)

### Requirements
1. Midair client (normally obtainable via Steam)
2. Python 3 (preferably the latest or closest to latest version)
3. Pymem package installed via PIP
4. This repository

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
