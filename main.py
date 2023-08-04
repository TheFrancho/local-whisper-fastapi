from typing import Annotated
import os

from fastapi import FastAPI, File, UploadFile

from transcriber import transcribe


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/transcribe")
async def create_upload_file(file: bytes = File(...)):
    filename_save = "saved.mp3"
    with open(filename_save, 'wb') as saved:
        saved.write(file)

    print("Audio recieved, starting transcription")

    transcription = transcribe(file_name=filename_save)
    
    print("deleting file and finishing process")

    os.remove(filename_save)

    return {"transcription": transcription}