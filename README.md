# vanilla_wow_battleground
Just for fun. 

The main goals of this program: 
1. Queue for a battleground.
2. Enter the battleground when the join dialog appears.
3. Keep the character not AFK.
4. Leave the battleground when it ends.
5. Repeat 1-4.

# Install Requirements
```
conda create -n vanilla_wow python=3.6 
conda activate vanilla_wow
conda install -c conda-forge pywinauto
conda install pyqt5 
```

# The Join/Leave Battleground Macro
```
/tar {NPC_name}
/run DeclineGroup()
/click GossipTitleButton1
/click BattlefieldFrameJoinButton
/click StaticPopup1Button1
/click PVPReadyDialogEnterBattleButton
/run if GetBattlefieldWinner() then LeaveBattlefield() end
```

# Keybindings
Keybinding 1: the macro of join/leave battleground BG <br>
Keybinding F12: interact with target NPC <br>
keybinding 2: any non-enemy-target spell <br>
Keybinding 3: any non-enemy-target spell <br>
Keybinding SPACE: jump

The program will repeat pressing the following key sequence:
*{1, F12, 1, 1, 2, 3, SPACE}*

# References
1. https://stackoverflow.com/questions/54362326/how-to-make-pywinauto-work-in-background
2. https://pywinauto.readthedocs.io/en/latest/code/pywinauto.keyboard.html
3. https://wowwiki-archive.fandom.com/wiki/World_of_Warcraft_API
4. https://stackoverflow.com/questions/49886313/how-to-run-a-while-loop-with-pyqt5