from tkinter import *
from PIL import ImageTk, Image
import os
import pyaudio
import speech_recognition as sr

def mom():
    root = Tk()
    img = ImageTk.PhotoImage(Image.open("C:\\Python Images\\mom.jpg"))
    panel = Label(root, image = img)
    panel.pack()
    root.after(3000, lambda: root.destroy())
    root.mainloop()
def boy():
    root = Tk()
    img = ImageTk.PhotoImage(Image.open("C:\\Python Images\\boy.jpg"))
    panel = Label(root, image = img)
    panel.pack()
    root.after(3000, lambda: root.destroy())
    root.mainloop()
def aunt():
    root = Tk()
    img = ImageTk.PhotoImage(Image.open("C:\\Python Images\\aunt.jpg"))
    panel = Label(root, image = img)
    panel.pack()
    root.after(3000, lambda: root.destroy())
    root.mainloop()
def baby():
    root = Tk()
    img = ImageTk.PhotoImage(Image.open("C:\\Python Images\\baby.jpg"))
    panel = Label(root, image = img)
    panel.pack()
    root.after(3000, lambda: root.destroy())
    root.mainloop()
def brother():
    root = Tk()
    img = ImageTk.PhotoImage(Image.open("C:\\Python Images\\brother.jpg"))
    panel = Label(root, image = img)
    panel.pack()
    root.after(3000, lambda: root.destroy())
    root.mainloop()
def come():
    root = Tk()
    img = ImageTk.PhotoImage(Image.open("C:\\Python Images\\come.jpg"))
    panel = Label(root, image = img)
    panel.pack()
    root.after(3000, lambda: root.destroy())
    root.mainloop()
    exit()
def girl():
    root = Tk()
    img = ImageTk.PhotoImage(Image.open("C:\\Python Images\\girl.jpg"))
    panel = Label(root, image = img)
    panel.pack()
    root.after(3000, lambda: root.destroy())
    root.mainloop()
def go():
    root = Tk()
    img = ImageTk.PhotoImage(Image.open("C:\\Python Images\\go.jpg"))
    panel = Label(root, image = img)
    panel.pack()
    root.after(3000, lambda: root.destroy())
    root.mainloop()
def grandfather():
    root = Tk()
    img = ImageTk.PhotoImage(Image.open("C:\\Python Images\\grandfather.jpg"))
    panel = Label(root, image = img)
    panel.pack()
    root.after(3000, lambda: root.destroy())
    root.mainloop()
def home():
    root = Tk()
    img = ImageTk.PhotoImage(Image.open("C:\\Python Images\\home.jpg"))
    panel = Label(root, image = img)
    panel.pack()
    root.after(3000, lambda: root.destroy())
    root.mainloop()
def school():
    root = Tk()
    img = ImageTk.PhotoImage(Image.open("C:\\Python Images\\school.jpg"))
    panel = Label(root, image = img)
    panel.pack()
    root.after(3000, lambda: root.destroy())
    root.mainloop()
def sister():
    root = Tk()
    img = ImageTk.PhotoImage(Image.open("C:\\Python Images\\sister.jpg"))
    panel = Label(root, image = img)
    panel.pack()
    root.after(3000, lambda: root.destroy())
    root.mainloop()
def store():
    root = Tk()
    img = ImageTk.PhotoImage(Image.open("C:\\Python Images\\store.jpg"))
    panel = Label(root, image = img)
    panel.pack()
    root.after(3000, lambda: root.destroy())
    root.mainloop()
def uncle():
    root = Tk()
    img = ImageTk.PhotoImage(Image.open("C:\\Python Images\\uncle.jpg"))
    panel = Label(root, image = img)
    panel.pack()
    root.after(3000, lambda: root.destroy())
    root.mainloop()
def with1():
    root = Tk()
    img = ImageTk.PhotoImage(Image.open("C:\\Python Images\\with.jpg"))
    panel = Label(root, image = img)
    panel.pack()
    root.after(3000, lambda: root.destroy())
    root.mainloop()
def car():
    root = Tk()
    img = ImageTk.PhotoImage(Image.open("C:\\Python Images\\car.jpg"))
    panel = Label(root, image = img)
    panel.pack()
    root.after(3000, lambda: root.destroy())
    root.mainloop()
def dad():
    root = Tk()
    img = ImageTk.PhotoImage(Image.open("C:\\Python Images\\dad.gif"))
    panel = Label(root, image = img)
    panel.pack()
    root.after(3000, lambda: root.destroy())
    root.mainloop()
def drive():
    root = Tk()
    img = ImageTk.PhotoImage(Image.open("C:\\Python Images\\drive.gif"))
    panel = Label(root, image = img)
    panel.pack()
    root.after(3000, lambda: root.destroy())
    root.mainloop()
def in1():
    root = Tk()
    img = ImageTk.PhotoImage(Image.open("C:\\Python Images\\in1.gif"))
    panel = Label(root, image = img)
    panel.pack()
    root.after(3000, lambda: root.destroy())
    root.mainloop()
def out():
    root = Tk()
    img = ImageTk.PhotoImage(Image.open("C:\\Python Images\\out.gif"))
    panel = Label(root, image = img)
    panel.pack()
    root.after(3000, lambda: root.destroy())
    root.mainloop()

def internet():
        os.system("start chrome.exe")


def mainfunction(source):
    audio = r.listen(source)
    user = r.recognize_google(audio)
    l=user.split()
    print(user)


if __name__ == "__main__":
    r = sr.Recognizer()    
    with sr.Microphone() as source:
        while 1:
            mainfunction(source)
    
a=user.split()
z=S.lower()
x=z.split()

Main={'mom':mom,'dad':dad,'boy':boy,'girl':girl,'brother':brother,'sister':sister,
'grandfather':grandfather,'aunt':aunt,'uncle':uncle,'baby':baby,'home':home,'school':school,
'store':store,'come':come,'go':go,'with':with1,'in':in1,'out':out,'car':car,'drive':drive}

for i in Main:
    for j in x:
        if i==j:
            y=Main[j]
            y()
