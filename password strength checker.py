import re
import tkinter as tk
from tkinter import messagebox

# -----------------------------
# Common weak passwords
# -----------------------------
COMMON_PASSWORDS = ["123456", "password", "123456789", "qwerty", "abc123"]


# -----------------------------
# Check password strength
# -----------------------------
def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*]", password):
        score += 1

    if password in COMMON_PASSWORDS:
        return "Very Weak ❌", "red"

    if score <= 2:
        return "Weak ❌", "red"
    elif score <= 4:
        return "Medium ⚠️", "orange"
    else:
        return "Strong ✅", "green"


# -----------------------------
# Suggestions for improvement
# -----------------------------
def get_suggestions(password):
    tips = []

    if len(password) < 8:
        tips.append("• Use at least 8 characters")
    if not re.search(r"[A-Z]", password):
        tips.append("• Add an uppercase letter")
    if not re.search(r"[a-z]", password):
        tips.append("• Add a lowercase letter")
    if not re.search(r"\d", password):
        tips.append("• Include a number")
    if not re.search(r"[!@#$%^&*]", password):
        tips.append("• Add a special character")

    return tips


# -----------------------------
# Button action
# -----------------------------
def analyze_password():
    password = password_entry.get()

    if not password:
        messagebox.showwarning("Input Error", "Please enter a password")
        return

    strength, color = check_strength(password)
    result_label.config(text=f"Strength: {strength}", fg=color)

    tips = get_suggestions(password)

    suggestions_box.delete("1.0", tk.END)

    if tips:
        for tip in tips:
            suggestions_box.insert(tk.END, tip + "\n")
    else:
        suggestions_box.insert(tk.END, "✅ Strong password! Good job!")


# -----------------------------
# Toggle show/hide password
# -----------------------------
def toggle_password():
    if show_password.get():
        password_entry.config(show="")   # show text
    else:
        password_entry.config(show="*")  # hide text


# -----------------------------
# UI Setup
# -----------------------------
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("420x450")
root.configure(bg="#1e1e2f")

# Title
tk.Label(root,
         text="🔐 Password Strength Checker",
         font=("Arial", 16, "bold"),
         bg="#1e1e2f",
         fg="white").pack(pady=15)

# Password input
password_entry = tk.Entry(root,
                          width=30,
                          show="*",
                          font=("Arial", 12),
                          bg="#2e2e3f",
                          fg="white",
                          insertbackground="white")
password_entry.pack(pady=10)

# Show/Hide checkbox
show_password = tk.BooleanVar()
tk.Checkbutton(root,
               text="Show Password",
               variable=show_password,
               command=toggle_password,
               bg="#1e1e2f",
               fg="white",
               selectcolor="#1e1e2f").pack()

# Check button
tk.Button(root,
          text="Check Strength",
          font=("Arial", 12, "bold"),
          bg="#4CAF50",
          fg="white",
          activebackground="#45a049",
          command=analyze_password).pack(pady=10)

# Result label
result_label = tk.Label(root,
                        text="Strength: ",
                        font=("Arial", 13, "bold"),
                        bg="#1e1e2f",
                        fg="white")
result_label.pack(pady=10)

# Suggestions box
suggestions_box = tk.Text(root,
                          height=8,
                          width=40,
                          bg="#2e2e3f",
                          fg="white",
                          font=("Arial", 10))
suggestions_box.pack(pady=10)

# Run app
root.mainloop()