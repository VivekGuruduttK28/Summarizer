from gtts import gTTS
import os
import random
from new.settings import MEDIA_ROOT
def text_audio(text):
    tts=gTTS(text)
    x=random.randint(1,1000)
    y=x
    x="{}.mp3".format(x)
    tts.save(x)
    import shutil

    source_path = x
    destination_path = MEDIA_ROOT

    try:
    # Move the file from the source to the destination
        shutil.move(source_path, destination_path)
        print("File moved successfully.")
    except FileNotFoundError:
        print("Source file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    return x,y
    
import time 
def delete_file(file_path,timeout_seconds):
    time.sleep(600)
    try:
        os.remove(file_path)
    except OSError as o:
        print("File deleted",str(o))
        

