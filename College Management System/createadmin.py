import traceback
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.messagebox import askquestion

import pymysql as pymysql

import parent


class CreateAdmin:

    def __init__(self):
        self.mywindow = Tk()
        self.mywindow.wm_title("Running First Time, Create Admin Account")


        self.mywindow.geometry("800x450+260+110")

        namebox = Label(self.mywindow, text="Username")
        namebox.place(x=100, y=100)

        self.nameentrybox = Entry(self.mywindow)
        self.nameentrybox.place(x=300, y=100)

        passwordbox = Label(self.mywindow, text="Password")
        passwordbox.place(x=100, y=150)

        self.passwordentrybox = Entry(self.mywindow, show="*")
        self.passwordentrybox.place(x=300, y=150)


        savebtn = Button(self.mywindow, text="Create Admin", command=self.createadmininfo, padx=20)
        savebtn.place(x=300, y=200)
        # messagebox.showinfo("Welcome", "Running First Time, Creating Admin Account First")
        self.mywindow.mainloop()


    def createadmininfo(self):
        try:
                mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                                db="collegedb")
                try:

                    with mydatabaseobj.cursor() as myconn:
                        myconn.execute("insert into usertable values(%s,%s,%s)", (self.nameentrybox.get(), self.passwordentrybox.get(), "Admin"))
                        mydatabaseobj.commit()
                        messagebox.showinfo("Success", "Admin Account created successfully")
                        self.mywindow.destroy()
                        parent.myparent()

                except Exception as ex:
                    messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex))
                finally:
                    mydatabaseobj.close()
        except Exception as ex:
                messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))


