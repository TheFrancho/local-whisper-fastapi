import requests

#hardcoding the urls, not a problem so far
url_files = "http://127.0.0.1:8000/transcribe"

#There is a multimedia audio for testing purposes
filename = "voice_note.mp3"

#Open the file in read binary format and load it on memory
with open(filename, 'rb') as fd:
    content = fd.read()

#Create the context for the request, will be a binary array
context = {
    "file" : content
}

#Lastly make a request and send the context via FILES (very important)
response = requests.post(url_files, files=context)

#If everything went well, the response should be a json with the transcription
print(response.json())