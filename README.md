
# Server side
- load the model to GPU
- listen to port 8001 for incoming audio file request
    - endpoint = "http://127.0.0.1:8001/transcribe"
- transcribe and translate the audio into Englisch text.

## Server side installation

```bash
# install pytortch with cuda 11.8
pip3 install 

# install requirements
pip3 install scipy "numpy<2" fastapi[standard] transformers

# other requirements through sudo apt-get install
# TBD, just install anything that is missing

```

## Server side running

The server side can be deployed in a local machine or in WS.

### With a local PC

```bash
# just run the python script audio_api.py
python3 audio_api.py
```

### With WS

```bash
# In WS, for whisper-medium, fast-api listens port 8001, start a worker
rlaunch -L 8001 --cpu=1 --gpu=1 --memory=8192 -- python3 audio_api.py    

# In local PC, start SSH forwarding
ssh -NL 8001:localhost:8001 <WS-username>@<WS-IP>
```

# Client side
- start recording with "v"
- stop recording with "v" again
- send the audio file to the server
- wait for the response, which is the string of the transcribed text

## Client side installation

```bash
pip3 install sounddevice pynput pydub scipy "numpy<2" 
```

## Client side running

```bash
python3 audio_client.py
```



---

# BB

- HTTP 422 UNPROCESSABLE CONTENT
    - key error (fastapi app arg)

- Noise in the recording
    - High-pass filter with a cut-off frequency of 40Hz

## whisper

- sampling rate need to be 16000