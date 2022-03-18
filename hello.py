import tkinter
window = tkinter.Tk()

window.title("Hello")
window.configure(bg='green')
window.geometry('100x100')

box1 = tkinter.Label(
    window,
    text="Hello Tkinter!",
    bg="yellow",
    fg="red"
)

box1.pack(
    ipadx=10,
    ipady=10,
    expand=True
)


window.mainloop()