# Import important libraries

import os 
import gc
from pprint import pprint 

# Get CWD
cwd = os.getcwd()


# Get the data from the user. It's all strings, so just prompt them.
categoryID = '90517'
id = input('Enter prompt ID\n')
rangeMin = input('Enter first point\n')
rangeMax = input('second point\n')
rangeType = 'ARROW'

# Create a data.jet file using the question text. Gotta make its directory first, then enter it.
try:
	os.makedirs(cwd+'/'+id)
except OSError:
	pass
newDataJetFile = open(cwd+'/'+id+'/data.jet', "w")
newDataJetFile.write('{\n "fields": \n [\n {\n  "t": "B",\n  "v": "true",\n  "n": "HasQuestionAudio"\n },\n {\n  "t": "A",\n  "v": "question",\n  "n": "QuestionAudio",\n  "s": "Where does this drawing belong between\\n'+rangeMin+' and '+rangeMax+'?"\n } \n ]\n}')
newDataJetFile.close()


# Now create or open and append the Nonsensor/v/ content file
newNonsensorveeContent = open(cwd+'/content.jet', "a")

# Write to it the stuff to copy out later
newNonsensorveeContent.write('{\n "allowedAuthorRangeValues": "ALL",\n "categoryId": "'+categoryID+'",\n "countrySpecific": false,\n ')
newNonsensorveeContent.write('"id": "'+id+'",\n "isValid": "",\n "preferredMax": 0,\n "preferredMin": 0,\n ')
newNonsensorveeContent.write('"promptText": "Draw something that sits here on a range from '+rangeMin+' to '+rangeMax+':",\n "questionText": "Where does this drawing belong between\\n'+rangeMin+' and '+rangeMax+'?",\n ')
newNonsensorveeContent.write('"rangeMax": "'+rangeMax+'",\n "rangeMin": "'+rangeMin+'",\n "rangeType": "'+rangeType+'",\n "x": false\n},\n')
newNonsensorveeContent.close()

# And collect garbage, juuuuuuuuust in case.
gc.collect()