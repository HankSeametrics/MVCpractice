import Tkinter
from Tkinter import *

class Application(Frame):
    def say_hi(self):
        print "Howdy Howdy Howdy"

    def createWidgets(self):
        self.QUIT =Button(self)
        self.QUIT["text"] = "STOP"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "hey Partner"
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side":"left"})
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
try:
    root =Tk()
    app =Application(master=root)
    app.mainloop()
    root.destroy()
except Exception as ex:
    print ex
    raw_input()