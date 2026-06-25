import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Title
        title_lbl = tk.Label(
            self.root,
            text="HELP",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="blue"
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Image
        img_top = Image.open("collage_image/4He9LjIo.png")
        img_top = img_top.resize((1530, 790), Image.Resampling.LANCZOS)

        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl_left = tk.Label(self.root, image=self.photoimg_top)
        f_lbl_left.place(x=0, y=45, width=1530, height=785)

        dev_label = tk.Label(f_lbl_left, text="Email:ksonu02feb2000@gmail.com", font=(
            "times new roman", 20, "bold"), bg="green")
        dev_label.place(x=80,y=400)



# Main function
if __name__ == "__main__":
    root = tk.Tk()
    obj = Help(root)
    root.mainloop()