from tkinter import *
from tkinter import messagebox
import time, sys
from pygame import mixer
from PIL import Image, ImageTk
def alarm():
    alarm_time=user_input.get()
    if alarm_time=="":
        messagebox.askretrycancel("error message","please enter Value")
    else:
        while True:
            time.sleep(1)
            if (alarm_time==time.strftime("%HH:%MM")):
                playmusic()

def playmusic():
    mixer.init()
    mixer.music.load("[iSongs.info] 01 - Chirunama Thana Chirunama.mp3")   
    mixer.music.play()
    while mixer.music.get_busy():
          time.sleep(2)
          mixer.music.stop()
          sys.exit()

root=Tk()
root.title("Alarm clock")
root.geometry("600x380")
canvas=Canvas(root,width=600,height=380)
image=ImageTk.PhotoImage(Image.open("Screenshot 2023-09-26 072352.png"))
canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()
header=Frame(root)

box1=Frame(root)
box1.place(x=250,y=180)
box2=Frame(root)
box2.place(x=250,y=260)


# time taken by user as a input:-
user_input=Entry(box1,text='HH:MM',font=('Arial Narrow',20),width=8)
user_input.grid(row=1,column=2)

# set Alarm Button:-
start_button=Button(box2,text='Set Alarm ',font=('Arial Narrow',16,'bold'))
start_button.grid(row=3,column=2)
root.mainloop()
