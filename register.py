from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector


class Register:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x900+0+0")
        self.root.title("Registration Window")

        # ================= Variables =================
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_password = StringVar()
        self.var_confirmpassword = StringVar()

        # ================= Background Image =================
        bg = Image.open("collage_image/Software Developer.jpg")
        bg = bg.resize((1600, 900))
        self.photo_bg = ImageTk.PhotoImage(bg)

        lbl_bg = Label(self.root, image=self.photo_bg)
        lbl_bg.place(x=0, y=0, width=1600, height=900)

        # ================= Left Image =================
        left_img = Image.open("collage_image/istockphoto-1410003855-170667a.jpg")
        left_img = left_img.resize((450, 550))
        self.photo_left = ImageTk.PhotoImage(left_img)

        lbl_left = Label(self.root, image=self.photo_left)
        lbl_left.place(x=80, y=100, width=450, height=550)

        # ================= Main Frame =================
        frame = Frame(self.root, bg="white")
        frame.place(x=530, y=100, width=800, height=550)

        register_lbl = Label(
            frame,
            text="REGISTER HERE",
            font=("times new roman", 25, "bold"),
            fg="red",
            bg="white"
        )
        register_lbl.place(x=50, y=20)

        # ================= First Name =================
        fname = Label(
            frame,
            text="First Name",
            font=("times new roman", 15, "bold"),
            bg="white",fg="black"
        )
        fname.place(x=50, y=80)

        txt_fname = ttk.Entry(
            frame,
            textvariable=self.var_fname,
            font=("times new roman", 15)
        )
        txt_fname.place(x=50, y=110, width=250)

        # ================= Last Name =================
        lname = Label(
            frame,
            text="Last Name",
            font=("times new roman", 15, "bold"),
            bg="white",fg="black"
        )
        lname.place(x=370, y=80)

        txt_lname = ttk.Entry(
            frame,
            textvariable=self.var_lname,
            font=("times new roman", 15)
        )
        txt_lname.place(x=370, y=110, width=250)

        # ================= Contact =================
        contact = Label(
            frame,
            text="Contact No",
            font=("times new roman", 15, "bold"),
            bg="white",fg="black"
        )
        contact.place(x=50, y=150)

        txt_contact = ttk.Entry(
            frame,
            textvariable=self.var_contact,
            font=("times new roman", 15)
        )
        txt_contact.place(x=50, y=180, width=250)

        # ================= Email =================
        email = Label(
            frame,
            text="Email",
            font=("times new roman", 15, "bold"),
            bg="white",fg="black"
        )
        email.place(x=370, y=150)

        txt_email = ttk.Entry(
            frame,
            textvariable=self.var_email,
            font=("times new roman", 15)
        )
        txt_email.place(x=370, y=180, width=250)

        # ================= Security Question =================
        security_Q = Label(
            frame,
            text="Select Security Questions",
            font=("times new roman", 15, "bold"),
            bg="white",fg="black"
        )
        security_Q.place(x=50, y=220)

        combo_security_Q = ttk.Combobox(
            frame,
            textvariable=self.var_securityQ,
            font=("times new roman", 13),
            state="readonly"
        )

        combo_security_Q["values"] = (
            "Select",
            "Your Birth Place",
            "Your Nick Name",
            "Your Pet Name"
        )

        combo_security_Q.current(0)
        combo_security_Q.place(x=50, y=250, width=250)

        # ================= Security Answer =================
        security_A = Label(
            frame,
            text="Security Answer",
            font=("times new roman", 15, "bold"),
            bg="white",fg="black"
        )
        security_A.place(x=370, y=220)

        txt_security = ttk.Entry(
            frame,
            textvariable=self.var_securityA,
            font=("times new roman", 15)
        )
        txt_security.place(x=370, y=250, width=250)

        # ================= Password =================
        pswd = Label(
            frame,
            text="Password",
            font=("times new roman", 15, "bold"),
            bg="white",fg="black"
        )
        pswd.place(x=50, y=290)

        txt_pswd = ttk.Entry(
            frame,
            textvariable=self.var_password,
            font=("times new roman", 15),
            show="*"
        )
        txt_pswd.place(x=50, y=320, width=250)

        # ================= Confirm Password =================
        confirm_pswd = Label(
            frame,
            text="Confirm Password",
            font=("times new roman", 15, "bold"),
            bg="white",fg="black"
        )
        confirm_pswd.place(x=370, y=290)

        txt_confirm_pswd = ttk.Entry(
            frame,
            textvariable=self.var_confirmpassword,
            font=("times new roman", 15),
            show="*"
        )
        txt_confirm_pswd.place(x=370, y=320, width=250)

        # ================= Check Button =================
        self.var_check = IntVar()

        checkbtn = Checkbutton(
            frame,
            variable=self.var_check,
            text="I Agree The Terms & Conditions",
            font=("times new roman", 12, "bold"),
            bg="white",fg="black",
            onvalue=1,
            offvalue=0
        )
        checkbtn.place(x=50, y=370)

        # ================= Buttons =================
        register_btn = Button(
            frame,
            text="Register Now",
            command=self.register_data,
            font=("times new roman", 15, "bold"),
            bd=3,
            relief=RIDGE,
            fg="black",
            bg="red",
            cursor="hand2"
        )
        register_btn.place(x=50, y=420, width=200, height=40)

        login_btn = Button(
            frame,
            text="Login Now",
            command=self.return_login,
            font=("times new roman", 15, "bold"),
            bd=3,
            relief=RIDGE,
            fg="black",
            bg="blue",
            cursor="hand2"
        )
        login_btn.place(x=300, y=420, width=200, height=40)

    # ================= Register Function =================
    def register_data(self):

     if self.var_fname.get() == "" or self.var_email.get() == "":
        messagebox.showerror(
            "Error",
            "All Fields Are Required",
            parent=self.root
        )

     elif self.var_password.get() != self.var_confirmpassword.get():
        messagebox.showerror(
            "Error",
            "Password & Confirm Password Must Be Same",
            parent=self.root
        )

     elif self.var_check.get() == 0:
        messagebox.showerror(
            "Error",
            "Please Agree Terms & Conditions",
            parent=self.root
        )

     else:
        try:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Sonu@123",
                database="student"
            )

            my_cursor = conn.cursor()

            query = "SELECT * FROM register WHERE email=%s"
            value = (self.var_email.get(),)

            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row is not None:
                messagebox.showerror(
                    "Error",
                    "User Already Exists",
                    parent=self.root
                )

            else:
                my_cursor.execute("""
                    INSERT INTO register
                    (fname, lname, email, securityQ, securityA, password, contact)
                    VALUES (%s,%s,%s,%s,%s,%s,%s)
                """, (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_password.get(),
                    self.var_contact.get()
                ))

                conn.commit()
                conn.close()

                messagebox.showinfo(
                    "Success",
                    "Registered Successfully",
                    parent=self.root
                )

        except Exception as es:
            messagebox.showerror(
                "Error",
                f"Due To : {str(es)}",
                parent=self.root
            )

    # ================= Return Login =================
    def return_login(self):
        self.root.destroy()

    


# ================= Main Function =================
if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()