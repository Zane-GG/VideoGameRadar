from tkinter import *
import tkinter.font as tkFont


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        # FONTS
        self.h1font = tkFont.Font(family="Serif", size=30)

        self.page1()

    def clickExitButton(self):
        exit()

    def page1(self):
        title = Label(text="Video Game Radar",
                      fg="black",
                      font=self.h1font
                      )
        title.place(relx=0.5, rely=0.1, anchor='center')

        startButton = Button(self, text="Start", width=15, height=5, command=self.page2)
        startButton.place(relx=0.45, rely=0.4, anchor='center')

        exitButton = Button(self, text="Exit", width=15, height=5, command=self.clickExitButton)
        exitButton.place(relx=0.55, rely=0.4, anchor='center')

    def page2(self):

        for widgets in root.winfo_children():
            widgets.destroy()

        a = Label(text="Testing",
                  fg="red",
                  font=self.h1font
                  )
        a.place(relx=0.5, rely=0.1, anchor='center')


root = Tk()
app = Window(root)
root.wm_title("Video Game Radar")
root.geometry("1200x700")
# root.resizable(False, False)
root.minsize(1200, 700)
# root.eval('tk::PlaceWindow . center') #Supposed to center window
root.mainloop()
