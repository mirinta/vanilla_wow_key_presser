# vanilla_battleground
Just for fun.

# Install Requirements
```conda install -c conda-forge pywinauto```

# The Join/Leave BattleGround Macro
```
/tar {NPC_name}
/run DeclineGroup()
/click GossipTitleButton1
/click BattlefieldFrameJoinButton
/click StaticPopup1Button1
/click PVPReadyDialogEnterBattleButton
/run if GetBattlefieldWinner() then LeaveBattlefield() end
```

# Keybinds
Keybinding 1: the join/leave BG macro <br>
Keybinding F12: interact with target NPC <br>
keybinding 2: any spell <br>
Keybinding 3: any spell <br>

# References
1. https://stackoverflow.com/questions/54362326/how-to-make-pywinauto-work-in-background
2. https://pywinauto.readthedocs.io/en/latest/code/pywinauto.keyboard.html
3. https://wowwiki-archive.fandom.com/wiki/World_of_Warcraft_API