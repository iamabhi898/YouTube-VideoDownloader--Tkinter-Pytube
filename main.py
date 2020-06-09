from pytube import YouTube


# returns list of available video/audio files
def getVideoList(videoUrl):

    videoUrl = str(videoUrl)
    video = YouTube(videoUrl)

    # making instance of list of video/audio
    listOfFiles = video.title
    streamList = video.streams.all()

    for stream in streamList:
        item = '\n'
        item += str(streamList.index(stream)+1) + ') '
        item += str(stream)
        # adding items of list line by line
        listOfFiles += item

    return listOfFiles


# selets the item from list then download it to the location
def downloader(videoUrl, itemNum, location):

    videoUrl = str(videoUrl)
    video = YouTube(videoUrl)

    # selecting item from list
    item = video.streams.all()[int(itemNum)-1]

    # downloading to location
    item.download(str(location))
