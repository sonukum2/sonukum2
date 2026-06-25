


import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
class student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("student details")

        #==============varibales=================
        self.var_dep = tk.StringVar()
        self.var_course = tk.StringVar()
        self.var_year = tk.StringVar()
        self.var_semester = tk.StringVar()
        self.var_std_id = tk.StringVar()
        self.var_std_name = tk.StringVar()
        self.var_std_roll = tk.StringVar()
        self.var_std_div = tk.StringVar()
        self.var_std_gender = tk.StringVar()
        self.var_std_dob = tk.StringVar()
        self.var_std_email = tk.StringVar()
        self.var_std_phone = tk.StringVar()
        self.var_std_address = tk.StringVar()
        self.var_std_teacher = tk.StringVar()
        

      # first image
        img = Image.open("collage_image/MONU1.jpg")
        img = img.resize((530, 390), Image.Resampling.LANCZOS)

        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = tk.Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=530, height=390)

        # second image
        img1 = Image.open("collage_image/download.jpeg")
        img1 = img1.resize((530, 390), Image.Resampling.LANCZOS)

        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = tk.Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=530, y=0, width=530, height=390)

        # third image
        img2 = Image.open("collage_image/images.jpeg")
        img2 = img2.resize((530, 390), Image.Resampling.LANCZOS)

        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl2 = tk.Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=1060, y=0, width=530, height=390)

        
       # bg image
        img3 = Image.open("collage_image/images (1).jpeg")
        img3 = img3.resize((1590, 790), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = tk.Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=390, width=1590, height=790)


        title_lbl = tk.Label(bg_img, text=" STUDENT MANAGEMENT SYSTEM ", font=(
            "times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1590, height=45)

        main_frame = tk.Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=5, y=55, width=1500, height=700)

       #left label frame
        Left_frame = tk.LabelFrame(main_frame, bd=2, bg="black",fg="white", relief=tk.RIDGE, text="Student Details", font=(
            "times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=750, height=680)

        img_left = Image.open("collage_image/images.jpeg")
        img_left = img_left.resize((740, 140), Image.Resampling.LANCZOS)

        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl_left = tk.Label(Left_frame, image=self.photoimg_left)
        f_lbl_left.place(x=10, y=10, width=740, height=140)

#current course
        current_course_Left_frame = tk.LabelFrame(main_frame, bd=2, bg="black",fg="white", relief=tk.RIDGE, text="Student Details", font=(
            "times new roman", 12, "bold"))
        current_course_Left_frame.place(x=10, y=160, width=750, height=530)

    #department

        dep_label = tk.Label(current_course_Left_frame, text="Department", font=(
            "times new roman", 12, "bold"), bg="red", fg="white")
        dep_label.grid(row=0, column=0, padx=10, pady=5)
        dep_combo = ttk.Combobox(current_course_Left_frame,textvariable=self.var_dep, font=(
            "times new roman", 12, "bold"), state="readonly")
        dep_combo["values"] = ("Select Department", "Computer Science", "Information Technology", "Civil", "Mechanical", "Electrical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=10, pady=5)

        #course
        course_label = tk.Label(current_course_Left_frame, text="Course", font=(
            "times new roman", 12, "bold"), bg="red", fg="white")
        course_label.grid(row=0, column=2, padx=10, pady=5, sticky=tk.W)
        course_combo = ttk.Combobox(current_course_Left_frame,textvariable=self.var_course, font=(
            "times new roman", 12, "bold"), state="readonly")
        course_combo["values"] = ("Select Course", "B.Tech", "M.Tech", "BCA", "MCA", "MBA")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=10, pady=5 ,sticky=tk.W)

        #year
        year_label = tk.Label(current_course_Left_frame, text="Year", font=(
            "times new roman", 12, "bold"), bg="red", fg="white")
        year_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        year_combo = ttk.Combobox(current_course_Left_frame,textvariable=self.var_year, font=(
            "times new roman", 12, "bold"), state="readonly")
        year_combo["values"] = ("Select Year", "2020-2024", "2021-2025", "2022-2026", "2023-2027")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
         
         #semester
        semester_label = tk.Label(current_course_Left_frame, text="Semester", font=(
            "times new roman", 12, "bold"), bg="red", fg="white")
        semester_label.grid(row=1, column=2, padx=10, pady=5, sticky=tk.W)
        semester_combo = ttk.Combobox(current_course_Left_frame,textvariable=self.var_semester, font=(
            "times new roman", 12, "bold"), state="readonly")
        semester_combo["values"] = ("Select Semester", "Semester 1", "Semester 2", "Semester 3", "Semester 4", "Semester 5", "Semester 6", "Semester 7", "Semester 8")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=10, pady=5, sticky=tk.W)


        #class student information
        current_course_Left_frame = tk.LabelFrame(main_frame, bd=2, bg="black",fg="white", relief=tk.RIDGE, text="Class Student Information", font=(
            "times new roman", 12, "bold"))
        current_course_Left_frame.place(x=10, y=260, width=750, height=530)

   #student id

        studentid_label = tk.Label(current_course_Left_frame, text="Student ID", font=(
            "times new roman", 12, "bold"), bg="red", fg="white")
        studentid_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        studentid_entry = tk.Entry(current_course_Left_frame,textvariable=self.var_std_id, font=(
            "times new roman", 12, "bold"))
        studentid_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

        # student name
        studentname_label = tk.Label(current_course_Left_frame, text="Student Name", font=(
            "times new roman", 12, "bold"), bg="red", fg="white")
        studentname_label.grid(row=0, column=2, padx=10, pady=5, sticky=tk.W)
        studentname_entry = tk.Entry(current_course_Left_frame,textvariable=self.var_std_name, font=(
            "times new roman", 12, "bold"))
        studentname_entry.grid(row=0, column=3, padx=10, pady=5, sticky=tk.W)

        # roll no
        rollno_label = tk.Label(current_course_Left_frame, text="Roll No", font=(
            "times new roman", 12, "bold"), bg="red", fg="white")
        rollno_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        rollno_entry = tk.Entry(current_course_Left_frame,textvariable=self.var_std_roll, font=(
            "times new roman", 12, "bold"))
        rollno_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        #class division
        class_div_label = tk.Label(current_course_Left_frame, text="Class Division", font=(
            "times new roman", 12, "bold"), bg="red", fg="white")
        class_div_label.grid(row=1, column=2, padx=10, pady=5, sticky=tk.W)
        class_div_combo = ttk.Combobox(current_course_Left_frame,textvariable=self.var_std_div, font=(
            "times new roman", 12, "bold"), state="readonly")
        class_div_combo["values"] = ("Select Division", "A", "B", "C", "D")
        class_div_combo.current(0)
        class_div_combo.grid(row=1, column=3, padx=10, pady=5, sticky=tk.W)

         #gender
        gender_label = tk.Label(current_course_Left_frame, text="Gender", font=(
            "times new roman", 12, "bold"), bg="red", fg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        gender_combo = ttk.Combobox(current_course_Left_frame,textvariable=self.var_std_gender, font=(
            "times new roman", 12, "bold"), state="readonly")
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

         #dob
        dob_label = tk.Label(current_course_Left_frame, text="DOB", font=(
            "times new roman", 12, "bold"), bg="red", fg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=tk.W)
        dob_entry = tk.Entry(current_course_Left_frame,textvariable=self.var_std_dob, font=(
            "times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=tk.W)

        #email
        email_label = tk.Label(current_course_Left_frame, text="Email", font=(
            "times new roman", 12, "bold"), bg="red", fg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        email_entry = tk.Entry(current_course_Left_frame,textvariable=self.var_std_email, font=(
            "times new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)

            #phone no
        phone_label = tk.Label(current_course_Left_frame, text="Phone No", font=(
            "times new roman", 12, "bold"), bg="red", fg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=tk.W)
        phone_entry = tk.Entry(current_course_Left_frame,textvariable=self.var_std_phone, font=(
            "times new roman", 12, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=tk.W)

        #address
        address_label = tk.Label(current_course_Left_frame, text="Address", font=(
            "times new roman", 12, "bold"), bg="red", fg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
        address_entry = tk.Entry(current_course_Left_frame,textvariable=self.var_std_address, font=(
            "times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)

         #teacher name
        teacher_label = tk.Label(current_course_Left_frame, text="Teacher Name", font=(
            "times new roman", 13, "bold"), bg="red", fg="white")
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=tk.W)
        teacher_entry = tk.Entry(current_course_Left_frame,textvariable=self.var_std_teacher, font=(
            "times new roman", 13, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=tk.W)
       
       
        #redio buttons
        var = tk.IntVar()
        yes = tk.IntVar()
        self.var_radio1 = tk.StringVar()

        
        radiobtn1 = tk.Radiobutton(current_course_Left_frame,variable=self.var_radio1, text="Take Photo Sample", value="yes")
        radiobtn1.grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)
        radiobtn2 = tk.Radiobutton(current_course_Left_frame,variable=self.var_radio1,text="No Photo Sample", value="No")
        radiobtn2.grid(row=6, column=1, padx=10, pady=5, sticky=tk.W)

        #buttons frame
        btn_frame = tk.Frame(current_course_Left_frame, bd=2, relief=tk.RIDGE, bg="white")
        btn_frame.place(x=0, y=220, width=870, height=103)
        
        
        save_btn = tk.Button(btn_frame, text="Save",command=self.add_data, font=(
            "times new roman", 12, "bold"), bg="blue", fg="black", width=17)
        save_btn.grid(row=0, column=0, padx=10, pady=10)
        update_btn = tk.Button(btn_frame, text="Update", command=self.update_data, font=(
            "times new roman", 12, "bold"), bg="blue", fg="black", width=17)
        update_btn.grid(row=0, column=1, padx=10, pady=10)
        delete_btn = tk.Button(btn_frame, text="Delete", command=self.delete_data, font=(
            "times new roman", 12, "bold"), bg="blue", fg="black", width=17)
        delete_btn.grid(row=0, column=2, padx=10, pady=10)
        reset_btn = tk.Button(btn_frame, text="Reset", command=self.reset_data, font=(
            "times new roman", 12, "bold"), bg="blue", fg="black", width=17)
        reset_btn.grid(row=0, column=3, padx=10, pady=10)





        take_photo_btn = tk.Button(btn_frame, text="Take Photo Sample",command=self.generate_dataset, font=(
            "times new roman", 12, "bold"), bg="blue", fg="black", width=17)
        take_photo_btn.grid(row=1, column=0, padx=10, pady=10)

        update_photo_btn = tk.Button(btn_frame, text="Update Photo Sample",  font=(
            "times new roman", 12, "bold"), bg="blue", fg="black", width=17)
        update_photo_btn.grid(row=1, column=1, padx=10, pady=10)

        



         #right label frame
        Right_frame = tk.LabelFrame(main_frame, bd=2, bg="black",fg="white", relief=tk.RIDGE, text="Student Details", font=(
            "times new roman", 12, "bold"))
        Right_frame.place(x=760, y=10, width=750, height=680)
        img_right = Image.open("collage_image/images.jpeg")
        img_right = img_right.resize((740, 140), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lbl_right = tk.Label(Right_frame, image=self.photoimg_right)
        f_lbl_right.place(x=10, y=10, width=740, height=135)


      
    

        
  
        
       
       
        #===========search system===========
        search_frame = tk.LabelFrame(Right_frame, bd=2, bg="black",fg="white", relief=tk.RIDGE, text="Search System", font=(
            "times new roman", 12, "bold"))
        search_frame.place(x=5, y=135, width=730, height=70)

        search_label = tk.Label(search_frame, text="Search By:", font=(
            "times new roman", 12, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=6, sticky=tk.W)
        search_combo = ttk.Combobox(search_frame, font=(
            "times new roman", 12, "bold"), state="readonly", width=15)
        search_combo["values"] = ("Select", "Roll No", "Phone No", "Student ID")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=10, pady=6, sticky=tk.W)
        search_entry = tk.Entry(search_frame, font=(
            "times new roman", 12, "bold"), width=20)
        search_entry.grid(row=0, column=2, padx=10, pady=6, sticky=tk.W)
        search_btn = tk.Button(search_frame, text="Search", font=(
            "times new roman", 12, "bold"), bg="blue", fg="black", width=10)
        search_btn.grid(row=0, column=3, padx=10, pady=6)
        showall_btn = tk.Button(search_frame, text="Show All", font=(
            "times new roman", 12, "bold"), bg="blue", fg="black", width=10)
        showall_btn.grid(row=0, column=4, padx=10, pady=6)
          
          
           #table frame
        table_frame = tk.Frame(Right_frame, bd=2, bg="black", relief=tk.RIDGE)
        table_frame.place(x=5, y=205, width=730, height=370)
        scroll_x = tk.Scrollbar(table_frame, orient=tk.HORIZONTAL)
        scroll_y = tk.Scrollbar(table_frame, orient=tk.VERTICAL)
        self.student_table = ttk.Treeview(table_frame, columns=("dep", "course", "year", "sem", "id", "name", "roll", "div", "gender", "dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Student Name")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("div", text="Class Division")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone No")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher Name")
        self.student_table.heading("photo", text="Photo Sample Status")
        self.student_table["show"] = "headings"
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)
        self.student_table.pack(fill=tk.BOTH, expand=1)
        self.root.bind("<Button-1>", self.get_cursor)

        self.fetch_data()

        

        
          




       #=================function declaration=================
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Sonu@123", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student (dep, course, year, semester,student_id, name, roll, division,gender, dob, email, phone,address, teacher, photo)values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (



                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_std_roll.get(),
                    self.var_std_div.get(),
                    self.var_std_gender.get(),
                    self.var_std_dob.get(),
                    self.var_std_email.get(),
                    self.var_std_phone.get(),
                    self.var_std_address.get(),
                    self.var_std_teacher.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Error adding student details: {e}", parent=self.root)
   

         #=================fetch data=================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Sonu@123", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", tk.END, values=i)
           
        conn.close()
            

          #=================get cursor=================
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        if not data:
            return
        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_std_roll.set(data[6])
        self.var_std_div.set(data[7])
        self.var_std_gender.set(data[8])
        self.var_std_dob.set(data[9])
        self.var_std_email.set(data[10])
        self.var_std_phone.set(data[11])
        self.var_std_address.set(data[12])
        self.var_std_teacher.set(data[13])
        self.var_radio1.set(data[14])
         #==================update function=================
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update this student details?", parent=self.root)
                if update :
                    conn = mysql.connector.connect(host="localhost", username="root", password="Sonu@123", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set dep=%s, course=%s, year=%s, semester=%s, name=%s, roll=%s, division=%s, gender=%s, dob=%s, email=%s, phone=%s, address=%s, teacher=%s, photo=%s where student_id=%s", (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_std_roll.get(),
                        self.var_std_div.get(),
                        self.var_std_gender.get(),
                        self.var_std_dob.get(),
                        self.var_std_email.get(),
                        self.var_std_phone.get(),
                        self.var_std_address.get(),
                        self.var_std_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Update", "Successfully updated student details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root) 
    
         #=================delete function=================
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student Id is required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to delete this student details?", parent=self.root)
                if delete :
                    conn = mysql.connector.connect(host="localhost", username="root", password="Sonu@123", database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from student where student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                    
                    conn.commit()
                    conn.close()
                    self.fetch_data()
                    messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
                #=================reset function=================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_std_roll.set("")
        self.var_std_div.set("Select Division")
        self.var_std_gender.set("Select Gender")
        self.var_std_dob.set("")
        self.var_std_email.set("")
        self.var_std_phone.set("")
        self.var_std_address.set("")
        self.var_std_teacher.set("")
        self.var_radio1.set("")


       #=================generate data set or take photo sample=================
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Sonu@123", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student where student_id=%s", (self.var_std_id.get(),))
                result = my_cursor.fetchone()
                id = result[4]
                name = result[5]
                my_cursor.execute("update student set dep=%s, course=%s, year=%s, semester=%s, name=%s, roll=%s, division=%s, gender=%s, dob=%s, email=%s, phone=%s, address=%s, teacher=%s, photo=%s where student_id=%s", (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_std_roll.get(),
                        self.var_std_div.get(),
                        self.var_std_gender.get(),
                        self.var_std_dob.get(),
                        self.var_std_email.get(),
                        self.var_std_phone.get(),
                        self.var_std_address.get(),
                        self.var_std_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))
                conn.commit()
                self.fetch_data()
                conn.close()



                #load predefined data on face frontals from opencv
                faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = faceCascade.detectMultiScale(gray, 1.3, 5)
                    #scaling factor=1.3
                    #minimum neighbor=5

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (750, 750))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data set completed!!!", parent=self.root)
                
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
                    
                
                  
if __name__ == "__main__":
    root = tk.Tk()
    obj = student(root)
    root.mainloop()
