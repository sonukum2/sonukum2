import csv
import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import csv
from tkinter import filedialog
mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance")



        #==========varaibles==========
        self.var_atten_id = tk.StringVar()
        self.var_atten_roll = tk.StringVar()
        self.var_atten_name = tk.StringVar()
        self.var_atten_dep = tk.StringVar()
        self.var_atten_time = tk.StringVar()
        self.var_atten_date = tk.StringVar()
        self.var_atten_attendance = tk.StringVar()


         # first image
        img = Image.open("collage_image/Student-Experience-Cover-2.jpg")
        img = img.resize((1000, 200), Image.Resampling.LANCZOS)

        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = tk.Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1000, height=200)

        # second image
        img1 = Image.open("collage_image/360_F_928531048_45ay4GSNYJuTLIHKtuR255O9ndjsHg5x.jpg")
        img1 = img1.resize((1000, 200), Image.Resampling.LANCZOS)

        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = tk.Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=800, y=0, width=1000, height=200)


            # background image
        img3 = Image.open("collage_image/download.jpeg")
        img3 = img3.resize((1930, 890), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = tk.Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1930, height=890)

        # title label
        title_lbl = tk.Label(
            bg_img,
            text="ATTENDANCE MANAGEMENT SYSTEM",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="green"
        )
        title_lbl.place(x=0, y=0, width=1830, height=45)

        main_frame = tk.Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=60, width=1665, height=790)

        # left label frame
        Left_frame = tk.LabelFrame(main_frame, bd=2, bg="white", relief=tk.RIDGE, text="Student Attendance", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=660, height=580)

        img_left = Image.open("collage_image/attendance-management.jpg")
        img_left = img_left.resize((650, 200), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl_left = tk.Label(Left_frame, image=self.photoimg_left)
        f_lbl_left.place(x=5, y=5, width=650, height=200)

        left_inside_frame = tk.Frame(Left_frame, bd=2, bg="white", relief=tk.RIDGE)
        left_inside_frame.place(x=0, y=210, width=650, height=370)

        #label and entry
        #attendance id
        attendanceId_label = tk.Label(left_inside_frame, text="Attendance ID:", font=("times new roman", 12, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        attendanceId_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_id,font=("times new roman", 12, "bold"))
        attendanceId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

        #roll number
        rollLabel = tk.Label(left_inside_frame, text="Roll No:", font=("times new roman", 12, "bold"), bg="white")
        rollLabel.grid(row=0, column=2, padx=10, pady=5, sticky=tk.W)
        roll_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_name, font=("times new roman", 12, "bold"))
        roll_entry.grid(row=0, column=3, padx=10, pady=5, sticky=tk.W)

        #department
        department_label = tk.Label(left_inside_frame, text="Department:", font=("times new roman", 12, "bold"), bg="white")
        department_label.grid(row=1, column=2, padx=10, pady=5, sticky=tk.W)
        department_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_dep, font=("times new roman", 12, "bold"))
        department_entry.grid(row=1, column=3, padx=10, pady=5, sticky=tk.W)
        #date
        date_label = tk.Label(left_inside_frame, text="Time:", font=("time new roman", 12, "bold"), bg="white")
        date_label.grid(row=2, column=2, padx=10, pady=5, sticky=tk.W)
        date_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_date, font=("times new roman", 12, "bold"))
        date_entry.grid(row=2, column=3, padx=10, pady=5, sticky=tk.W)

        #name
        name_label = tk.Label(left_inside_frame, text="Name:", font=("times new roman", 12, "bold"), bg="white")
        name_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        name_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_name, font=("times new roman", 12, "bold"))
        name_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        

        
        #time
        time_label = tk.Label(left_inside_frame, text="Date:", font=("date new roman", 12, "bold"), bg="white")
        time_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        time_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_time, font=("times new roman", 12, "bold"))
        time_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

        #attendance status
        attendance_status_label = tk.Label(left_inside_frame, text="Attendance Status:", font=("times new roman", 12, "bold"), bg="white")
        attendance_status_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        
        self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance, font=("times new roman", 12, "bold"), state="readonly", width=18)
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)




        #button frame
        btn_frame = tk.Frame(left_inside_frame, bd=2, relief=tk.RIDGE, bg="white")
        btn_frame.place(x=0, y=300, width=650, height=50)
        save_btn = tk.Button(btn_frame, text="Import CSV",command=self.import_csv, width=15, font=("times new roman", 12, "bold"), bg="blue", fg="black")
        save_btn.grid(row=0, column=0, padx=10, pady=5)
        update_btn = tk.Button(btn_frame, text="Export CSV",command=self.export_csv, width=15, font=("times new roman", 12, "bold"), bg="blue", fg="black")
        update_btn.grid(row=0, column=1, padx=10, pady=5)
        delete_btn = tk.Button(btn_frame, text="Update", width=15, font=("times new roman", 12, "bold"), bg="blue", fg="black")
        delete_btn.grid(row=0, column=2, padx=10, pady=5)
        reset_btn = tk.Button(btn_frame, text="Reset",command=self.reset_data, width=15, font=("times new roman", 12, "bold"), bg="blue", fg="black")
        reset_btn.grid(row=0, column=3, padx=10, pady=5)

           # right label frame
        Right_frame = tk.LabelFrame(main_frame, bd=2, bg="white", relief=tk.RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=680, y=10, width=660, height=580)

        table_frame = tk.Frame(Right_frame, bd=2, bg="white", relief=tk.RIDGE)
        table_frame.place(x=5, y=5, width=650, height=550)

        # scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=tk.VERTICAL)
        self.AttendanceReportTable = ttk.Treeview(table_frame, column=(
            "id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll No")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance Status")
        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)
        
        self.AttendanceReportTable.pack(fill=tk.BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)




        #-------------face data----------------
    def face_data(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", tk.END, values=i)
   #----------------import csv----------------

    def import_csv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.face_data(mydata)

            #--------export csv----------------
    def export_csv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Exported","Your data exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)



            #--------------gate_cursor----------
    def get_cursor(self,event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']

        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])




        #------------reset-----------
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


                

            

        

        




if __name__ == "__main__":
       root = tk.Tk()
       obj = Attendance(root)
       root.mainloop()
