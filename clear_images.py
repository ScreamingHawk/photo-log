#! /usr/bin/env python3

from os import listdir, path, remove

IMG_FOLDER = "imgs"

print("Clearing all saved images")
if input("Are you sure? (y/N)") != "y":
    exit()

[remove(path.join(IMG_FOLDER, name)) for name in listdir(IMG_FOLDER) if path.isfile(path.join(IMG_FOLDER, name))]

print("All images")
