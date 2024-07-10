# Import important libraries

import os 
import gc
from pprint import pprint 

# Get CWD
cwd = os.getcwd()


# Get the data from the user. It's all strings, so just prompt them.
categoryID = input('Enter Category ID\n')
categoryText = input('Enter Category text\n')

# Create a data.jet file using the question text. Gotta make its directory first, then enter it.
try:
	os.makedirs(cwd+'/'+categoryID)
except OSError:
	pass
newDataJetFile = open(cwd+'/'+categoryID+'/data.jet', "w")
newDataJetFile.write('{\n "fields": \n [\n {\n  "t": "B",\n  "v": "true",\n  "n": "HasAudio"\n },\n {\n  "t": "A",\n  "v": "category",\n  "n": "Audio",\n  "s": "'+categoryText+'"\n } \n ]\n}')
newDataJetFile.close()


# Now create or open and append the Nonsensor/v/ content file
newNonsensorveeContent = open(cwd+'/content.jet', "a")

# Write to it the stuff to copy out later
newNonsensorveeContent.write('{\n "difficulty": "EASY",\n "id": "'+categoryID+'",\n "isValid": "",\n "text": "'+categoryText+'"\n},\n')
newNonsensorveeContent.close()

# And collect garbage, juuuuuuuuust in case.
gc.collect()