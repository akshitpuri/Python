import traceback
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.messagebox import askquestion

import pymysql as pymysql
import tkinter as tk


class ExamClass:
    def __init__(self, myframe):
        self.mytop = Toplevel(myframe)
        self.mytop.geometry("1130x560+213+128")
        self.mytop.title("Exam Management")
        self.mytop.configure(background="#d9d9d9")
        self.mytop.configure(highlightbackground="#d9d9d9")
        self.mytop.configure(highlightcolor="black")

        self.TNotebook1 = ttk.Notebook(self.mytop)
        self.TNotebook1.place(relx=0.013, rely=0.038, relheight=0.953
                              , relwidth=0.979)
        self.TNotebook1.configure(width=754)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t0 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t0, padding=3)
        self.TNotebook1.tab(0, text="Result", compound="left", underline="-1", )
        self.TNotebook1_t0.configure(background="#d9d9d9")
        self.TNotebook1_t0.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t0.configure(highlightcolor="black")
        self.TNotebook1_t1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(1, text="Data", compound="left", underline="-1", )
        self.TNotebook1_t1.configure(background="#d9d9d9")
        self.TNotebook1_t1.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t1.configure(highlightcolor="black")

        self.Label1 = tk.Label(self.TNotebook1_t0)
        self.Label1.place(relx=0.04, rely=0.063, height=21, width=38)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Name''')

        self.Entry1 = tk.Entry(self.TNotebook1_t0)
        self.Entry1.place(relx=0.213, rely=0.063, height=20, relwidth=0.179)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Label2 = tk.Label(self.TNotebook1_t0)
        self.Label2.place(relx=0.04, rely=0.146, height=21, width=109)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Admission Number''')

        self.Entry2 = tk.Entry(self.TNotebook1_t0)
        self.Entry2.place(relx=0.213, rely=0.146, height=20, relwidth=0.179)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")

        self.Label3 = tk.Label(self.TNotebook1_t0)
        self.Label3.place(relx=0.04, rely=0.229, height=21, width=90)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Marks Obtained''')

        self.Entry3 = tk.Entry(self.TNotebook1_t0)
        self.Entry3.place(relx=0.213, rely=0.229, height=20, relwidth=0.179)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#d9d9d9")
        self.Entry3.configure(highlightcolor="black")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(selectbackground="#c4c4c4")
        self.Entry3.configure(selectforeground="black")


        self.Label4 = tk.Label(self.TNotebook1_t0)
        self.Label4.place(relx=0.04, rely=0.313, height=21, width=68)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Total Marks''')

        self.Entry4 = tk.Entry(self.TNotebook1_t0)
        self.Entry4.place(relx=0.213, rely=0.313, height=20, relwidth=0.179)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(highlightbackground="#d9d9d9")
        self.Entry4.configure(highlightcolor="black")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(selectbackground="#c4c4c4")
        self.Entry4.configure(selectforeground="black")

        self.Button1 = tk.Button(self.TNotebook1_t0)
        self.Button1.place(relx=0.453, rely=0.063, height=20, width=46)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Search''',command=self.searchinfo)

        self.Button2 = tk.Button(self.TNotebook1_t0)
        self.Button2.place(relx=0.213, rely=0.5, height=24, width=35)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Save''',command=self.saveinfo)

        self.Button3 = tk.Button(self.TNotebook1_t0)
        self.Button3.place(relx=0.293, rely=0.5, height=24, width=49)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Update''',command=self.updateinfo)

        self.Button4 = tk.Button(self.TNotebook1_t0)
        self.Button4.place(relx=0.253, rely=0.583, height=24, width=44)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Delete''',command=self.deleteinfo)

        self.Label5 = tk.Label(self.TNotebook1_t0)
        self.Label5.place(relx=0.04, rely=0.396, height=21, width=65)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Percentage''')

        self.Entry5 = tk.Entry(self.TNotebook1_t0)
        self.Entry5.place(relx=0.213, rely=0.396, height=20, relwidth=0.179)
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(highlightbackground="#d9d9d9")
        self.Entry5.configure(highlightcolor="black")

        self.Entry4.bind("<Return>", self.mousee)

        self.Label6 = tk.Label(self.TNotebook1_t0)
        self.Label6.place(relx=0.4, rely=0.396, height=21, width=16)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''%''')


        mytablearea = Frame(self.TNotebook1_t0)
        scrollbarx = Scrollbar(mytablearea, orient=HORIZONTAL)
        scrollbary = Scrollbar(mytablearea, orient=VERTICAL)

        self.mytable = ttk.Treeview(mytablearea, columns=("srno", "name", "phone","course"),
                                    xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)
        self.mytable['show'] = 'headings'
        scrollbarx.config(command=self.mytable.xview)
        scrollbary.config(command=self.mytable.yview)

        scrollbarx.pack(side=BOTTOM, fill=X)
        scrollbary.pack(side=RIGHT, fill=Y)

        self.mytable.heading("srno", text="Sr No")
        self.mytable.heading("name", text="Student Name")
        self.mytable.heading("phone", text="Phone")

        self.mytable.heading("course", text="Course")

        self.mytable.column('#0', stretch=NO, minwidth=0, width=0)
        self.mytable.column('#1', stretch=NO, minwidth=0, width=50)
        self.mytable.column('#2', stretch=NO, minwidth=0, width=140)
        self.mytable.column('#3', stretch=NO, minwidth=0, width=140)
        self.mytable.column('#4', stretch=NO, minwidth=0, width=150)
        self.mytable.bind("<ButtonRelease-1>", self.fetchbysrno)
        self.mytable.pack()
        mytablearea.place(relx=0.453, rely=0.167, height=200, width=500)

        self.Label7 = tk.Label(self.TNotebook1_t1)
        self.Label7.place(relx=0.04, rely=0.063, height=21, width=92)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''Search By Name''')

        self.Entry6 = tk.Entry(self.TNotebook1_t1)
        self.Entry6.place(relx=0.213, rely=0.063, height=20, relwidth=0.219)
        self.Entry6.configure(background="white")
        self.Entry6.configure(disabledforeground="#a3a3a3")
        self.Entry6.configure(font="TkFixedFont")
        self.Entry6.configure(foreground="#000000")
        self.Entry6.configure(highlightbackground="#d9d9d9")
        self.Entry6.configure(highlightcolor="black")
        self.Entry6.configure(insertbackground="black")
        self.Entry6.configure(selectbackground="#c4c4c4")
        self.Entry6.configure(selectforeground="black")

        self.Button5 = tk.Button(self.TNotebook1_t1)
        self.Button5.place(relx=0.48, rely=0.063, height=20, width=46)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''Search''',command=self.searchinfo1)

        self.Label8 = tk.Label(self.TNotebook1_t1)
        self.Label8.place(relx=0.04, rely=0.188, height=371, width=704)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(text='''Label''')
        self.Label8.configure(width=704)

        self.TSeparator1 = ttk.Separator(self.TNotebook1_t1)
        self.TSeparator1.place(relx=0.04, rely=0.146, relwidth=0.933)

        mytablearea1 = Frame(self.TNotebook1_t1)
        scrollbarx1 = Scrollbar(mytablearea1, orient=HORIZONTAL)
        scrollbary1 = Scrollbar(mytablearea1, orient=VERTICAL)

        self.mytable1 = ttk.Treeview(mytablearea1, columns=("srno", "name","marks", "tmarks", "percentage"),
                                    xscrollcommand=scrollbarx1.set, yscrollcommand=scrollbary1.set)
        self.mytable1['show'] = 'headings'
        scrollbarx1.config(command=self.mytable1.xview)
        scrollbary1.config(command=self.mytable1.yview)

        scrollbarx1.pack(side=BOTTOM, fill=X)
        scrollbary1.pack(side=RIGHT, fill=Y)

        self.mytable1.heading("srno", text="Serial No")
        self.mytable1.heading("name", text="Student Name")
        self.mytable1.heading("marks", text="Marks Obtained")
        self.mytable1.heading("tmarks", text="Total Marks")
        self.mytable1.heading("percentage", text="Percentage")

        self.mytable1.column('#0', stretch=NO)
        self.mytable1.column('#1', stretch=NO)
        self.mytable1.column('#2', stretch=NO)
        self.mytable1.column('#3', stretch=NO)
        self.mytable1.column('#4', stretch=NO)
        self.mytable1.column('#5', stretch=NO)
        self.mytable1.pack()
        mytablearea1.place(relx=0.04, rely=0.188, height=371, width=1000)

    def updateinfo(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="collegedb")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute(
                        "update examtable set name=%s,marks=%s,tmarks=%s,percentage=%s where srno=%s",
                        (self.Entry1.get(),self.Entry3.get(),self.Entry4.get(),self.Entry5.get(), self.serialno
                        ))
                    mydatabaseobj.commit()
                    messagebox.showinfo("Success", "Record Updated Successfully",parent=self.TNotebook1_t0)
            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex))
            finally:
                mydatabaseobj.close()


            self.Entry1.delete(0, END)
            self.Entry3.delete(0, END)

            self.Entry4.delete(0, END)

            self.Entry2.delete(0, END)

            self.Entry5.delete(0, END)
            self.mytable.delete(*self.mytable.get_children())

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
                            "delete from examtable where srno=%s",
                            (self.serialno))
                        mydatabaseobj.commit()
                        messagebox.showinfo("Success", "Record Deleted Successfully",parent=self.TNotebook1_t0)
                except Exception as ex:
                    messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex),
                                        )

                finally:
                    mydatabaseobj.close()
                self.Entry1.delete(0, END)
                self.Entry3.delete(0, END)

                self.Entry4.delete(0, END)

                self.Entry2.delete(0, END)

                self.Entry5.delete(0, END)
                self.mytable.delete(*self.mytable.get_children())

            except Exception as ex:
                messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))



    def searchinfo1(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="collegedb")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select srno,name, marks, tmarks, percentage from examtable where name like %s", (self.Entry1.get() + "%"))
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

    def mousee(self,e):

        a=int(self.Entry3.get())
        b=int(self.Entry4.get())
        self.c=(a/b)*100
        self.Entry5.insert(0,self.c)
        print(self.c)

    def saveinfo(self):

        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="", db="collegedb")
            try:
                with mydatabaseobj.cursor() as myconn:
                    myconn.execute(
                        "insert into examtable(srno,name,marks,tmarks,percentage) "
                        "values(%s,%s,%s,%s,%s)",
                        (self.Entry2.get(),self.Entry1.get(),self.Entry3.get(), self.Entry4.get(), self.Entry5.get()
                         ))
                    mydatabaseobj.commit()
                    messagebox.showinfo("Success", "Record Saved Successfully", parent=self.TNotebook1_t0)

            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex))
            finally:
                mydatabaseobj.close()

            self.Entry1.delete(0, END)
            self.Entry3.delete(0, END)

            self.Entry4.delete(0, END)

            self.Entry2.delete(0, END)

            self.Entry5.delete(0, END)
            self.mytable.delete(*self.mytable.get_children())


        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))





    def searchinfo(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                        db="collegedb")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select srno, name, phone,course from studenttable"
                               " where name like %s", (self.Entry1.get() + "%"))
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
                        self.Entry2.delete(0, END)
                        self.Entry2.insert(0,self.serialno)
                        self.Entry1.delete(0,END)
                        self.Entry1.insert(0,row[1])

                    if myresultdata == None:
                        messagebox.showerror("No Records Found", "No Students added yet.")

            except Exception as ex:
                traceback.print_exc()
                messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex))
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))






