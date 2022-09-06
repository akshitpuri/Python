from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import parent
import pymysql


class login:
    def __init__(self):
        self.mytop = Tk()
        self.mytop.configure(background="#d9d9d9")
        self.mytop.configure(highlightbackground="#d9d9d9")
        self.mytop.configure(highlightcolor="black")
        self.mytop.geometry("800x450+260+110")
        self.mytop.title("Login")

        self.TSeparator1 = ttk.Separator(self.mytop)
        self.TSeparator1.place(relx=0.638, rely=0.022, relheight=0.956)
        self.TSeparator1.configure(orient="vertical")

        self.Label1 = tk.Label(self.mytop)
        self.Label1.place(relx=0.225, rely=0.156, height=110, width=150)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.pic = PhotoImage(file="../College Management System Project/images/Graduation Cap_96px.png")
        self.Label1.configure(image=self.pic)


        self.Label2 = tk.Label(self.mytop)
        self.Label2.place(relx=0.088, rely=0.422, height=51, width=382)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")

        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''COLLEGE MANAGEMENT''',font=('Arial Black','20','bold'))

        self.Label3 = tk.Label(self.mytop)
        self.Label3.place(relx=0.213, rely=0.533, height=51, width=177)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")

        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''SOFTWARE''',font=('Arial Black','20','bold'))

        self.Label4 = tk.Label(self.mytop)
        self.Label4.place(relx=0.731, rely=0.156, height=110, width=150)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.pic1 = PhotoImage(file="../College Management System Project/images/User_96px.png")
        self.Label4.configure(image=self.pic1)

        self.Label5 = tk.Label(self.mytop)
        self.Label5.place(relx=0.688, rely=0.444, height=21, width=59)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Username''')

        self.Entry1 = tk.Entry(self.mytop)
        self.Entry1.place(relx=0.788, rely=0.444,height=20, relwidth=0.155)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=124)
        self.Entry1.focus_set()

        self.Label6 = tk.Label(self.mytop)
        self.Label6.place(relx=0.688, rely=0.533, height=21, width=56)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Password''')

        self.Entry2 = tk.Entry(self.mytop)
        self.Entry2.place(relx=0.788, rely=0.533,height=20, relwidth=0.155)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black", show="*")
        self.Entry2.configure(width=124)

        self.Button1 = tk.Button(self.mytop)
        self.Button1.place(relx=0.825, rely=0.622, height=28, width=58)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.pic2 = PhotoImage(file="../College Management System Project/images/Chevron Right_32px.png")
        self.Button1.configure(image=self.pic2)
        self.Button1.configure(pady="0")
        self.Button1.configure(relief="groove")
        self.Button1.configure(text='''Button''', command=self.logininfo)
        self.Button1.configure(width=58)
        self.mytop.mainloop()

    def logininfo(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="collegedb")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select * from usertable where uname=%s and pass=%s",
                                   (self.Entry1.get(), self.Entry2.get()))
                    myresultdata = myconn.fetchone()

                    if myresultdata is not None:
                        if myresultdata[2] == "Admin":
                            self.mytop.destroy()
                            parent.myparent()

                    else:

                        messagebox.showerror("Login Failed", "Incorrect Username/Password")
                        self.Entry1.delete(0, END)
                        self.Entry2.delete(0, END)




            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex))
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))



