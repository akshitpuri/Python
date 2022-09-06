import traceback
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.messagebox import askquestion

import pymysql as pymysql
import tkinter as tk

from tkcalendar import DateEntry



class Att:

    def __init__(self, myframe):
        self.mytop= tk.Toplevel(myframe)
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
        self.TNotebook1.tab(0, text="Student", compound="left", underline="-1"
                            , )
        self.TNotebook1_t0.configure(background="#d9d9d9")
        self.TNotebook1_t0.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t0.configure(highlightcolor="black")
        self.TNotebook1_t1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(1, text="Staff", compound="left", underline="-1"
                            , )
        self.TNotebook1_t1.configure(background="#d9d9d9")
        self.TNotebook1_t1.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t1.configure(highlightcolor="black")
        self.TNotebook1_t2 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2, padding=3)
        self.TNotebook1.tab(2, text="Data", compound="left", underline="-1"
                            , )
        self.TNotebook1_t2.configure(background="#d9d9d9")
        self.TNotebook1_t2.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t2.configure(highlightcolor="black")

        self.Label1111 = tk.Label(self.TNotebook1_t0)
        self.Label1111.place(relx=0.034, rely=0.068, height=21, width=38)
        self.Label1111.configure(text='''Name''')

        self.name1 = tk.Entry(self.TNotebook1_t0)
        self.name1.place(relx=0.101, rely=0.068, height=20, relwidth=0.183)

        self.Label311 = tk.Label(self.TNotebook1_t0)
        self.Label311.place(relx=0.034, rely=0.159, height=21, width=34)
        self.Label311.configure(text='''From''')

        self.l14 = tk.Label(self.TNotebook1_t0)
        self.l14.place(relx=0.324, rely=0.159, height=21, width=20)
        self.l14.configure(text='''To''')

        self.Ll5 = tk.Label(self.TNotebook1_t0)
        self.Ll5.place(relx=0.034, rely=0.251, height=21, width=124)
        self.Ll5.configure(text='''Total Number Of Days''')

        self.tdays = tk.Label(self.TNotebook1_t0)
        self.tdays.place(relx=0.212, rely=0.251, height=20, relwidth=0.183)

        self.Ll6 = tk.Label(self.TNotebook1_t0)
        self.Ll6.place(relx=0.034, rely=0.433, height=21, width=136)
        self.Ll6.configure(text='''Number Of Days Present''')

        self.p = tk.Entry(self.TNotebook1_t0)
        self.p.place(relx=0.212, rely=0.433,height=20, relwidth=0.183)

        self.Ll7 = tk.Label(self.TNotebook1_t0)
        self.Ll7.place(relx=0.034, rely=0.524, height=21, width=134)
        self.Ll7.configure(text='''Number Of Days Absent''')

        self.a = tk.Entry(self.TNotebook1_t0)
        self.a.place(relx=0.212, rely=0.524,height=20, relwidth=0.183)

        self.Label11 = tk.Label(self.TNotebook1_t0)
        self.Label11.place(relx=0.425, rely=0.068, height=21, width=50)
        self.Label11.configure(text='''Number''')

        self.Entry2 = tk.Entry(self.TNotebook1_t0)
        self.Entry2.place(relx=0.514, rely=0.068, height=20, relwidth=0.183)

        self.Label2 = tk.Label(self.TNotebook1_t0)
        self.Label2.place(relx=0.034, rely=0.342, height=21, width=32)
        self.Label2.configure(text='''Type''')




        self.savebtn = tk.Button(self.TNotebook1_t0)
        self.savebtn.place(relx=0.212, rely=0.615, height=24, width=35)
        self.savebtn.configure(text='''Save''',command=self.saveinfo)

        self.deleteat = tk.Button(self.TNotebook1_t0)
        self.deleteat.place(relx=0.346, rely=0.615, height=24, width=44)
        self.deleteat.configure(text='''Delete''',command=self.deleteat)

        self.Button3 = tk.Button(self.TNotebook1_t0)
        self.Button3.place(relx=0.268, rely=0.615, height=24, width=59)
        self.Button3.configure(text='''Update''',command=self.updateinfo)


        self.fr = DateEntry(self.TNotebook1_t0, background='darkblue', foreground='white', borderwidth=2)
        self.fr.place(relx=0.101, rely=0.159, height=21,relwidth=0.183)

        self.to = DateEntry(self.TNotebook1_t0, background='darkblue', foreground='white', borderwidth=2)
        self.to.place(relx=0.469, rely=0.159, height=21,relwidth=0.183)
        self.to.bind("<Return>", self.mouseev)


        self.searchat = tk.Button(self.TNotebook1_t0)
        self.searchat.place(relx=0.313, rely=0.068, height=20, width=46)
        self.searchat.configure(text='''Search''',command=self.searchinfo)

        self.Label11111 = tk.Label(self.TNotebook1_t1)
        self.Label11111.place(relx=0.034, rely=0.068, height=21, width=38)
        self.Label11111.configure(text='''Name''')

        self.name11 = tk.Entry(self.TNotebook1_t1)
        self.name11.place(relx=0.101, rely=0.068, height=20, relwidth=0.183)

        self.Label3111 = tk.Label(self.TNotebook1_t1)
        self.Label3111.place(relx=0.034, rely=0.159, height=21, width=34)
        self.Label3111.configure(text='''From''')

        self.l141 = tk.Label(self.TNotebook1_t1)
        self.l141.place(relx=0.324, rely=0.159, height=21, width=20)
        self.l141.configure(text='''To''')

        v=StringVar(self.TNotebook1_t0,value='Student')
        self.utype =tk.Entry(self.TNotebook1_t0)
        self.utype.place(relx=0.212, rely=0.342, relheight=0.048
                , relwidth=0.182)
        self.utype.configure(state='readonly')
        self.utype.configure(textvariable=v)

        u = StringVar(self.TNotebook1_t1, value='Staff')
        self.utype1 = tk.Entry(self.TNotebook1_t1)
        self.utype1.place(relx=0.212, rely=0.342, relheight=0.048
                         , relwidth=0.182)
        self.utype1.configure(text="Staff", state='readonly')
        self.utype1.configure(textvariable=u)


        self.Ll51 = tk.Label(self.TNotebook1_t1)
        self.Ll51.place(relx=0.034, rely=0.251, height=21, width=124)
        self.Ll51.configure(text='''Total Number Of Days''')

        self.tdays1 = tk.Label(self.TNotebook1_t1)
        self.tdays1.place(relx=0.212, rely=0.251, height=20, relwidth=0.183)

        self.Ll61 = tk.Label(self.TNotebook1_t1)
        self.Ll61.place(relx=0.034, rely=0.433, height=21, width=136)
        self.Ll61.configure(text='''Number Of Days Present''')

        self.p1 = tk.Entry(self.TNotebook1_t1)
        self.p1.place(relx=0.212, rely=0.433, height=20, relwidth=0.183)

        self.Ll71 = tk.Label(self.TNotebook1_t1)
        self.Ll71.place(relx=0.034, rely=0.524, height=21, width=134)
        self.Ll71.configure(text='''Number Of Days Absent''')

        self.a1 = tk.Entry(self.TNotebook1_t1)
        self.a1.place(relx=0.212, rely=0.524, height=20, relwidth=0.183)

        self.Label111 = tk.Label(self.TNotebook1_t1)
        self.Label111.place(relx=0.425, rely=0.068, height=21, width=50)
        self.Label111.configure(text='''Number''')

        self.Entry21 = tk.Entry(self.TNotebook1_t1)
        self.Entry21.place(relx=0.514, rely=0.068, height=20, relwidth=0.183)

        self.Label21 = tk.Label(self.TNotebook1_t1)
        self.Label21.place(relx=0.034, rely=0.342, height=21, width=32)
        self.Label21.configure(text='''Type''')


        self.savebtn1 = tk.Button(self.TNotebook1_t1)
        self.savebtn1.place(relx=0.212, rely=0.615, height=24, width=35)
        self.savebtn1.configure(text='''Save''', command=self.saveinfo1)

        self.deleteat1 = tk.Button(self.TNotebook1_t1)
        self.deleteat1.place(relx=0.346, rely=0.615, height=24, width=44)
        self.deleteat1.configure(text='''Delete''', command=self.deleteat1)

        self.Button31 = tk.Button(self.TNotebook1_t1)
        self.Button31.place(relx=0.268, rely=0.615, height=24, width=59)
        self.Button31.configure(text='''Update''', command=self.updateinfo1)

        self.fr1 = DateEntry(self.TNotebook1_t1, background='darkblue', foreground='white', borderwidth=2)
        self.fr1.place(relx=0.101, rely=0.159, height=21, relwidth=0.183)

        self.to1 = DateEntry(self.TNotebook1_t1, background='darkblue', foreground='white', borderwidth=2)
        self.to1.place(relx=0.469, rely=0.159, height=21, relwidth=0.183)
        self.to1.bind("<Return>", self.mouseev1)

        self.searchat1 = tk.Button(self.TNotebook1_t1)
        self.searchat1.place(relx=0.313, rely=0.068, height=20, width=46)
        self.searchat1.configure(text='''Search''', command=self.searchinfo11)


        self.course = StringVar()
        coursebox = ttk.Combobox(self.TNotebook1_t2, textvariable=self.course, state='readonly')
        coursebox.config(values=('Student', 'Staff'))
        coursebox.bind("<<ComboboxSelected>>", self.searchinfo1)
        coursebox.set("Choose Type")
        coursebox.place(relx=0.034, rely=0.063, height=21, width=92)

        self.TSeparator1 = ttk.Separator(self.TNotebook1_t2)
        self.TSeparator1.place(relx=0.034, rely=0.146, relwidth=0.955)

        mytablearea = Frame(self.TNotebook1_t0)
        scrollbarx = Scrollbar(mytablearea, orient=HORIZONTAL)
        scrollbary = Scrollbar(mytablearea, orient=VERTICAL)

        self.mytable = ttk.Treeview(mytablearea, columns=("srno", "name", "course"),
                                    xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)
        self.mytable['show'] = 'headings'
        scrollbarx.config(command=self.mytable.xview)
        scrollbary.config(command=self.mytable.yview)

        scrollbarx.pack(side=BOTTOM, fill=X)
        scrollbary.pack(side=RIGHT, fill=Y)

        self.mytable.heading("srno", text="Number")
        self.mytable.heading("name", text="Name")
        self.mytable.heading("course", text="Course")


        self.mytable.column('#0', stretch=NO,minwidth=0, width=0)
        self.mytable.column('#1', stretch=NO,minwidth=0, width=150)
        self.mytable.column('#2', stretch=NO,minwidth=0, width=150)
        self.mytable.column('#3', stretch=NO,minwidth=0, width=150)

        self.mytable.bind("<ButtonRelease-1>", self.fetchbysrno)
        self.mytable.pack()
        mytablearea.place(relx=0.469, rely=0.251, height=141, width=454)

        mytablearea2 = Frame(self.TNotebook1_t1)
        scrollbarx2 = Scrollbar(mytablearea2, orient=HORIZONTAL)
        scrollbary2 = Scrollbar(mytablearea2, orient=VERTICAL)

        self.mytable2 = ttk.Treeview(mytablearea2, columns=("srno", "name", "course"),
                                    xscrollcommand=scrollbarx2.set, yscrollcommand=scrollbary2.set)
        self.mytable2['show'] = 'headings'
        scrollbarx2.config(command=self.mytable2.xview)
        scrollbary2.config(command=self.mytable2.yview)

        scrollbarx2.pack(side=BOTTOM, fill=X)
        scrollbary2.pack(side=RIGHT, fill=Y)

        self.mytable2.heading("srno", text="Name")
        self.mytable2.heading("name", text="Number")
        self.mytable2.heading("course", text="Course")

        self.mytable2.column('#0', stretch=NO,minwidth=0, width=0)
        self.mytable2.column('#1', stretch=NO,minwidth=0, width=150)
        self.mytable2.column('#2', stretch=NO,minwidth=0, width=150)
        self.mytable2.column('#3', stretch=NO,minwidth=0, width=150)

        self.mytable2.bind("<ButtonRelease-1>", self.fetchbysrno1)
        self.mytable2.pack()
        mytablearea2.place(relx=0.469, rely=0.251, height=141, width=454)

        mytablearea1 = Frame(self.TNotebook1_t2)
        scrollbarx1 = Scrollbar(mytablearea1, orient=HORIZONTAL)
        scrollbary1 = Scrollbar(mytablearea1, orient=VERTICAL)

        self.mytable1 = ttk.Treeview(mytablearea1,
                                     columns=("srno", "name","attfrom",	"attto",	"pdays",	"adays"),
                                     xscrollcommand=scrollbarx1.set, yscrollcommand=scrollbary1.set)
        self.mytable1['show'] = 'headings'
        scrollbarx1.config(command=self.mytable1.xview)
        scrollbary1.config(command=self.mytable1.yview)

        scrollbarx1.pack(side=BOTTOM, fill=X)
        scrollbary1.pack(side=RIGHT, fill=Y)

        self.mytable1.heading("srno", text="Name")
        self.mytable1.heading("name", text="Number")
        self.mytable1.heading("attfrom", text="Attend From")
        self.mytable1.heading("attto", text="Attend To")

        self.mytable1.heading("pdays", text="Present Days")
        self.mytable1.heading("adays", text="Absent Days")


        self.mytable1.column('#0', stretch=NO, minwidth=0, width=0)
        self.mytable1.column('#1', stretch=NO, minwidth=0, width=142)
        self.mytable1.column('#2', stretch=NO, minwidth=0, width=142)
        self.mytable1.column('#3', stretch=NO, minwidth=0, width=142)
        self.mytable1.column('#4', stretch=NO, minwidth=0, width=142)
        self.mytable1.column('#5', stretch=NO, minwidth=0, width=142)

        self.mytable1.column('#6', stretch=NO, minwidth=0, width=142)

        self.mytable1.pack()
        mytablearea1.place(relx=0.04, rely=0.188, height=371, width=1000)

    def updateinfo(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="collegedb")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute(
                        "update attendtable set name=%s,attfrom=%s,utype=%s,attto=%s,pdays=%s,adays=%s where srno=%s",
                        (self.name1.get(), self.fr.get_date(), self.utype.get(),
                         self.to.get_date(), self.p.get(), self.a.get(), self.serialno
                         ))
                    mydatabaseobj.commit()
                    messagebox.showinfo("Success", "Record Updated Successfully", parent=self.TNotebook1_t0)
            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex))
            finally:
                mydatabaseobj.close()

            self.Entry2.delete(0, END)
            self.name1.delete(0, END)


            self.fr.delete(0, END)
            self.to.delete(0, END)

            self.a.delete(0, END)

            self.p.delete(0, END)
            self.mytable.delete(*self.mytable.get_children())

        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))

    def updateinfo1(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="collegedb")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute(
                        "update attendtable set name=%s,attfrom=%s,utype=%s,attto=%s,pdays=%s,adays=%s where srno=%s",
                        (self.name11.get(), self.fr1.get_date(), self.utype1.get(),
                         self.to1.get_date(), self.p1.get(), self.a1.get(), self.serialno
                         ))
                    mydatabaseobj.commit()
                    messagebox.showinfo("Success", "Record Updated Successfully", parent=self.TNotebook1_t1)
            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex))
            finally:
                mydatabaseobj.close()

            self.Entry21.delete(0, END)
            self.name11.delete(0, END)


            self.fr1.delete(0, END)
            self.to1.delete(0, END)

            self.a1.delete(0, END)

            self.p1.delete(0, END)
            self.mytable2.delete(*self.mytable2.get_children())

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
                            "delete from attendtable where srno=%s",
                            (self.serialno))
                        mydatabaseobj.commit()
                        messagebox.showinfo("Success", "Record Deleted Successfully", parent=self.TNotebook1_t0)
                except Exception as ex:
                    messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex),
                                         )

                finally:
                    mydatabaseobj.close()

                self.Entry2.delete(0, END)
                self.name1.delete(0, END)

                self.fr.delete(0, END)
                self.to.delete(0, END)

                self.a.delete(0, END)

                self.p.delete(0, END)
                self.mytable.delete(*self.mytable.get_children())

            except Exception as ex:
                messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))

    def deleteinfo1(self):
        answer = askquestion("Confirm", "Do you really want to delete?", icon="warning")

        if answer == "yes":
            try:
                mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                                db="collegedb")
                try:

                    with mydatabaseobj.cursor() as myconn:
                        myconn.execute(
                            "delete from attendtable where srno=%s",
                            (self.serialno))
                        mydatabaseobj.commit()
                        messagebox.showinfo("Success", "Record Deleted Successfully", parent=self.TNotebook1_t1)
                except Exception as ex:
                    messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex),
                                         )

                finally:
                    mydatabaseobj.close()

                self.Entry21.delete(0, END)
                self.name11.delete(0, END)

                self.fr1.delete(0, END)
                self.to1.delete(0, END)

                self.a1.delete(0, END)

                self.p1.delete(0, END)
                self.mytable2.delete(*self.mytable2.get_children())

            except Exception as ex:
                messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))

    def searchinfo1(self,ev):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="collegedb")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select name,srno,attfrom,attto,pdays,adays from attendtable where utype=%s", (self.course.get()))
                    myresultdata = myconn.fetchall()
                    self.mytable1.delete(*self.mytable1.get_children())
                    for row in myresultdata:
                        self.mytable1.insert('', END, value=(row))

                    if myresultdata == None:
                        messagebox.showerror("No Records Found", "No Students added yet.")

            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex))
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))




    def mouseev(self,ev):
        self.delta = self.to.get_date() - self.fr.get_date()
        self.day=self.delta.days
        self.tdays.config(text=self.day)
        print(self.day)

    def mouseev1(self,ev):
        self.delta1 = self.to1.get_date() - self.fr1.get_date()
        self.day1=self.delta1.days
        self.tdays1.config(text=self.day1)
        print(self.day1)

    def saveinfo(self):

        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="", db="collegedb")
            try:
                with mydatabaseobj.cursor() as myconn:
                    myconn.execute(
                        "insert into attendtable(name,srno,attfrom,utype,attto,pdays,adays) "
                        "values(%s,%s,%s,%s,%s,%s,%s)",
                        (self.name1.get(), self.Entry2.get(), self.fr.get_date(), self.utype.get(),
                         self.to.get_date(), self.p.get(), self.a.get()
                         ))
                    mydatabaseobj.commit()
                    messagebox.showinfo("Success", "Record Saved Successfully", parent=self.TNotebook1_t0)

            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex))
            finally:
                mydatabaseobj.close()
            self.Entry2.delete(0, END)
            self.name1.delete(0, END)


            self.fr.delete(0, END)
            self.to.delete(0, END)

            self.a.delete(0, END)

            self.p.delete(0, END)
            self.mytable.delete(*self.mytable.get_children())

        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))

    def saveinfo1(self):

        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="", db="collegedb")
            try:
                with mydatabaseobj.cursor() as myconn:
                    myconn.execute(
                        "insert into attendtable(name,srno,attfrom,utype,attto,pdays,adays) "
                        "values(%s,%s,%s,%s,%s,%s,%s)",
                        (self.name11.get(), self.Entry21.get(), self.fr1.get_date(), self.utype1.get(),
                         self.to1.get_date(), self.p1.get(), self.a1.get()
                         ))
                    mydatabaseobj.commit()
                    messagebox.showinfo("Success", "Record Saved Successfully", parent=self.TNotebook1_t1)

            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex))
            finally:
                mydatabaseobj.close()
            self.Entry21.delete(0, END)
            self.name11.delete(0, END)


            self.fr1.delete(0, END)
            self.to1.delete(0, END)

            self.a1.delete(0, END)

            self.p1.delete(0, END)
            self.mytable2.delete(*self.mytable2.get_children())

        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))

    def searchinfo(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="collegedb")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select srno, name,course from studenttable"
                                   " where name like %s", (self.name1.get() + "%"))
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
    def searchinfo11(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                        db="collegedb")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select fname,phone,course from stafftable"
                               " where fname like %s", (self.name1.get() + "%"))
                    myresultdata = myconn.fetchall()
                    self.mytable2.delete(*self.mytable2.get_children())
                    for row in myresultdata:
                        self.mytable2.insert('', END, value=(row))

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
                        self.Entry2.delete(0, END)
                        self.Entry2.insert(0, self.serialno)
                        self.name1.delete(0, END)
                        self.name1.insert(0, row[1])

                    if myresultdata == None:
                        messagebox.showerror("No Records Found", "No Students added yet.")

            except Exception as ex:
                traceback.print_exc()
                messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex))
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))

    def fetchbysrno1(self, e):
        currentItem = self.mytable2.focus()
        contents = self.mytable2.item(currentItem)
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
                        self.Entry21.delete(0, END)
                        self.Entry21.insert(0, self.serialno)
                        self.name11.delete(0, END)
                        self.name11.insert(0, row[0])

                    if myresultdata == None:
                        messagebox.showerror("No Records Found", "No Staff added yet.")

            except Exception as ex:
                traceback.print_exc()
                messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex))
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))