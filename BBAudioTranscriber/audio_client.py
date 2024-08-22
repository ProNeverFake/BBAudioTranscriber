import requests
import io

# BB 
from .keyboard_record import record_voice

def send_voice_request(url = "http://127.0.0.1:8001/transcribe") -> str:
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
    

class AudioClient:
    '''
    An audio client to send voice request to the server
    It expects a return of the transcription with the key "what"
    '''
    def __init__(self, protocol = "http", url = "127.0.0.1", port = 8001, endpoint = "transcribe"):
        self.protocol = protocol
        self.url = url
        self.port = port
        self.endpoint = endpoint

    def send_voice_request(self) -> str:
        '''
        send the voice in Bytes to the server and get the transcription with the key "what"
        return str if the request is successful (200)
        '''
        # record and convert audio to bytes
        audio_bytes = record_voice().tobytes()

        # prepare request
        recording = {"voice": io.BytesIO(audio_bytes)}

        try:
            response = requests.post(self.get_full_url(), files=recording, timeout=20)
        except requests.exceptions.Timeout:
            raise Exception(f'Request timed out!')
        
        if response.status_code == 200:
            data = response.json()
            transcription = data["what"]
            return transcription
        else:
            raise Exception(f'Request failed with status code {response.status_code}')
        
    def send_request(self):
        '''
        a test function to send a request to the server
        currently not in use because the endpoint for testing is ceased
        '''
        try:
            response = requests.post(self.get_full_url(), timeout=10)
        except requests.exceptions.Timeout:
            raise Exception(f'Request timed out!')
        if response.status_code == 200:
            data = response.json()
            transcription = data["what"]
            print(transcription)
            return transcription
        else:
            raise Exception(f'Request failed with status code {response.status_code}')
        
    def set_connection(self, protocol, url, port, endpoint):
        self.protocol = protocol
        self.url = url
        self.port = port
        self.endpoint = endpoint

    def get_full_url(self) -> str:
        return f"{self.protocol}://{self.url}:{self.port}/{self.endpoint}"

    
if __name__ == "__main__":
    
    AT = AudioClient(protocol="http", url="127.0.0.1", port=8001, endpoint="transcribe")
    transcription = AT.send_voice_request()
    print(transcription)