# to rename all the music files to simple names

import os

inputFolder = "./ClassicalMusic"

files = os.listdir(inputFolder)

for number, file in enumerate(files):
    newName = os.path.join(inputFolder, f"musicFile{number}.flac")
    oldName = os.path.join(inputFolder, file)
    os.rename(oldName, newName)
