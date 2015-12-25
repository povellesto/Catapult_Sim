from Tkinter import*
import tkMessageBox
import Tkinter
class Catapult(Frame):
    def create_gameOp(self):
        root2 = Tk()
        root2.config(width=200, height=200)
        w = Canvas(root2, width=200, height=200,bg="lightblue")
        w.pack()
        w.create_line(0,0,200,200, fill="darkblue", dash=(4, 4))
        w.create_line(200,0,000,200, fill="darkblue", dash=(4, 4))
        w.create_line(100,200,100,0, fill="blue", dash=(4, 4))
        w.create_line(0,100,200,100, fill="blue", dash=(4, 4))

        root3 = Tk()
        w2 = Canvas(root3, width=200, height=200)
        root3.config(width=200, height=200)
        w2 = Label(root3, text="Power")
        w9 = Label(root3, text="Angle")
        w2.pack()
        w9.pack()

        
        e = Entry(root3)
        e.pack()
        e1 = Entry(root3)
        e1.pack()
        def say():
            print(e)
            print(e1)
        b = Button(root3, text="Submit", command=say)
        b.pack()
    def start_items(self):
        Label(self, text="First Name").pack()
        Label(self, text="Last Name").pack()
        e1 = Entry(self)
        e2 = Entry(self)
        
        e1.pack()
        e2.pack()
    def create_Options(self):
        #Creates second window in first screen that has options
        self.text1 = Label(self,text="Welcome to the options!")
        self.text2 = Label(self,text="Here you can change what you start with and the volume,  have fun!")
        self.text1.pack()
        self.text2.pack()
        self.button1 = Button(self, text="Volume")
        self.button2 = Button(self, text="Starting Items", command = self.start_items)
        self.button1.pack()
        self.button2.pack()
    def createWidgets(self):
#
        
        self.text1 = Label(self,text="Welcome to my catapult simulator ")
        self.text1.pack()
        #Text on first page
        self.text1 = Label(self,text="You will have to Enter the power(force) of the shot, the wind force(mph), the angle. ALL OF THE RIGHTS ARE RESERVED  ")
        self.text1.pack()
        self.mb=  Menubutton ( self, text="Menu", relief=RAISED )
        self.mb.grid()
        self.mb.menu  =  Menu ( self.mb, tearoff = 0 )
        self.mb["menu"]  =  self.mb.menu
        # Scroll Bar

        #Scroll bar Stop
        StartVar  = 0
        OptionsVar = 0
#        Exit = root.destroy()    
        
        self.mb.menu.add_checkbutton ( label="Start", command= self.create_gameOp)
        self.mb.menu.add_checkbutton ( label="Options", command = self.create_Options)
#        self.mb.menu.add_checkbutton (label="Exit", variable=Exit)
        self.mb.pack()
        
    def __init__(self, master= None):
        Frame.__init__(self,master)
        self. master = master
        self.pack()
        self.createWidgets()
root = Tk()
app = Catapult(master= root)
app.mainloop()
root.mainloop()