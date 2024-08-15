from fastapi import FastAPI, UploadFile, File
import uvicorn
import numpy as np

## BB
from whisper_transcriber import WhisperTranscriber

transcriber = WhisperTranscriber()


app = FastAPI()

# @app.post("/transcribe")
# def transcribe(file: UploadFile = File(...)):
#     # Process the voice file here and return the transcription
#     transcription = process_voice_file(file)
#     return {"transcription": transcription}

# def process_voice_file(file):
#     result = transcriber(inputs = "./mlk.flac")
#     pass

@app.post("/transcribe")
def transcribe(voice: UploadFile = File(...)):
    input_speech = np.frombuffer(voice.file.read(), dtype=np.int16)
    result = transcriber.infer(input_speech)
    # file = file.file
    # print("I receiced the file")
    return {"what": result}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)


'''
# for base
rlaunch -L 8001 --cpu=1 --gpu=1 --memory=4096 -- python3 audio_api.py
# for medium
rlaunch -L 8001 --cpu=1 --gpu=1 --memory=8192 -- python3 audio_api.py
'''