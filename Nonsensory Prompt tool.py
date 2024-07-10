# Import important libraries

import os 
import gc
from pprint import pprint 

# Get CWD
cwd = os.getcwd()


# Get the data from the user. It's all strings, so just prompt them.
categoryID = input('Enter Category ID (90517 for round 3)\n')
id = input('Enter prompt ID\n')
promptText = input('Enter Prompt Text for Player\n')
questionText = input('Enter Question Text\n')
rangeMax = input('Enter Range Maximum Label\n')
rangeMin = input('Enter Range Minimum Label\n')
rangeType = input('Enter Range Type (PERCENT, 1_TO_10, 10_TO_100, YEAR, STAR, ARROW\n')

# Create a data.jet file using the question text. Gotta make its directory first, then enter it.
try:
	os.makedirs(cwd+'/'+id)
except OSError:
	pass
newDataJetFile = open(cwd+'/'+id+'/data.jet', "w")
newDataJetFile.write('{\n "fields": \n [\n {\n  "t": "B",\n  "v": "true",\n  "n": "HasQuestionAudio"\n },\n {\n  "t": "A",\n  "v": "question",\n  "n": "QuestionAudio",\n  "s": "'+questionText+'"\n } \n ]\n}')
newDataJetFile.close()


# Now create or open and append the Nonsensor/v/ content file
newNonsensorveeContent = open(cwd+'/content.jet', "a")

# Write to it the stuff to copy out later
newNonsensorveeContent.write('{\n "allowedAuthorRangeValues": "ALL",\n "categoryId": "'+categoryID+'",\n "countrySpecific": false,\n ')
newNonsensorveeContent.write('"id": "'+id+'",\n "isValid": "",\n "preferredMax": 0,\n "preferredMin": 0,\n ')
newNonsensorveeContent.write('"promptText": "'+promptText+': {{ratio}}",\n "questionText": "'+questionText+'",\n ')
newNonsensorveeContent.write('"rangeMax": "'+rangeMax+'",\n "rangeMin": "'+rangeMin+'",\n "rangeType": "'+rangeType+'",\n "x": false\n},\n')
newNonsensorveeContent.close()

# And collect garbage, juuuuuuuuust in case.
gc.collect()