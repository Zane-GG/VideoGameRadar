from tkinter import *
import tkinter.font as tkFont
from bs4 import BeautifulSoup
import website

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

        soup = BeautifulSoup(website.html, 'html.parser')

        # data = soup.find('.wikitable').get_text()
        # print(data)

        i = 0.0

        for item in soup.select('.wikitable')[6]:
            print(item.get_text())

            # b = Label(text=item,
            #       fg="black",
            #       font=self.h1font,
            #       width=10000
            #       )
            # b.place(relx=0.5, rely=0.2+i, anchor='center')

            i += 0.1

        a = Label(text='2022 Game Releases',
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
