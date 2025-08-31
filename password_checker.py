import tkinter as tk
from tkinter import ttk
import string

def check_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in string.punctuation for c in password):
        strength += 1

    return strength

def update_strength(event=None):
    password = entry.get()
    strength = check_strength(password)
    
    if strength == 0:
        strength_label.config(text="Too Weak", foreground="red")
        progress['value'] = 20
    elif strength == 1:
        strength_label.config(text="Weak", foreground="orange")
        progress['value'] = 40
    elif strength == 2:
        strength_label.config(text="Medium", foreground="blue")
        progress['value'] = 60
    elif strength == 3:
        strength_label.config(text="Strong", foreground="green")
        progress['value'] = 80
    elif strength == 4:
        strength_label.config(text="Very Strong", foreground="darkgreen")
        progress['value'] = 100

def toggle_password():
    if entry.cget('show') == '':
        entry.config(show='*')
        toggle_btn.config(text="👁")
    else:
        entry.config(show='')
        toggle_btn.config(text="🙈")

# Main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")
root.config(bg="white")

# Title
title = tk.Label(root, text="Enter Password", font=("Arial", 14, "bold"), bg="white")
title.pack(pady=10)

# Frame for input with border
box_frame = tk.Frame(root, bg="white", highlightbackground="black", highlightthickness=1)
box_frame.pack(pady=10)

entry = tk.Entry(box_frame, font=("Arial", 14), width=20, show="*", bd=0, relief="flat")
entry.pack(side=tk.LEFT, padx=5, pady=5)

toggle_btn = tk.Button(box_frame, text="👁", command=toggle_password, font=("Arial", 12), relief="flat", bg="white")
toggle_btn.pack(side=tk.LEFT, padx=5)

# Strength Progress Bar (smaller + thinner)
progress = ttk.Progressbar(root, length=150, mode="determinate")
progress.pack(pady=10)

strength_label = tk.Label(root, text="", font=("Arial", 11, "bold"), bg="white")
strength_label.pack(pady=5)

# Bind entry event
entry.bind("<KeyRelease>", update_strength)

root.mainloop()
