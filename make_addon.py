# Make a zip of project/addons/mongo-driver-godot

import shutil

ADDON_DIR = "project/addons/mongo-driver-godot"
version = input("Enter version: ")
shutil.make_archive("mongo-driver-godot.v" + version, 'zip', ADDON_DIR)
print("Done")
