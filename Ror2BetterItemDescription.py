import re

#
# Items
#

ReadFile = open("Items.txt", "r")


ToReplace = ": *\".*\""
ReplaceWith = "\"ITEM_(.*)_DESC\"( *: \".*\")"


Lines = ReadFile.readlines()

for i in range(len(Lines)):
    Match = re.findall(ReplaceWith, Lines[i])
    if len(Match):
        Item = Match[0][0]
        desc = Match[0][1]

        Lines[i - 1] = re.sub(ToReplace, desc, Lines[i - 1])

ReadFile.close()


WriteToFile = open("Items.txt", "w")
WriteToFile.write("".join(Lines))

#
# Equipement
#

EquipementFile = open("Equipment.txt", "r")

ToReplaceEquipement = ": *\".*\""
ReplaceWithEquipement = "\"EQUIPMENT_(.*)_DESC\"( *: \".*\")"

Lines = EquipementFile.readlines()

for i in range(len(Lines)):
    Match = re.findall(ReplaceWithEquipement, Lines[i])
    if len(Match):
        Item = Match[0][0]
        desc = Match[0][1]

        Lines[i - 1] = re.sub(ToReplaceEquipement, desc, Lines[i - 1])

EquipementFile.close()


WriteToFile = open("Equipment.txt", "w")
WriteToFile.write("".join(Lines))

print("Done!")
print("Press ANY key to exit")

input()
