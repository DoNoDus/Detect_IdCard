import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import img_to_text.convertText as ct
import threading
import time

# custom_font = ("Arial", 16, "bold")
# custom_font = ("Helvetica", 12, "italic")
# custom_font = ("Times New Roman", 14)

def tk_start():
    for widget in root.winfo_children():
        widget.destroy()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 1200
    window_height = 800
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
                profile, img , im2 = ct.start(path=file_path)
                for step in range(101):
                    time.sleep(0.01)  # Simulate some work being done
                    progress_var.set(step)  
                update_ui(profile)
                ct.show('original image', img)
                ct.show('Detection Text', im2)
                ct.destroy()
            except Exception as e:
                update_ui(f"Error: {str(e)}")
            finally:
                # Re-enable the Open File button when OCR is done
                open_file_button.config(state=tk.NORMAL)

        ocr_thread = threading.Thread(target=ocr_task)
        ocr_thread.start()

def update_ui(profile):
    custom_font = ("Times New Roman", 30)
    if isinstance(profile, list):
        label1.config(text=f"รหัสประจำตัวประชาชน : {profile[0]}", font=custom_font, anchor='w')
        label2.config(text=f"ชื่อ : {profile[1][0]} {profile[1][1]}", font=custom_font, anchor='w')
        label3.config(text=f"นามสกุล : {profile[1][2]}", font=custom_font, anchor='w')
        label4.config(text=f"Name : {profile[2][0]} {profile[2][1]}", font=custom_font, anchor='w')
        label5.config(text=f"Last Name : {profile[2][2]}", font=custom_font, anchor='w')
        label6.config(text=f"เกิดเมื่อวันที่ : {profile[3]}", font=custom_font, anchor='w')
        label7.config(text=f"Date of Birth : {profile[4]}", font=custom_font, anchor='w')
        label8.config(text=f"ที่อยู่ : {profile[5]}", font=custom_font, anchor='w')
        label9.config(text=f"ออกบัตรเมื่อวันที่ : {profile[6]}", font=custom_font, anchor='w')
        label10.config(text=f"Date of Issue : {profile[7]}", font=custom_font, anchor='w')
        label11.config(text=f"วันบัตรหมดอายุ : {profile[8]}", font=custom_font, anchor='w')
        label12.config(text=f"Date of Expiry : {profile[9]}", font=custom_font, anchor='w')
        label13.config(text=f"เจ้าหนักงานออกบัตร : {profile[10]}", font=custom_font, anchor='w')
    else:
        file_label.config(text=f"Error: {profile}", anchor='w')

root = tk.Tk()
root.title("Identification Card")
tk_start()
# Create buttons to open file and folder dialogs
open_file_button = tk.Button(root, text="Open File", command=run_ocr)
open_file_button.pack(pady=10)
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100, length=400)
progress_bar.pack(pady=10)
label1 = tk.Label(root, text="")
label1.pack(fill='x')
label2 = tk.Label(root, text="")
label2.pack(fill='x')
label3 = tk.Label(root, text="")
label3.pack(fill='x')
label4 = tk.Label(root, text="")
label4.pack(fill='x')
label5 = tk.Label(root, text="")
label5.pack(fill='x')
label6 = tk.Label(root, text="")
label6.pack(fill='x')
label7 = tk.Label(root, text="")
label7.pack(fill='x')
label8 = tk.Label(root, text="")
label8.pack(fill='x')
label9 = tk.Label(root, text="")
label9.pack(fill='x')
label10 = tk.Label(root, text="")
label10.pack(fill='x')
label11 = tk.Label(root, text="")
label11.pack(fill='x')
label12 = tk.Label(root, text="")
label12.pack(fill='x')
label13 = tk.Label(root, text="")
label13.pack(fill='x')
# Create labels to display selected file and folder paths
file_label = tk.Label(root, text="")
file_label.pack()
root.mainloop()