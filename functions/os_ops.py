# In this file we are gonna configure some offline functions

# region Imports
import os
import subprocess as sp
# endregion

paths = {
    'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
    'discord': "C:\\Users\\ashut\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}

#region Opening Programms (Discord & Notepadd)
def open_notepad():
    os.startfile(paths['notepad'])
def open_discord():
    os.startfile(paths['discord'])
#endregion

# region Opening cmd
def open_cmd():
    os.system('start cmd')
# endregion