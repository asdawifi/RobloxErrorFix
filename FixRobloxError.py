import os
globalbasicsettings = os.getenv('LOCALAPPDATA') + "/Roblox/GlobalBasicSettings_13.xml"
globalsettings = os.getenv('LOCALAPPDATA') + "/Roblox/GlobalSettings_13.xml"
try:
	os.remove(globalbasicsettings)
	os.remove(globalsettings)
	print("Successfully fixed Unexpected client behaviour error!")
except:
	print("Error, contact rith#0001 on discord.")
