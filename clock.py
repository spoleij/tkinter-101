import tkinter
import time
window = tkinter.Tk()

window.title("Clock")
window.configure(bg='green')
window.geometry('600x200')

stringVar = tkinter.StringVar(value="test")

label = tkinter.Label(window)
label.configure(textvariable=stringVar, bg='yellow', font=("Comic Sans MS", 80))

label.pack(
    fill= 'both',
    expand= True,

)

def updateLabel():
    clock = time.localtime()
    newClock = f' {clock.tm_hour} : {clock.tm_min} : {clock.tm_sec}'
    stringVar.set(newClock)

def updateClock():
    updateLabel()
    window.after(1,updateClock)

updateClock()

window.mainloop()