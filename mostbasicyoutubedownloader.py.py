import tkinter as tk
from pytube import YouTube
def vid_download():
    try:
        link = entry.get()
        path = entry2.get()
        vidlink=YouTube(link)
        video=vidlink.streams.get_highest_resolution()
        video.download(path)
        status_label.config(text="The video has been downloaded successfully...") 
    except Exception as e:
        print("Error:",str(e))    

#link=input(print("Enter the link of the video: "))
#path=r"D:\devarth\video"   #This is a raw string. This will treat the slashes as slashes itself and not as escape sequences.
#vid_download(link,path)

window = tk.Tk()
window.configure(background="black")
greeting=tk.Label(text="##DOWNTUBE##",
                  fg="black",
                  bg="white",
                  font=("Times",30),
                  width=15,
                  height=2)
newlabel = tk.Label(text="Enter the  video link",
                    font=("Arial",15) )
path=tk.Label(text="Enter the path of the folder to which the video is to be downloaded",
              font=("Arial",15) )
entry = tk.Entry()
entry2=tk.Entry()
link=entry.get()
greeting.pack()
newlabel.pack()
entry.pack()
path.pack()
path1=entry2.get()
entry2.pack()
status_label = tk.Label(
    text="",  # Initially empty, will be updated when the video is downloaded
    font=("Arial", 12),
    fg="green")


button=tk.Button(text="<DOWNLOAD>",
                font=("Arial",15),
                 command=vid_download)
button.pack()
window.mainloop()
