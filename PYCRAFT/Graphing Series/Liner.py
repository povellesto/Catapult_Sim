from Tkinter import*

root = Tk()
w = Canvas(root, width=200, height=200)
w.config(bg='lightblue')
w.create_line(100,0,100,200, width=0, fill = "black")
w.create_line(0,100,200,100, width=0, fill = "black")
w.pack()
print("Hello and Welcome!")
a = input("Do you want to do half or 2 ")
y = input("y value")
x = (ax)
mainloop()



