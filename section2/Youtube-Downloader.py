from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=JGwWNGJdvx8") # 다운받을 동영상 URL 지정

videos = yt.streams.all()

print('videos',videos)
