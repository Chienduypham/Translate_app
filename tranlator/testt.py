from tkinter import *
from PIL import Image ,ImageTk
from googletrans import Translator
import tkinter.ttk as exTk

window = Tk() 
window.title("Translator")
window.geometry("500x580")
window.iconbitmap("logo-g.ico") 

load = Image.open("background-1.jpeg").resize((500,580,),Image.ANTIALIAS)
render = ImageTk.PhotoImage(load) 
img = Label(window,image=render)
img.place(x=0,y=0)

name = Label(window ,text="TRANSLATOR", fg="#ffffff",bg="#005b7a")
name.pack(pady=5)
name.config(font=("Transformers Movie",30))

cmb_1 = exTk.Combobox(window , width = 5, font=("Times", 14))
cmb_1["values"] = ("vi","en")
cmb_1.current(1)
cmb_1.place(x=0,y=2)

cmb_2 = exTk.Combobox(window , width = 5, font=("Times", 14))
cmb_2["values"] = ("vi","en","ja")
cmb_2.current(1)
cmb_2.place(x=435,y=2)

box = Text(window, width=35, height=7,font=("ROBOTO",15))
box.pack(pady=10)

button_frame = Frame(window).pack(side=BOTTOM)

def clear():
	box.delete(1.0,END)
	box_1.delete(1.0,END)

def translate():
	a = cmb_1.get()
	b = cmb_2.get()
	text_input = box.get(1.0,END)
	print(text_input)
	t = Translator()
	text_translate = t.translate(text_input, src=a, dest=b)
	x = text_translate.text
	box_1.insert(END,x)


button_clear = Button(button_frame,text="Clear text" ,font=("Arian",10,"bold"),bg="#303030",fg="#ffffff",command=clear)
button_clear.place(x=100, y=265)
button_translate = Button(button_frame,text="Translate" ,font=("Arian",10,"bold"),bg="#303030",fg="#ffffff",command=translate)
button_translate.place(x=320, y=265)

box_1 = Text(window, width=35, height=10,font=("ROBOTO",15))
box_1.pack(pady=70)


window.mainloop() 