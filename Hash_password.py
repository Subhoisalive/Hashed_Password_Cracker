import hashlib
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

# ---------------------- PASSWORD CRACK FUNCTION ----------------------
def crack_password():
    hash_input = hash_entry.get().strip()
    algorithm = algo_var.get()

    if not hash_input or algorithm == "Select":
        messagebox.showwarning("Input Error", "Please enter a hash and select an algorithm.")
        return

    try:
        with open("rockyou.txt", "r", encoding="latin-1") as f:
            for line in f:
                password = line.strip()

                if algorithm == "MD5":
                    hashed = hashlib.md5(password.encode()).hexdigest()
                elif algorithm == "SHA1":
                    hashed = hashlib.sha1(password.encode()).hexdigest()
                elif algorithm == "SHA256":
                    hashed = hashlib.sha256(password.encode()).hexdigest()
                else:
                    messagebox.showerror("Error", "Unsupported algorithm selected.")
                    return

                status_label.config(text=f"🧪 Trying: {password}")
                window.update_idletasks()

                if hashed == hash_input:
                    result_label.config(text=f"✅ Password Found: {password}", fg="#00FF00")
                    return

        result_label.config(text="❌ Password not found in wordlist.", fg="#FF5555")

    except FileNotFoundError:
        messagebox.showerror("File Error", "rockyou.txt not found in the script folder!")

# ---------------------- GUI SETUP ----------------------
window = tk.Tk()
window.title("🚀 Hashed Password Cracker by Suvhankar")
window.geometry("600x400")
window.configure(bg="#1f1f1f")
window.resizable(False, False)

# Fonts & Colors
font_title = ("Orbitron", 18, "bold")
font_text = ("Segoe UI", 11)
font_result = ("Consolas", 12, "bold")
accent_color = "#00FFCC"

# Title
tk.Label(window, text="🔐 Hashed Password Cracker by Suvhankar", font=font_title, bg="#1f1f1f", fg=accent_color).pack(pady=20)

# Hash Input
tk.Label(window, text="Enter Hashed Password:", font=font_text, bg="#1f1f1f", fg="white").pack()
hash_entry = tk.Entry(window, width=60, font=font_text, bg="#333", fg="#00FFCC", insertbackground="#00FFCC")
hash_entry.pack(pady=8)

# Algorithm Dropdown
tk.Label(window, text="Select Hashing Algorithm:", font=font_text, bg="#1f1f1f", fg="white").pack()
algo_var = tk.StringVar()
algo_var.set("Select")
algo_menu = tk.OptionMenu(window, algo_var, "MD5", "SHA1", "SHA256")
algo_menu.config(font=font_text, bg="#2e2e2e", fg=accent_color, activebackground="#00FFCC", activeforeground="black")
algo_menu.pack(pady=5)

# Crack Button
crack_button = tk.Button(window, text="🔍 Crack Password", font=("Orbitron", 12), bg=accent_color, fg="black", command=crack_password)
crack_button.pack(pady=20)

# Result Label
result_label = tk.Label(window, text="", font=font_result, bg="#1f1f1f")
result_label.pack(pady=10)

# Status Label
status_label = tk.Label(window, text="", font=("Segoe UI", 10), fg="#888", bg="#1f1f1f")
status_label.pack(side="bottom", pady=5)

window.mainloop()
