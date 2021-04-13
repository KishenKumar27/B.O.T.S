print("The title of the story is 'Battle of Sexes'.\n")
title = "Battle of Sexes"
fillchar = "*"
print(title.center(50, fillchar))

print("Here's what happens when row names are omitted.\n")
psphelper.ShowTableByList(title, [], subjects, marksList)
input("Press ENTER to move on.")
psphelper.ClearScreen()
