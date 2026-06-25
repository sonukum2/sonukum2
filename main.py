
from time import strftime
from datetime import datetime

import os
import tkinter
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from student import student
import subprocess
from train import train
from face_recognition import FaceRecognition
from attendance import Attendance
from developer import developer
from help import Help

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1590x790+0+0")
        self.root.title("face recognition system")

        # ===== top images =====
        img = Image.open("collage_image/MONU1.jpg").resize((530, 390), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        tk.Label(self.root, image=self.photoimg).place(x=0, y=0, width=530, height=390)

        img1 = Image.open("collage_image/download.jpeg").resize((530, 390), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        tk.Label(self.root, image=self.photoimg1).place(x=530, y=0, width=530, height=390)

        img2 = Image.open("collage_image/images.jpeg").resize((530, 390), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        tk.Label(self.root, image=self.photoimg2).place(x=1060, y=0, width=530, height=390)

        # ===== background =====
        img3 = Image.open("collage_image/images (1).jpeg").resize((1590, 790), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = tk.Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=390, width=1590, height=790)

        title_lbl = tk.Label(
            bg_img,
            text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="red",
        )
        title_lbl.place(x=0, y=0, width=1590, height=45)

        #----------=time==========
        def time():
            string = strftime('%H:%M:%S %P')
            lbl.config(text = string)
            lbl.after(1000,time)

        lbl = tk.Label(title_lbl,
               font=('times new roman',24,'bold'),
               background='white',
               foreground='blue')
        lbl.place(x=0,y=0,width=115,height=40)
        time()




        # ===== student button =====
        img4 = Image.open("collage_image/4381741771650ft7wlobucn6tzvxd0pykzxthqhaqtzhuyqjknvuwn2knbokro9hcmx5akmc3dt6upeoovmylkbqel2kfnbj2jradbwnyrgthuzpg.webp")
        img4 = img4.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        btn_student = tk.Button(bg_img, image=self.photoimg4,command=self.student_details, cursor="hand2")
    

        btn_student.place(x=200, y=100, width=220, height=220)

        tk.Label(bg_img, text="STUDENT DETAILS", bg="white", fg="black").place(x=200, y=300, width=220, height=40)

        # ===== detect face button =====
        img5 = Image.open("collage_image/chessboard_1-mobile2x.jpg").resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        tk.Button(bg_img, image=self.photoimg5, cursor="hand2", command=self.face_data).place(x=450, y=100, width=220, height=220)
        tk.Label(bg_img, text="DETECT FACE", bg="white", fg="black").place(x=450, y=300, width=220, height=40)

        # ===== attendance =====
        img6 = Image.open("collage_image/download (1).jpeg").resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        tk.Button(bg_img, image=self.photoimg6, cursor="hand2",command=self.attendance).place(x=700, y=100, width=220, height=220)
        tk.Label(bg_img, text="ATTENDANCE").place(x=700, y=300, width=220, height=40)

        # ===== help =====
        img7 = Image.open("collage_image/pngtree-smart-chatbot-cartoon-clipart-png-image_6620453.png")
        img7 = img7.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        tk.Button(bg_img, image=self.photoimg7, cursor="hand2",command=self.help_data).place(x=950, y=100, width=220, height=220)
        tk.Label(bg_img, text="HELP").place(x=950, y=300, width=220, height=40)

        # ===== train data =====
        img8 = Image.open("collage_image/download (2).jpeg").resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        tk.Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.train_data).place(x=200, y=350, width=220, height=220)
        tk.Label(bg_img, text="TRAIN DATA").place(x=200, y=550, width=220, height=40)

        # ===== photos =====
        img9 = Image.open("collage_image/media_190fe059034957a13092d986eacaf7679e1a9510c.png")
        img9 = img9.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        tk.Button(
    bg_img,image=self.photoimg9,command=self.open_img,cursor="hand2").place(x=450, y=350, width=220, height=220)
        tk.Label(bg_img, text="PHOTOS").place(x=450, y=550, width=220, height=40)

        # ===== developer =====
        img11 = Image.open("collage_image/download (3).jpeg").resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        tk.Button(bg_img, image=self.photoimg11,command=self.developer_data, cursor="hand2").place(x=700, y=350, width=220, height=220)
        tk.Label(bg_img, text="DEVELOPER").place(x=700, y=550, width=220, height=40)

        # ===== exit =====
        img10 = Image.open("collage_image/images.png").resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        tk.Button(bg_img, image=self.photoimg10, cursor="hand2", command=self.iExit).place(x=950, y=350, width=220, height=220)
        tk.Label(bg_img, text="EXIT").place(x=950, y=550, width=220, height=40)

    # ===== function =====
    def student_details(self):
        print("student details button clicked")
        self.new_window = tk.Toplevel(self.root)
        self.app = student(self.new_window)
   
   
    def train_data(self):
        print("train data button clicked")
        self.new_window = tk.Toplevel(self.root)
        self.app = train(self.new_window)

    def face_data(self):
        print("face data button clicked")
        self.new_window = tk.Toplevel(self.root)
        self.app = FaceRecognition(self.new_window)

    def attendance(self):
        print("attendance button clicked")
        self.new_window = tk.Toplevel(self.root)
        self.app = Attendance(self.new_window)


    def developer_data(self):
        print("attendance button clicked")
        self.new_window = tk.Toplevel(self.root)
        self.app = developer(self.new_window)


    def help_data(self):
        print("attendance button clicked")
        self.new_window = tk.Toplevel(self.root)
        self.app = Help(self.new_window)

        
    def open_img(self):
        subprocess.call(["open", "data"])

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition ",parent=self.root)
        if   self.iExit >0:
            self.root.destroy()
        else:
            return    






if __name__ == "__main__":
    root = tk.Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
