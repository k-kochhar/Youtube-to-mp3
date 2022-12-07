import youtube_dl

'''
Required Packages
pip install youtube_dl
'''

ytURL = input("Enter a valid Youtube URL: ").strip()
videoInfo = youtube_dl.YoutubeDL().extract_info(url = ytURL,download=False)
filename = f"{videoInfo['title']}.mp3"
options={
    'format':'bestaudio/best',
    'keepvideo':False,
    'outtmpl':filename,
}

with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download([videoInfo['webpage_url']])

print(f'Download complete!')
