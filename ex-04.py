import tkinter as tk 
from tkinter import messagebox

#function to handle form submission
def submit():
    name = name_entry.get()
    gender = gender_var.get()
    hobbies  =[]
    if hobby1_var.get():
        hobbies.append("Dancing")
    if hobby2_var.get():
        hobbies.append("Singing")
    if hobby3_var.get():
        hobbies.append("Travelling")
    hobbies_text = ", ".join(hobbies) if hobbies else "None"
    messagebox.showinfo("Form Submitted", f"Name : {name} \n Gender : {gender} \n Hobbies : {hobbies_text}")

#function to show a custom dialog
def show_custom_dialogue():
    top = tk.Toplevel(root)
    top.title("Custom Dialogue")
    top.geometry("250x150")

    tk.Label(top, text="This is a custom dialog!").pack(pady=10)
    tk.Button(top, text="OK", command=top.destroy).pack(pady=10)

#main window
root = tk.Tk()
root.title("My Tkinter Application")
root.geometry("500x500")

#label
tk.Label(root, text="Enter Name: ").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

#Radio Buttons for Gender
tk.Label(root, text="Select gender: ").pack(pady=5)
gender_var = tk.StringVar(value='None')
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()

#Checkboxes for Hobbies
tk.Label(root, text="Select Hobbies: ").pack(pady = 5)
hobby1_var = tk.BooleanVar()
hobby2_var = tk.BooleanVar()
hobby3_var = tk.BooleanVar()

tk.Checkbutton(root, text="Dancing", variable=hobby1_var).pack()
tk.Checkbutton(root, text="Singing", variable=hobby2_var).pack()
tk.Checkbutton(root, text="Travelling", variable=hobby3_var).pack()

#submit button
tk.Button(root, text="Submit", command=submit).pack(pady=10)

#custom dialogue box
tk.Button(root, text="Open Custom Dialog", command = show_custom_dialogue).pack(pady=10)
root.mainloop()