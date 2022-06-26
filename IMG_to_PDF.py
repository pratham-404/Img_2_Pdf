# Import Module
from tkinter import *
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilenames
from os import startfile
import img2pdf

def select_file():
    global file_names
    file_names = askopenfilenames(initialdir="C:\\Users\\Pratham\\Desktop\\Image To PDF\\Images", title="Select Images")

# IMAGES TO PDF
def images_to_pdf():
    with open(f"file.pdf", "wb") as f:
        f.write(img2pdf.convert(file_names))
        startfile(f"file.pdf")

# Create Object
root = Tk()
# Setting Geometry
root.geometry('600x325')
root.maxsize(600,325)
root.minsize(600,325)
root.title("Converter")
root.configure(background='#1C1B29')

# Inserting an Image Canvas
canvas = Canvas(root, width=200, height=120, bg='#1C1B29', highlightthickness=0)
img = ImageTk.PhotoImage(file="icon.png")
canvas.create_image(100, 60, image=img)
canvas.pack()

# Add Labels and Buttons
Label(root, text="IMAGE to PDF Converter", font="Sans 20 bold", bg='#1C1B29', fg='white').pack(pady=10)

button1 = Button(root, text="Select Images", command=select_file, relief="solid", font=12, bg='#3b3a5f', fg='white')
button1.pack(pady=12, anchor=CENTER)

button2 = Button(root, text="Convert", command=images_to_pdf, relief="solid", font=12, bg='#3b3a5f', fg='white')
button2.pack(pady=12, anchor=CENTER)

# Execute Tkinter
root.mainloop()