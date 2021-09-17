# 17-Sep-21
# Python 3.9
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from pytube import YouTube
import time

version = 1.1


def show_info():
    link = EntryLink.get()
    if link:
        yt = YouTube(link)
        ListboxInfo.delete(0, 4)
        ListboxInfo.insert(0, f"Title: {yt.title}")
        ListboxInfo.insert(1, f"Number of views: {yt.views}")
        ListboxInfo.insert(2, f"Length of video: {yt.length}")
        ListboxInfo.insert(3, f"Rating of video: {yt.rating}")
        ListboxInfo.insert(4, f"Age restricted: {yt.age_restricted}")
    else:
        messagebox.showerror("Invalid link", "The link you entered is invalid!")


def download_video():
    link = EntryLink.get()
    if link:
        yt = YouTube(link)
        ListboxInfo.delete(0, 4)
        ListboxInfo.insert(0, f"Title: {yt.title}")
        ListboxInfo.insert(1, f"Number of views: {yt.views}")
        ListboxInfo.insert(2, f"Length of video: {yt.length}")
        ListboxInfo.insert(3, f"Rating of video: {yt.rating}")
        ListboxInfo.insert(4, f"Age restricted: {yt.age_restricted}")

        location = EntryLocation.get()

        ys = yt.streams.get_highest_resolution()
        time.sleep(1)
        ListboxInfo.delete(0, 4)
        ListboxInfo.insert(0, "Downloading video...")

        if location:
            ys.download(location)
        else:
            ys.download("media/")
        time.sleep(2)
        ListboxInfo.insert(1, "Download completed!!")
    else:
        messagebox.showerror("Invalid link", "The link you entered is invalid!")


def download_audio():
    link = EntryLink.get()
    if link:
        yt = YouTube(link)
        ListboxInfo.delete(0, 4)
        ListboxInfo.insert(0, f"Title: {yt.title}")
        ListboxInfo.insert(1, f"Number of views: {yt.views}")
        ListboxInfo.insert(2, f"Length of video: {yt.length}")
        ListboxInfo.insert(3, f"Rating of video: {yt.rating}")
        ListboxInfo.insert(4, f"Age restricted: {yt.age_restricted}")

        location = EntryLocation.get()

        ys = yt.streams.get_audio_only()
        time.sleep(1)
        ListboxInfo.delete(0, 4)
        ListboxInfo.insert(0, "Downloading audio...")

        if location:
            ys.download(location)
        else:
            ys.download("media/")

        time.sleep(2)
        ListboxInfo.insert(1, "Download completed!!")
    else:
        messagebox.showerror("Invalid link", "The link you entered is invalid!")


background = "#333"
white = "#fff"
NASLOV = ("Roboto", 20)

root = Tk()
root.geometry("1000x600")
root.title(f"YouTube Downloader {version}")
root.iconbitmap("img/yt.ico")

image1 = Image.open("img/YTdwl.png")
image1 = image1.resize((100, 100), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(image1)
LabelLogo = Label(root, image=logo, bg=background)
LabelLogo.grid(row=0, column=0)
LabelWelcome = Label(root, text=f"Welcome to the YouTube Downloader v{version}", bg=background, fg=white, font=NASLOV)
LabelWelcome.grid(row=0, column=1)

LeftFrame = Frame(master=root, width=500, bg=background)
LeftFrame.grid(row=1, column=0)
RightFrame = Frame(master=root, width=500, bg=background)
RightFrame.grid(row=1, column=1)

LabelLink = Label(LeftFrame, text="Enter valid YouTube link: ", bg=background, font=NASLOV, fg=white)
LabelLink.grid(row=0, column=0, pady=10, padx=10)
EntryLink = Entry(LeftFrame, width=50)
EntryLink.grid(row=1, column=0, pady=10)

LabelLocation = Label(LeftFrame, text="Enter a download PATH:"
                                      "\n(If it's empty the file will be"
                                      " saved in \\media)", bg=background, font=("Roboto", 12), fg=white)
LabelLocation.grid(row=2, column=0, pady=10, padx=10)
EntryLocation = Entry(LeftFrame, width=50)
EntryLocation.grid(row=3, column=0, pady=10)

ButtonInfo = Button(LeftFrame, text="Show Information", bg="darkblue", fg=white, command=show_info)
ButtonInfo.grid(row=4, column=0, pady=10)
ButtonDownloadVideo = Button(LeftFrame, text="Download Video", bg="lime", fg=background, command=download_video)
ButtonDownloadVideo.grid(row=5, column=0, pady=10)
ButtonDownloadAudio = Button(LeftFrame, text="Download Audio", bg="lemonchiffon", fg=background, command=download_audio)
ButtonDownloadAudio.grid(row=6, column=0, pady=10)


ListboxInfo = Listbox(RightFrame, height=20, width=60, font=("Roboto", 12))
ListboxInfo.grid(row=0, column=0)
LabelCopyRight = Label(RightFrame, text="Copyright© Mitar Milovanovic", bg=background, fg=white)
LabelCopyRight.grid(row=1, column=0, pady=10, sticky="e")
ButtonExit = Button(RightFrame, text="Exit Application", bg="red", fg=white, command=root.quit)
ButtonExit.grid(row=2, column=0, sticky="e")

root.config(bg=background)
root.mainloop()