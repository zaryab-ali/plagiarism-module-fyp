from flask import Flask
import speech_recognition as sr
from pydub import AudioSegment
from pydub.utils import make_chunks
import os
import requests
from pathlib import Path

app = Flask(__name__)


@app.route("/")
def shit():
    return f"hello"


@app.route("/bullshit")
def shit():
    return f"yes u are shit"


@app.route("/try/<string:what>")
def inging(what):
    return f"u wrote {what}"


@app.route("/final/<string:url>")
def download(url, out_file="audio.mp3"):
    big = []
    text = ""
    out_file = Path(f"/{out_file}").expanduser()
    resp = requests.get(url)
    resp.raise_for_status()
    with open(out_file, "wb") as fout:
        fout.write(resp.content)
    sound = AudioSegment.from_mp3("/audio.mp3")
    sound.export("blindingLights.wav", format="wav")
    filename = "blindingLights.wav"
    os.mkdir("/temp")
    myaudio = AudioSegment.from_wav(filename)
    chunk_lenght_ms = 5000
    chunks = make_chunks(myaudio, chunk_lenght_ms)
    for i, chunk in enumerate(chunks):
        chunkName = '/temp/' + filename + "_{0}.wav".format(i)
        chunk.export(chunkName, format="wav")

    for files in sorted(os.listdir("/temp")):
        filesss = "/temp/" + files
        print(files)
        r = sr.Recognizer()

        # open the file
        with sr.AudioFile(filesss) as source:
            # listen for the data (load audio to memory)
            audio_data = r.record(source)
            # recognize (convert from speech to text)
            try:
                text = r.recognize_google(audio_data)
                print(text)
            except:
                print("...")
                text = "..."
        small = [text]
        big.append(small)
    print(big)
    return (big)
