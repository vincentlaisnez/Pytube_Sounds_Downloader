import os
from pathlib import Path
from pytube import YouTube

PATH = Path.home()
DL_DIR = PATH.joinpath(PATH / "Documents" / "Pytube_Sounds_Downloader")
DL_DIR.mkdir(exist_ok=True)
os.chdir(DL_DIR)

url = []
capture = " "

while capture:
    print("Faire 'Entrer' sur le clavier sans sasir d'url pour arreter l'application")
    capture = input("Saisir l'url de la video Yt: ")
    if capture.startswith("https://") and capture:
        url.append(capture)

print("liste des URL:")
for i, items in enumerate(url, start=1):
    print(f"{i}: {items}")

for item in url:
    youtube_video = YouTube(item)
    print(f"\nTitre:{youtube_video.title}")
    # youtube_video.streams pour voir les différents itag video et audio
    print("téléchargement en cours...")
    stream = youtube_video.streams.get_by_itag(140)  # itag 140: audio-only 128kbps/ 18:360p/ 22: 720p/ 137:1080p
    stream.download()
    print("téléchargement fini !")
