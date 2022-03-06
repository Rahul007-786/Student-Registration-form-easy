from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "12345",
    database = "TECHNO"
    )
mycursor  = mydb.cursor()
class MyWindow:
    def __init__(self,win):
        #Label
        self.lbl1 = Label(win,text = 'Roll no')
        self.lbl2 = Label(win,text = 'Name')
        self.lbl3 = Label(win,text = 'Age')
        self.lbl4 = Label(win,text = 'Marks')

        #Entry
        self.t1 = Entry()
        self.t2 = Entry()
        self.t3 = Entry()
        self.t4 = Entry()

        #place
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200,y=100)
        self.lbl3.place(x=100, y=150)
        self.t3.place(x=200,y=150)
        self.lbl4.place(x=100, y=200 )
        self.t4.place(x=200, y=200)

        #Button
        self.b1 = Button(win, text = 'Save', command = self.save)
        self.b1.place(x=160,y=250)

    def save(self):
        enter = "INSERT INTO tech_table (Roll_no,S_NAme,Age,Marks) VALUES(%s,%s,%s,%s)"
        g1 = int(self.t1.get())
        g2 =(self.t2.get())
        g3 = int(self.t3.get())
        g4 = int(self.t4.get())
        data = (g1,g2,g3,g4)
        mycursor.execute(enter, data)
        print(mycursor.rowcount, "Record insert")
        mydb.commit()

window=Tk()
mywin=MyWindow(window)
window.title('Hello Python')
window.geometry("400x300+10+10")
window.mainloop()