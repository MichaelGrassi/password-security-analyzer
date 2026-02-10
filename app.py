import tkinter as tk

def analyze_password():
    pwd = entry.get()
    length = len(pwd)

    if length < 8:
        strength = "Weak"
    elif length < 12:
        strength = "Medium"
    else:
        strength = "Strong"

    result.config(text=f"Length: {length} | Strength: {strength}")

root = tk.Tk()
root.title("Password Security Analyzer")
root.geometry("400x250")

label = tk.Label(root, text="Enter a password to analyze:")
label.pack(pady=10)

entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=5)

button = tk.Button(root, text="Analyze", command=analyze_password)
button.pack(pady=10)

result = tk.Label(root, text="")
result.pack(pady=10)

root.mainloop()
