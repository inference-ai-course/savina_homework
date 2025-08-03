# Automatic Speech Recognition - Video Transcription using Whisper ASR and yt-dlp

import yt_dlp
import whisper
import json
import os

class VideoTranscriber:
    def __init__(self, model_name='base'):
        self.model = whisper.load_model(model_name)
        self.download_files =[]

    def download_audio(self, urls, output_path='./output'):
        video_file_list = []
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        ydl_opts = {
            'format': 'best',
            'outtmpl': os.path.join(output_path, '%(id)s.%(ext)s'),
            'noplaylist': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3', # Save as mp3
                'preferredquality': 0    # Best quality
            }]
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            count = 0
            for url in urls:
                try:
                    ydl.download([url])
                    count += 1
                except Exception as e:
                    print(f"An error occurred while downloading {url}: {e}")
                    continue
            return count    
        
    def transcribe_audio(self, audio_path):
        """Transcribes the audio file using Whisper ASR."""
        #get audio files from given path
        audio_files = [f for f in os.listdir(audio_path) if f.endswith('.mp3')]
        transcriptions = []

        for audio_file in audio_files:
            try:
                audio_file_path = os.path.join(audio_path, audio_file)
                print(f"Transcribing {audio_file_path}...")
                result = self.model.transcribe(audio_file_path, language='en')
                transcription = result['text']
                transcriptions.append({
                    'file': audio_file,
                    'transcription': transcription,
                    'timestamp': result.get('segments', []),
                    'language': result.get('language', 'en')
                })
                print(f"Transcription for {audio_file}: {transcription}")
            except Exception as e:
                print(f"An error occurred during transcription: {e}")
                transcriptions = []
                continue
        # Save transcriptions to a JSON file
        output_file = os.path.join(audio_path, 'talks_transcripts.jsonl')
        with open(output_file, 'w', encoding='utf-8') as f:
            for item in transcriptions:
                f.write(json.dumps(item, ensure_ascii=False) + '\n')    
        print(f"Transcriptions saved to {output_file}")
        return transcriptions
        

if __name__ == "__main__":
    video_lists = [
    # "https://www.youtube.com/watch?v=_6z8lPmEfIE",
    # "https://www.youtube.com/watch?v=KkahojMtl1w",
    # "https://www.youtube.com/watch?v=LxkpIAMOFVA",
    # "https://www.youtube.com/watch?v=DHeqlVJQV9o",
    # "https://www.youtube.com/watch?v=WFqulKjREos",
    # "https://www.youtube.com/watch?v=SEj9bc2bH3E",
    # "https://www.youtube.com/watch?v=L3rqnv55GmE",
    # "https://www.youtube.com/watch?v=7gwhdRz3W40",
    # "https://www.youtube.com/watch?v=Lzzp82HlARc",
    "https://www.youtube.com/watch?v=mZGPM0qJ6l0"
    ]
    print("*"*20+" Downloading videos... "+"*"*20)

    transcriber = VideoTranscriber(model_name='base')
    count=transcriber.download_audio(video_lists)
    print( f"\n ======> Total {count} Audio was downloaded\n" )
    
    print("*"*20+" Transcribing videos... "+"*"*20)
    transcriber.transcribe_audio('./output')
    print("*"*20+" Transcription completed! "+"*"*20)






          





