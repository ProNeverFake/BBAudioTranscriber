import requests
import io

## BB 
from keyboard_record import record_voice

def send_voice_request(url = "http://127.0.0.1:8001/transcribe"):
    '''
    send the voice in Bytes to the server and get the transcription with the key "what"
    return None if the request is not successful (200)
    '''
    # record and convert audio to bytes
    audio_bytes = record_voice().tobytes()

    # Send request
    recording = {"voice": io.BytesIO(audio_bytes)}
    response = requests.post(url, files=recording)

    # print(response)

    if response.status_code == 200:
        data = response.json()
        transcription = data["what"]
        return transcription
    else:
        return None
    
def send_request(url):
    '''
    a test function to send a request to the server
    currently not in use because the endpoint for testing is ceased
    '''
    response = requests.post(url)
    if response.status_code == 200:
        data = response.json()
        transcription = data["what"]
        print(transcription)
        return transcription
    else:
        return None
    
if __name__ == "__main__":
    url = "http://localhost:8001/transcribe"
    # transcription = send_request(url)
    print(send_voice_request())