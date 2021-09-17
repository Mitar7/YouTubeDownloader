from tkinter import *
from tkinter import messagebox
from pytube import YouTube
from PIL import ImageTk, Image
import time
version = 1.0


def show_info():
    link = EntryDownload.get()
    if link:
        yt = YouTube(link)
        ListboxVideo.delete(0, 4)
        ListboxVideo.insert(0, f"Title: {yt.title}")
        ListboxVideo.insert(1, f"Number of views: {yt.views}")
        ListboxVideo.insert(2, f"Length of video: {yt.length} seconds")
        ListboxVideo.insert(3, f"Rating of video: {yt.rating}")
        ListboxVideo.insert(4, f"Age Restricted: {yt.age_restricted}")
    else:
        messagebox.showerror("Invalid input!", "Please enter valid YouTube link!")


def download():
    link = EntryDownload.get()
    if link:
        yt = YouTube(link)
        ListboxVideo.delete(0, 4)
        ListboxVideo.insert(0, f"Title: {yt.title}")
        ListboxVideo.insert(1, f"Number of views: {yt.views}")
        ListboxVideo.insert(2, f"Length of video: {yt.length} seconds")
        ListboxVideo.insert(3, f"Rating of video: {yt.rating}")
        ListboxVideo.insert(4, f"Age Restricted: {yt.age_restricted}")

        ys = yt.streams.get_highest_resolution()
        time.sleep(2)
        ListboxVideo.delete(0, 4)
        ListboxVideo.insert(0, f"Video downloading...")
        time.sleep(1)

        location = EntryLocation.get()
        if location:
            ys.download(location)
        else:
            ys.download()
        ListboxVideo.insert(1, f"Download completed!!")
    else:
        messagebox.showerror("Invalid input!", "Please enter valid YouTube link!")


def audio():
    link = EntryDownload.get()
    if link:
        yt = YouTube(link)
        ListboxVideo.delete(0, 4)
        ListboxVideo.insert(0, f"Title: {yt.title}")
        ListboxVideo.insert(1, f"Number of views: {yt.views}")
        ListboxVideo.insert(2, f"Length of video: {yt.length} seconds")
        ListboxVideo.insert(3, f"Rating of video: {yt.rating}")
        ListboxVideo.insert(4, f"Age Restricted: {yt.age_restricted}")

        ys = yt.streams.get_audio_only()
        time.sleep(2)
        ListboxVideo.delete(0, 4)
        ListboxVideo.insert(0, f"Audio downloading...")
        time.sleep(1)

        location = EntryLocation.get()
        if location:
            ys.download(location)
        else:
            ys.download()
        ListboxVideo.insert(1, f"Download completed!!")
    else:
        messagebox.showerror("Invalid input!", "Please enter valid YouTube link!")


root = Tk()
root.geometry("900x500")
root.title(f"YouTube Dowloader {version}")
root.iconbitmap('img/yt.ico')

FontYT = ("Roboto", 20)
back = "#333"
bela = "#fff"

FrameLeft = Frame(root, width=300, bg=back)
FrameLeft.grid(row=1, column=0)
FrameRight = Frame(root, width=300, bg=back)
FrameRight.grid(row=1, column=1)

logo = Image.open("img/YTdwl.png")
logo = logo.resize((100, 100), Image.ANTIALIAS)
logoSlika = ImageTk.PhotoImage(logo)
LabelLogo = Label(root, image=logoSlika, bg=back)
LabelLogo.grid(row=0, column=0)
LabelOpen = Label(root, text=f"Welcome to the YouTube Dowloader {version}", font=("Roboto", 18), fg=bela, bg=back)
LabelOpen.grid(row=0, column=1, sticky="w")

LabelDownload = Label(FrameLeft, text="Paste YouTube Link: ", font=FontYT, fg=bela, bg=back)
LabelDownload.grid(row=0, column=0, padx=10, pady=20)
EntryDownload = Entry(FrameLeft, width=50)
EntryDownload.grid(row=1, column=0, padx=30)

LabelLocation = Label(FrameLeft, text="Enter Location of a video\n"
                                      " (if empty, it will be saved in"
                                      " the same folder as project) : ", font=("Roboto", 12), fg=bela, bg=back)
LabelLocation.grid(row=2, column=0, padx=10, pady=20)
EntryLocation = Entry(FrameLeft, width=50)
EntryLocation.grid(row=3, column=0, padx=30)

ButtonShow = Button(FrameLeft, text="Show information", bg="darkblue", fg=bela, command=show_info)
ButtonShow.grid(row=4, column=0, pady=10)
ButtonDownload = Button(FrameLeft, text="Download Video", bg="lime", fg=back, command=download)
ButtonDownload.grid(row=5, column=0, pady=10)
ButtonAudio = Button(FrameLeft, text="Download Audio", bg="#FFFACD", fg=back, command=audio)
ButtonAudio.grid(row=6, column=0, pady=10)

ListboxVideo = Listbox(FrameRight, font=("Roboto", 12), width=45, height=15)
ListboxVideo.grid(row=0, column=0)
LabelDownload = Label(FrameRight, text="Copyrighted© Mitar Milovanovic ", fg=bela, bg=back)
LabelDownload.grid(row=1, column=0, sticky="e")
ButtonExit = Button(FrameRight, text="Exit Application", bg="red", fg=bela, command=root.quit)
ButtonExit.grid(row=2, column=0, sticky="e", pady=10)


root.config(bg=back)
root.mainloop()