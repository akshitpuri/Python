from tkinter import messagebox

import pymysql

import login
import createadmin


class MainClass:
    def __init__(self):

        try:
                mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                                db="collegedb")
                try:

                    with mydatabaseobj.cursor() as myconn:
                        myconn.execute("select * from usertable")
                        myresultdata = myconn.fetchone()

                        if myresultdata is not None:
                            login.login()
                        else:
                            createadmin.CreateAdmin()


                except Exception as ex:
                    messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex))
                finally:
                    mydatabaseobj.close()
        except Exception as ex:
                messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))

MainClass()