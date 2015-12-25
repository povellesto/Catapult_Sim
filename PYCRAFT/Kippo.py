from Tkinter import *
root = Tk()


starts = ["Hi my name is Kippo, what would you like","Hi what would you like","Do you like choclate? Any way what would you like"]
T = Text("Hi my name is Kippo, what would you like")
T()





canvas = Canvas(root, width = 200, height=250)
canvas.pack()
root.resizable(width=0, height=0)
root.canvas = canvas.canvas = canvas
root.wm_title("Blob Rage")
commands = input("")
if commands == quit:
    canvas.destroy()
root.mainloop()