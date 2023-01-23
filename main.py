import tkinter as tk
import tkinter.font as font
from record import record
from PIL import Image, ImageTk
from motion import find_motion
from stolen import find_stolen

window = tk.Tk()
window.title("Smart CCTV")
window.iconphoto(False, tk.PhotoImage(file='mn.png'))
window.geometry('1080x700')


frame1 = tk.Frame(window)

label_title = tk.Label(frame1, text="Smart cctv Camera")
label_font = font.Font(size=35, weight='bold',family='Helvetica')
label_title['font'] = label_font
label_title.grid(pady=(10,10), column=2)


icon = Image.open('icons/spy.png')
icon = icon.resize((150,150), Image.ANTIALIAS)
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon)
label_icon.grid(row=1, pady=(5,10), column=2)


btn1_image = Image.open('icons/exit.png')
btn1_image = btn1_image.resize((50,50), Image.ANTIALIAS)
btn1_image = ImageTk.PhotoImage(btn1_image)

btn2_image = Image.open('icons/security-camera.png')
btn2_image = btn2_image.resize((50,50), Image.ANTIALIAS)
btn2_image = ImageTk.PhotoImage(btn2_image)


btn3_image = Image.open('icons/rec.png')
btn3_image = btn3_image.resize((50,50), Image.ANTIALIAS)
btn3_image = ImageTk.PhotoImage(btn3_image)

btn4_image = Image.open('icons/lamp.png')
btn4_image = btn4_image.resize((50,50), Image.ANTIALIAS)
btn4_image = ImageTk.PhotoImage(btn4_image)



# --------------- Button -------------------#
btn_font = font.Font(size=25)
btn1 = tk.Button(frame1, height=90, width=180, fg='red', command=window.quit, image=btn1_image)
btn1['font'] = btn_font
btn1.grid(row=6, pady=(20,10), column=2)

btn_font = font.Font(size=25)
btn2 = tk.Button(frame1, text='Motion', height=90, width=180, fg='green', command=find_motion, image=btn2_image, compound='left')
btn2['font'] = btn_font
btn2.grid(row=5, pady=(20,10))

btn3 = tk.Button(frame1, text='Record', height=90, width=180, fg='orange', command=record, image=btn3_image, compound='left')
btn3['font'] = btn_font
btn3.grid(row=5, pady=(20,10), column=3)

btn4 = tk.Button(frame1, text='Monitor', height=90, width=180, fg='green', command=find_stolen, image=btn4_image, compound='left')
btn4['font'] = btn_font
btn4.grid(row=5, pady=(20,10), column=2)




frame1.pack()
window.mainloop()


