from tkinter import *
from datetime import date

root = Tk()
root.title("Age Finder App")
root.geometry("400x400")

def CheckAge():
    today = date.today()
    print(today)
    year = int(inputField.get())
    age = today.year - year
    label["text"] = "You are " + str(age) + " years old."

inputField = Entry(root, width=20, font=("Arial, 22"), justify="center")
button = Button(root, text="Check Age", font=("Arial, 20"), command=CheckAge)
label = Label(root, text="????????", font=("Arial, 20"))

inputField.pack()
button.pack()
label.pack()

root.mainloop()
