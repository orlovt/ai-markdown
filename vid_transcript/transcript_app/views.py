from django.shortcuts import render
from .forms import VideoLinkForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pytube as pt
import openai
import os

key = "sk-<your-key>"  

def editor(request):
    return render(request, 'editor.html', {})

def index(request):
    if request.method == 'POST':
        form = VideoLinkForm(request.POST)
        if form.is_valid():
            # TODO: Process the URL and generate the transcript
            pass
    else:
        form = VideoLinkForm()

    return render(request, 'index.html', {'form': form})


def transcribe(url, key): 
    # Download the audio from the video
    yt = pt.YouTube(url)
    stream = yt.streams.get_audio_only()
    # Save file locally
    stream.download(filename="audio_english.mp3")
    
    # Check key 
    openai.api_key = key

    # Transcribe the audio
    with open("audio_english.mp3", "rb") as audio_file:
        transcript = openai.Audio.transcribe(
        file = audio_file,
        model = "whisper-1",
        response_format="text",
        language="en"
    )
    # Delete the audio file
    os.remove("audio_english.mp3")
    return transcript

def index(request):
    if request.method == 'POST':
        form = VideoLinkForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            # replace with your OpenAI key
            transcript = transcribe(url, key)
            return render(request, 'transcript.html', {'transcript': transcript})
            # TODO: Handle the transcript (e.g., save it, display it, etc.)
    else:
        form = VideoLinkForm()

    return render(request, 'index.html', {'form': form})


@csrf_exempt
def write(request):
    prompt = request.POST.get('prompt')
    transcript = request.POST.get('transcript')
    openai.api_key = key
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": transcript}
        ]
    )
    return JsonResponse({'message': completion.choices[0].message['content']})