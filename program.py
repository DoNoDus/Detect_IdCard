import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import img_to_text.convertText as ct
import threading
import time
import cv2

# custom_font = ("Arial", 16, "bold")
# custom_font = ("Helvetica", 30, "italic")
# custom_font = ("Times New Roman", 14)

def tk_start():
    for widget in root.winfo_children():
        widget.destroy()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 1000
    window_height = 850
    x_coordinate = (screen_width / 2) - (window_width / 2)
    y_coordinate = (screen_height / 2) - (window_height / 2)
    root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate - 100))

def run_ocr():
    file_path = filedialog.askopenfilename()
    if file_path:
        # Disable the Open File button while OCR is running
        open_file_button.config(state=tk.DISABLED)

        def ocr_task():
            try:
                profile, img , im2 ,thresh1= ct.start(path=file_path)

                h, w = im2.shape
                im2 = cv2.resize(im2, (int(w/1.5), int(h/1.5)))
                h, w = thresh1.shape
                thresh1 = cv2.resize(thresh1, (int(w/1.5), int(h/1.5)))

                for step in range(101):
                    time.sleep(0.01)  # Simulate some work being done
                    progress_var.set(step)  
                update_ui(profile)

                def imshow_1():
                    ct.show("Original image", img)
                def imshow_2():
                    ct.show("Text Detection image", im2)
                def imshow_3():
                    ct.show("Threshold image", thresh1)

                custom_font2 = ("Arial", 14, "bold")
                button1 = tk.Button(root, text="Original image", command=imshow_1, font=custom_font2)
                button2 = tk.Button(root, text="Text Detection image", command=imshow_2, font=custom_font2)
                button3 = tk.Button(root, text="Threshold image", command=imshow_3, font=custom_font2)
                # Use the grid geometry manager to place buttons in a single row
                button1.pack(fill='x')
                button2.pack(fill='x')
                button3.pack(fill='x')
            except Exception as e:
                update_ui(f"Error: {str(e)}")
            finally:
                # Re-enable the Open File button when OCR is done
                open_file_button.config(state=tk.NORMAL)

        ocr_thread = threading.Thread(target=ocr_task)
        ocr_thread.start()

def update_ui(profile):
    custom_font3 = ("Times New Roman", 24)
    if isinstance(profile, list):
        label1.config(text=f"รหัสประจำตัวประชาชน : {profile[0]}", font=custom_font3, anchor='w')
        label2.config(text=f"ชื่อ : {profile[1][0]} {profile[1][1]}",font=custom_font3, anchor='w')
        label3.config(text=f"นามสกุล : {profile[1][2]}",font=custom_font3, anchor='w')
        label4.config(text=f"Name : {profile[2][0]} {profile[2][1]}",font=custom_font3, anchor='w')
        label5.config(text=f"Last Name : {profile[2][2]}",font=custom_font3, anchor='w')
        label6.config(text=f"เกิดเมื่อวันที่ : {profile[3]}",font=custom_font3, anchor='w')
        label7.config(text=f"Date of Birth : {profile[4]}",font=custom_font3, anchor='w')
        label8.config(text=f"ที่อยู่ : {profile[5]}",font=custom_font3, anchor='w')
        label9.config(text=f"ออกบัตรเมื่อวันที่ : {profile[6]}",font=custom_font3, anchor='w')
        label10.config(text=f"Date of Issue : {profile[7]}",font=custom_font3, anchor='w')
        label11.config(text=f"วันบัตรหมดอายุ : {profile[8]}",font=custom_font3, anchor='w')
        label12.config(text=f"Date of Expiry : {profile[9]}",font=custom_font3, anchor='w')
        label13.config(text=f"เจ้าหนักงานออกบัตร : {profile[10]}",font=custom_font3, anchor='w')
    else:
        file_label.config(text=f"Error: {profile}")


root = tk.Tk()
root.title("Identification Card")
tk_start()
# Create buttons to open file and folder dialogs
custom_font1 = ("Helvetica", 26, "italic")
open_file_button = tk.Button(root, text="Open File", command=run_ocr , font=custom_font1)
open_file_button.pack(pady=2)

progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100, length=600)
progress_bar.pack(pady=2)

label1 = tk.Label(root, text="")
label1.pack(fill='x',pady=1,padx=10)
label2 = tk.Label(root, text="")
label2.pack(fill='x',pady=1,padx=10)
label3 = tk.Label(root, text="")
label3.pack(fill='x',pady=1,padx=10)
label4 = tk.Label(root, text="")
label4.pack(fill='x',pady=1,padx=10)
label5 = tk.Label(root, text="")
label5.pack(fill='x',pady=1,padx=10)
label6 = tk.Label(root, text="")
label6.pack(fill='x',pady=1,padx=10)
label7 = tk.Label(root, text="")
label7.pack(fill='x',pady=1,padx=10)
label8 = tk.Label(root, text="")
label8.pack(fill='x',pady=1,padx=10)
label9 = tk.Label(root, text="")
label9.pack(fill='x',pady=1,padx=10)
label10 = tk.Label(root, text="")
label10.pack(fill='x',pady=1,padx=10)
label11 = tk.Label(root, text="")
label11.pack(fill='x',pady=1,padx=10)
label12 = tk.Label(root, text="")
label12.pack(fill='x',pady=1,padx=10)
label13 = tk.Label(root, text="")
label13.pack(fill='x',pady=1,padx=10)

file_label = tk.Label(root, text="")
file_label.pack(fill='x')
root.mainloop()