from tkinter import *
from tkinter import filedialog
from main import getVideoList
from main import downloader


# returns directory path
def directoryLocation():
    filename = filedialog.askdirectory()
    return filename


# insert path in location entry
def insertPath(entry):
    entry.delete(0, END)
    entry.insert(0, directoryLocation())


# gets entry form videoLinkEntry and then call getVideoList(videoUrl) and then
# insert it to available video/audio list
def insertList(searchEntry, textEntry):

    url = searchEntry.get()
    videoList = getVideoList(url)

    # clearing entries
    textEntry.delete('1.0', END)

    # dispalying list
    textEntry.insert('1.0', videoList)


# instance of window
window = Tk()

# window title
window.title("YouTube Downloader")

# setting window size
window.geometry("950x950")

# youtube logo
logo = PhotoImage(file="youtube.png")
Label(window, image=logo).grid(row=0, column=0, columnspan=3)

# label (video link)
videoLinkLabel = Label(window, text="Video Link: ", font=20)

# video link input
videoLinkEntry = Entry(window, borderwidth=0, width=50)

# search Button
searchButton = Button(window, text="Search", width=10,
                      command=lambda: insertList(videoLinkEntry, videoListText))

# label (video list)
videoListLabel = Label(window, text="Available Video/Audio: ", font=20)

# list of available video/audio types
videoListText = Text(window, height=20, width=88)

# label (select file)
selectLabel = Label(window, text="Select File: ", font=20)

# select file input
selectEntry = Entry(window, borderwidth=0, width=3)

# location label
locationLabel = Label(window, text="Location:", font=20)

# location input
locationEntry = Entry(window, borderwidth=0, width=50)

# location button
locationButton = Button(window, text="Choose",
                        width=10, command=lambda: insertPath(locationEntry))

# download button
downloadButton = Button(window, text="Download",
                        width=20, bg="green", fg="white", command=lambda: downloader(videoLinkEntry.get(), selectEntry.get(), locationEntry.get()))

# packing
videoLinkLabel.grid(row=1, column=0, pady=30, padx=20)
videoLinkEntry.grid(row=1, column=1, pady=30, padx=20)
searchButton.grid(row=1, column=2, pady=30, padx=20)
videoListLabel.grid(row=2, column=0, columnspan=3)
videoListText.grid(row=3, column=0, columnspan=3)
selectLabel.grid(row=4, column=0, pady=30, padx=20)
selectEntry.grid(row=4, column=1, pady=30, padx=20)
locationLabel.grid(row=5, column=0, pady=30, padx=20)
locationEntry.grid(row=5, column=1, pady=30, padx=20)
locationButton.grid(row=5, column=2, pady=30, padx=10)
downloadButton.grid(row=6, column=0, columnspan=3)


# window loop
window.mainloop()
