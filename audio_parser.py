import whisper

class Audio_parser:
    def __init__(self):
        self.model = whisper.load_model('base')

    def parse_audio (self, audio_path):
        result = self.model.transcribe(audio_path)
        return(result["text"])

    def parse_audio_complex(self, audio_path):
        # load audio and pad/trim it to fit 30 seconds
        audio = whisper.load_audio(audio_path)
        audio = whisper.pad_or_trim(audio)

        # make log-Mel spectrogram and move to the same device as the model
        mel = whisper.log_mel_spectrogram(audio).to(self.model.device)

        # detect the spoken language
        _, probs = self.model.detect_language(mel)
        print(f"Detected language: {max(probs, key=probs.get)}")

        # decode the audio
        options = whisper.DecodingOptions()
        result = whisper.decode(self.model, mel, options)

        # print the recognized text
        return(result.text)
