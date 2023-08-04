# Local whisper api implementation

This is the [server implementation of the telegram whisper bot](https://github.com/TheFrancho/telegram-whisper-bot)

This implementation uses FastAPI to ingest mp3 files to the Whisper model and return a transcription of the audio.

Inside the repo there is a requests.py script that shows you how to use the endpoint

Working on localhost:8000, only uses the "/transcribe" endpoint

## Installation

- If you are using WSL you may have a problem with some dependencies, to fix it you have to add this line to the bash file

```bash
nano ~/.bashrc
LD_LIBRARY_PATH=/usr/lib/wsl/lib:$LD_LIBRARY_PATH
```

- Because this is a FastAPI server, you have to install uvicorn

```python
pip install uvicorn
```

- Now create a virtual environment and install the requirements:

```python
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```

- To run the server:

```bash
uvicorn main:app --reload
```

And the server will be ready to receive requests

## Requirements

- Python 3.8+
- uvicorn

## Usage

Just look at the [requests.py](https://github.com/TheFrancho/local-whisper-fastapi/blob/main/request.py) file to know how to use the endpoint
