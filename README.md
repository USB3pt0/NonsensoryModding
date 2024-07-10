# NonsensoryModdingTool
Set of Python scripts to make modding Nonsensory for The Jackbox Party Pack 9 easier.

I hacked together these scripts as I had been modding Nonsensory and Poll Mine by hand, but the files of both having another folder with data the game uses became tedious and I was making mistakes.  More than I did writing these scripts, anyway.  These instructions assume a basic knowledge of scripting/coding logic, primarily because you have to copy and paste the entries to the .jet files yourself, and you don't want to muck up the formatting for {} brackets, or extra commas, and soforth.

# PREREQUISITES
You need Python 3 installed.  Keep the three scripts in separate folders; each puts out a "content.jet" file that will just be appended to by the others, and it'll be a mess to navigate, and they also make subfolders the game requires.  You also need to know where your Nonsensory folder is; it will be in [JPP9 install directory]/games/RangeGame. The files you need to edit are in content, as are the folders you need to put the folders these scripts generate.

# INSTRUCTIONS
# Categories
1. To make a new Category for Nonsensory, run Nonsensory Content tool.py by double clicking, or command line if you prefer that.
2. A window will pop up. You need to enter a Category ID and Category Text. I personally format categories with the format XYY0. X is either 1 or 2 depending on round. YY is incremented by 2 each time I make a new category for that round, for wiggle room. As far as I know, this is entirely arbitrary and you can use any numbers you want so long as they aren't being used.  My categories, for example, are like 1000 is Make Up a Tagline and 1020 is Make Up a Magazine. For Category Text, whatever you type here appears on screen. For my 1000, the text is "Make Up a Tagline."  You can use an existing Category ID if you find it in the category .jet files in your Nonsensory content directory.
3. Once both are entered, the window will automatically close and a content.jet file will appear or be appended to if it already exists.  A folder matching your new category ID is also made. In this folder, you MUST place a file named category.ogg or the game will not function. Either make an empty sound file with Audacity, or record yourself saying it, or pay someone on Fiver, or generate the voicelines using TTS or fancy-pants new ML voice stuff, or just cut together audio files of Professor Nanners saying "this category" or "this prompt", whatever.  Just make sure the file is there.
4. Copy that new folder to RangeGame/content/yourlanguagefolder/appropriatecategoryfolder, return to the language folder, open the associated RangeGame*Category.jet, and copy the content from the generated content.jet, matching the format.  You can delete the other categories if you want, the folders can remain but nothing that is not within these .jet files will be used by the game, so you can leave all the data for anything removed in the folders.  Or delete it, to save some marginal space.
5. Open the game and play! Your new categories should be there.  Although it will break immediately because you need some...

# Prompts
1. To make a new prompt for Nonsensory is a bit more involved. Much of the above is the same, however the fields are now more.
2. First it asks for a Category ID.  This must match an existing category ID, either from the game or one you made.
3. Next is Prompt ID. This should, like Category ID, be a unique number.  I like to number mine like, 1021, 1022, 1023, etc.
4. Next is Prompt Text.  This is what the player writing or drawing sees on their device. You need only put in the prompt, example "Make up a tagline for a video game this violent". The script will add a colon and the operator the game uses for the ratio the player must match.
5. Next up is the Question Text.  This is what will appear on the screen for all players. Ex: "How violent is the game this tagline is selling?"
6. Finally, the tool will ask for rangeMax, the label at the top of the scale; rangeMin, the label at the bottom; and rangeType, the type of scale. I will list the rangeType options below.
7. Once entered, the window will close and generate a new folder and make or append the content.jet file. Copy a file named question.ogg in that folder, similarly to above, only reading QuestionText.
8. Copy all made folders and entries in content.jet to the proper places, and you're good to go!

# Round 3 Prompts
1. Use the Final Round Prompt Tool for this. It has the built-in "Draw something between Two Points" category ID baked into the script, as well as the scaletype it uses. If you wanted to change round 3 entirely, however, use the above tools.  As far as I know it should work, however I have noticed there is no category.ogg for round 3's category, so something may not work.
2. You will be prompted for a Prompt ID, Prompt Text for player, Question text, the SECOND POINT YOU LISTED, then the FIRST POINT YOU LISTED, and the window will close. This is because, for whatever reason, the third round uses the first thing in the prompt/question as the bottom of the scale and the other as the top. Ex: For the prompt/question "(Draw something that/Where does this) belong(s) between MARIO and SONIC", you would put SONIC for SECOND point, and MARIO for FIRST.
3. Add a question.ogg to the newly generated folder, then copy the folder to RangeGame/content/yourlanguagefolder/RangeGameFinalRoundPrompt, and copy the content from content.jet to the RangeGameFinalRoundPrompt.jet files. You're golden!

# NOTES
For each content.jet, a comma is written at the end of each entry so it can be copied and pasted right into the game's .jet files.  However, a trailing comma at the end of the last entry left in the game's .jet files can break it.  It's hard to explain for me, but as a rule of thumb, whenever you copy stuff from a content.jet to the game's category or prompt .jet file, do not copy the VERY LAST comma in the file.

For each category, there needs to be at least 1 prompt per two players or it WILL softlock.  I try to keep it in sets of 4, but I imagine it doesn't really matter any game as long as it's 4 or more to prevent softlocks.

rangeType values:
```
1_TO_10 : this is just from 1-10.  easy.
1_TO_10_ALT: no idea
PERCENT : percentage from 10% to 100%.
10_TO_100: scale goes from 10 to 100. simple.
YEAR: Puts years going from 1950 to 2040.
STAR: Puts .5 stars at the bottom, incrementing by .5 up to 5 stars.
EXCLAMATION: I think this just starts at one ! at the bottom then goes to !!!!!!!!!! at the top.
ARROW: This is only used by the last round.  Shows 100% to 60% counting down from the top, then 60% to 100% towards the bottom.
ARROW is hard baked into the round 3 prompt tool.
```

There are some fields I don't have in here; preferredMin and preferredMax both set a cap on the ratio's maximum or minimum; this is used by the base game when a prompt is supposed to be drawn poorly, for example.

# TO-DO AND FUTURE THOUGHTS
I wrote these pretty quickly and had to hotfix them mid-game, but they're still rather user unfriendly. In the coming months I plan on writing a python GUI application that will allow you to edit the game's .jet itself and put things where they need to be, with a nice table layout or something, while still requiring minor work from the user.


