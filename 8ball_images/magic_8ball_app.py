from tkinter import *
import random
from tkinter import messagebox
import os
from PIL import Image, ImageTk

root = Tk()
root.title("Magic 8 Ball")
root.geometry("610x510")

# Variables
magic_8_ball_images = []
folder_dir = "C:\\Users\\Admin\\Documents\\GitHub\\Aaradhya-python\\PythonPractice\\8ball_images\\"

# events and functions
for images in os.listdir(folder_dir):
    if images.endswith(".jpg"):
        image = ImageTk.PhotoImage(Image.open(folder_dir + "/" + images).resize((400, 350)))
        magic_8_ball_images.append(image)

print("total image available", len(magic_8_ball_images))

# Adding the event

def AskQuestion(event):
    if len(inputBox.get()) == 0:
        messagebox.showinfo("Jetbrains says: ", " Enter a question first")
    else:
        ShowAnswer()

def ShowAnswer():
    num = random.randint(0, len(magic_8_ball_images) - 1)
    image_label.config(image=magic_8_ball_images[num])
    inputBox.delete(0, "end")

# GUI components
image_label = Label(root, image=magic_8_ball_images[0])
inputBox = Entry(root, width=30, font=("Arial 18 bold"), fg="maroon", bg="yellow", justify="center")
click_button = Button(root, text="Ask the question", font=("Arial 18 bold"), bg="plum")

# pack the GUI
image_label.pack()
inputBox.pack(pady=10)
click_button.pack(side="bottom", pady=30)

click_button.bind("<Button-1>", AskQuestion)
inputBox.bind("<Return>", AskQuestion)

root.mainloop()