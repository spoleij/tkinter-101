import tkinter
import random
from tkinter.messagebox import showinfo
window = tkinter.Tk()

window.title("Grabbelton 3000")
window.configure(bg='red')
window.geometry('600x300')

def pressButton():
    count = len(itemList)
    if count == 0:
        showinfo (
        title = "Grabbel Info",
        message= f"Helaas, de grabbelton is leeg!"
    )
        return
    randomItem = random.choice(itemList)
    itemList.pop(itemList.index(randomItem))
    count = len(itemList)
    stringVar.set(f"er zitten {count} items in de grabbelton")

    showinfo (
        title = "Grabbel Info",
        message= f"Gefeliciteerd, je hebt een {randomItem} gegrabbeld!"
    )
  

button = tkinter.Button(text='Grabbelen', bg="white", fg="black", font=("Comic Sans MS", 15), command=pressButton)                      
button.pack(pady = 20, padx = 20)

itemList = ['aardappel', 'pindakaaspotje', 'gerda', 'kussensloop', 'paaseitje', 'bitterbal', 'dvd-speler', 'ps5', 'sok met een gat er in', 'kikker']

stringVar = tkinter.StringVar(value="er zitten 10 items in de grabbelton")

label = tkinter.Label(window)
label.configure(textvariable=stringVar, bg='yellow', font=("Comic Sans MS", 15))
label.pack()

window.mainloop()