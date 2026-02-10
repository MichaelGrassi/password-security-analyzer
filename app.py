import tkinter as tk

root = tk.Tk()
root.title("Password Security Analyzer")
root.geometry("400x250")

label = tk.Label(root, text="Enter a password to analyze:")
label.pack(pady=10)

entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=5)

button = tk.Button(root, text="Analyze")
button.pack(pady=10)

result = tk.Label(root, text="")
result.pack(pady=10)

root.mainloop()
