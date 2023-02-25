from datetime import timedelta
import os
import pywhisper
import moviepy.editor as mp
import urllib.request
import json
import requests


# model = pywhisper.load_model("base")
# result = model.transcribe("converted1.mp3")
# print(result["text"])


def transcribe_audio(path, output_path):
    # Extract the directory name and file name from the path
    dirName, fileName = path.rsplit('\\', 1)

    # Remove the ".mp4" extension from the file name and add ".srt" instead
    srtFileName = fileName[:-4] + ".srt"

    # Extract the project name from the directory name and add "_modified"
    projectName = dirName.split('\\')[-3] + '_modified'

    # Replace "uploads" with "downloads" in the directory name
    newDirName = dirName.replace("uploads", "downloads")

    # Replace the project name in the directory name and construct the new path
    newDirName = newDirName.replace(projectName[:-9], projectName)
    newPath = newDirName + '\\' + srtFileName

    # # # Step 2: Video to Audio conversion
    VidClip = mp.VideoFileClip(path)

    VidClip.audio.write_audiofile("converted.mp3")
    model = pywhisper.load_model("base")  # Change this to your desired model
    print("Whisper model loaded.")
    transcribe = model.transcribe(audio="converted.mp3")
    segments = transcribe['segments']

    for segment in segments:
        startTime = str(0)+str(timedelta(seconds=int(segment['start'])))+',000'
        endTime = str(0)+str(timedelta(seconds=int(segment['end'])))+',000'
        text = segment['text']
        segmentId = segment['id']+1
        segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] is ' ' else text}\n\n"

        with open(srtFileName, 'a', encoding='utf-8') as srtFile:
            srtFile.write(segment)

    # Upload the SRT file to file.io
    download_link = upload_srt_to_remote_service(srtFileName)
    print(f"download LInk: {download_link}")

    return download_link


def upload_srt_to_remote_service(srt_path):
    # Upload the SRT file to the remote service and get the URL
    with open(srt_path, 'rb') as f:
        srt_data = f.read()

    url = "https://file.io"
    response = requests.post(url, files={'file': srt_data}, verify=False)
    response_json = response.json()

    # Get the URL of the uploaded file
    download_url = response_json["link"]

    return download_url
