from tkinter import Tk, Label, Button

class MainGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text = "This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Gang Gang", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Shhkeeeraaa", command=master.quit)
        self.close_button.pack()

    def greet(self):
        self.label['text'] = "Un saludico eeehh!"


root = Tk()
root.geometry("%dx%d" %(root.winfo_screenwidth()/2,root.winfo_screenheight()/2) )
gui = MainGUI(root)
root.mainloop()
