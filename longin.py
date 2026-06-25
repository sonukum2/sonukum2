from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter as tk
from tkinter import messagebox
import mysql.connector

from register import Register


class login:
     def __init__(self, root):
        self.root = root
        self.root.geometry("1730x890+0+0")
        self.root.title("Face Recognition System")

        self.bg=ImageTk.PhotoImage(file=r"collage_image/Student-Experience-Cover-2.jpg")
       
        f_lbl = Label(self.root, image=self.bg)
        f_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(f_lbl, bd=2, bg="white")
        frame.place(x=610, y=180, width=330, height=450)

        img = Image.open("collage_image/login-icon-button-vector-illustration-isolated-white-background-126999474.webp")
        img = img.resize((140, 140), Image.Resampling.LANCZOS)

        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg,)
        f_lbl.place(x=720, y=185, width=110, height=130)

        
        get_str = Label(frame, text=" Get started ",
                font=("times new roman", 20, "bold"),
                bg="white", fg="darkgreen")
        get_str.place(x=100, y=120)
        
        #label
        username = Label(frame, text=" username ",font=("times new roman", 20, "bold"),bg="white", fg="darkgreen")
        username.place(x=50, y=150)

        self.txtuser=Entry(frame,font=("time new roman",12,"bold"))
        self.txtuser.place(x=40,y=180,width=250)

        password = Label(frame, text=" password ",font=("times new roman", 20, "bold"),bg="white", fg="darkgreen")
        password.place(x=50, y=225)

        self.txtpass=Entry(frame,font=("time new roman",12,"bold"))
        self.txtpass.place(x=40,y=270,width=250)

        #============icon  image=============


        img1 = Image.open("collage_image/11284777.png")
        img1 = img1.resize((14, 14), Image.Resampling.LANCZOS)

        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1,borderwidth=0)
        f_lbl.place(x=655, y=345, width=15, height=15)
        

        img2 = Image.open("collage_image/login-icon-in-flat-style-password-access-vector-illustration-on-white-isolated-background-padlock-entry-business-concept-2AC5AD9.jpg")
        img2 = img2.resize((14, 14), Image.Resampling.LANCZOS)

        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2,borderwidth=0)
        f_lbl.place(x=655, y=421, width=15, height=15)

        loginbtn = tk.Button(frame,
                                text="Login", cursor="hand2",command=self.login,
                                font=("times new roman", 15, "bold"),
                                bg="red",bd=3,relief=RIDGE,fg="black",activebackground="white",activeforeground="red")

        loginbtn.place(x=110, y=300, width=130, height=35)



        registerbtn = tk.Button(frame, text="New User Register", cursor="hand2",command=self.register_window,font=("times new roman", 14, "bold"),borderwidth=1,fg="black",bg="white",activebackground="white",activeforeground="black")

        registerbtn.place(x=10, y=350, width=160)


        Forgetpasswordbtn = tk.Button(frame,text="Forget Password", cursor="hand2",font=("times new roman", 14, "bold"),borderwidth=1,fg="black",bg="white",activebackground="white",activeforeground="black")

        Forgetpasswordbtn.place(x=10, y=380, width=160, )


     

    # ================= Open Register Window =================
     def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    # ================= Login Function =================
     def login(self):

        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror(
                "Error",
                "All Fields Are Required"
            )

        else:
            try:
                conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sonu@123",
    database="student"

                )

                my_cursor = conn.cursor()

                my_cursor.execute(
                    "select * from register where email=%s and password=%s",
                    (
                        self.txtuser.get(),
                        self.txtpass.get()
                    )
                )

                row = my_cursor.fetchone()

                if row is None:
                    messagebox.showerror(
                        "Error",
                        "Invalid Email or Password"
                    )

                else:
                    messagebox.showinfo(
                        "Success",
                        "Welcome To Face Recognition System"
                    )

                conn.close()

            except Exception as es:
                messagebox.showerror(
                    "Error",
                    f"Error Due To : {str(es)}"
                )


        








if __name__ == "__main__":
    root = Tk()
    obj = login(root)
    root.mainloop()
