from tkinter import *
import tkinter.font as font
from tkinter import messagebox
import backend as bk

st = ""
def function():
    global st
    bk.final_one()

def function_():
    messagebox.showinfo("Message :) ", "Hello, World!")

def about():
    messagebox.showinfo("About Us","This is an application in which you can Extract Text from Screenshot usin OCR.This application will help you to solve many problems like extracting code from youtube videos directly,extracting paragraphs from images and many more....\nThis Application is Created by Simran Sharma")

window=Tk()
# btn=Button(window, text="This is Button widget", fg='blue')
# btn.place(x=80, y=100)

a = "#04bf9d"
b = "#25126C"
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 379,
    width = 678,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

f = font.Font(size = 24,weight="bold")

lbl = Label(window,text="Extract Text from Screenshot Easily!!",background=a,fg = b,font=f)
lbl.pack(pady=50, side= TOP, anchor="center")

main_btn = Button(window,text = "Take Screenshot",font=f,bg=b,fg=a,borderwidth=0)
main_btn.pack(pady=20,side=TOP,anchor="center")
main_btn["command"] =function

abt = Button(window,text = "About",font=font.Font(size = 14),bg=b,fg=a,borderwidth=0)
abt.pack(pady=5,padx = 5,side=LEFT,anchor="se",expand=True)
abt["command"] =about


abt = Button(window,text = "Contact",font=font.Font(size = 14),bg=b,fg=a,borderwidth=0)
abt.pack(pady=5,padx = 5,side=RIGHT,anchor="se")

canvas.create_rectangle(
    0,0,678,379,
    fill = "#04bf9d",
    outline = "")

# window.clipboard_append(st)
# print(st)
window.title('Hello Python')
window.geometry("678x379+10+10")
window.mainloop()
# main_btn["command"] = command=function()