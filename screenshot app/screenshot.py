import time
import tkinter as tk
import pyautogui
def screenshot():
    root.withdraw()
    time.sleep(3)
    name = int(round(time.time()*1000))
    name = "E:/Python/Screenshots/{}.png".format(name)
    img = pyautogui.screenshot(name)
    img.show()
    root.deiconify()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame,text = "Take Screenshot",command= screenshot)
button.pack(side=tk.LEFT)
close = tk.Button(frame,text = "Quit",command= root.destroy)
close.pack(side=tk.LEFT)
root.mainloop()
