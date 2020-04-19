# NBAPlayerSearch
NBA player stat searcher, for all current and retired players. Made this when I first started learning, plan to visit and update code to be concurrent with my current knowledge.

#BUGFIXES

#players with same lastname and same first two letters of first name do not yield stats/ yield the older player's stats = fixed
#< will appear in some stats if they are not double digit = fixed
#cedi osman needs custom url due to website error = fixed
#duplicate data in sqlite3 = fixed
#invalid names yielding "Data already stored" when supposed to yield "No played found" = fixed
#user could type anything when prompted "Type Done to exit, press Enter to continue searching: " = fixed
#user could type anything when prompted "Is this player reitred(Yes/No)" = fixed
#clint capela needs custom url due to website error = fixed
#add when needed

#Conceptual Goals

#reduce copy paste using more if/elif/else along with function
#reduce total size of code by using more concise commands
#create a web application out of this code
#reformat so that retirement question follows first and last name no matter the fullname (even for cedi, kemba, etc.)
#add when needed