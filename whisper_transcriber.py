
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import torch
import numpy as np

device = "cuda:0" if torch.cuda.is_available() else "cpu"

class WhisperTranscriber:

    def __init__(self):
        self.processor = WhisperProcessor.from_pretrained("./whisper-base")
        self.model = WhisperForConditionalGeneration.from_pretrained("./whisper-base").to(device)   
        self.forced_decoder_ids = self.processor.get_decoder_prompt_ids(language="Mandarin", task="translate")

    def infer(self, input_speech:np.int16) -> list[str]:
        '''
        preprocess the input speech and infer the transcription.
        to "device".
        batch = 1
        '''
        input_speech = self._preprocess(input_speech)
        input_features = self.processor(input_speech, sampling_rate=16000, return_tensors="pt").input_features.to(device)
        predicted_ids = self.model.generate(input_features, forced_decoder_ids=self.forced_decoder_ids)
        transcription = self.processor.batch_decode(predicted_ids, skip_special_tokens=True)
        return transcription
    
    def _preprocess(self, recording: np.int16):
        '''
        normalize the voice to constrain it between -1 and 1
        '''
        normalized_recording = recording / np.max(np.abs(recording))
        return normalized_recording

if __name__ == "__main__":

    print("Testing WhisperTranscriber")
    wt = WhisperTranscriber()
    recording = np.random.randint(-32768, 32767, 16000)
    transcription = wt.infer(recording)
    print(transcription)