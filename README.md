# Introduction
Send custom key sequences to vanilla WoW (CN) processes.

# Install Requirements
```
conda create -n vanilla_wow python=3.6 
conda activate vanilla_wow
conda install -c conda-forge pywinauto
conda install pyqt5 
```

# TODO List
- [ ] Timer (program running duration)
- [x] Exception handler (stop sending keys when exception appears)
- [x] Custom key sequence (load configuration file) 
- [ ] Show screenshot (double click process ID to show a screenshot)
- [ ] Multiple tasks (one key sequence for one process ID)

# Useful Macros
## The Join/Leave Battleground Macro
```
/tar {NPC_name}
/run DeclineGroup()
/click GossipTitleButton1
/click BattlefieldFrameJoinButton
/click StaticPopup1Button1
/click PVPReadyDialogEnterBattleButton
/run if GetBattlefieldWinner() then LeaveBattlefield() end
```
Note: for group join, use `/click BattlefieldFrameGroupJoinButton`

## The Automatic Retrieve/Resurrect Macro
```
/run RepopMe()
/run RetrieveCorpse()
/run AcceptResurrect()
/run AcceptXPLoss()
```
Note: 
Make sure the character stands next to the spirit healer.
Manually accept a resurrection with sickness for the first time.
Then use this macro to automatically retrieve and resurrect. 

## The Logout Macro
```
/run LeaveParty()
/logout
```

# References
1. https://stackoverflow.com/questions/54362326/how-to-make-pywinauto-work-in-background
2. https://pywinauto.readthedocs.io/en/latest/code/pywinauto.keyboard.html
3. https://vanilla-wow-archive.fandom.com/wiki/World_of_Warcraft_API
4. https://wowwiki-archive.fandom.com/wiki/World_of_Warcraft_API
5. https://stackoverflow.com/questions/49886313/how-to-run-a-while-loop-with-pyqt5
