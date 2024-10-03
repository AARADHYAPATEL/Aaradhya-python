from tkinter import *

root = Tk()
root.title("Python Clicker App")
root.geometry("400x400")

number = 0

# Add the button function here
def ClickButton():
    global number
    number += 1
    ShowInfo["text"] = "You clicked " + str(number) + " times."

ClickingButton = Button(root, text="Click Me!", padx = 50, pady = 50, bg="blue", font=("Arial, 22"), command=ClickButton)
ShowInfo = Label(root, text="Click the button to increase the number", font=("Arial, 20"), fg="purple", pady=20)

ClickingButton.pack()
ShowInfo.pack()

root.mainloop()