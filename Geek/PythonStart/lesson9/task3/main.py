import pytube

try:
    youtube_video = pytube.YouTube('https://youtu.be/x5oGW6kv08A?list=RDx5oGW6kv08A')

    filters = youtube_video.streams.filter(progressive=True, file_extension='mp4')

    # download the highest quality video
    filters.get_highest_resolution().download()
    print('Downloaded Successfully')
except Exception as e:
    print(e)
