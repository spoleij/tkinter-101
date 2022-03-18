from itertools import cycle
import tkinter
window = tkinter.Tk()

# SCHRIJF CODE HIER TUSSEN

window.title("My First Window")
window.configure(bg='white')
window.geometry('50x50')
colors = ['white','yellow','orange','red','purple','black']

boom = 6

def updateWindow (i):
    size = (i+1) * 50
    calc = f'{size}x{size}'
    color = colors[i]
    print (f'{color} {calc}') #test de kleur
    print (boom)                        
    window.geometry(calc)
    window.configure(bg=color)
    window.update()
    
for i in range (6): 
    window.after(2000, updateWindow(i))
    boom = boom - 1
    
print ('BOOM!')
window.destroy()

# SCHRIJF CODE HIER TUSSEN

window.mainloop()