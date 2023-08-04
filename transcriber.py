import whisper

def transcribe(file_name = "voice_note.mp3", lang = "es", model_size = "tiny"):
    print("LOADING MODEL")
    model = whisper.load_model(model_size)

    print("LOADING AUDIO")
    audio = whisper.load_audio(f"{file_name}")
    audio = whisper.pad_or_trim(audio)

    print("PROCESS AUDIO")
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    print("DECODE AND TRANSCRIPT")
    options = whisper.DecodingOptions(language=lang, without_timestamps=True)
    result = whisper.decode(model, mel, options)

    print("TRANSCRIPTION COMPLETED")
    return result.text