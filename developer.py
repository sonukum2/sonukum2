import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
class developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition system")


        title_lbl = tk.Label(self.root, text="DEVELOPER",
                             font=("times new roman", 35, "bold"),
                             bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open("collage_image/gfxtoolz104262-1024x576.jpg")
        img_top = img_top.resize((1530, 790), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl_left = tk.Label(self.root, image=self.photoimg_top)
        f_lbl_left.place(x=0, y=45, width=1530, height=785) 

        #frame
        main_frame = tk.Frame(f_lbl_left, bd=2, bg="white")
        main_frame.place(x=1000, y=0, width=650, height=600)


        img_top1 = Image.open("collage_image/gfxtoolz104262-1024x576.jpg")
        img_top1 = img_top.resize((200, 200), Image.Resampling.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl_left = tk.Label(main_frame, image=self.photoimg_top1)
        f_lbl_left.place(x=300, y=0, width=200, height=200) 

        # developer info
        dev_label = tk.Label(main_frame, text="hello my name ,sonu", font=(
            "times new roman", 20, "bold"), bg="green")
        dev_label.place(x=0,y=5)

        dev_label = tk.Label(main_frame, text="i am full stack developer", font=(
            "times new roman", 20, "bold"), bg="green")
        dev_label.place(x=0,y=35)



        img2 = Image.open("collage_image/Facebook-Linkedin-image-template-10.jpg")
        img2 = img2.resize((530, 390), Image.Resampling.LANCZOS)

        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl2 = tk.Label(main_frame, image=self.photoimg2)
        f_lbl2.place(x=0, y=210, width=530, height=390)



                
                  
if __name__ == "__main__":
    root = tk.Tk()
    obj = developer(root)
    root.mainloop()