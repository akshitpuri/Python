import time
import traceback
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import askquestion

import pymysql as pymysql
import tkinter as tk

from PIL import ImageTk
from tkcalendar import DateEntry


class StaffClass:
    def __init__(self, myframe):
        self.mytop = Toplevel(myframe)
        self.mytop.geometry("1130x560+213+128")
        self.mytop.title("Staff Management")
        self.mytop.configure(background="#d9d9d9")
        self.mytop.configure(highlightbackground="#d9d9d9")
        self.mytop.configure(highlightcolor="black")



        self.TNotebook1 = ttk.Notebook(self.mytop)
        self.TNotebook1.place(relx=0.02, rely=0.033, relheight=0.943
                              , relwidth=0.968)
        self.TNotebook1.configure(width=964)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t0 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t0, padding=3)
        self.TNotebook1.tab(0, text="Info", compound="left", underline="-1", )
        self.TNotebook1_t0.configure(background="#d9d9d9")
        self.TNotebook1_t0.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t0.configure(highlightcolor="black")
        self.TNotebook1_t1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(1, text="Search", compound="left", underline="-1", )
        self.TNotebook1_t1.configure(background="#d9d9d9")
        self.TNotebook1_t1.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t1.configure(highlightcolor="black")

        self.Label1 = tk.Label(self.TNotebook1_t0)
        self.Label1.place(relx=0.031, rely=0.056, height=21, width=63)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''First Name''')

        self.Entry1 = tk.Entry(self.TNotebook1_t0)
        self.Entry1.place(relx=0.135, rely=0.056, height=20, relwidth=0.171)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Label2 = tk.Label(self.TNotebook1_t0)
        self.Label2.place(relx=0.385, rely=0.056, height=21, width=62)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Last Name''')

        self.Entry2 = tk.Entry(self.TNotebook1_t0)
        self.Entry2.place(relx=0.479, rely=0.056, height=20, relwidth=0.171)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Label3 = tk.Label(self.TNotebook1_t0)
        self.Label3.place(relx=0.031, rely=0.13, height=21, width=74)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Qualification''')

        self.Entry3 = tk.Entry(self.TNotebook1_t0)
        self.Entry3.place(relx=0.135, rely=0.13, height=20, relwidth=0.171)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")

        self.Label4 = tk.Label(self.TNotebook1_t0)
        self.Label4.place(relx=0.385, rely=0.13, height=21, width=80)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Email Address''')

        self.Entry4 = tk.Entry(self.TNotebook1_t0)
        self.Entry4.place(relx=0.479, rely=0.13, height=20, relwidth=0.171)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")

        self.Label5 = tk.Label(self.TNotebook1_t0)
        self.Label5.place(relx=0.031, rely=0.204, height=21, width=45)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Subject''')

        self.fetch_subject()

        self.sub=StringVar()
        self.TCombobox1 = ttk.Combobox(self.TNotebook1_t0)
        self.TCombobox1.place(relx=0.135, rely=0.204, relheight=0.039
                              , relwidth=0.17)
        self.TCombobox1.configure(takefocus="", textvariable=self.sub, state='readonly', values=self.subjectnames)
        self.TCombobox1.configure(width=163)
        self.TCombobox1.set("Choose Subject")
        self.TCombobox1.configure(takefocus="")

        self.Label6 = tk.Label(self.TNotebook1_t0)
        self.Label6.place(relx=0.385, rely=0.204, height=21, width=37)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Salary''')

        self.Entry5 = tk.Entry(self.TNotebook1_t0)
        self.Entry5.place(relx=0.479, rely=0.204, height=20, relwidth=0.171)
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(insertbackground="black")

        self.Label7 = tk.Label(self.TNotebook1_t0)
        self.Label7.place(relx=0.031, rely=0.278, height=21, width=30)
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text='''DOB''')

        self.dt = DateEntry(self.TNotebook1_t0, background='darkblue', foreground='white', borderwidth=2)
        self.dt.place(relx=0.135, rely=0.278, height=20, relwidth=0.171)

        self.Label8 = tk.Label(self.TNotebook1_t0)
        self.Label8.place(relx=0.385, rely=0.278, height=21, width=44)
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(text='''Gender''')

        self.gender = StringVar()
        self.TRadiobutton1 = ttk.Radiobutton(self.TNotebook1_t0)
        self.TRadiobutton1.place(relx=0.479, rely=0.278, relheight=0.046
                                , relwidth=0.056)
        self.TRadiobutton1.configure(value="Male")
        self.TRadiobutton1.configure(text='''Male''', variable=self.gender)
        self.TRadiobutton1.configure(width=59)

        self.TRadiobutton2 = ttk.Radiobutton(self.TNotebook1_t0)
        self.TRadiobutton2.place(relx=0.563, rely=0.278, relheight=0.046
                                , relwidth=0.069)
        self.TRadiobutton2.configure(takefocus="", value="Female")
        self.TRadiobutton2.configure(text='''Female''', variable=self.gender)
        self.TRadiobutton2.configure(width=71)

        self.Label9 = tk.Label(self.TNotebook1_t0)
        self.Label9.place(relx=0.031, rely=0.352, height=21, width=43)
        self.Label9.configure(background="#d9d9d9")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(text='''Course''')

        self.fetch_courses()

        self.course = StringVar()
        self.TCombobox2 = ttk.Combobox(self.TNotebook1_t0)
        self.TCombobox2.place(relx=0.135, rely=0.352, relheight=0.039
                              , relwidth=0.17)
        self.TCombobox2.configure(takefocus="", textvariable=self.course, state='readonly', values=self.coursenames)
        self.TCombobox2.set('Choose Course')
        self.TCombobox2.configure(width=163)
        self.TCombobox2.configure(takefocus="")


        self.Label10 = tk.Label(self.TNotebook1_t0)
        self.Label10.place(relx=0.031, rely=0.426, height=21, width=87)
        self.Label10.configure(background="#d9d9d9")
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(text='''Phone Number''')

        self.Entry7 = tk.Entry(self.TNotebook1_t0)
        self.Entry7.place(relx=0.135, rely=0.426, height=20, relwidth=0.171)
        self.Entry7.configure(background="white")
        self.Entry7.configure(disabledforeground="#a3a3a3")
        self.Entry7.configure(font="TkFixedFont")
        self.Entry7.configure(foreground="#000000")
        self.Entry7.configure(insertbackground="black")

        self.Label11 = tk.Label(self.TNotebook1_t0)
        self.Label11.place(relx=0.042, rely=0.5, height=21, width=48)
        self.Label11.configure(background="#d9d9d9")
        self.Label11.configure(disabledforeground="#a3a3a3")
        self.Label11.configure(foreground="#000000")
        self.Label11.configure(text='''Address''')

        self.Text1 = tk.Text(self.TNotebook1_t0)
        self.Text1.place(relx=0.135, rely=0.5, relheight=0.193, relwidth=0.338)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=324)
        self.Text1.configure(wrap="word")

        self.Button1 = tk.Button(self.TNotebook1_t0)
        self.Button1.place(relx=0.135, rely=0.741, height=24, width=35)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Save''',command=self.saveinfo)

        self.img = tk.Label(self.TNotebook1_t0)
        self.img.place(x=800,y=50, height=150, width=150)

        self.Button2 = tk.Button(self.TNotebook1_t0)
        self.Button2.place(x=850,y=225, height=24, width=49)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Upload''',command=self.uploadimage)

        self.Label1 = tk.Label(self.TNotebook1_t1)
        self.Label1.place(relx=0.031, rely=0.056, height=21, width=63)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''First Name''')

        self.name = tk.Entry(self.TNotebook1_t1)
        self.name.place(relx=0.135, rely=0.056, height=20, relwidth=0.171)
        self.name.configure(background="white")
        self.name.configure(disabledforeground="#a3a3a3")
        self.name.configure(font="TkFixedFont")
        self.name.configure(foreground="#000000")
        self.name.configure(insertbackground="black")

        self.Label2 = tk.Label(self.TNotebook1_t1)
        self.Label2.place(relx=0.385, rely=0.056, height=21, width=62)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Last Name''')

        self.lname = tk.Entry(self.TNotebook1_t1)
        self.lname.place(relx=0.479, rely=0.056, height=20, relwidth=0.171)
        self.lname.configure(background="white")
        self.lname.configure(disabledforeground="#a3a3a3")
        self.lname.configure(font="TkFixedFont")
        self.lname.configure(foreground="#000000")
        self.lname.configure(insertbackground="black")

        self.Label3 = tk.Label(self.TNotebook1_t1)
        self.Label3.place(relx=0.031, rely=0.13, height=21, width=74)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Qualification''')

        self.qual = tk.Entry(self.TNotebook1_t1)
        self.qual.place(relx=0.135, rely=0.13, height=20, relwidth=0.171)
        self.qual.configure(background="white")
        self.qual.configure(disabledforeground="#a3a3a3")
        self.qual.configure(font="TkFixedFont")
        self.qual.configure(foreground="#000000")
        self.qual.configure(insertbackground="black")

        self.Label4 = tk.Label(self.TNotebook1_t1)
        self.Label4.place(relx=0.385, rely=0.13, height=21, width=80)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Email Address''')

        self.eadd = tk.Entry(self.TNotebook1_t1)
        self.eadd.place(relx=0.479, rely=0.13, height=20, relwidth=0.171)
        self.eadd.configure(background="white")
        self.eadd.configure(disabledforeground="#a3a3a3")
        self.eadd.configure(font="TkFixedFont")
        self.eadd.configure(foreground="#000000")
        self.eadd.configure(insertbackground="black")

        self.Label5 = tk.Label(self.TNotebook1_t1)
        self.Label5.place(relx=0.031, rely=0.204, height=21, width=45)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Subject''')

        self.fetch_subject()

        self.subject = StringVar()
        self.TCombobox = ttk.Combobox(self.TNotebook1_t1)
        self.TCombobox.place(relx=0.135, rely=0.204, relheight=0.039
                              , relwidth=0.17)
        self.TCombobox.configure(takefocus="", textvariable=self.subject, state='readonly', values=self.subjectnames)
        self.TCombobox.configure(width=163)
        self.TCombobox.set("Choose Subject")
        self.TCombobox.configure(takefocus="")

        self.Label6 = tk.Label(self.TNotebook1_t1)
        self.Label6.place(relx=0.385, rely=0.204, height=21, width=37)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Salary''')

        self.sal = tk.Entry(self.TNotebook1_t1)
        self.sal.place(relx=0.479, rely=0.204, height=20, relwidth=0.171)
        self.sal.configure(background="white")
        self.sal.configure(disabledforeground="#a3a3a3")
        self.sal.configure(font="TkFixedFont")
        self.sal.configure(foreground="#000000")
        self.sal.configure(insertbackground="black")

        self.Label7 = tk.Label(self.TNotebook1_t1)
        self.Label7.place(relx=0.031, rely=0.278, height=21, width=30)
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text='''DOB''')

        self.dob = DateEntry(self.TNotebook1_t1, background='darkblue', foreground='white', borderwidth=2)
        self.dob.place(relx=0.135, rely=0.278, height=20, relwidth=0.171)

        self.Label8 = tk.Label(self.TNotebook1_t1)
        self.Label8.place(relx=0.385, rely=0.278, height=21, width=44)
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(text='''Gender''')

        self.gender1 = StringVar()
        self.TRadiobutton3 = ttk.Radiobutton(self.TNotebook1_t1)
        self.TRadiobutton3.place(relx=0.479, rely=0.278, relheight=0.046
                                 , relwidth=0.056)
        self.TRadiobutton3.configure(value="Male")
        self.TRadiobutton3.configure(text='''Male''', variable=self.gender1)
        self.TRadiobutton3.configure(width=59)

        self.TRadiobutton4 = ttk.Radiobutton(self.TNotebook1_t1)
        self.TRadiobutton4.place(relx=0.563, rely=0.278, relheight=0.046
                                 , relwidth=0.069)
        self.TRadiobutton4.configure(takefocus="", value="Female")
        self.TRadiobutton4.configure(text='''Female''', variable=self.gender1)
        self.TRadiobutton4.configure(width=71)

        self.Label9 = tk.Label(self.TNotebook1_t1)
        self.Label9.place(relx=0.031, rely=0.352, height=21, width=43)
        self.Label9.configure(background="#d9d9d9")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(text='''Course''')

        self.fetch_courses()

        self.course1 = StringVar()
        self.cr = ttk.Combobox(self.TNotebook1_t1)
        self.cr.place(relx=0.135, rely=0.352, relheight=0.039
                              , relwidth=0.17)
        self.cr.configure(takefocus="", textvariable=self.course1, state='readonly', values=self.coursenames)
        self.cr.set('Choose Course')
        self.cr.configure(width=163)
        self.cr.configure(takefocus="")

        self.Label10 = tk.Label(self.TNotebook1_t1)
        self.Label10.place(relx=0.031, rely=0.426, height=21, width=87)
        self.Label10.configure(background="#d9d9d9")
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(text='''Phone Number''')

        self.ph = tk.Entry(self.TNotebook1_t1)
        self.ph.place(relx=0.135, rely=0.426, height=20, relwidth=0.171)
        self.ph.configure(background="white")
        self.ph.configure(disabledforeground="#a3a3a3")
        self.ph.configure(font="TkFixedFont")
        self.ph.configure(foreground="#000000")
        self.ph.configure(insertbackground="black")

        self.Label11 = tk.Label(self.TNotebook1_t1)
        self.Label11.place(relx=0.042, rely=0.5, height=21, width=48)
        self.Label11.configure(background="#d9d9d9")
        self.Label11.configure(disabledforeground="#a3a3a3")
        self.Label11.configure(foreground="#000000")
        self.Label11.configure(text='''Address''')

        self.add = tk.Text(self.TNotebook1_t1)
        self.add.place(relx=0.135, rely=0.5, relheight=0.193, relwidth=0.338)
        self.add.configure(background="white")
        self.add.configure(font="TkTextFont")
        self.add.configure(foreground="black")
        self.add.configure(highlightbackground="#d9d9d9")
        self.add.configure(highlightcolor="black")
        self.add.configure(insertbackground="black")
        self.add.configure(selectbackground="#c4c4c4")
        self.add.configure(selectforeground="black")
        self.add.configure(width=324)
        self.add.configure(wrap="word")



        self.img1 = tk.Label(self.TNotebook1_t1)
        self.img1.place(x=800, y=20, height=150, width=150)
        self.filename = ImageTk.PhotoImage(file="images/default.png" )
        self.img1.config(image=self.filename)
        self.img.config(image=self.filename)

        self.update = tk.Button(self.TNotebook1_t1)
        self.update.place(relx=0.135, rely=0.741, height=24, width=55)
        self.update.configure(text='Update', command=self.updateinfo)

        self.delete = tk.Button(self.TNotebook1_t1)
        self.delete.place(relx=0.195, rely=0.741, height=24, width=55)
        self.delete.configure(text='Delete', command=self.deleteinfo)

        self.search = tk.Button(self.TNotebook1_t1)
        self.search.place(relx=0.255, rely=0.741, height=24, width=55)
        self.search.configure(text='Search', command=self.searchinfo)

        mytablearea = Frame(self.TNotebook1_t1)
        scrollbarx = Scrollbar(mytablearea, orient=HORIZONTAL)
        scrollbary = Scrollbar(mytablearea, orient=VERTICAL)

        self.mytable = ttk.Treeview(mytablearea, columns=("fname", "phone", "subject"),
                                    xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)
        self.mytable['show'] = 'headings'
        scrollbarx.config(command=self.mytable.xview)
        scrollbary.config(command=self.mytable.yview)

        scrollbarx.pack(side=BOTTOM, fill=X)
        scrollbary.pack(side=RIGHT, fill=Y)


        self.mytable.heading("fname", text="Name")
        self.mytable.heading("phone", text="Phone")

        self.mytable.heading("subject", text="Subject")

        self.mytable.column('#0', stretch=NO, minwidth=0, width=0)
        self.mytable.column('#1', stretch=NO, minwidth=0, width=120)
        self.mytable.column('#2', stretch=NO, minwidth=0, width=140)
        self.mytable.column('#3', stretch=NO, minwidth=0, width=140)

        self.mytable.bind("<ButtonRelease-1>", self.fetchbysrno)
        self.mytable.pack()
        mytablearea.place(relx = 0.521, rely = 0.5, height = 101, width = 414)

    def searchinfo(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                        db="collegedb")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select fname, phone,subject from stafftable"
                               " where fname like %s", (self.name.get() + "%"))
                    myresultdata = myconn.fetchall()
                    self.mytable.delete(*self.mytable.get_children())
                    for row in myresultdata:
                        self.mytable.insert('', END, value=(row))

                    if myresultdata == None:
                        messagebox.showerror("No Records Found", "No Students added yet.")

            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex))
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))


    def fetchbysrno(self, e):
        currentItem = self.mytable.focus()
        contents = self.mytable.item(currentItem)
        selectedRow = contents['values']
        self.serialno = selectedRow[1]
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                        db="collegedb")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select * from stafftable where phone=%s",
                               (self.serialno))
                    myresultdata = myconn.fetchall()

                    for row in myresultdata:
                        self.ph.delete(0, END)
                        self.ph.insert(0,self.serialno)
                        self.name.delete(0,END)
                        self.name.insert(0,row[0])
                        self.lname.delete(0, END)
                        self.lname.insert(0, row[1])
                        self.qual.delete(0, END)
                        self.qual.insert(0, row[2])
                        self.eadd.delete(0, END)
                        self.eadd.insert(0, row[3])

                        self.sal.delete(0, END)
                        self.sal.insert(0, row[5])
                        self.dob.delete(0, END)
                        self.dob.insert(0, row[6])
                        self.add.delete('1.0', END)
                        self.add.insert('1.0', row[10])

                        self.filename = ImageTk.PhotoImage(file="images//" + row[11])

                        self.img1.config(image=self.filename)
                        self.course1.set(row[8])
                        self.subject.set(row[4])
                        if row[7] == "Male":
                            self.gender1.set("Male")
                        else:
                            self.gender1.set("Female")

                    if myresultdata == None:
                        messagebox.showerror("No Records Found", "No Staff added yet.")

            except Exception as ex:
                traceback.print_exc()
                messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex))
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))


    def updateinfo(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="collegedb")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute(
                        "update stafftable set fname=%s,lname=%s,qualf=%s,eadd=%s,subject=%s,salary=%s,dob=%s,gender=%s,course=%s,address=%s,phone=%s where phone=%s",
                        (self.name.get(),self.lname.get(),self.qual.get(),self.eadd.get(),self.subject.get(),self.sal.get(),
                         self.dob.get_date(),self.gender1.get(),self.course1.get(),self.add.get('1.0',END),self.ph.get(), self.serialno
                        ))
                    mydatabaseobj.commit()
                    messagebox.showinfo("Success", "Record Updated Successfully",parent=self.TNotebook1_t1)
            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex))
            finally:
                mydatabaseobj.close()
            self.gender1.set(" ")
            self.course1.set("Choose Course")
            self.subject.set("Choose Subject")
            self.ph.delete(0, END)
            self.name.delete(0, END)
            self.lname.delete(0, END)
            self.filename2 = ImageTk.PhotoImage(file="images/default.png")

            self.img1.config(image=self.filename2)

            self.qual.delete(0, END)

            self.eadd.delete(0, END)

            self.sal.delete(0, END)

            self.dob.delete(0, END)
            self.mytable.delete(*self.mytable.get_children())
            self.add.delete('1.0', END)
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))

    def deleteinfo(self):
        answer = askquestion("Confirm", "Do you really want to delete?", icon="warning")

        if answer == "yes":
            try:
                mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                                db="collegedb")
                try:

                    with mydatabaseobj.cursor() as myconn:
                        myconn.execute(
                            "delete from stafftable where phone=%s",
                            (self.serialno))
                        mydatabaseobj.commit()
                        messagebox.showinfo("Success", "Record Deleted Successfully",parent=self.TNotebook1_t1)
                except Exception as ex:
                    messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex),
                                        )

                finally:
                    mydatabaseobj.close()
                self.mytable.delete(*self.mytable.get_children())
                self.gender1.set(" ")
                self.course1.set("Choose Course")
                self.subject.set("Choose Subject")
                self.ph.delete(0, END)
                self.name.delete(0, END)
                self.filename1 = ImageTk.PhotoImage(file="images/default.png")

                self.img1.config(image=self.filename1)

                self.lname.delete(0, END)

                self.qual.delete(0, END)

                self.eadd.delete(0, END)


                self.sal.delete(0, END)

                self.dob.delete(0, END)

                self.add.delete('1.0', END)


            except Exception as ex:
                messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))


    def saveinfo(self):

        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="", db="collegedb")



            try:
                with mydatabaseobj.cursor() as myconn:
                    myconn.execute(
                        "insert into stafftable(fname,lname,qualf,eadd,subject,salary,dob,gender,course,phone,address,image) "
                        "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (self.Entry1.get(),self.Entry2.get(),self.Entry3.get(),self.Entry4.get(),self.TCombobox1.get(),self.Entry5.get(),
                         self.dt.get_date(),self.gender.get(),self.course.get(),self.Entry7.get(),self.Text1.get('1.0',END),self.myfinalname
                        ))
                    mydatabaseobj.commit()
                    messagebox.showinfo("Success", "Record Saved Successfully", parent=self.TNotebook1_t0)

            except Exception as ex:
                messagebox.showerror("Error Occured","Please Fill All Blocks!", parent=self.TNotebook1_t0)
            finally:
                mydatabaseobj.close()
            self.gender.set(" ")
            self.course.set("Choose Course")
            self.TCombobox1.set("Choose Subject")
            self.Entry7.delete(0, END)
            self.Entry1.delete(0, END)

            self.filename = ImageTk.PhotoImage(file="images/default.png")

            self.img.config(image=self.filename)
            self.Entry2.delete(0, END)

            self.Entry3.delete(0, END)

            self.Entry4.delete(0, END)

            self.Entry5.delete(0, END)

            self.dt.delete(0, END)

            self.Text1.delete('1.0', END)
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))

    def fetch_subject(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="collegedb")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select * from subjecttable")
                    myresultdata = myconn.fetchall()
                    self.subjectnames = []
                    for row in myresultdata:
                        self.subjectnames.append(row[0])

                    if len(self.subjectnames) == 0:
                        messagebox.showerror("Error Occured", "No Subject added. Add Subject from Misc Menu first")

            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex))
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))

    def fetch_courses(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="collegedb")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select * from coursetable")
                    myresultdata = myconn.fetchall()
                    self.coursenames = []
                    for row in myresultdata:
                        self.coursenames.append(row[0])

                    if len(self.coursenames) == 0:
                        messagebox.showerror("Error Occured", "No Courses added. Add Course from Misc Menu first")

            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex))
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))

    def uploadimage(self):
        filename = askopenfilename(filetypes=[(("Picture Files", "*.jpg;*.png;*.gif"))])

        self.image = ImageTk.PhotoImage(file=filename)
        mydata = filename.split("/")
        self.myfinalname = str(int(time.time())) + mydata[-1]

        infile = open(filename, "rb")
        outfile = open("images//" + self.myfinalname, "wb")
        for line in infile:
            outfile.write(line)
        infile.close()
        outfile.close()
        self.img.configure(image=self.image)







