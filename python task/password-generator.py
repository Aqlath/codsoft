import tkinter as tk
from tkinter import messagebox
import random
import string 
#generating password
def pass_gen():
    try:
        length=int(entry_length.get())
        if length<4:
            messagebox.showerror("Error","password length must be atleast 4")
            return 
        #defining charecter
        lowercase=string.ascii_lowercase
        uppercase=string.ascii_uppercase
        numbers=string.digits if var_numbers.get() else ""
        symbol=string.punctuation if var_symbol.get() else ""

        all=lowercase + uppercase + numbers + symbol

        if len(all) < 4:
            messagebox.showerror("Error","password length must be atleast 4")
            return 
        
        #ensure atleast one of each selected type(if enabled)
        password=[
            random.choice(lowercase),
            random.choice(uppercase),
            random.choice(numbers) if numbers else random.choice(lowercase),
            random.choice(symbol) if symbol else random.choice(uppercase)
        ]
        password+=random.choices(all,k=length-4)
        random.shuffle(password)
        password=''.join(password)
        
        #display the entry
        entry_password.delete(0,tk.END)  #clear
        entry_password.insert(0,password)   #display new password
         
        check_strength(password)
    
    except ValueError:
        messagebox.showerror("Error","please enter the valid number")

#function for checking strength of the password
def check_strength(password):
    length=len(password)
    has_upper=any(c.isupper() for c in password)
    has_lower=any(c.islower() for c in password)
    has_num=any(c.isdigit() for c in password)
    has_symbol=any(c in string.punctuation for c in password)

    strength="weak"
    if length >=8 and has_lower and has_upper and has_num:
        strength="medium"
    if length >=12 and has_lower and has_upper and has_num and has_symbol:
        strength="strong"
    lbl_strength.config(text=f" strength = {strength}", fg='green' if strength=="strong" else "orange" if strength=="medium" else "red")

#copying password to clip board
def copy_clip():
    root.clipboard_clear()
    root.clipboard_append(entry_password.get())
    root.update()
    messagebox.showinfo("copied","password copied to clipboard")

root=tk.Tk()
root.title("PASSWORD GENERATOR")
root.geometry("450x300")
root.resizable(False,False)
tk.Label(root,text="Enter your password length").pack(pady=5)
entry_length=tk.Entry(root)
entry_length.pack(pady=5)
var_numbers=tk.BooleanVar(value=True)
var_symbol=tk.BooleanVar(value=True)
tk.Checkbutton(root,text="Include numbers",variable=var_numbers).pack()
tk.Checkbutton(root,text="Include symbol",variable=var_symbol).pack()
tk.Button(root,text='Generate Password',command=pass_gen).pack(pady=5)
entry_password=tk.Entry(root,width=40)
entry_password.pack(pady=5)
lbl_strength=tk.Label(root,text="strength" , fg="black")
lbl_strength.pack()
tk.Button(root,text="copy to clipboard",command=copy_clip).pack(pady=5)
root.mainloop()




