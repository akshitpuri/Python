from tkinter import *
import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk

from student import AddStudent
from misc import MiscClass
from fee import FeesClass
from exam import ExamClass
from staff import StaffClass
from changepass import ChangePass
from attendance import Att
import login


class myparent:
    def __init__(self):
        self.mytop=Tk()
        self.mytop.geometry("%dx%d+%d+%d" % (self.mytop.winfo_screenwidth(), self.mytop.winfo_screenheight(), 0, 0))
        self.mytop.title("College Management System")
        self.mytop.configure(relief="groove")
        self.mytop.configure(background="#d9d9d9")

        self.Frame1 = tk.Frame(self.mytop)
        self.Frame1.place(relx=0.007, rely=0.014, relheight=0.979, relwidth=0.139)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(width=190)

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.158, rely=0.0, height=101, width=114)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.pic = PhotoImage(file="../College Management System Project/images/Capture.PNG")
        self.Label2.configure(image=self.pic)


        self.Button3 = tk.Button(self.Frame1)
        self.Button3.place(relx=0.053, rely=0.246, height=45, width=167)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.student = PhotoImage(file="../College Management System Project/images/Add User.png")
        self.Button3.configure(relief="groove")
        self.Button3.configure(text="Student Management",command=self.addstudentframe,image=self.student,compound=LEFT)
        self.Button3.configure(width=167)

        self.Button4 = tk.Button(self.Frame1)
        self.Button4.place(relx=0.053, rely=0.333, height=45, width=167)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")

        self.Button4.configure(pady="0")

        self.staff = PhotoImage(file="../College Management System Project/images/People_32px.png")
        self.Button4.configure(relief="groove")
        self.Button4.configure(text="Staff Management", command=self.addstaffframe, image=self.staff,compound=LEFT)
        self.Button4.configure(width=167)



        self.Button5 = tk.Button(self.Frame1)
        self.Button5.place(relx=0.053, rely=0.507, height=45, width=167)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        # photo_location = os.path.join(prog_location, "../Python Project/images/Payment History_32px.png")
        self.fee = PhotoImage(file="../College Management System Project/images/Payment History_32px.png")
        self.Button5.configure(relief="groove")
        self.Button5.configure(text="Fees Management", command=self.addfeesframe, image=self.fee, compound=LEFT)
        self.Button5.configure(width=167)

        self.Button6 = tk.Button(self.Frame1)
        self.Button6.place(relx=0.053, rely=0.42, height=45, width=167)
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        # photo_location = os.path.join(prog_location, "../Python Project/images/Stocks_32px.png")
        self.exam = PhotoImage(file="../College Management System Project/images/Stocks_32px.png")
        self.Button6.configure(relief="groove")
        self.Button6.configure(text="Exam Management", command=self.examframe, image=self.exam, compound=LEFT)
        self.Button6.configure(width=167)

        self.Button7 = tk.Button(self.Frame1)
        self.Button7.place(relx=0.053, rely=0.681, height=45, width=167)
        self.Button7.configure(activebackground="#ececec")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#d9d9d9")
        self.Button7.configure(disabledforeground="#a3a3a3")
        self.Button7.configure(foreground="#000000")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        # photo_location = os.path.join(prog_location, "../Python Project/images/Chevron Right_32px.png")
        # global _img5
        # _img5 = tk.PhotoImage(file=photo_location)
        # self.Button7.configure(image=_img5)
        # self.Button7.configure(pady="0")
        self.misc = PhotoImage(file="../College Management System Project/images/Chevron Right_32px.png")
        self.Button7.configure(relief="groove")
        self.Button7.configure(text="Miscellaneous",command=self.miscframe,image=self.misc,compound=LEFT)
        self.Button7.configure(width=167)

        self.Button8=tk.Button(self.Frame1)
        self.Button8.place(relx=0.053, rely=0.594, height=45, width=167)
        self.att = PhotoImage(file="../College Management System Project/images/Stocks_32px.png")
        self.Button8.configure(relief="groove")
        self.Button8.configure(activebackground="#ececec")
        self.Button8.configure(activeforeground="#000000")
        self.Button8.configure(background="#d9d9d9")
        self.Button8.configure(disabledforeground="#a3a3a3")
        self.Button8.configure(foreground="#000000")
        self.Button8.configure(highlightbackground="#d9d9d9")
        self.Button8.configure(highlightcolor="black")
        self.Button8.configure(text="     Attendance     ", command=self.attframe, image=self.att, compound=LEFT)

        self.Frame2 = tk.Frame(self.mytop)
        self.Frame2.place(relx=0.161, rely=0.014, relheight=0.128
                          , relwidth=0.831)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(width=1135)

        self.Button1 = tk.Button(self.Frame2)
        self.Button1.place(relx=0.925, rely=0.222, height=38, width=38)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        # photo_location = os.path.join(prog_location, "../Python Project/images/Sign Out_32px.png")
        self.signout = PhotoImage(file="../College Management System Project/images/Sign Out_32px.png")
        # global _img6
        # _img6 = tk.PhotoImage(file=photo_location)
        self.Button1.configure(image=self.signout, command=self.logout)
        # self.Button1.configure(pady="0")
        # self.Button1.configure(relief="groove")
        # self.Button1.configure(text='''Logout''')

        self.Button2 = tk.Button(self.Frame2)
        self.Button2.place(relx=0.811, rely=0.222, height=38, width=110)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(relief="groove")
        self.Button2.configure(text='''Change Password''')
        self.Button2.configure(width=110,command=self.changepass)

        self.TSeparator2 = ttk.Separator(self.Frame2)
        self.TSeparator2.place(relx=0.018, rely=0.778, relwidth=0.449)

        self.Label1 = tk.Label(self.Frame2)
        self.Label1.place(relx=0.009, rely=0.222, height=41, width=517)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(justify='left')
        self.Label1.configure(text='''COLLEGE MANAGEMENT SYSTEM''',font=('Arial Black','18','bold'))
        self.Label1.configure(width=517)

        self.TSeparator1 = ttk.Separator(self.mytop)
        self.TSeparator1.place(relx=0.154, rely=0.014, relheight=0.979)
        self.TSeparator1.configure(orient="vertical")

        self.menubar = tk.Menu(self.mytop, font="TkMenuFont")
        self.mytop.configure(menu=self.menubar)

    def addstudentframe(self):
        AddStudent(self.mytop)

    def miscframe(self):
        MiscClass(self.mytop)

    def addstaffframe(self):
        StaffClass(self.mytop)

    def addfeesframe(self):
        FeesClass(self.mytop)

    def examframe(self):
        ExamClass(self.mytop)

    def logout(self):
        self.mytop.destroy()
        login.login()

    def changepass(self):
        ChangePass(self.mytop)

    def attframe(self):
        Att(self.mytop)
