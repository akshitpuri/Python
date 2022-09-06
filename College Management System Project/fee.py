import traceback
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.messagebox import askquestion

import pymysql as pymysql
import tkinter as tk

from tkcalendar import DateEntry


class FeesClass:
    def __init__(self, myframe):
        self.mytop = Toplevel(myframe)
        self.mytop.geometry("1130x560+213+128")
        self.mytop.title("Fees Management")
        self.mytop.configure(background="#d9d9d9")
        self.mytop.configure(highlightbackground="#d9d9d9")
        self.mytop.configure(highlightcolor="black")


        self.TNotebook1 = ttk.Notebook(self.mytop)
        self.TNotebook1.place(relx=0.011, rely=0.019, relheight=0.971
                , relwidth=0.983)
        self.TNotebook1.configure(width=884)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t0 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t0, padding=3)
        self.TNotebook1.tab(0, text="Fees",compound="left",underline="-1",)
        self.TNotebook1_t0.configure(background="#d9d9d9")
        self.TNotebook1_t0.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t0.configure(highlightcolor="black")
        self.TNotebook1_t1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(1, text="Data",compound="left",underline="-1",)
        self.TNotebook1_t1.configure(background="#d9d9d9")
        self.TNotebook1_t1.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t1.configure(highlightcolor="black")

        self.TLabel1 = ttk.Label(self.TNotebook1_t0)
        self.TLabel1.place(relx=0.034, rely=0.063, height=19, width=90)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(text='''Search By Name''')

        self.Entry1 = tk.Entry(self.TNotebook1_t0)
        self.Entry1.place(relx=0.182, rely=0.063,height=20, relwidth=0.186)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Button1 = tk.Button(self.TNotebook1_t0)
        self.Button1.place(relx=0.409, rely=0.063, height=20, width=46)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Search''',command=self.searchinfo)

        self.Label1 = tk.Label(self.TNotebook1_t0)
        self.Label1.place(relx=0.034, rely=0.146, height=21, width=59)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Total Fees''')

        self.Entry2 = tk.Entry(self.TNotebook1_t0)
        self.Entry2.place(relx=0.182, rely=0.146,height=20, relwidth=0.186)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Label2 = tk.Label(self.TNotebook1_t0)
        self.Label2.place(relx=0.034, rely=0.229, height=21, width=54)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Semester''')

        self.TCombobox1 = ttk.Combobox(self.TNotebook1_t0)
        self.TCombobox1.place(relx=0.182, rely=0.229, relheight=0.044
                , relwidth=0.185)

        self.TCombobox1.configure(width=163)
        self.TCombobox1.configure(takefocus="")
        self.TCombobox1.set('Choose Semester')
        self.TCombobox1.configure(values=('1st', '2nd', '3rd', '4th', '5th','6th','7th','8th'))

        self.Entry3 = tk.Entry(self.TNotebook1_t0)
        self.Entry3.place(relx=0.182, rely=0.313,height=20, relwidth=0.186)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")

        self.Label3 = tk.Label(self.TNotebook1_t0)
        self.Label3.place(relx=0.034, rely=0.313, height=21, width=29)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Paid''')

        self.Label4 = tk.Label(self.TNotebook1_t0)
        self.Label4.place(relx=0.034, rely=0.396, height=21, width=56)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Paid Date''')


        self.pd = DateEntry(self.TNotebook1_t0, background='darkblue', foreground='white', borderwidth=2)
        self.pd.place(relx=0.182, rely=0.396,height=20, relwidth=0.186)

        self.Label5 = tk.Label(self.TNotebook1_t0)
        self.Label5.place(relx=0.034, rely=0.479, height=21, width=103)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Mode Of Payment''')

        self.mode = StringVar()
        self.TRadiobutton1 = ttk.Radiobutton(self.TNotebook1_t0)
        self.TRadiobutton1.place(relx=0.182, rely=0.479, relheight=0.052
                , relwidth=0.078)
        self.TRadiobutton1.configure(text='''Cheque''')
        self.TRadiobutton1.configure(value="Cheque")
        self.TRadiobutton1.configure(variable=self.mode)
        self.TRadiobutton1.configure(width=59)

        self.TRadiobutton2 = ttk.Radiobutton(self.TNotebook1_t0)
        self.TRadiobutton2.place(relx=0.273, rely=0.479, relheight=0.052
                , relwidth=0.061)
        self.TRadiobutton2.configure(text='''Cash''')
        self.TRadiobutton2.configure(value="Cash")
        self.TRadiobutton2.configure(takefocus="",variable=self.mode)
        self.TRadiobutton2.configure(width=59)

        self.Label6 = tk.Label(self.TNotebook1_t0)
        self.Label6.place(relx=0.034, rely=0.563, height=21, width=74)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Due Amount''')

        self.Entry5 = tk.Entry(self.TNotebook1_t0)
        self.Entry5.place(relx=0.182, rely=0.563,height=20, relwidth=0.186)
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(foreground="#000000")
        self.Entry3.bind("<Return>", self.mousee)



        self.Button2 = tk.Button(self.TNotebook1_t0)
        self.Button2.place(relx=0.182, rely=0.646, height=24, width=35)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Save''',command=self.saveinfo)

        self.Label10 = tk.Label(self.TNotebook1_t0)
        self.Label10.place(relx=0.534, rely=0.063, height=21, width=109)
        self.Label10.configure(background="#d9d9d9")
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(text='''Admission Number''')

        self.Entry7 = tk.Entry(self.TNotebook1_t0)
        self.Entry7.place(relx=0.693, rely=0.063, height=20, relwidth=0.186)
        self.Entry7.configure(background="white")
        self.Entry7.configure(disabledforeground="#a3a3a3")
        self.Entry7.configure(font="TkFixedFont")
        self.Entry7.configure(foreground="#000000")
        self.Entry7.configure(insertbackground="black")

        self.Button3 = tk.Button(self.TNotebook1_t0)
        self.Button3.place(relx=0.242, rely=0.646, height=24, width=49)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Update''',command=self.updateinfo)

        self.delete = tk.Button(self.TNotebook1_t0)
        self.delete.place(relx=0.302, rely=0.646, height=24, width=49)
        self.delete.configure(text='Delete', command=self.deleteinfo)

        self.Label8 = tk.Label(self.TNotebook1_t1)
        self.Label8.place(relx=0.034, rely=0.063, height=21, width=92)
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(text='''Search By Name''')

        self.Entry6 = tk.Entry(self.TNotebook1_t1)
        self.Entry6.place(relx=0.193, rely=0.063,height=20, relwidth=0.186)
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
        self.Button4.configure(text='''Search''',command=self.searchinfo1)

        self.TSeparator1 = ttk.Separator(self.TNotebook1_t1)
        self.TSeparator1.place(relx=0.034, rely=0.146, relwidth=0.955)


        mytablearea = Frame(self.TNotebook1_t0)
        scrollbarx = Scrollbar(mytablearea, orient=HORIZONTAL)
        scrollbary = Scrollbar(mytablearea, orient=VERTICAL)

        self.mytable = ttk.Treeview(mytablearea, columns=("srno", "name", "phone", "course"),
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
        mytablearea.place(relx=0.42, rely=0.229, height=200, width=500)

        mytablearea1 = Frame(self.TNotebook1_t1)
        scrollbarx1 = Scrollbar(mytablearea1, orient=HORIZONTAL)
        scrollbary1 = Scrollbar(mytablearea1, orient=VERTICAL)

        self.mytable1 = ttk.Treeview(mytablearea1, columns=("srno", "name", "tfee", "sem", "paid","pdate","mode","due"),
                                     xscrollcommand=scrollbarx1.set, yscrollcommand=scrollbary1.set)
        self.mytable1['show'] = 'headings'
        scrollbarx1.config(command=self.mytable1.xview)
        scrollbary1.config(command=self.mytable1.yview)

        scrollbarx1.pack(side=BOTTOM, fill=X)
        scrollbary1.pack(side=RIGHT, fill=Y)

        self.mytable1.heading("srno", text="Serial No")
        self.mytable1.heading("name", text="Student Name")
        self.mytable1.heading("tfee", text="Total Fees")
        self.mytable1.heading("sem", text="Semester")
        self.mytable1.heading("paid", text="Fees Paid")
        self.mytable1.heading("pdate", text="Payment Date")
        self.mytable1.heading("mode", text="Mode Of Payment")
        self.mytable1.heading("due", text="Fees Due")

        self.mytable1.column('#0', stretch=NO,minwidth=0, width=0)
        self.mytable1.column('#1', stretch=NO,minwidth=0, width=124)
        self.mytable1.column('#2', stretch=NO,minwidth=0, width=124)
        self.mytable1.column('#3', stretch=NO,minwidth=0, width=124)
        self.mytable1.column('#4', stretch=NO,minwidth=0, width=120)
        self.mytable1.column('#5', stretch=NO,minwidth=0, width=120)
        self.mytable1.column('#6', stretch=NO,minwidth=0, width=124)
        self.mytable1.column('#7', stretch=NO,minwidth=0, width=124)
        self.mytable1.column('#8', stretch=NO,minwidth=0, width=124)
        self.mytable1.pack()
        mytablearea1.place(relx=0.04, rely=0.188, height=371, width=1000)

    def updateinfo(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="collegedb")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute(
                        "update feetable set name=%s,tfee=%s,sem=%s,paid=%s,pdate=%s,mode=%s,due=%s where srno=%s",
                        (self.Entry1.get(),self.Entry2.get(),self.TCombobox1.get(),self.Entry3.get(),self.pd.get_date(),self.mode.get(),self.Entry5.get(), self.serialno
                        ))
                    mydatabaseobj.commit()
                    messagebox.showinfo("Success", "Record Updated Successfully",parent=self.TNotebook1_t0)
            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex))
            finally:
                mydatabaseobj.close()


            self.Entry1.delete(0, END)
            self.Entry3.delete(0, END)
            self.mode.set(" ")
            self.TCombobox1.set("Choose Semester")
            self.Entry7.delete(0, END)
            self.pd.delete(0, END)

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
                            "delete from feetable where srno=%s",
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
                self.mode.set(" ")
                self.TCombobox1.set("Choose Semester")
                self.Entry7.delete(0, END)
                self.pd.delete(0, END)

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
                    myconn.execute("select srno,name,tfee,sem,paid,pdate,mode,due from feetable where name like %s",
                                   (self.Entry1.get() + "%"))
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
        a=int(self.Entry2.get())
        b=int(self.Entry3.get())
        self.c=a-b
        self.Entry5.insert(0,self.c)
        print(self.c)

    def saveinfo(self):

        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="", db="collegedb")
            try:
                with mydatabaseobj.cursor() as myconn:
                    myconn.execute(
                        "insert into feetable(name,srno,tfee,sem,paid,pdate,mode,due) "
                        "values(%s,%s,%s,%s,%s,%s,%s,%s)",
                        (self.Entry1.get(),self.Entry7.get(),self.Entry2.get(),self.TCombobox1.get(),self.Entry3.get(),self.pd.get_date(),self.mode.get(),self.Entry5.get()
                        ))
                    mydatabaseobj.commit()
                    messagebox.showinfo("Success", "Record Saved Successfully", parent=self.TNotebook1_t0)

            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex))
            finally:
                mydatabaseobj.close()
            self.Entry1.delete(0, END)
            self.Entry3.delete(0, END)
            self.mode.set(" ")
            self.TCombobox1.set("Choose Semester")
            self.Entry7.delete(0, END)
            self.pd.delete(0, END)

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
                        self.Entry7.delete(0, END)
                        self.Entry7.insert(0, self.serialno)
                        self.Entry1.delete(0, END)
                        self.Entry1.insert(0, row[1])

                    if myresultdata == None:
                        messagebox.showerror("No Records Found", "No Students added yet.")

            except Exception as ex:
                traceback.print_exc()
                messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex))
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))

