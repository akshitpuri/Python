from tkinter import *
from tkinter import ttk, messagebox
from tkinter.messagebox import askquestion

import pymysql
import tkinter as tk

class MiscClass:
    def __init__(self, myframe):
        self.mytop = Toplevel(myframe)

        self.mytop.geometry("1130x560+213+128")
        self.mytop.title("Miscellaneous")
        self.mytop.configure(background="#d9d9d9")
        self.mytop.configure(highlightbackground="#d9d9d9")
        self.mytop.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(self.mytop)
        self.Frame1.place(relx=0.009, rely=0.018, relheight=0.973
                , relwidth=0.982)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=1110)


        self.TNotebook1 = ttk.Notebook(self.Frame1)
        self.TNotebook1.place(relx=0.009, rely=0.018, relheight=0.965
                , relwidth=0.977)
        self.TNotebook1.configure(width=1084)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t0 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t0, padding=3)
        self.TNotebook1.tab(0, text="Student Data", compound="left"
                ,underline="-1", )

        self.Label81 = tk.Label(self.TNotebook1_t0)
        self.Label81.place(relx=0.034, rely=0.063, height=21, width=92)
        self.Label81.configure(background="#d9d9d9")
        self.Label81.configure(disabledforeground="#a3a3a3")
        self.Label81.configure(foreground="#000000")
        self.Label81.configure(text='''Search By Name''')

        self.Entry61 = tk.Entry(self.TNotebook1_t0)
        self.Entry61.place(relx=0.193, rely=0.063, height=20, relwidth=0.186)
        self.Entry61.configure(background="white")
        self.Entry61.configure(disabledforeground="#a3a3a3")
        self.Entry61.configure(font="TkFixedFont")
        self.Entry61.configure(foreground="#000000")
        self.Entry61.configure(insertbackground="black")

        self.Button41 = tk.Button(self.TNotebook1_t0)
        self.Button41.place(relx=0.42, rely=0.063, height=20, width=46)
        self.Button41.configure(activebackground="#ececec")
        self.Button41.configure(activeforeground="#000000")
        self.Button41.configure(background="#d9d9d9")
        self.Button41.configure(disabledforeground="#a3a3a3")
        self.Button41.configure(foreground="#000000")
        self.Button41.configure(highlightbackground="#d9d9d9")
        self.Button41.configure(highlightcolor="black")
        self.Button41.configure(pady="0")
        self.Button41.configure(text='''Search''', command=self.searchstu)

        self.TSeparator11 = ttk.Separator(self.TNotebook1_t0)
        self.TSeparator11.place(relx=0.034, rely=0.146, relwidth=0.955)

        # self.fetch_courses()
        # self.course = StringVar()
        # coursebox = ttk.Combobox(self.TNotebook1_t0, textvariable=self.course, state='readonly')
        # coursebox.config(values=self.coursenames)
        # coursebox.bind("<<ComboboxSelected>>", self.showrecords)
        # coursebox.set("Choose course")
        # coursebox.place(x=50, y=50)

        mytablearea = Frame(self.TNotebook1_t0)
        scrollbarx = Scrollbar(mytablearea, orient=HORIZONTAL)
        scrollbary = Scrollbar(mytablearea, orient=VERTICAL)

        self.mytable = ttk.Treeview(mytablearea, columns=("srno", "name", "phone","course","dob"),
                                    xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)
        self.mytable['show'] = 'headings'
        scrollbarx.config(command=self.mytable.xview)
        scrollbary.config(command=self.mytable.yview)

        scrollbarx.pack(side=BOTTOM, fill=X)
        scrollbary.pack(side=RIGHT, fill=Y)

        self.mytable.heading("srno", text="Serial No")
        self.mytable.heading("name", text="Student Name")
        self.mytable.heading("phone", text="Phone")
        self.mytable.heading("course", text="Course")
        self.mytable.heading("dob", text="D.O.B")


        self.mytable.column('#0', stretch=NO)
        self.mytable.column('#1', stretch=NO)
        self.mytable.column('#2', stretch=NO)
        self.mytable.column('#3', stretch=NO)
        self.mytable.column('#4', stretch=NO)
        self.mytable.column('#5', stretch=NO)

        self.mytable.pack()
        mytablearea.place(relx=0.04, rely=0.188, height=371, width=1000)







        self.TNotebook1_t0.configure(background="#d9d9d9")
        self.TNotebook1_t0.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t0.configure(highlightcolor="black")



        self.TNotebook1_t1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(1, text="Staff Data", compound="left", underline="-1"
                ,)
        self.TNotebook1_t1.configure(background="#d9d9d9")
        self.TNotebook1_t1.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t1.configure(highlightcolor="black")

        self.Label8 = tk.Label(self.TNotebook1_t1)
        self.Label8.place(relx=0.034, rely=0.063, height=21, width=92)
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(text='''Search By Name''')

        self.Entry6 = tk.Entry(self.TNotebook1_t1)
        self.Entry6.place(relx=0.193, rely=0.063, height=20, relwidth=0.186)
        self.Entry6.configure(background="white")
        self.Entry6.configure(disabledforeground="#a3a3a3")
        self.Entry6.configure(font="TkFixedFont")
        self.Entry6.configure(foreground="#000000")
        self.Entry6.configure(insertbackground="black")

        self.Button4 = tk.Button(self.TNotebook1_t1)
        self.Button4.place(relx=0.42, rely=0.063, height=20, width=46)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Search''',command=self.searchinfo)

        self.TSeparator1 = ttk.Separator(self.TNotebook1_t1)
        self.TSeparator1.place(relx=0.034, rely=0.146, relwidth=0.955)

        mytablearea1 = Frame(self.TNotebook1_t1)
        scrollbarx1 = Scrollbar(mytablearea1, orient=HORIZONTAL)
        scrollbary1 = Scrollbar(mytablearea1, orient=VERTICAL)

        self.mytable1 = ttk.Treeview(mytablearea1, columns=("fname","qualf","subject","phone","eadd"),
                                    xscrollcommand=scrollbarx1.set, yscrollcommand=scrollbary1.set)
        self.mytable1['show'] = 'headings'
        scrollbarx1.config(command=self.mytable1.xview)
        scrollbary1.config(command=self.mytable1.yview)

        scrollbarx1.pack(side=BOTTOM, fill=X)
        scrollbary1.pack(side=RIGHT, fill=Y)

        self.mytable1.heading("fname", text="Name")
        self.mytable1.heading("qualf", text="Qualification")
        self.mytable1.heading("subject", text="Subject")
        self.mytable1.heading("phone", text="Phone Number")
        self.mytable1.heading("eadd", text="Email Address")

        self.mytable1.column('#0', stretch=NO)
        self.mytable1.column('#1', stretch=NO)
        self.mytable1.column('#2', stretch=NO)
        self.mytable1.column('#3', stretch=NO)
        self.mytable1.column('#4', stretch=NO)
        self.mytable1.column('#5', stretch=NO)

        self.mytable1.pack()
        mytablearea1.place(relx=0.04, rely=0.188, height=371, width=1000)


        self.TNotebook1_t2 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2, padding=3)
        self.TNotebook1.tab(2, text="Add Course", compound="none", underline="-1"
                ,)
        self.TNotebook1_t2.configure(background="#d9d9d9")
        self.TNotebook1_t2.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t2.configure(highlightcolor="black")
        self.TNotebook1_t3 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t3, padding=3)
        self.TNotebook1.tab(3, text="Add Section", compound="none", underline="-1"
                ,)
        self.TNotebook1_t3.configure(background="#d9d9d9")
        self.TNotebook1_t3.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t3.configure(highlightcolor="black")
        self.TNotebook1_t4 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t4, padding=3)
        self.TNotebook1.tab(4, text="Add Subject", compound="none", underline="-1"
                ,)
        self.TNotebook1_t4.configure(background="#d9d9d9")
        self.TNotebook1_t4.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t4.configure(highlightcolor="black")

        self.TLabel1 = ttk.Label(self.TNotebook1_t2)
        self.TLabel1.place(relx=0.028, rely=0.06, height=19, width=41)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(text='''Course''')

        self.TEntry1 = ttk.Entry(self.TNotebook1_t2)
        self.TEntry1.place(relx=0.12, rely=0.06, relheight=0.042, relwidth=0.117)

        self.TEntry1.configure(takefocus="")
        self.TEntry1.configure(cursor="ibeam")

        self.TButton1 = ttk.Button(self.TNotebook1_t2)
        self.TButton1.place(relx=0.12, rely=0.14, height=25, width=56)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Save''',command=self.courseframe)
        self.TButton1.configure(width=56)

        self.TButton2 = ttk.Button(self.TNotebook1_t2)
        self.TButton2.place(relx=0.185, rely=0.14, height=25, width=56)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''Delete''',command=self.deletecourse)
        self.TButton2.configure(width=56)

        self.TLabel2 = ttk.Label(self.TNotebook1_t3)
        self.TLabel2.place(relx=0.028, rely=0.06, height=19, width=43)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font="TkDefaultFont")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(text='''Section''')

        self.TEntry2 = ttk.Entry(self.TNotebook1_t3)
        self.TEntry2.place(relx=0.12, rely=0.06, relheight=0.042, relwidth=0.117)

        self.TEntry2.configure(takefocus="")
        self.TEntry2.configure(cursor="ibeam")

        self.TButton3 = ttk.Button(self.TNotebook1_t3)
        self.TButton3.place(relx=0.12, rely=0.14, height=25, width=56)
        self.TButton3.configure(takefocus="")
        self.TButton3.configure(text='''Save''',command=self.sectionframe)
        self.TButton3.configure(width=56)

        self.TButton4 = ttk.Button(self.TNotebook1_t3)
        self.TButton4.place(relx=0.185, rely=0.14, height=25, width=56)
        self.TButton4.configure(takefocus="")
        self.TButton4.configure(text='''Delete''',command=self.deletesection)
        self.TButton4.configure(width=56)

        self.TLabel3 = ttk.Label(self.TNotebook1_t4)
        self.TLabel3.place(relx=0.028, rely=0.06, height=19, width=43)
        self.TLabel3.configure(background="#d9d9d9")
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(font="TkDefaultFont")
        self.TLabel3.configure(relief="flat")
        self.TLabel3.configure(text='''Subject''')

        self.TEntry3 = ttk.Entry(self.TNotebook1_t4)
        self.TEntry3.place(relx=0.12, rely=0.06, relheight=0.042, relwidth=0.117)

        self.TEntry3.configure(takefocus="")
        self.TEntry3.configure(cursor="ibeam")

        self.TButton5 = ttk.Button(self.TNotebook1_t4)
        self.TButton5.place(relx=0.12, rely=0.14, height=25, width=56)
        self.TButton5.configure(takefocus="")
        self.TButton5.configure(text='''Save''',command=self.subjectframe)
        self.TButton5.configure(width=56)

        self.TButton6 = ttk.Button(self.TNotebook1_t4)
        self.TButton6.place(relx=0.185, rely=0.14, height=25, width=56)
        self.TButton6.configure(takefocus="")
        self.TButton6.configure(text='''Delete''',command=self.deletesubject)
        self.TButton6.configure(width=56)

    def deletecourse(self):
        answer = askquestion("Confirm", "Do you really want to delete?", icon="warning")

        if answer == "yes":
            try:
                mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                                db="collegedb")
                try:

                    with mydatabaseobj.cursor() as myconn:
                        myconn.execute(
                            "delete from coursetable where course=%s",
                            (self.TEntry1.get()))
                        mydatabaseobj.commit()
                        messagebox.showinfo("Success", "Record Deleted Successfully",parent=self.TNotebook1_t2)
                except Exception as ex:
                    messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex),
                                        )

                finally:
                    mydatabaseobj.close()

                self.TEntry1.delete(0, END)



            except Exception as ex:
                messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))
    def deletesection(self):
        answer = askquestion("Confirm", "Do you really want to delete?", icon="warning")

        if answer == "yes":
            try:
                mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                                db="collegedb")
                try:

                    with mydatabaseobj.cursor() as myconn:
                        myconn.execute(
                            "delete from sectiontable where course=%s",
                            (self.TEntry2.get()))
                        mydatabaseobj.commit()
                        messagebox.showinfo("Success", "Record Deleted Successfully",parent=self.TNotebook1_t3)
                except Exception as ex:
                    messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex),
                                        )

                finally:
                    mydatabaseobj.close()

                self.TEntry2.delete(0, END)



            except Exception as ex:
                messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))
    def deletesubject(self):
        answer = askquestion("Confirm", "Do you really want to delete?", icon="warning")

        if answer == "yes":
            try:
                mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                                db="collegedb")
                try:

                    with mydatabaseobj.cursor() as myconn:
                        myconn.execute(
                            "delete from subjecttable where subject=%s",
                            (self.TEntry3.get()))
                        mydatabaseobj.commit()
                        messagebox.showinfo("Success", "Record Deleted Successfully",parent=self.TNotebook1_t4)
                except Exception as ex:
                    messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex),
                                        )

                finally:
                    mydatabaseobj.close()

                self.TEntry3.delete(0, END)



            except Exception as ex:
                messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))

    def courseframe(self):

            try:
                myobj = pymysql.connect(host="localhost", user="root",
                                        password="", db="collegedb")
                try:
                    with myobj.cursor() as myconn:

                        myconn.execute("insert into coursetable "
                                       "values(%s)", (self.TEntry1.get()))
                        myobj.commit()
                        messagebox.showinfo("Success", "Course added Successfully",parent=self.TNotebook1_t2)


                except Exception as ex:
                    messagebox.showerror("Error Occured", "Error occured in Query due to " + str(ex))
                finally:
                    myobj.close()

                self.TEntry1.delete(0, END)
            except Exception as ex:
                messagebox.showerror("Error Occured", "Error occured in Connection due to " + str(ex))

    def sectionframe(self):

            try:
                myobj = pymysql.connect(host="localhost", user="root",
                                        password="", db="collegedb")
                try:
                    with myobj.cursor() as myconn:

                        myconn.execute("insert into sectiontable "
                                       "values(%s)", (self.TEntry2.get()))
                        myobj.commit()
                        messagebox.showinfo("Success", "Section added Successfully",parent=self.TNotebook1_t3)


                except Exception as ex:
                    messagebox.showerror("Error Occured", "Error occured in Query due to " + str(ex))
                finally:
                    myobj.close()

                self.TEntry2.delete(0,END)
            except Exception as ex:
                messagebox.showerror("Error Occured", "Error occured in Connection due to " + str(ex))

    def subjectframe(self):

            try:
                myobj = pymysql.connect(host="localhost", user="root",
                                        password="", db="collegedb")
                try:
                    with myobj.cursor() as myconn:

                        myconn.execute("insert into subjecttable "
                                       "values(%s)", (self.TEntry3.get()))
                        myobj.commit()
                        messagebox.showinfo("Success", "Subject added Successfully",parent=self.TNotebook1_t4)


                except Exception as ex:
                    messagebox.showerror("Error Occured", "Error occured in Query due to " + str(ex))
                finally:
                    myobj.close()

                self.TEntry3.delete(0, END)
            except Exception as ex:
                messagebox.showerror("Error Occured", "Error occured in Connection due to " + str(ex))


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

    def showrecords(self, e):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="collegedb")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select srno, name, phone, course,dob from studenttable where course=%s",
                                   (self.course.get()))
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

    def searchinfo(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="collegedb")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select fname,qualf,subject,phone,eadd from stafftable where fname like %s", (self.Entry6.get() + "%"))
                    myresultdata = myconn.fetchall()
                    self.mytable1.delete(*self.mytable1.get_children())
                    for row in myresultdata:
                        self.mytable1.insert('', END, value=(row))

                    if myresultdata == None:
                        messagebox.showerror("No Records Found", "No Staff added yet.")

            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex))
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))

    def searchstu(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="collegedb")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select srno, name, phone, course,dob from studenttable where name like %s", (self.Entry61.get() + "%"))
                    myresultdata = myconn.fetchall()
                    self.mytable.delete(*self.mytable.get_children())
                    for row in myresultdata:
                        self.mytable.insert('', END, value=(row))

                    if myresultdata == None:
                        messagebox.showerror("No Records Found", "No Student added yet.")

            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex))
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))

