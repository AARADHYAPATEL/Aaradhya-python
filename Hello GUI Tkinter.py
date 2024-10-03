from tkinter import *

root = Tk()
root.title("Hello GUI Tkinter")
root.geometry("400x400")

def ClickButton():
    if len(inputField.get()) == 0:
        labelOne["text"] = "Please enter a name!!"
    else:
        labelOne["text"] = "Hello " + inputField.get()

inputField = Entry(root, width=50, font=("Arial, 22"), bg="coral", fg="black", justify="center")
buttonOne = Button(root, text="Click Me", padx=50, pady=5, command=ClickButton, bg="gold", font=("Arial, 14"))
labelOne = Label(root, text="????????", font=("Arial, 14"), fg="purple", pady=20)

inputField.pack(pady=20)
buttonOne.pack(pady=10)
labelOne.pack()

root.mainloop()