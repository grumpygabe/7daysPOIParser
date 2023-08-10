# written recklessly fast by grumpybeard
# https://discordapp.com/users/176104171316051968
# updated 8/10/2023
# version 1.4

import os
import xml.etree.ElementTree as ET
from tkinter import filedialog as fd

rootpath = fd.askdirectory()
csvline = ""

# walk through the target directory
for root, dirs, files in os.walk(rootpath):
    path = root.split(os.sep)
    if True:
        for file in files:
            if file.endswith(".xml"):
                print(str(root) + "/" + file)
                poitree = ET.parse(root + "/" + file)

                poiroot = poitree.getroot()

                # initialize some properties
                tier = (
                    tags
                ) = themetags = quest = duprepeatdist = themerepeatdist = yoffset = ""
                x = y = z = yoffset = ""
                minzed, maxzed, avgzed = 0, 0, 0

                zeds = []
                for prop in poiroot:
                    match prop.get("name"):
                        case "DifficultyTier":
                            tier = prop.get("value")
                        case "PrefabSize":
                            dims = prop.get("value")
                            if len(dims.split(",")) == 3:
                                x = dims.split(",")[0]
                                y = dims.split(",")[1]
                                z = dims.split(",")[2]
                        case "QuestTags":
                            quest = prop.get("value")
                        case "YOffset":
                            yoffset = prop.get("value")
                        case "Tags":
                            tags = prop.get("value")
                        case "ThemeTags":
                            themetags == prop.get("value")
                        case "DuplicateRepeatDistance":
                            duprepeatdist == prop.get("value")
                        case "ThemeRepeatDistance":
                            themerepeatdist == prop.get("value")
                        case "SleeperVolumeGroup":
                            zeds = prop.get("value").split(",")

                if zeds != [""]:
                    for i in range(0, len(zeds), 3):
                        minzed += int(zeds[i + 1])
                        maxzed += int(zeds[i + 2])
                        avgzed += (int(zeds[i + 1]) + int(zeds[i + 2])) / 2.0

                # fix delimeters
                quest = "/".join([str.strip(" ") for str in quest.split(",")])
                tags = "/".join([str.strip(" ") for str in tags.split(",")])
                themetags = "/".join([str.strip(" ") for themetags in quest.split(",")])

                csvline = (
                    csvline
                    + root
                    + ","
                    + file.split(".")[0]
                    + ","
                    + tier
                    + ","
                    + "/".join([str.strip(" ") for str in quest.split(",")])
                    + ","
                    + tags
                    + ","
                    + themetags
                    + ","
                    + duprepeatdist
                    + ","
                    + themerepeatdist
                    + ","
                    + x
                    + ","
                    + y
                    + ","
                    + z
                    + ","
                    + yoffset
                    + ","
                    + str(minzed)
                    + ","
                    + str(maxzed)
                    + ","
                    + str(avgzed)
                    + "\n"
                )

f = open("poistats.csv", "w")
f.write(
    "Collection, Prefab, Tier, QuestTags, Tags, ThemeTags, DuplicateRepeatDistance, ThemeRepeatDistance, X, Y, Z, YOffset, MinSleepers, MaxSleepers, AvgSleepers "
    + "\n"
)
f.write(csvline)
f.close()
print("Finished")
