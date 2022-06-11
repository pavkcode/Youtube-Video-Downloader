import os
from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from tkinter import messagebox
from tkinter.ttk import Combobox

def open_directory():
   file = filedialog.askdirectory()
   savefolder_var.set(file)

def download_video():
    file_type = Combo_filetype.get()
    print(file_type)
    link = Entry_link.get()
    savefolder = savefolder_var.get()
    yt = YouTube(link)
    ytresolution = Combo_fileres.get()
    if('mp4' in file_type):
        print(f"Youtube Link  : {link}")
        print(f"File Saved In : {savefolder}")
        try:
            yt.streams.filter(progressive = True, 
        file_extension = "mp4").first().download(output_path = savefolder, 
        filename = (yt.title + '.mp4'))
            messagebox.showinfo('PavK YouTube Video Downloader','File Downloaded!\nCheck the given directory.')
        except:
            print("Error!")
            messagebox.showerror("Download",'Error!\nCheck your internet connection.')
    elif('mp3' in file_type):
        try:
            video = yt.streams.filter(only_audio=True).first()
            out_file = video.download(output_path=savefolder)
            file_name = yt.title
            new_file = file_name + '.mp3'
            os.rename(out_file, new_file)
            messagebox.showinfo('PavK YouTube Video Downloader','File Downloaded!\nCheck the given directory.')
        except:
            print("Error!")
            messagebox.showerror("Download",'Error!\nCheck your internet connection.')


app = Tk()
app_title = 'PavK YouTube Video Downloader'
app_geometry = '500x250'
folder_image = PhotoImage(file='F:\\Coding\\PYTHON\\GUI\\YoutubeVideoDownloader\\Assests\\folder.png')
app_icon = PhotoImage(file=(os.path.join('F:\Coding\PYTHON\GUI\YoutubeVideoDownloader\Assests\pavk.png')))
app.title(app_title)
app.geometry(app_geometry)
app.resizable(False,False)
app.iconphoto(False,app_icon)

Frame_full = Frame(app,bg="#E6ECF3",height=600,width=500)
Frame_full.place(x=0,y=0)
Label(app,text="PavK - YouTube Video Downloader",bg='#F2F8FD',font="arial 12").place(x=130,y=3.5)

Label_link = Label(app,text= "Link        :")
Label_link.place(x = 10, y= 50)
link_var=StringVar()
link_var.set("Paste YouTube Video")
Entry_link = Entry(app,width=48,textvariable = link_var, font=('calibre',10,'normal'))
Entry_link.place(x=80,y=49)


Label_savefolder = Label(app,text= "Save To  :")
Label_savefolder.place(x = 10, y= 90)
savefolder_var=StringVar()
savefolder_var.set("Directory Path")
Entry_savefolder = Entry(app,width=48,textvariable = savefolder_var, font=('calibre',10,'normal'))
Entry_savefolder.place(x=80,y=89)
Button(app,command=open_directory,image=folder_image).place(x=472,y=86)

Label_filetype = Label(app,text= "File Type:")
Label_filetype.place(x = 10, y= 130)
Combo_filetype = Combobox(app,width=48,values=("mp4 (video)",
"mp3 (audio)"))
Combo_filetype.set("mp4 (video)")
Combo_filetype.place(x= 80,y= 130)

Label_fileres = Label(app,text= "Resolution:")
Label_fileres.place(x = 10, y= 170)
Combo_fileres = Combobox(app,width=48,values=('144p','240p','360p',
'480p','720p','1080p'))
Combo_fileres.set('480p')
Combo_fileres.place(x= 80,y= 170)

Button(app,command=download_video,text="Download").place(x= 200,y= 200)

app.mainloop()