# vanilla_wow_battleground
Just for fun.
Automatically join/leave battleground

# Install Requirements
```
conda create -n vanilla_bg python=3.6 
conda activate vanilla_bg
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

# References
1. https://stackoverflow.com/questions/54362326/how-to-make-pywinauto-work-in-background
2. https://pywinauto.readthedocs.io/en/latest/code/pywinauto.keyboard.html
3. https://wowwiki-archive.fandom.com/wiki/World_of_Warcraft_API
4. https://stackoverflow.com/questions/49886313/how-to-run-a-while-loop-with-pyqt5