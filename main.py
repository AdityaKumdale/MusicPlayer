import tkinter as tk                #for UI
import fnmatch
import os 

#installed pygame
from pygame import mixer

#designing UI of the app 
canvas = tk.Tk()                    #canvas is object
canvas.title("Meditational Waves")
canvas.geometry("600x800")
canvas.config(bg = 'black')         #setting background

rootpath = "C:\\Users\Aditya Kumdale\Music\EMINEM" 
#we need to match all the files in this folder with pattern cause we only want to play mp3
pattern = "*.mp3"

mixer.init()  #initializing mixer

prev_img = tk.PhotoImage(file = "prev_img.png")
stop_img = tk.PhotoImage(file = "stop_img.png")
play_img = tk.PhotoImage(file = "play_img.png")
pause_img = tk.PhotoImage(file = "pause_img.png")
next_img = tk.PhotoImage(file = "next_img.png")

def select():
    label.config(text= listBox.get("anchor"))  #anchor to get selected song
    mixer.music.load(rootpath + "\\" + listBox.get("anchor"))   #to play our song
    mixer.music.play()

def stop():
    mixer.music.stop()
    listBox.select_clear('active')

def play_next():
    next_song = listBox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listBox.get(next_song)
    label.config(text = next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    #to move hover to next selected song
    listBox.select_clear(0,'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

def play_prev():
    next_song = listBox.curselection()
    next_song = next_song[0] - 1
    next_song_name = listBox.get(next_song)
    label.config(text = next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    #to move hover to next selected song
    listBox.select_clear(0,'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

def pause_song():
    if pauseButton["text"] == "Pause":
        mixer.music.pause()
        pauseButton["text"] = "Play"
    else:
        mixer.music.unpause()
        pauseButton["text"] = "Pause"


#to show our files in our UI box(tkinter)
listBox = tk.Listbox(canvas,fg = "cyan",bg = "black",width=100,font = ('poppins',14))
listBox.pack(padx=15,pady=150)
#to make our buttons
label = tk.Label(canvas,text = '',bg="black",fg = "yellow",font = ('poppins',14))
label.pack(pady = 15)

#to make our buttons in horizontal order
top = tk.Frame(canvas, bg = "black")
top.pack(padx = 10,pady = 5,anchor= 'center')

prevButton = tk.Button(canvas, text = "Prev",image= prev_img,bg='black',borderwidth= 0,command=play_prev)
prevButton.pack(pady = 15, in_ = top, side = 'left')      # side will store next button left of each other

stopButton = tk.Button(canvas, text = "Stop",image= stop_img,bg='black',borderwidth= 0,command=stop)
stopButton.pack(pady = 15,in_ = top, side = 'left')

playButton = tk.Button(canvas, text = "Play",image= play_img,bg='black',borderwidth= 0,command=select)
playButton.pack(pady = 15,in_ = top, side = 'left')

pauseButton = tk.Button(canvas, text = "Pause",image= pause_img,bg='black',borderwidth= 0,command=pause_song)
pauseButton.pack(pady = 15,in_ = top, side = 'left')

nextButton = tk.Button(canvas, text = "Next",image= next_img,bg='black',borderwidth= 0,command = play_next)
nextButton.pack(pady = 15,in_ = top, side = 'left')
# listBox.insert(0,"Coding")
# listBox.insert(1,"With")
# listBox.insert(2,"Aditya")

#searching mp3 files in rootpath
for root,dirs,files in os.walk(rootpath):   #traversing rootpath in files dirs 
    for filename in fnmatch.filter(files,pattern):           #matching files with pattern
        listBox.insert('end',filename)

canvas.mainloop()