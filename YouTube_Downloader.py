from tkinter import *
from pytube import YouTube
from tkinter import ttk
from tkinter import filedialog

root = Tk()
root.title("My Youtube Downloader.")
root.geometry("400x450")
root.minsize(400, 450)
root.maxsize(400, 450)
root.columnconfigure(0, weight=1)

Folder_Name = ""

try:
    def chfile():
        global Folder_Name
        Folder_Name = filedialog.askdirectory()
        if (len(Folder_Name) > 1):
            errormsg1.config(text=Folder_Name)
        else:
            errormsg1.config(text="Plz.. Choose A Folder...!")


    def downloadfile():
        choice = ch1.get()
        url = vidurl.get()
        if (len(url) > 1):
            errormsg2.config(text="No Error Yet...!")
        else:
            errormsg2.config(text="Plz.. Enter URL...!")

        yt = YouTube(url)
        if (choice == chval[0]):
            select = yt.streams.filter(progressive=True).first()
        elif (choice == chval[1]):
            select = yt.streams.filter(progressive=True).last()
        elif (choice == chval[2]):
            select = yt.streams.filter(only_audio=True).first()
        else:
            errormsg2.config(text="Error: Check The Link Again...!")

        select.download(Folder_Name)
        cmpmsg.config(text="...Download Completed...")
except Exception as e:
    print(e)
# l1 = Label(root, text="Enter The URL Of Video", font="bold")
# l1.pack()
#
# vidlink = Entry(width=50)
# vidlink.pack(pady=5)

l2 = Label(text="Select The Location Where To Save")
l2.pack(pady=5)

btnfile = Button(text="Choose Path", bg="green", fg="black", command=chfile).pack()

errormsg1 = Label(text="", fg="Red")
errormsg1.pack(pady=5)

l3 = Label(text="Enter Video URL")
l3.pack(pady=5)

vidurl = Entry(width=50)
vidurl.pack(pady=5)

errormsg2 = Label(text="", fg="Red")
errormsg2.pack(pady=5)

l4 = Label(root, text="Select Quality", font="bold")
l4.pack(pady=5)

chval = ["720p", "144p", "Only Audio"]
ch1 = ttk.Combobox(value=chval)
ch1.pack(pady=5)

btndownload = Button(text="*Download*", bg="green", fg="black", command=downloadfile).pack(pady=5)

cmpmsg = Label(text="", fg="green")
cmpmsg.pack(pady=5)

root.mainloop()
