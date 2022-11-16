# from cProfile import label
from tkinter import *
from tkinter import font
from tkinter import messagebox
from turtle import bgcolor
from matplotlib.pyplot import margins, text
from playsound import playsound
import gtts
from gtts import gTTS
from sqlalchemy import false

root = Tk()
root.geometry('550x300')
root.resizable(False, False)
root.configure(bg='black',highlightbackground='green',border='2px',highlightcolor='green',takefocus='green')
root.title("SahilKhan - TEXT2SPEECH")

Label(root, text='TEXT2SPEECH', font='arial 25 bold',bg='black',fg='red' ).pack(fill='x', pady=10)
Label(text='SahilKhan',font='arial 15 bold', bg='black',fg='red',width='20').pack(side='bottom')

msg = StringVar()
Label(root,text='Enter Text:',font='arial 15 bold',bg='black',fg='green').place(x=20,y=80)
entry_field=Entry(root,textvariable=msg,width='36',bg='black',highlightcolor='green',fg='green', font='arial 15',highlightbackground='black',insertbackground='green')
entry_field.place(x=133,y=80)


def text2speech():
        Message = entry_field.get()
        if len(Message)==0:
            a = messagebox.showinfo("Error","No text input!!").pack
        else:
            speech = gTTS(text=Message)
            music = f'{Message[::1]}.mp3'
            speech.save(music)
            playsound(music)
def Exit():
    b=messagebox.askyesno('Exit','Are you sure?')
    if b == True:
        root.quit()
    elif b == False:
        pass
    else:
        messagebox.showerror('error','something went wrong')
def Reset():
    msg.set('')

Button(root,text='Play',font='arial 15 bold',command=text2speech,width='4', bg='black',fg='green',highlightcolor='green',highlightbackground='black').place(x=100,y=140)
Button(root,text='Reset',font='arial 15 bold',command=Reset,width='4', bg='black',fg='green',highlightcolor='green',highlightbackground='black').place(x=250,y=140)
Button(root,text='Exit',font='arial 15 bold',command=Exit,width='4', bg='black',fg='green',highlightcolor='green',highlightbackground='black').place(x=400,y=140)
# Label(root,text="Speech saved!!",font='arial 15 bold',bg='black',fg='green').place(x=20,y=100)
root.mainloop()