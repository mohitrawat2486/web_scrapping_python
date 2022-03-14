#import qrcode
#img = qrcode.make("https://www.youtube.com/")
#img = qrcode.make("India is a country with many religions. I love India.")
#img.save("youtubeQR.jpg")

#import cv2
#d = cv2.QRCodeDetector()
#val, _, _ = d.detectAndDecode(cv2.imread("youtubeQR.jpg"))
#print("Decoded text is: ", val)

import calendar
from tkinter import *

#This function displays calendar for a given year
def showCalender():
    gui = Tk()
    gui.config(background='grey')
    gui.title("Calender for the year")
    gui.geometry("550x600")
    year = int(year_field.get())
    gui_content= calendar.calendar(year)
    calYear = Label(gui, text= gui_content, font= "Consolas 10 bold")
    calYear.grid(row=5, column=1,padx=20)
    gui.mainloop()

#Driver code
if __name__=='__main__':
    new = Tk()
    new.config(background='grey')
    new.title("Calender")
    new.geometry("250x140")
    cal = Label(new, text="Calender",bg='grey',font=("times", 28, "bold"))
    #Label for enter year
    year = Label(new, text="Enter year", bg='dark grey')
    #text box for year input
    year_field=Entry(new)
    button = Button(new, text='Show Calender',fg='Black',bg='Blue',command=showCalender)
    
    #adjusting widgets in position
    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    button.grid(row=4, column=1)
    #Exit.grid(row=6, column=1)
    new.mainloop()