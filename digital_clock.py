import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

def time():
    string = strftime('%H:%M:%S\n%m/%d/%y')
    label.config(text=string)
    label.after(1000,time)

label = tk.Label(root, font=('calibri', 50, 'bold'), background = 'blue', foreground = 'lavender')  
label.pack(anchor = 'center') 

time()

root.mainloop()

