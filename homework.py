import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("ATM PIN Setup")
root.geometry("500x580")
root.resizable(False, False)
root.configure(bg="#e8edf2")
title = tk.Label(
    root,
    text="ATM PIN SETUP",
    font=("Arial", 20, "bold"),
    bg="#17365d",
    fg="white",
    pady=12
)
title.pack(fill="x")
account_frame = tk.LabelFrame(
    root,
    text="Account Details",
    font=("Arial", 11, "bold"),
    relief=tk.RAISED,
    bd=4,
    padx=10,
    pady=10
)
account_frame.place(x=30, y=75, width=440, height=155)
tk.Label(account_frame, text="Account Number:").place(x=10, y=15)
account_entry = tk.Entry(account_frame, width=28)
account_entry.place(x=150, y=15)
tk.Label(account_frame, text="Account Holder:").place(x=10, y=50)
name_entry = tk.Entry(account_frame, width=28)
name_entry.place(x=150, y=50)
tk.Label(account_frame, text="Set 4-digit PIN:").place(x=10, y=85)
pin_entry = tk.Entry(account_frame, width=28, show="*")
pin_entry.place(x=150, y=85)
keypad_frame = tk.LabelFrame(
    root,
    text="Numeric Keypad",
    font=("Arial", 11, "bold"),
    relief=tk.SUNKEN,
    bd=4,
    padx=10,
    pady=10
)
keypad_frame.place(x=65, y=245, width=370, height=190)
def add_digit(digit):
    pin_entry.insert(tk.END, digit)
def clear_pin():
    pin_entry.delete(0, tk.END)
def delete_digit():
    current = pin_entry.get()
    if current:
        pin_entry.delete(len(current) - 1, tk.END)
digits = [
    ("1", 0, 0), ("2", 0, 1), ("3", 0, 2),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2),
    ("Clear", 3, 0), ("0", 3, 1), ("Delete", 3, 2)
]
for text, row, col in digits:
    if text == "Clear":
        command = clear_pin
    elif text == "Delete":
        command = delete_digit
    else:
        command = lambda digit=text: add_digit(digit)
    tk.Button(
        keypad_frame,
        text=text,
        width=9,
        height=1,
        font=("Arial", 10, "bold"),
        command=command
    ).grid(row=row, column=col, padx=7, pady=3)
output_frame = tk.LabelFrame(
    root,
    text="Setup Summary",
    font=("Arial", 10, "bold"),
    relief=tk.RAISED,
    bd=3
)
output_frame.place(x=30, y=445, width=440, height=95)
output_text = tk.Text(output_frame, width=48, height=3, font=("Arial", 9))
output_text.place(x=8, y=5)
def setup_pin():
    account = account_entry.get().strip()
    name = name_entry.get().strip()
    pin = pin_entry.get()
    if not account or not name or not pin:
        messagebox.showwarning(
            "Missing Details",
            "Please enter all account details and a PIN."
        )
        return
    if not pin.isdigit() or len(pin) != 4:
        messagebox.showerror(
            "Invalid PIN",
            "The PIN must contain exactly 4 digits."
        )
        return
    output_text.delete("1.0", tk.END)
    output_text.insert(
        tk.END,
        f"Account: {account}\n"
        f"Holder: {name}\n"
        "PIN setup completed successfully."
    )
    messagebox.showinfo("Success", "Your PIN has been set up!")
tk.Button(
    root,
    text="SET UP PIN",
    font=("Arial", 12, "bold"),
    bg="#17365d",
    fg="white",
    activebackground="#285a8e",
    command=setup_pin
).place(x=175, y=545, width=150, height=30)
root.mainloop()