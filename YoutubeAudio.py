from pytube import YouTube

def Download(link):
  youtubeObject = YouTube(link)
  youtubeObject = youtubeObject.streams.get_audio_only
  try:
      youtubeObject.download()
  except:
   print("There has been an error in downloading your youtube video")
  print("This download has completed! Yahooooo!")
link = input("Put your youtube link here!! URL: ")
Download(link)