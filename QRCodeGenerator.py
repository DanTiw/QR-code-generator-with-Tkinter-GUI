import qrcode
import tkinter as tk
from tkinter import filedialog 
from PIL import ImageTk, Image
from tkinter import *

def generate_qr_code():
    data = entry.get()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image = qr_image.resize((200, 200))  # Resize for display
    img = ImageTk.PhotoImage(qr_image)
    qr_label.config(image=img)
    qr_label.image = img

def save_qr_code():
    filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
    if filename:
        qr_image.save(filename)

# Create the main window
root = tk.Tk()
root.title("QR Code Generator")

# Create input entry
label1=Label(root,text="Enter URL")
entry = tk.Entry(root, width=30)
label1.pack()
entry.pack()

# Create the Generate button
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code)
generate_button.pack()

# Create the Save button
save_button = tk.Button(root, text="Save QR Code", command=save_qr_code)
save_button.pack()

# Create the label to display the QR code image
qr_label = tk.Label(root)
qr_label.pack(pady=10)

root.mainloop()
