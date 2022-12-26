from pytube import YouTube
import uuid
import settings as st

class YoutubeException(BaseException):
    pass

def dowload_audio(youtube_url: str ):
    y_tube = YouTube(youtube_url)
    audio_id = uuid.uuid4().fields[-1]
    y_tube.streams.filter(only_audio=True).first().download(st.YOUTUBE_LOAD_PATH, f'{audio_id}.mp3')
    return f'{audio_id}.mp3'
