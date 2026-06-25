
from datetime import datetime
from time import strftime
import os
import numpy as np
import cv2
import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector


class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1590x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = tk.Label(
            self.root,
            text="FACE RECOGNITION",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="green"
        )
        title_lbl.place(x=0, y=0, width=1590, height=40)

        base_dir = os.path.dirname(os.path.abspath(__file__))

        # Left Image
        try:
            img_top = Image.open(
                os.path.join(base_dir, "collage_image/images (4).jpeg")
            )
            img_top = img_top.resize((650, 700), Image.Resampling.LANCZOS)
            self.photoimg_top = ImageTk.PhotoImage(img_top)

            tk.Label(self.root, image=self.photoimg_top).place(
                x=0, y=40, width=650, height=750
            )
        except Exception as e:
            print("Top image error:", e)

        # Right Image
        try:
            img_bottom = Image.open(
                os.path.join(
                    base_dir,
                    "collage_image/facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-orig.webp"
                )
            )
            img_bottom = img_bottom.resize((950, 700), Image.Resampling.LANCZOS)
            self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

            tk.Label(self.root, image=self.photoimg_bottom).place(
                x=650, y=40, width=950, height=750
            )
        except Exception as e:
            print("Bottom image error:", e)

        # Button
        tk.Button(
            self.root,
            text="Face Recognition",
            command=self.face_recog,
            font=("times new roman", 18, "bold"),
            bg="green",
            fg="white"
        ).place(x=1015, y=680, width=200, height=40)



        # ================== ATTENDANCE ==================
    def mark_attendance(self, i, r, n, d):
        with open("kiran.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split(",")
                nameList.append(entry[0])
            if(i not in nameList) and (r not in nameList) and (n not in nameList) and (d not in nameList):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{d1},{dtString},Present")
                 

    # ================= FACE RECOGNITION =================
    def face_recog(self):

        def draw_boundary(img, classifier, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, 1.1, 10)

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

                id, pred = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int(100 * (1 - pred / 300))

                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Sonu@123",
                    database="face_recognizer"
                )

                my_cursor = conn.cursor()

                # Correct SQL Queries
                my_cursor.execute(
                    "SELECT Name, Roll, Dep FROM student WHERE student_id=%s",
                    (id,)
                )

                result = my_cursor.fetchone()

                if result:
                    n, r, d = result
                else:
                    n, r, d = "Unknown", "Unknown", "Unknown"
               
                my_cursor.execute("select student_id from student where student_id=%s", (id,))
                i = my_cursor.fetchone()
                i = str(i[0]) if i else "Unknown"


                conn.close()

                if confidence > 77:
                    cv2.putText(
                        img,
                        f"Name: {n}",
                        (x, y - 75),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (255, 255, 255),
                        2
                    )

                    cv2.putText(img,f"id: {i}",(x, y - 55),
                        cv2.FONT_HERSHEY_SIMPLEX,0.8, (255, 255, 255), 2
                    )

                    cv2.putText(
                        img,
                        f"Roll: {r}",
                        (x, y - 30),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (255, 255, 255),
                        2
                    )

                    cv2.putText(
                        img,
                        f"Department: {d}",
                        (x, y - 5),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (255, 255, 255),
                        2
                    )
                    self.mark_attendance(i, r, n, d)
                else:
                    cv2.rectangle(
                        img,
                        (x, y),
                        (x + w, y + h),
                        (0, 0, 255),
                        3
                    )

                    cv2.putText(
                        img,
                        "Unknown Face",
                        (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (255, 255, 255),
                        2
                    )

            return img

        # Haarcascade file path
        cascade_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "haarcascade_frontalface_default.xml"
        )

        faceCascade = cv2.CascadeClassifier(cascade_path)

        # Load trained classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        # Start Camera
        video_capture = cv2.VideoCapture(0)

        while True:
            ret, img = video_capture.read()

            if not ret:
                break

            img = draw_boundary(img, faceCascade, clf)

            cv2.imshow("Face Recognition", img)

            # Press ENTER to close
            if cv2.waitKey(1) == 13:
                break

        video_capture.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = tk.Tk()
    app = FaceRecognition(root)
    root.mainloop()
