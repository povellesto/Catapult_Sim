
from Tkinter import *
from tkFileDialog   import askopenfilename
def NewFile():
    yo = Tk()
    b2 = Button(yo, text="Next", command=callback3)
    b2.pack()
def OpenFile():
    name = askopenfilename() 
    print name
def About():
    print "This is a simple example of a menu"
root = Tk()


menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)


S = Scrollbar(root)
T = Text(root, height=4, width=50)
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
quote = """Kippo:
This is my interface, I would like to introduce it to you.
Please follow me through my walk through. """
T.insert(END, quote)
def callback3():
    root2 = Tk()
    b2 = Button(root2, text="Next", command=callback3)
    b2.pack()
    T = Text(root2, height=4, width=50)
    T.pack(side=LEFT, fill=Y)
    T.config(yscrollcommand=S.set)
    quote = """Kippo:
. """
    T.insert(END, quote)
def callback2():
    root2 = Tk()
    b2 = Button(root2, text="Next", command=callback3)
    b2.pack()
    T = Text(root2, height=4, width=50)
    T.pack(side=LEFT, fill=Y)
    T.config(yscrollcommand=S.set)
    quote = """Kippo:
    Thats it!
    Tell me if you need help """
    T.insert(END, quote)
def callback():
    root2 = Tk()
    b2 = Button(root2, text="Next", command=callback2)
    b2.pack()
    T = Text(root2, height=4, width=50)
    T.pack(side=LEFT, fill=Y)
    T.config(yscrollcommand=S.set)
    quote = """Kippo:
    One,
    I love using buttons, why?
    WHY NOT"""
    T.insert(END, quote)
b = Button(root, text="Let's begin", command=callback)
b.pack()



mainloop(  )
