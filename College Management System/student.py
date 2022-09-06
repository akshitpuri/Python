import time
import traceback
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import askquestion

import pymysql as pymysql
import tkinter as tk

from PIL import ImageTk
from datetime import date
from tkcalendar import DateEntry



class AddStudent:

    def __init__(self, myframe):
        self.mytop=Toplevel(myframe)
        self.mytop.geometry("1130x560+213+128")
        self.mytop.title("Student Management")
        self.mytop.configure(background="#d9d9d9")
        self.mytop.configure(highlightbackground="#d9d9d9")
        self.mytop.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(self.mytop)
        self.Frame1.place(relx=0.009, rely=0.018, relheight=0.965
                          , relwidth=0.978)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=1105)



        self.TNotebook1 = ttk.Notebook(self.Frame1)
        self.TNotebook1.place(relx=0.009, rely=0.018, relheight=0.964
                              , relwidth=0.981)
        self.TNotebook1.configure(width=1084)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t0 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t0, padding=3)
        self.TNotebook1.tab(0, text="Admissions", compound="left", underline="-1"
                            , )
        self.TNotebook1_t0.configure(background="#d9d9d9")
        self.TNotebook1_t0.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t0.configure(highlightcolor="black")
        self.TNotebook1_t1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(1, text="Search", compound="left", underline="-1"
                            , )
        self.TNotebook1_t1.configure(background="#d9d9d9")
        self.TNotebook1_t1.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t1.configure(highlightcolor="black")


        self.Label3 = tk.Label(self.TNotebook1_t0)
        self.Label3.place(relx=0.028, rely=0.139, height=21, width=63)
        self.Label3.configure(text='''First Name''')

        self.Entry1 = tk.Entry(self.TNotebook1_t0)
        self.Entry1.place(relx=0.167, rely=0.139, height=20, relwidth=0.152)


        self.Label4 = tk.Label(self.TNotebook1_t0)
        self.Label4.place(relx=0.361, rely=0.139, height=21, width=62)
        self.Label4.configure(text='''Last Name''')

        self.Entry2 = tk.Entry(self.TNotebook1_t0)
        self.Entry2.place(relx=0.481, rely=0.139, height=20, relwidth=0.152)

        self.Label5 = tk.Label(self.TNotebook1_t0)
        self.Label5.place(relx=0.028, rely=0.218, height=21, width=82)
        self.Label5.configure(text='''Father's Name''')

        self.Entry3 = tk.Entry(self.TNotebook1_t0)
        self.Entry3.place(relx=0.167, rely=0.218, height=20, relwidth=0.152)

        self.Label6 = tk.Label(self.TNotebook1_t0)
        self.Label6.place(relx=0.361, rely=0.218, height=21, width=88)
        self.Label6.configure(text='''Mother's Name''')

        self.Entry4 = tk.Entry(self.TNotebook1_t0)
        self.Entry4.place(relx=0.481, rely=0.218, height=20, relwidth=0.152)


        self.Label7 = tk.Label(self.TNotebook1_t0)
        self.Label7.place(relx=0.028, rely=0.298, height=21, width=112)
        self.Label7.configure(text='''Father's Occupation''')

        self.occu=StringVar()
        self.TCombobox1 = ttk.Combobox(self.TNotebook1_t0)
        self.TCombobox1.place(relx=0.167, rely=0.298, relheight=0.042
                              , relwidth=0.151)
        self.TCombobox1.configure(textvariable=self.occu,state='readonly')
        self.TCombobox1.configure(values=('Business','Service','Doctor','Engineer','Other'))
        self.TCombobox1.set("Choose Occupation")

        self.Label8 = tk.Label(self.TNotebook1_t0)
        self.Label8.place(relx=0.361, rely=0.298, height=21, width=118)
        self.Label8.configure(text='''Mother's Occupation''')
        self.occu1 = StringVar()
        self.TCombobox2 = ttk.Combobox(self.TNotebook1_t0)
        self.TCombobox2.place(relx=0.481, rely=0.298, relheight=0.042
                              , relwidth=0.151)
        self.TCombobox2.configure(textvariable=self.occu1,state='readonly')
        self.TCombobox2.set('Choose Occupation')
        self.TCombobox2.configure(values=('Business', 'Service', 'Doctor', 'Engineer', 'Other'))

        self.Label9 = tk.Label(self.TNotebook1_t0)
        self.Label9.place(relx=0.028, rely=0.377, height=21, width=30)
        self.Label9.configure(text='''DOB''')


        self.dt = DateEntry(self.TNotebook1_t0, foreground='white', borderwidth=2)
        self.dt.place(relx=0.167, rely=0.377, height=20, relwidth=0.152)

        self.dob = DateEntry(self.TNotebook1_t1, foreground='white', borderwidth=2)
        self.dob.place(relx=0.167, rely=0.377, height=20, relwidth=0.152)

        self.TLabel1 = ttk.Label(self.TNotebook1_t0)
        self.TLabel1.place(relx=0.361, rely=0.377, height=19, width=42)
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(text='''Gender''')

        self.gender=StringVar()
        self.TRadiobutton1 = ttk.Radiobutton(self.TNotebook1_t0)
        self.TRadiobutton1.place(relx=0.481, rely=0.377, relwidth=0.055
                                 , relheight=0.0, height=21)
        self.TRadiobutton1.configure(value="Male")
        self.TRadiobutton1.configure(text='''Male''',variable=self.gender)
        self.TRadiobutton1.configure(width=59)

        self.TRadiobutton2 = ttk.Radiobutton(self.TNotebook1_t0)
        self.TRadiobutton2.place(relx=0.556, rely=0.377, relwidth=0.066
                                 , relheight=0.0, height=21)
        self.TRadiobutton2.configure(takefocus="",value="Female")
        self.TRadiobutton2.configure(text='''Female''',variable=self.gender)
        self.TRadiobutton2.configure(width=71)

        self.Label10 = tk.Label(self.TNotebook1_t0)
        self.Label10.place(relx=0.028, rely=0.456, height=21, width=45)
        self.Label10.configure(text='''Course''')

        self.fetch_courses()

        self.course=StringVar()
        self.TCombobox3 = ttk.Combobox(self.TNotebook1_t0)
        self.TCombobox3.place(relx=0.167, rely=0.456, relheight=0.042
                              , relwidth=0.151)
        self.TCombobox3.configure(takefocus="",textvariable=self.course,state='readonly',values=self.coursenames)
        self.TCombobox3.set('Choose Course')

        self.Label11 = tk.Label(self.TNotebook1_t0)
        self.Label11.place(relx=0.361, rely=0.456, height=21, width=45)
        self.Label11.configure(text='''Section''')

        self.fetch_section()
        self.section=StringVar()
        self.TCombobox4 = ttk.Combobox(self.TNotebook1_t0)
        self.TCombobox4.place(relx=0.481, rely=0.456, relheight=0.042
                              , relwidth=0.151)
        self.TCombobox4.configure(takefocus="",textvariable=self.section,state='readonly',values=self.sectionnames)
        self.TCombobox4.set('Choose Section')

        self.TLabel2 = ttk.Label(self.TNotebook1_t0)
        self.TLabel2.place(relx=0.028, rely=0.536, height=19, width=85)

        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(text='''Phone Number''')

        self.img = tk.Label(self.TNotebook1_t0)
        self.img.place(x=780,y=25,width=200, height=250)



        self.Button21 = tk.Button(self.TNotebook1_t0)
        self.Button21.place(x=850,y=300,height=24, width=49)
        self.Button21.configure(text='''Upload''',command=self.uploadimage)

        self.img1 = tk.Label(self.TNotebook1_t1)
        self.img1.place(x=780,y=25,width=200, height=225)

        self.filename = ImageTk.PhotoImage(file="images/default.png")

        self.img1.config(image=self.filename)

        self.filename1 = ImageTk.PhotoImage(file="images/default.png")

        self.img.config(image=self.filename1)

        self.TEntry1 = ttk.Entry(self.TNotebook1_t0)
        self.TEntry1.place(relx=0.167, rely=0.536, relheight=0.042
                           , relwidth=0.154)
        self.TEntry1.configure(takefocus="")
        self.TEntry1.configure(cursor="ibeam")

        self.TLabel3 = ttk.Label(self.TNotebook1_t0)
        self.TLabel3.place(relx=0.361, rely=0.536, height=19, width=71)
        self.TLabel3.configure(font="TkDefaultFont")
        self.TLabel3.configure(relief="flat")
        self.TLabel3.configure(text='''Blood Group''')

        self.bg=StringVar()
        self.TCombobox5 = ttk.Combobox(self.TNotebook1_t0)
        self.TCombobox5.place(relx=0.481, rely=0.536, relheight=0.042
                              , relwidth=0.151)
        self.TCombobox5.configure(textvariable=self.bg, state='readonly')
        self.TCombobox5.set('Choose Blood Group')
        self.TCombobox5.configure(values=('A+', 'A-', 'B+', 'B-', 'AB+','AB-','O+','O-'))
        self.TCombobox5.configure(takefocus="")

        self.Label12 = tk.Label(self.TNotebook1_t0)
        self.Label12.place(relx=0.028, rely=0.615, height=21, width=98)
        self.Label12.configure(text='''Landline Number''')

        self.Entry5 = tk.Entry(self.TNotebook1_t0)
        self.Entry5.place(relx=0.167, rely=0.615, height=20, relwidth=0.152)


        self.Label13 = tk.Label(self.TNotebook1_t0)
        self.Label13.place(relx=0.361, rely=0.615, height=21, width=49)
        self.Label13.configure(text='''Religion''')
        self.religion=StringVar()
        self.TCombobox6 = ttk.Combobox(self.TNotebook1_t0)
        self.TCombobox6.place(relx=0.481, rely=0.615, relheight=0.042
                              , relwidth=0.151)
        self.TCombobox6.configure(textvariable=self.religion, state='readonly')
        self.TCombobox6.set('Choose Religion')
        self.TCombobox6.configure(values=('Hindu', 'Sikh', 'Muslim', 'Christian', 'Other'))
        self.TCombobox6.configure(takefocus="")

        self.TLabel4 = ttk.Label(self.TNotebook1_t0)
        self.TLabel4.place(relx=0.028, rely=0.694, height=19, width=46)
        self.TLabel4.configure(text='''Address''')

        self.Text1 = tk.Text(self.TNotebook1_t0)
        self.Text1.place(relx=0.167, rely=0.694, relheight=0.159, relwidth=0.467)
        self.Text1.configure(width=504)
        self.Text1.configure(wrap="word")

        self.Button1 = tk.Button(self.TNotebook1_t0)
        self.Button1.place(relx=0.167, rely=0.893, height=24, width=35)
        self.Button1.configure(text='''Save''', command=self.saveinfo)

        self.Label14 = tk.Label(self.TNotebook1_t0)
        self.Label14.place(relx=0.361, rely=0.06, height=21, width=89)
        self.Label14.configure(text='''Admission Date''')


        self.today=date.today()
        v = StringVar(self.TNotebook1_t0, value=self.today)
        self.ad = tk.Entry(self.TNotebook1_t0)
        self.ad.place(relx=0.481, rely=0.06, height=20, relwidth=0.152)
        self.ad.configure(text=self.today)
        self.ad.configure(textvariable=v)

        u = StringVar(self.TNotebook1_t1, value=self.today)
        self.addt = tk.Entry(self.TNotebook1_t1)
        self.addt.place(relx=0.481, rely=0.06, height=20, relwidth=0.152)
        self.addt.configure(text=self.today)
        self.addt.configure(textvariable=v)




        self.Label1 = tk.Label(self.TNotebook1_t1)
        self.Label1.place(relx=0.028, rely=0.06, height=21, width=109)
        self.Label1.configure(text='''Admission Number''')



        self.adat = tk.Entry(self.TNotebook1_t1)
        self.adat.place(relx=0.167, rely=0.06, height=21, relwidth=0.152)


        self.Ll3 = tk.Label(self.TNotebook1_t1)
        self.Ll3.place(relx=0.028, rely=0.139, height=21, width=63)
        self.Ll3.configure(text='''First Name''')

        self.fname = tk.Entry(self.TNotebook1_t1)
        self.fname.place(relx=0.167, rely=0.139, height=20, relwidth=0.152)
        self.fname.focus_set()

        self.Lal4 = tk.Label(self.TNotebook1_t1)
        self.Lal4.place(relx=0.361, rely=0.139, height=21, width=62)
        self.Lal4.configure(text='''Last Name''')

        self.lname = tk.Entry(self.TNotebook1_t1)
        self.lname.place(relx=0.481, rely=0.139, height=20, relwidth=0.152)

        self.Lal5 = tk.Label(self.TNotebook1_t1)
        self.Lal5.place(relx=0.028, rely=0.218, height=21, width=82)
        self.Lal5.configure(text='''Father's Name''')

        self.fathername = tk.Entry(self.TNotebook1_t1)
        self.fathername.place(relx=0.167, rely=0.218, height=20, relwidth=0.152)

        self.Label61 = tk.Label(self.TNotebook1_t1)
        self.Label61.place(relx=0.361, rely=0.218, height=21, width=88)
        self.Label61.configure(text='''Mother's Name''')

        self.mname = tk.Entry(self.TNotebook1_t1)
        self.mname.place(relx=0.481, rely=0.218, height=20, relwidth=0.152)

        self.Label71 = tk.Label(self.TNotebook1_t1)
        self.Label71.place(relx=0.028, rely=0.298, height=21, width=112)
        self.Label71.configure(text='''Father's Occupation''')

        self.occupation = StringVar()
        self.fatheroccu = ttk.Combobox(self.TNotebook1_t1)
        self.fatheroccu.place(relx=0.167, rely=0.298, relheight=0.042
                              , relwidth=0.151)
        self.fatheroccu.configure(textvariable=self.occupation, state='readonly')
        self.fatheroccu.configure(values=('Business', 'Service', 'Doctor', 'Engineer', 'Other'))
        self.fatheroccu.set("Choose Occupation")

        self.Label81 = tk.Label(self.TNotebook1_t1)
        self.Label81.place(relx=0.361, rely=0.298, height=21, width=118)
        self.Label81.configure(text='''Mother's Occupation''')
        self.occupation1 = StringVar()
        self.motheroccu = ttk.Combobox(self.TNotebook1_t1)
        self.motheroccu.place(relx=0.481, rely=0.298, relheight=0.042
                              , relwidth=0.151)
        self.motheroccu.configure(textvariable=self.occupation1, state='readonly')
        self.motheroccu.set('Choose Occupation')
        self.motheroccu.configure(values=('Business', 'Service', 'Doctor', 'Engineer', 'Other'))

        self.Label91 = tk.Label(self.TNotebook1_t1)
        self.Label91.place(relx=0.028, rely=0.377, height=21, width=30)
        self.Label91.configure(text='''DOB''')

        self.TLabel11 = ttk.Label(self.TNotebook1_t1)
        self.TLabel11.place(relx=0.361, rely=0.377, height=19, width=42)
        self.TLabel11.configure(text='''Gender''')

        self.gender1 = StringVar()
        self.TRadiobutton3 = ttk.Radiobutton(self.TNotebook1_t1)
        self.TRadiobutton3.place(relx=0.481, rely=0.377, relwidth=0.055
                                 , relheight=0.0, height=21)
        self.TRadiobutton3.configure(value="Male")
        self.TRadiobutton3.configure(text='''Male''', variable=self.gender1)
        self.TRadiobutton3.configure(width=59)

        self.TRadiobutton4 = ttk.Radiobutton(self.TNotebook1_t1)
        self.TRadiobutton4.place(relx=0.556, rely=0.377, relwidth=0.066
                                 , relheight=0.0, height=21)
        self.TRadiobutton4.configure(takefocus="", value="Female")
        self.TRadiobutton4.configure(text='''Female''', variable=self.gender1)
        self.TRadiobutton4.configure(width=71)

        self.Label101 = tk.Label(self.TNotebook1_t1)
        self.Label101.place(relx=0.028, rely=0.456, height=21, width=45)
        self.Label101.configure(text='''Course''')

        self.fetch_courses()

        self.course1 = StringVar()
        self.cr = ttk.Combobox(self.TNotebook1_t1)
        self.cr.place(relx=0.167, rely=0.456, relheight=0.042
                              , relwidth=0.151)
        self.cr.configure(takefocus="", textvariable=self.course1, state='readonly', values=self.coursenames)
        self.cr.set('Choose Course')

        self.Label111 = tk.Label(self.TNotebook1_t1)
        self.Label111.place(relx=0.361, rely=0.456, height=21, width=45)
        self.Label111.configure(text='''Section''')

        self.fetch_section()
        self.sections = StringVar()
        self.sec = ttk.Combobox(self.TNotebook1_t1)
        self.sec.place(relx=0.481, rely=0.456, relheight=0.042
                              , relwidth=0.151)
        self.sec.configure(takefocus="", textvariable=self.sections, state='readonly', values=self.sectionnames)
        self.sec.set('Choose Section')

        self.TLabel21 = ttk.Label(self.TNotebook1_t1)
        self.TLabel21.place(relx=0.028, rely=0.536, height=19, width=85)
        self.TLabel21.configure(text='''Phone Number''')

        self.phno = ttk.Entry(self.TNotebook1_t1)
        self.phno.place(relx=0.167, rely=0.536, relheight=0.042
                           , relwidth=0.154)
        self.phno.configure(takefocus="")
        self.phno.configure(cursor="ibeam")

        self.TLabel31 = ttk.Label(self.TNotebook1_t1)
        self.TLabel31.place(relx=0.361, rely=0.536, height=19, width=71)
        self.TLabel31.configure(text='''Blood Group''')

        self.bgp = StringVar()
        self.bgroup = ttk.Combobox(self.TNotebook1_t1)
        self.bgroup.place(relx=0.481, rely=0.536, relheight=0.042
                              , relwidth=0.151)
        self.bgroup.configure(textvariable=self.bgp, state='readonly')
        self.bgroup.set('Choose Blood Group')
        self.bgroup.configure(values=('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'))
        self.bgroup.configure(takefocus="")

        self.ldno = tk.Label(self.TNotebook1_t1)
        self.ldno.place(relx=0.028, rely=0.615, height=21, width=98)
        self.ldno.configure(text='''Landline Number''')

        self.lno = tk.Entry(self.TNotebook1_t1)
        self.lno.place(relx=0.167, rely=0.615, height=20, relwidth=0.152)

        self.rel = tk.Label(self.TNotebook1_t1)
        self.rel.place(relx=0.361, rely=0.615, height=21, width=49)
        self.rel.configure(text='''Religion''')
        self.relg = StringVar()
        self.relgion = ttk.Combobox(self.TNotebook1_t1)
        self.relgion.place(relx=0.481, rely=0.615, relheight=0.042
                              , relwidth=0.151)
        self.relgion.configure(textvariable=self.relg, state='readonly')
        self.relgion.set('Choose Religion')
        self.relgion.configure(values=('Hindu', 'Sikh', 'Muslim', 'Christian', 'Other'))
        self.relgion.configure(takefocus="")

        self.address = ttk.Label(self.TNotebook1_t1)
        self.address.place(relx=0.028, rely=0.694, height=19, width=46)
        self.address.configure(text='''Address''')

        self.txt1 = tk.Text(self.TNotebook1_t1)
        self.txt1.place(relx=0.167, rely=0.694, relheight=0.159, relwidth=0.467)

        self.txt1.configure(background="white")
        self.txt1.configure(font="TkTextFont")
        self.txt1.configure(width=504)
        self.txt1.configure(wrap="word")

        self.update = tk.Button(self.TNotebook1_t1)
        self.update.place(relx=0.167, rely=0.893, height=24, width=55)
        self.update.configure(text='Update', command=self.updateinfo)

        self.delete = tk.Button(self.TNotebook1_t1)
        self.delete.place(relx=0.227, rely=0.893, height=24, width=55)
        self.delete.configure(text='Delete', command=self.deleteinfo)

        self.search = tk.Button(self.TNotebook1_t1)
        self.search.place(relx=0.287, rely=0.893, height=24, width=55)
        self.search.configure(text='Search', command=self.searchinfo)

        self.admdate = tk.Label(self.TNotebook1_t1)
        self.admdate.place(relx=0.361, rely=0.06, height=21, width=89)
        self.admdate.configure(text="Admission Date")

        mytablearea = Frame(self.TNotebook1_t1)
        scrollbarx = Scrollbar(mytablearea, orient=HORIZONTAL)
        scrollbary = Scrollbar(mytablearea, orient=VERTICAL)

        self.mytable = ttk.Treeview(mytablearea, columns=("srno", "name", "course"),
                                    xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)
        self.mytable['show'] = 'headings'
        scrollbarx.config(command=self.mytable.xview)
        scrollbary.config(command=self.mytable.yview)

        scrollbarx.pack(side=BOTTOM, fill=X)
        scrollbary.pack(side=RIGHT, fill=Y)

        self.mytable.heading("srno", text="Sr No")
        self.mytable.heading("name", text="Name")
        self.mytable.heading("course", text="Course")

        self.mytable.column('#0', stretch=NO, minwidth=0, width=0)
        self.mytable.column('#1', stretch=NO, minwidth=0, width=115)
        self.mytable.column('#2', stretch=NO, minwidth=0, width=115)
        self.mytable.column('#3', stretch=NO, minwidth=0, width=115)

        self.mytable.bind("<ButtonRelease-1>", self.fetchbysrno)
        self.mytable.pack()
        mytablearea.place(relx=0.657, rely=0.694, relheight=0.159, width=350)

    def searchinfo(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="collegedb")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select srno, name,course from studenttable"
                                   " where name like %s", (self.fname.get() + "%"))
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
        self.serialno = selectedRow[0]
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="collegedb")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select * from studenttable where srno=%s",
                                   (self.serialno))
                    myresultdata = myconn.fetchall()

                    for row in myresultdata:

                        self.adat.delete(0, END)
                        self.adat.insert(0, self.serialno)
                        self.fname.delete(0, END)
                        self.fname.insert(0, row[1])
                        self.lname.delete(0, END)
                        self.lname.insert(0, row[2])
                        self.fathername.delete(0, END)
                        self.fathername.insert(0, row[3])
                        self.mname.delete(0, END)
                        self.mname.insert(0, row[4])

                        self.phno.delete(0, END)
                        self.phno.insert(0, row[11])
                        self.lno.delete(0, END)
                        self.lno.insert(0, row[13])
                        self.dob.delete(0, END)
                        self.dob.insert(0, row[7])
                        self.txt1.delete('1.0', END)
                        self.txt1.insert('1.0', row[15])
                        self.addt.delete(0, END)
                        self.addt.insert(0, row[16])

                        self.filename4 = ImageTk.PhotoImage(file="images//" + row[17])

                        self.img1.config(image=self.filename4)
                        self.occupation.set(row[5])
                        self.relg.set(row[14])
                        self.bgp.set(row[12])
                        self.occupation1.set(row[6])
                        self.course1.set(row[9])
                        self.sections.set(row[10])
                        if row[8] == "Male":
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
                        "update studenttable set name=%s,lname=%s,fathername=%s,mothername=%s,foccu=%s,moccu=%s,dob=%s,gender=%s,course=%s,section=%s,phone=%s,bg=%s,landline=%s,religion=%s,address=%s,admdate=%s where srno=%s",
                        (self.fname.get(), self.lname.get(), self.fathername.get(), self.mname.get(), self.occupation.get(),
                         self.occupation1.get(),self.dob.get_date(), self.gender1.get(), self.course1.get(),self.sections.get(),self.phno.get(),self.bgp.get(),self.lno.get(),self.relg.get(), self.txt1.get('1.0', END),self.addt.get(), self.serialno
                         ))
                    mydatabaseobj.commit()
                    messagebox.showinfo("Success", "Record Updated Successfully", parent=self.TNotebook1_t1)
            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex))
            finally:
                mydatabaseobj.close()
            self.gender1.set(" ")
            self.course1.set("Choose Course")
            self.sections.set("Choose Section")
            self.phno.delete(0, END)
            self.fname.delete(0, END)
            self.lname.delete(0, END)
            self.occupation.set("Choose Occupation")
            self.occupation1.set("Choose Occupation")
            self.relg.set("Choose Religion")
            self.bgp.set("Choose Blood Group")
            self.fathername.delete(0, END)
            self.filename3 = ImageTk.PhotoImage(file="images/default.png")

            self.img1.config(image=self.filename3)

            self.mname.delete(0, END)
            self.adat.delete(0,END)
            self.lno.delete(0, END)

            self.mytable.delete(*self.mytable.get_children())
            self.txt1.delete('1.0', END)
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
                            "delete from studenttable where srno=%s",
                            (self.serialno))
                        mydatabaseobj.commit()
                        messagebox.showinfo("Success", "Record Deleted Successfully", parent=self.TNotebook1_t1)
                except Exception as ex:
                    messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex),
                                         )

                finally:
                    mydatabaseobj.close()
                self.gender1.set(" ")
                self.course1.set("Choose Course")
                self.sections.set("Choose Section")
                self.phno.delete(0, END)
                self.fname.delete(0, END)
                self.lname.delete(0, END)
                self.occupation.set("Choose Occupation")
                self.occupation1.set("Choose Occupation")
                self.relg.set("Choose Religion")
                self.bgp.set("Choose Blood Group")
                self.fathername.delete(0, END)
                self.filename1 = ImageTk.PhotoImage(file="images/default.png")
                self.adat.delete(0,END)
                self.img1.config(image=self.filename1)
                self.mname.delete(0, END)

                self.lno.delete(0, END)

                self.mytable.delete(*self.mytable.get_children())
                self.txt1.delete('1.0', END)


            except Exception as ex:
                messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))

    def mouseev(self,ev):
        self.delta = self.to.get_date() - self.fr.get_date()
        self.day=self.delta.days
        self.tdays.config(text=self.day)
        print(self.day)




    def saveinfo(self):

            try:
                mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",db="collegedb")
                try:
                    with mydatabaseobj.cursor() as myconn:
                        myconn.execute(
                        "insert into studenttable(name,lname,fathername,mothername,foccu,moccu,dob,gender,course,section,phone,bg,landline,religion,address,admdate,image) "
                        "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (self.Entry1.get(), self.Entry2.get(), self.Entry3.get(), self.Entry4.get(),
                         self.TCombobox1.get(), self.TCombobox2.get(),self.dt.get_date(), self.gender.get(), self.TCombobox3.get()
                         , self.TCombobox4.get(), self.TEntry1.get(), self.TCombobox5.get(), self.Entry5.get(),
                         self.TCombobox6.get(),self.Text1.get('1.0',END),self.ad.get(),self.myfinalname))

                        mydatabaseobj.commit()
                        messagebox.showinfo("Success", "Record Saved Successfully",parent=self.TNotebook1_t0)

                except Exception as ex:
                    messagebox.showerror("Error Occured","Please Fill All Blocks!",parent=self.TNotebook1_t0)
                finally:
                    mydatabaseobj.close()

                self.gender.set(" ")
                self.TCombobox3.set("Choose Course")
                self.TCombobox4.set("Choose Section")
                self.TEntry1.delete(0, END)
                self.Entry1.delete(0, END)
                self.Entry2.delete(0, END)
                self.TCombobox1.set("Choose Occupation")
                self.TCombobox2.set("Choose Occupation")
                self.TCombobox6.set("Choose Religion")
                self.TCombobox5.set("Choose Blood Group")
                self.Entry3.delete(0, END)
                self.filename2 = ImageTk.PhotoImage(file="images/default.png")

                self.img.config(image=self.filename2)
                self.Entry4.delete(0, END)

                self.Entry5.delete(0, END)

                self.mytable.delete(*self.mytable.get_children())
                self.Text1.delete('1.0', END)
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

    def fetch_section(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="collegedb")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select * from sectiontable")
                    myresultdata = myconn.fetchall()
                    self.sectionnames = []
                    for row in myresultdata:
                        self.sectionnames.append(row[0])

                    if len(self.sectionnames ) == 0:
                        messagebox.showerror("Error Occured", "No Section added. Add Section from Misc Menu first")

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

